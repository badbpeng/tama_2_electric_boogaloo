import pickle
import time
import random
import json
from things.Pet import Pet
from things.actors import actor

MY_GAME_LOGIC = {}
with open('Lily_Chatbot.json', 'r') as myfile:
    MY_GAME_LOGIC = json.loads(myfile.read())

class User(actor):
    def __init__(self, phone_number):
        # TODO after bug fixing make vars private
        self.pet = self.give_pet() # make the pet [TEST]
        self.time = time.time() # record the time of pet creation [Every time the pet is updated, record the time]
        self.points = 0 # user starts with 0 points
        super().__init__(phone_number)
        #self.state = "init" # user starts in tutorial

        # dump the inital user class as a pickle in a file named after their phone 
        with open(phone_number, 'wb') as p:
            pickle.dump(self, p)

    def get_output(self,msg_input):
        found_match = False
        output = [  ]
        media = []
        print(self.state)
        print(msg_input)
        if type( MY_GAME_LOGIC[ self.state ]['next_state'] ) != str: # we have choices
            print('running here too')
            for next_state in MY_GAME_LOGIC[ self.state ]['next_state']:
                if msg_input.lower() ==  next_state['input'].lower():
                    self.state = next_state['next_state']
                    if 'feed_pet' in  next_state:
                        self.feed_pet()
                    if 'clean_pet' in next_state:
                        self.clean_pet()
                    if 'media' in next_state:
                        media.append(MY_GAME_LOGIC[ self.state ]['media'])
                    found_match = True
                    break

            if found_match == False:
                return ['Ooops.. Not a valid choice...']

        while True:
            output.append( MY_GAME_LOGIC[ self.state ]['content'])
            if 'media' in MY_GAME_LOGIC[ self.state ]:
                media.append(MY_GAME_LOGIC[ self.state ]['media'])
            if 'next_state' not in MY_GAME_LOGIC[ self.state ] or type( MY_GAME_LOGIC[ self.state ]['next_state'] ) != str:
                break
            self.state = MY_GAME_LOGIC[ self.state ]['next_state']
        
        return output, media

    
    # TODO: add rng, grab pet's name and noise from database
    def give_pet(self):
        return Pet("test_name", "test_sound")

    # game logic will need to load this user's pickle before calling this function, key for every user's pickle is thier phone #
    # checks if the pet's values needs to be updated
    def check_pet(self):
        # decreases the pet's values by 1 for every hour since last updated, if it is not in the hotel
        while self.pet.check_hotel() == False and time.time() - self.time > 3600:
            # decrease all of the pets values
            if self.pet.decrease_hunger() == False:
                self.pet_leave()
                # TODO exit out of the old pet's function that called this (return state to input)
                exit(1)
            if self.pet.decrease_happiness() == False:
                self.pet_leave()
                # TODO exit out of the old pet's function that called this (return state to input)
                exit(1)
            if self.pet.decrease_health() == False:
                self.pet_leave()
                # TODO exit out of the old pet's function that called this (return state to input)
                exit(1)
            self.time += 3600 # advance an hour

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

    # plays with pet
    # returns false if pet cannot be played with
    def tic_tac_toe(self):
        self.check_pet() # check pet's values against time

        if self.pet.check_happiness == 10:
            return False
        
        self.pet.increase_happiness()

        # TODO play the game
        won = 0 # test value
        
        # award player with points
        self.give_points(won)

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)
    
    # plays with pet
    # returns false if pet cannot be played with
    def guess_that_birb(self):
        self.check_pet() # check pet's values against time

        if self.pet.check_happiness == 10:
            return False
        
        self.pet.increase_happiness()
        
        # TODO play the game
        won = 0 # test value
        
        # award player with points
        self.give_points(won)

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)
    
    # plays with pet
    # returns false if pet cannot be played with
    def what_am_i(self):
        self.check_pet() # check pet's values against time

        if self.pet.check_happiness == 10:
            return False
        
        self.pet.increase_happiness()
        
        # TODO play the game
        won = 0 # test value
        
        # award player with points
        self.give_points(won)

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)
    
    # cannot feed pet is pet is full
    def feed_pet(self):
        self.check_pet() # check pet's values against time

        if self.pet.check_hunger() == 10:
            return False
        
        self.pet.increase_hunger()

        # 20% chance to get a point after feeding
        if random.randint(1, 5) == 1:
            self.give_points(1)

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

    # cannot clean if pet is fully clean
    def clean_pet(self):
        self.check_pet() # check pet's values against time

        if self.pet.check_health() == 10:
            return False
        
        self.pet.increase_health()

        # 20% chance to get a point after cleaning
        if random.randint(1, 5) == 1:
            self.give_points(1)

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

    # spend points put pet in the hotel
    # returns false if user doesn't have enough points or pet is alread in the hotel
    def hotel_pet(self):
        self.check_pet() # check pet's values against time

        if self.pet.check_hotel() == True or self.points < 10:
            return False
        
        self.pet.change_hotel()
        # TODO send a message that the pet has entered the hotel

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)
    
    # take pet out of the hotel
    # returns false if the pet is not in the hotel
    def check_out_pet(self):
        if self.pet.check_hunger == False:
            return False
        
        self.pet.change_hotel()
        # TODO send a message that the pet has exited the hotel

        # update the time [so the pet won't decrease hunger/health/etc.]
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

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