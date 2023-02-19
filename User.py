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
        # decreases the pet's values by 1 for every hour since last updated
        if (time.time() - self.time > 3600):
            # decrease all of the pets values
            self.pet.decrease_hunger()
            self.pet.decrease_health()
            self.pet.decrease_happiness()
            self.time += 3600 # advance an hour

            #update the time
            self.time = time.time()

            # update the pet
            with open(self.phone, 'wb') as p:
                pickle.dump(self, p)

    # takes string from user, name of the game user wants to play
    # returns False for pet that cannot be played with, or incorrect game name entered
    def play_with_pet(self, game_name):
        games = {"tic tac toe", "guess that birb", "what am i"}
        if game_name.lower() not in games or self.pet.check_happiness != 10:
            return False
        
        self.pet.increase_happiness()

        if (game_name.lower() == "tic tac toe"):
            self.points += self.tic_tac_toe()
        elif (game_name.lower() == "guess that birb"):
            self.points += self.guess_that_birb()
        elif (game_name.lower() == "what am i"):
            self.points += self.what_am_i()

    def tic_tac_toe(self):
        # play the game

        # display amount of points won
        return
    
    def guess_that_birb():
        # play the game

        # display amount of points won
        return
    
    def what_am_i():
        # play the game

        # display amount of points won
        return
