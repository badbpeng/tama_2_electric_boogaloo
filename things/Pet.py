class Pet:
    def __init__(self):
        self.hunger = 10 # pet starts full (/10)
        self.health = 10 # pet starts healthy (/10)
        self.happiness = 10 # pet starts happy (/10)
        self.name = "Your pet" # string, pet's name
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
        if self.happiness == 1:
            return False
        else:
            self.happiness -= 1

    # returns pets happiness
    def check_happiness(self):
        return self.happiness

    # returns a string based on the pet's degree of happiness
    def status_happiness(self):
        return "%s has %d/10 happiness." % (self.name, self.happiness)

    # game logic must prevent user from feeding when hungry = 10
    # bad naming convention
    def increase_hunger(self):
        self.hunger += 1

    # decrease hunger doesn't sound right, could use a better method name
    # decreases the pet's hunger
    # returns false if hunger = 0 (pet will leave)
    def decrease_hunger(self):
        if self.hunger == 1:
            return False
        else:
            self.hunger -= 1

    # returns pets hunger
    def check_hunger(self):
        return self.hunger

    # returns a string based on the pet's degree of hunger
    def status_hunger(self):
        return "%s has %d/10 hunger." % (self.name, self.hunger)

    # game logic must prevent user from cleaning when health = 10
    def increase_health(self):
        self.health += 1

    # decreases the pet's health
    # returns false if health = 0 (pet will leave)
    def decrease_health(self):
        if self.health == 1:
            return False
        else:
            self.health -= 1

    # returns pets health
    def check_health(self):
        return self.health

    # returns a string based on the pet's degree of health/cleanliness
    def status_health(self):
        return "%s has %d/10 health." % (self.name, self.health)
    
    # returns whether or not the pet is in the hotel
    def check_hotel(self):
        return self.hotel
    
    # changes the bool value of hotel
    def change_hotel(self):
        self.hotel = not self.hotel

    def get_name(self):
        return self.name