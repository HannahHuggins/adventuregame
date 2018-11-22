# class Stages:
#
#     def __init__(self, first_stage, second_stage, third_stage):


# need to map out the areas and stages for the different levels to figure out where character will go
# avoid repetition

from enemies import Goblin

def first_stage_wizard():
    print("You're walking through a forest, twirling your staff between your fingers, bored out of your mind."
          "\nYou're not sure where you're going but you don't care, you just need to wander and clear your mind."
          "\nYou notice that ahead the forest is darker and overgrown. To your left is a small path leading to the"
          "\nthe edge of the forest. To your right in the distance it looks as if there is a small camp."
          "\nWhich direction do you choose?")

    choice = input("> ")

    if "left" in choice:
        first_stage_w_left()
    elif "right" in choice:
        first_stage_w_right()
    elif "front" or "in front" in choice:
        first_stage_w_front()
    else:
        print("Do you want to continue?")

        if "y" or "yes":
            first_stage_wizard()
        else:
            print("okaaay")



def first_stage_archer():
    print("woah nelly")

def first_stage_warrior():
    print("You're walking through a forest, twirling a small dagger between your fingers, bored out of your mind.")
    print("")



def first_stage_w_left():
    print("")


def first_stage_w_right():
    print("hey hey")
    Goblin(10, 10, 10)


def first_stage_w_front():
    print("")