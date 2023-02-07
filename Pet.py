class Pet:
    def __init__(self, hunger, restlessness, noise):
        self.maxHunger = hunger
        self.curHunger = hunger # pet starts full
        self.maxRestlessness = restlessness
        self.curRestlessness = 0 # pet starts tired
        self.sound = noise # string, pet's default noise (i.e. chirp)
        # [idea] add data base of images for each pet
        # have data member called curImage which selects an image from the database
        # i.e. pet is hungry, curImage is the "feed me" image

    # does not check pet's restlessness
    # game must prevent user (or punish) from selecting a trick that will lower curRestlessness below 0
    # each trick has an amount of restlessness it removes
    def doTrick(self, trick):
        self.curRestlessness -= trick

    def addRestlessness(self):
        if (self.curRestlessness == self.maxRestlessness):
            self.hyperactive()
        else:
            self.curRestlessness += 1 # maybe different pets get more restless (i.e. humming bird gets +3 restlessness each hour)

    # think of some punishment for ignoring a pet's restlessness
    def hyperactive():
        return

    # getter method for restlessness
    # maybe add tired thresholds (i.e. when cur is half max...)
    def isTired(self):
        if (self.curRestlessness == 0):
            return True
        return False

    def makeSound(self):
        return self.sound

    # maybe add hunger thresholds (0 is starving, when cur is quarter of max pet is really hungry.. etc.)
    def isHungry(self):
        if (self.curHunger == 0):
            return True
        return False

    # does not check pets curHunger
    # game must prevent user (or punish) from selecting a food that will raise curHunger above maxHunger
    # different food will restore different hunger (i.e. porkchop adds +4 hunger)
    def eat(self, food):
        self.curHunger += food

    def removeHunger(self):
        if (self.curHunger == 0):
            self.starving()
        else:
            self.curHunger += 1 # maybe different pets get more hungry (i.e. ostrich gets +3 hunger each hour)
