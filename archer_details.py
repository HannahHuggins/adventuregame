import first_stage_of_game


class Archer(object):

    def archer(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        print(f"Your stats: HP = {hp}, ATTACK = {attack}, DEFENSE = {defense}")
        print("Press any key to continue.")
        enter = input()

        if "" in enter:
            first_stage_of_game.first_stage_archer()

