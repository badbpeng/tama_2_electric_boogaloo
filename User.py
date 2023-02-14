import pickle
import time
import Pet

class User:
    def __init__(self, phone_number):
        # TODO after bug fixing make vars private
        self.pet = self.give_pet() # make the pet
        self.time = time.time() # record the time of pet creation [Every time the pet is updated, record the time]
        self.phone = phone_number # save the user's phone number

        # dump the inital user class as a pickle in a file named after their phone 
        with open(phone_number, 'wb') as p:
            pickle.dump(self, p)

    # TODO: add rng, grab pet's name and noise from database
    def give_pet(self):
        return Pet("test_name", "test_sound")

    # game logic will need to load this user's pickle before calling this function, key for every user's pickle is thier phone #
    # checks if the pet's values needs to be updated
    def check_pet(self):
        # checks if it's been over an hour since the pet has been updated
        if (time.time() - self.time > 3600):
            # decrease all of the pets values
            self.pet.decrease_hunger()
            self.pet.decrease_health()
            self.pet.decrease_happiness()
            # record the time
            self.time = time.time()

            # update the pet
            with open(self.phone, 'wb') as p:
                pickle.dump(self, p)
