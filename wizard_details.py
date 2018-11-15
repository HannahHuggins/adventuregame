import first_stage_of_game


class Wizard(object):

    def wizard(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        print(f"Your stats: HP = {self.hp}, ATTACK = {self.attack}, DEFENSE = {self.defense}")
        print("Press any key to continue.")
        enter = input()

        if "" in enter:
            first_stage_of_game.first_stage_wizard()
