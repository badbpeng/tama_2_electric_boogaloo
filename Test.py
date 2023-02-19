from User import User
import pickle
import random
import os.path
from os import path

debug = True

if __name__ == '__main__':
    print("Enter phone #")
    phone_number = input()
    while not path.exists(phone_number):
        user = User(phone_number)

    with open(phone_number, 'rb') as p:
        user = pickle.load(p)

    # uncomment to manually change pet's values for testing
    #user.pet.hunger = 5
    #user.pet.happiness = 5
    #user.pet.health = 5
    #user.points = 5
    #user.time = user.time - 3600 * 4

    print(user.status_pet())

    while (True):
        print("What do you want to do?")
        command = input()

        match command.lower().strip():
            case "status":
                print(user.status_pet())
            case "feed":
                user.feed_pet()
                if debug:
                    print(user.status_pet())
            case "clean":
                user.clean_pet()
                if debug:
                    print(user.status_pet())
            case "play":
                    match random.randint(1, 3):
                        case 1:
                            user.tic_tac_toe()
                            if debug:
                                print("Played tic tac toe")
                                print(user.status_pet())
                        case 2:
                            user.guess_that_birb()
                            if debug:
                                print("Played guess that birb")
                                print(user.status_pet())
                        case 3:
                            user.what_am_i()
                            if debug:
                                print("Played what am i")
                                print(user.status_pet())
            case "get hotel":
                user.hotel_pet()
                if debug:
                    print(user.status_pet())
            case "leave hotel":
                user.check_out_pet()
                if debug:
                    print(user.status_pet())