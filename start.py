import pickle
from sys import exit
from character_name import start
from character_description import description
from items import Item
from instructions import instruction



instruction()
start()
description()

# player = (description(),Item())
# level_state = Level(room())
#saving
# with open('savefile.dat','wb') as f:
#     pickle.dump([player, ], f, protocol=2)

#loading
# with open('savefile.dat', 'rb') as f:
#     player, level_state = pickle.load()


item = Item

if "i" in input():
    print(item)
else:
    print("what")


