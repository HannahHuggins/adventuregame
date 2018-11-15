def start():
    print("Welcome, please enter your name.")

    name = input("> ")

    if "" in name:
        print(f"Hey {name}, welcome to the game!")
    else:
        print("Try again.")