from warrior_details import Warrior
from archer_details import archer
from create_character import own_description
from wizard_details import Wizard


def description():
    print("Is your character a wizard, archer, or warrior?")

    character = input("> ")

    if "wizard" in character:
        Wizard.wizard(Wizard, 50, 40, 50)

    elif "archer" in character:
        archer()
    elif "warrior" in character:
        Warrior.warrior(Warrior, 50, 50, 50)
    else:
        own_description()

