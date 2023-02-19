import pickle
import time
from Pet import Pet

class User:
    def __init__(self, phone_number):
        # TODO after bug fixing make vars private
        self.pet = self.give_pet() # make the pet [TEST]
        self.time = time.time() # record the time of pet creation [Every time the pet is updated, record the time]
        self.phone = phone_number # save the user's phone number
        self.points = 0 # user starts with 0 points

        # dump the inital user class as a pickle in a file named after their phone 
        with open(phone_number, 'wb') as p:
            pickle.dump(self, p)

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
                break
            if self.pet.decrease_happiness() == False:
                self.pet_leave()
                break
            if self.pet.decrease_health() == False:
                self.pet_leave()
                break
            self.time += 3600 # advance an hour

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

    # plays with pet
    # returns false if pet cannot be played with
    def tic_tac_toe(self):
        if self.pet.check_happiness == 10:
            return False
        
        self.pet.increase_happiness()

        # TODO play the game
        # TODO display & return amount of points won

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)
    
    # plays with pet
    # returns false if pet cannot be played with
    def guess_that_birb(self):
        if self.pet.check_happiness == 10:
            return False
        
        self.pet.increase_happiness()
        
        # TODO play the game
        # TODO display & return amount of points won

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)
    
    # plays with pet
    # returns false if pet cannot be played with
    def what_am_i(self):
        if self.pet.check_happiness == 10:
            return False
        
        self.pet.increase_happiness()
        
        # TODO play the game
        # TODO display & return amount of points won

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)
    
    # cannot feed pet is pet is full
    def feed_pet(self):
        if self.pet.check_hunger() == 10:
            return False
        
        self.pet.increase_hunger()

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

    # cannot clean if pet is fully clean
    def clean_pet(self):
        if self.pet.check_health() == 10:
            return False
        
        self.pet.increase_health()

        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)

    # spend points put pet in the hotel
    # returns false if user doesn't have enough points or pet is alread in the hotel
    def hotel_pet(self):
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
    def pet_status(self):
        string = self.pet.check_happiness()
        string += self.pet.check_health()
        string += self.pet.check_hunger()

    def pet_leave(self):
        #TODO message the user that they're pet has left/died

        # give the user a new pet
        self.pet = self.give_pet() # garbage collector on old pet?
        # user will keep points
        # update the time
        self.time = time.time()
        # update the pickle
        with open(self.phone, 'wb') as p:
            pickle.dump(self, p)