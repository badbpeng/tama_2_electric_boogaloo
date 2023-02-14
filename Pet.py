class Pet:
    def __init__(self, name, noise):
        self.hunger = 10 # pet starts full (/10)
        self.health = 10 # pet starts healthy (/10)
        self.happiness = 10 # pet starts happy (/10)
        self.sound = noise # string, pet's default noise (i.e. chirp)
        self.name = name # string, pet's name

        # [idea] add data base of images for each pet
        # have data member called curImage which selects an image from the database
        # i.e. pet is hungry, curImage is the "feed me" image

    # game logic must prevent user from playing when happiness = 10
    def play(self):
        self.happiness += 1

    def decrease_happiness(self):
        if (self.happiness == 0):
            self.leave()
        else:
            self.happiness -= 1

    # returns a string based on the pet's degree of happiness
    def check_happiness(self):
        if (self.happiness == 10):
            return self.name + " is very happy."
        elif (self.happiness > 5):
            return self.name + " is pleased."
        elif (self.hapiness > 1):
            return self.name + " is unhappy."
        else:
            return self.name + " is very sad!"

    # returns a string, the pet's noise
    def make_sound(self):
        return self.sound

    # game logic must prevent user from feeding when hungry = 10
    def eat(self):
        self.hunger += 1

    # decrease hunger doesn't sound right, could use a better method name
    def decrease_hunger(self):
        if (self.hunger == 0):
            self.leave()
        else:
            self.hunger -= 1

    # returns a string based on the pet's degree of hunger
    def check_hunger(self):
        if (self.hunger == 10):
            return self.name + " is full."
        elif (self.hunger > 5):
            return self.name + " is content."
        elif (self.hunger > 1):
            return self.name + " is hungry."
        else:
            return self.name + " is starving!"

    # game logic must prevent user from cleaning when health = 10
    def clean(self):
        self.health += 1

    def decrease_health(self):
        if (self.health == 0):
            self.leave()
        else:
            self.health -= 1

    # returns a string based on the pet's degree of health/cleanliness
    def check_health(self):
        if (self.health == 10):
            return self.name + " is fabulous."
        elif (self.health > 5):
            return self.name + " is clean."
        elif (self.health > 1):
            return self.name + " is dirty."
        else:
            return self.name + " is filthy!"