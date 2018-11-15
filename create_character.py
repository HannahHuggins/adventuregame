import first_stage_of_game


def own_description():
    print("Please describe your character.")

    character = input("> ")

    if "" in character:
        print(f"You are a {character}")
        first_stage()
    else:
        print("Please try again.")
        own_description()
