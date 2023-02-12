import pickle
import Pet

class User:
    # TODO: properly dump the pet 
    def __init__(self):
        self.pet = self.give_pet()
        pickle.dump(self.pet)

    # TODO: add rng, grab name and noise from database
    def give_pet(self):
        return Pet("test_name", "test_sound")

    # TODO: check the latest time the pet has been unpickled
    def check_time(self):
        return
