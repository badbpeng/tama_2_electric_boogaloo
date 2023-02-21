class Pet:
    def __init__(self, name, noise):
        self.hunger = 10 # pet starts full (/10)
        self.health = 10 # pet starts healthy (/10)
        self.happiness = 10 # pet starts happy (/10)
        self.sound = noise # string, pet's default noise (i.e. chirp)
        self.name = name # string, pet's name
        self.hotel = False # pet starts not in hotel

        # [idea] add data base of images for each pet
        # have data member called curImage which selects an image from the database
        # i.e. pet is hungry, curImage is the "feed me" image

    # game logic must prevent user from playing when happiness = 10
    def increase_happiness(self):
        self.happiness += 1
        

    # decreases the pet's happiness
    # returns false if happiness = 0 (pet will leave)
    def decrease_happiness(self):
        if self.happiness == 0:
            return False
        else:
            self.happiness -= 1

    # returns pets happiness
    def check_happiness(self):
        return self.happiness

    # returns a string based on the pet's degree of happiness
    def status_happiness(self):
        if self.happiness == 10:
            return self.name + " is very happy."
        elif self.happiness > 5:
            return self.name + " is pleased."
        elif self.happiness > 1:
            return self.name + " is unhappy."
        else:
            return self.name + " is very sad!"

    # returns a string, the pet's noise
    def make_sound(self):
        return self.sound

    # game logic must prevent user from feeding when hungry = 10
    # bad naming convention
    def increase_hunger(self):
        self.hunger += 1

    # decrease hunger doesn't sound right, could use a better method name
    # decreases the pet's hunger
    # returns false if hunger = 0 (pet will leave)
    def decrease_hunger(self):
        if self.hunger == 0:
            return False
        else:
            self.hunger -= 1

    # returns pets hunger
    def check_hunger(self):
        return self.hunger

    # returns a string based on the pet's degree of hunger
    def status_hunger(self):
        if self.hunger == 10:
            return self.name + " is full."
        elif self.hunger > 5:
            return self.name + " is content."
        elif self.hunger > 1:
            return self.name + " is hungry."
        else:
            return self.name + " is starving!"

    # game logic must prevent user from cleaning when health = 10
    def increase_health(self):
        self.health += 1

    # decreases the pet's health
    # returns false if health = 0 (pet will leave)
    def decrease_health(self):
        if (self.health == 0):
            return False
        else:
            self.health -= 1

    # returns pets health
    def check_health(self):
        return self.health

    # returns a string based on the pet's degree of health/cleanliness
    def status_health(self):
        if self.health == 10:
            return self.name + " is fabulous."
        elif self.health > 5:
            return self.name + " is clean."
        elif self.health > 1:
            return self.name + " is dirty."
        else:
            return self.name + " is filthy!"
    
    # returns whether or not the pet is in the hotel
    def check_hotel(self):
        return self.hotel
    
    # changes the bool value of hotel
    def change_hotel(self):
        self.hotel = not self.hotel