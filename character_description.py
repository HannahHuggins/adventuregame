from character import Wizard
from character import Archer
from character import Warrior


def description():
    print("Is your character a wizard, archer, or warrior?")

    character = input("> ")

    if "wizard" in character:
        Wizard(10,20,30,30)
    elif "archer" in character:
        Archer(50, 50, 50, 50)
    elif "warrior" in character:
        Warrior(50, 50, 50, 60)
    else:
        print("Please try again.")


        random

