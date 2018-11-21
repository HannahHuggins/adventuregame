from first_stage_of_game import first_stage_wizard
from first_stage_of_game import first_stage_archer
from first_stage_of_game import first_stage_warrior


class Character:
    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense


class Wizard(Character):

    def __init__(self, hp, attack, defense, magic):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.magic = magic

        print(f"Your stats: HP = {self.hp}, ATTACK = {self.attack}, DEFENSE = {self.defense}, MAGIC = {self.magic}")
        print("Press any key to continue.")
        enter = input()

        if "" in enter:
            first_stage_wizard()


class Warrior(Character):

    def __init__(self, hp, attack, defense, strength):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.strength = strength

        print(f"Your stats: HP = {self.hp}, ATTACK = {self.attack}, DEFENSE = {self.defense}, STRENGTH = {self.strength}")
        print("Press any key to continue.")
        enter = input()

        if "" in enter:
            first_stage_warrior()


class Archer(Character):

    def __init__(self, hp, attack, defense, skill):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skill = skill

        print(f"Your stats: HP = {self.hp}, ATTACK = {self.attack}, DEFENSE = {self.defense}, SKILL = {self.skill}")
        print("Press any key to continue.")
        enter = input()

        if "" in enter:
            first_stage_archer()






