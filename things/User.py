import pickle
import time
import random
import json
from things.Pet import Pet
from things.actors import actor

MY_GAME_LOGIC = {}
with open('Lily_Chatbot_Reformatted.json', 'r') as myfile:
    MY_GAME_LOGIC = json.loads(myfile.read())

#print(json.dumps(MY_GAME_LOGIC, indent=4))
#print(MY_GAME_LOGIC.keys())

class User(actor):
    def __init__(self, phone_number):
        # TODO after bug fixing make vars private
        self.pet = self.give_pet() # make the pet [TEST]
        self.time = time.time() # record the time of pet creation [Every time the pet is updated, record the time]
        self.points = 1000000000 # user starts with 0 points
        super().__init__(phone_number)
        #self.state = "init" # user starts in tutorial

        # dump the inital user class as a pickle in a file named after their phone 
        with open(phone_number, 'wb') as p:
            pickle.dump(self, p)

    def get_output(self,msg_input):
        found_match = False
        output = []
        media = []
        
        #print(self.state)
        print(msg_input)
        if type( MY_GAME_LOGIC[ self.state ]['next_state'] ) != str: # we have choices
            print('running here too')
            for next_state in MY_GAME_LOGIC[ self.state ]['next_state']:
                if msg_input.lower() == next_state['input'].lower():
                    self.state = next_state['next_state']
                    print(self.state)
                    if 'feed_pet' in  next_state:
                        output.append(self.feed_pet())
                    if 'clean_pet' in next_state:
                        output.append(self.clean_pet())
                    if 'play_pet' in next_state:
                        output.append(self.play_pet())
                    if 'media' in next_state:
                        media.append(MY_GAME_LOGIC[ self.state ]['media'])
                    if 'status_pet' in next_state:
                        output.append(self.status_pet())
                    if 'increase_happiness' in next_state:
                        s = self.play_pet()
                        rand_int = random.randrange(2) #random index
                        # The below line gets a random string from said random index
                        string_pain = random.choice(MY_GAME_LOGIC['guess the number']['next_state'][rand_int]['content'])
                        print (string_pain) #WHEN IN DOUBT, PRINT IT OUT
                        if(s == ''):
                            output.append(string_pain) # Appends that random string
                        else:
                            output.append(s) #else append the error message from the method
                    if 'cost' in next_state:
                        #check for bought item
                        if msg_input == "gacha" or msg_input == "Gacha":
                            #points modifier
                            if self.points >= 3:
                                self.points -= 3
                            else:
                                output.append("You do not have enough points to spend on the gacha game.")
                                self.state = "idle" #skip straight back to idle
                        
                        if msg_input == "pet hotel" or msg_input == "Pet hotel" or msg_input == "Pet Hotel":
                            if self.pet.check_hotel() == True: #don't buy another stay at the hotel, ask to check out borb early instead
                                self.state = "get BORB" #skip straight to get borb
                            else: #pet isn't already in hotel, allow user to buy stay if enough funds
                                if self.points >= 2:
                                    self.points -= 2
                                else:
                                    output.append("You do not have enough points to spend on the BORB hotel.")
                                    self.state = "idle" #skip straight back to idle
                        # TODO get that cost change working
                    if 'get gacha' in next_state: #Gets a random gacha image and throws it into the media list
                        media.append(random.choice(MY_GAME_LOGIC[self.state]['gacha_pic']))
                        print(random.choice(MY_GAME_LOGIC[self.state]['gacha_pic']))
                        print("get gacha triggered")
                    found_match = True
                    break

            if found_match == False:
                return ['Ooops.. Not a valid choice...'], media

        while True:
            print(self.state)
            if self.state != "idle":
                if type(MY_GAME_LOGIC[ self.state ]['content']) is str:
                    output.append(MY_GAME_LOGIC[ self.state ]['content'])
                if self.state is "points amount":
                    output[-1] = output[-1].replace("[points]", self.points)
                    print("triggered")
            if 'get gacha' in MY_GAME_LOGIC[ self.state ]: #Gets a random gacha image and throws it into the media list
                media.append(random.choice(MY_GAME_LOGIC[self.state]['gacha_pic']))
                print(random.choice(MY_GAME_LOGIC[self.state]['gacha_pic']))
                print("get gacha triggered outside choice for loop")
            if 'media' in MY_GAME_LOGIC[ self.state ]:
                media.append(MY_GAME_LOGIC[ self.state ]['media'])
            if 'next_state' not in MY_GAME_LOGIC[ self.state ] or type( MY_GAME_LOGIC[ self.state ]['next_state'] ) != str:
                break
            self.state = MY_GAME_LOGIC[ self.state ]['next_state']
        
        #print("in get_output")
        print(output)
        return output, media

    
    # TODO: add rng, grab pet's name and noise from database
    def give_pet(self):
        return Pet()

    # game logic will need to load this user's pickle before calling this function, key for every user's pickle is thier phone #
    # checks if the pet's values needs to be updated
    def check_pet(self):
        # decreases the pet's values by 1 for every hour since last updated, if it is not in the hotel
        while self.pet.check_hotel() == False and time.time() - self.time > 3600:
            # decrease all of the pets values
            if self.pet.decrease_hunger() == False:
                self.pet_leave()
                # TODO exit out of the old pet's function that called this (return state to input)
                return False
            if self.pet.decrease_happiness() == False:
                self.pet_leave()
                # TODO exit out of the old pet's function that called this (return state to input)
                return False
            if self.pet.decrease_health() == False:
                self.pet_leave()
                # TODO exit out of the old pet's function that called this (return state to input)
                return False
            self.time += 3600 # advance an hour

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

        return True

    # plays with pet
    def play_pet(self):
        if not self.check_pet(): # check pet's values against time
            return "Your pet has died, you have been given a new pet."
        
        if self.pet.check_happiness() == 10:
            return "Your pet doesn't want to play"
        
        self.pet.increase_happiness()
        #msg = ""

        # 20% chance to get a point after feeding
        if random.randint(1, 5) == 1:
            self.give_points(1)
        #    msg = "You have earned a BORB point for taking care of your shimaenaga!"


        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

        return ""
        #return msg
    
    # cannot feed pet is pet is full
    def feed_pet(self):
        if not self.check_pet(): # check pet's values against time
            return "Your pet has died, you have been given a new pet."

        if self.pet.check_hunger() == 10:
            return "Your pet is too full to eat."
        
        self.pet.increase_hunger()

        # 20% chance to get a point after feeding
        if random.randint(1, 5) == 1:
            self.give_points(1)

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

        return "You have fed your pet."

    # cannot clean if pet is fully clean
    def clean_pet(self):
        if not self.check_pet(): # check pet's values against time
            return "Your pet has died, you have been given a new pet."

        if self.pet.check_health() == 10:
            return "Your pet is already clean."
        
        self.pet.increase_health()

        # 20% chance to get a point after cleaning
        if random.randint(1, 5) == 1:
            self.give_points(1)

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

        return "You have cleaned you pet."

    # spend points put pet in the hotel
    # returns false if user doesn't have enough points or pet is alread in the hotel
    def hotel_pet(self):
        if not self.check_pet(): # check pet's values against time
            return "Your pet has died, you have been given a new pet."

        if self.pet.check_hotel() == True or self.points < 10:
            return "Your pet cannot enter the hotel."
        
        self.pet.change_hotel()
        # TODO send a message that the pet has entered the hotel

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

        return ""
    
    # take pet out of the hotel
    # returns false if the pet is not in the hotel
    def check_out_pet(self):
        if not self.check_pet(): # check pet's values against time
            return "Your pet has died, you have been given a new pet."
        
        self.pet.change_hotel()
        # TODO send a message that the pet has exited the hotel

        # update the time [so the pet won't decrease hunger/health/etc.]
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)
        
        return ""

    # returns string of pet's values
    def status_pet(self):
        self.check_pet() # check pet's values against time

        status = self.pet.status_happiness() + "\n"
        status = status + self.pet.status_health() + "\n"
        status = status + self.pet.status_hunger() + "\n"
        status += "You have %d point" % self.points
        if self.points != 1:
            status += "s"
        status += " to spend."

        return status

    def pet_leave(self):
        #TODO message the user that they're pet has left/died

        # give the user a new pet
        self.pet = self.give_pet() # garbage collector on old pet?
        # user will keep points from last pet
        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

    def give_points(self, points):
        # TODO send message that user has gained point(s)

        # add points
        self.points += points

        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)