import first_stage_of_game


class Warrior(object):

    def warrior(self, hp, attack, defense):

        self.hp = hp
        self.attack = attack
        self.defense = defense
        print(f"Your stats: HP = {hp}, ATTACK = {attack}, DEFENSE = {defense}")
        print("You're a gawky warrior with armor that's too big for you and glasses that have been broken"
              "\nfor a while.")
        print("Press any key to continue.")
        enter = input()

        if "" in enter:
            first_stage_of_game.first_stage_warrior()




