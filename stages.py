#
# from first_stage_of_game import first_stage_archer
# from first_stage_of_game import first_stage_warrior
#
# class Map(object):
#
#     scenes = {
#
#         'first_stage_wizard':first_stage_wizard(),
#         'first_stage_archer':first_stage_archer(),
#         'first_stage_warrior':first_stage_warrior(),
#         'second_stage_wizard':second_stage_wizard(),
#         'second_stage_archer':second_stage_archer(),
#         'second_stage_warrior':second_stage_warrior(),
#
#     }
#
#
#
# def first_stage_wizard():
#     print("You're walking through a forest, twirling your staff between your fingers, bored out of your mind."
#           "\nYou're not sure where you're going but you don't care, you just need to wander and clear your mind."
#           "\nYou notice that ahead the forest is darker and overgrown. To your left is a small path leading to the"
#           "\nthe edge of the forest. To your right in the distance it looks as if there is a small camp."
#           "\nWhich direction do you choose?")
#
#     choice = input("> ")
#
#     if "left" in choice:
#         first_stage_w_left()
#     elif "right" in choice:
#         first_stage_w_right()
#     elif "front" or "in front" in choice:
#         first_stage_w_front()
#     else:
#         print("Do you want to continue?")
#
#         if "y" or "yes":
#             first_stage_wizard()
#         else:
#             print("okaaay")