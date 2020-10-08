import random

# Fall sem prentar út allar mögulegar leiðir
def possible_directions(north, east, south, west): 
    first = False
    print("You can travel: ", end="")
    if north:
        print("(N)orth", end="")
        first = True
    if east:
        if first:
            print(" or ", end="")
        print("(E)ast", end="")
        first = True
    if south:
        if first:
            print(" or ", end="")
        print("(S)outh", end="")
        first = True
    if west:
        if first:
            print(" or ", end="")
        print("(W)est", end="")
        first = True
    print(".")

def pull_lever(levers_pulled, position, choice):
    if position not in levers_pulled:
        if choice.lower() == "y":
            levers_pulled.append(position)
            print(f"You received 1 coin, your total is now {len(levers_pulled)}.")

# Fall færir leikmann
def move(next_input, position, levers_pulled, choice_lever): 
    if position == "1,1":
        if next_input.upper() == "N":
            pull_lever(levers_pulled, position, choice_lever)
            position = "1,2"
            possible_directions(True, True, True, False)
        else:
            print("Not a valid direction!")
            possible_directions(True, False, False, False)
    elif position == "1,2":
        if next_input.upper() == "E":
            pull_lever(levers_pulled, position, choice_lever)
            position = "2,2"
            possible_directions(False, False, True, True)
        elif next_input.upper() == "N":
            position = "1,3"
            possible_directions(False, True, True, False)
        elif next_input.upper() == "S":
            position = "1,1"
            possible_directions(True, False, False, False)
        else:
            print("Not a valid direction!")
            possible_directions(True, True, True, False)
    elif position == "2,2":
        if next_input.upper() == "W":
            pull_lever(levers_pulled, position, choice_lever)
            position = "1,2"
            possible_directions(True, True, True, False)
        elif next_input.upper() == "S":
            position = "2,1"
            possible_directions(True, False, False, False)
        else:
            print("Not a valid direction!")
            possible_directions(False, False, True, True)
    elif position == "2,1":
        if next_input.upper() == "N":
            pull_lever(levers_pulled, position, choice_lever)
            position = "2,2"
            possible_directions(False, False, True, True)
        else:
            print("Not a valid direction!")
            possible_directions(True, False, False, False)
    elif position == "1,3":
        if next_input.upper() == "E":
            pull_lever(levers_pulled, position, choice_lever)
            position = "2,3"
            possible_directions(False, True, False, True)
        elif next_input.upper() == "S":
            pull_lever(levers_pulled, position, choice_lever)
            position = "1,2"
            possible_directions(True, True, True, False)
        else:
            print("Not a valid direction!")
            possible_directions(False, True, True, False)
    elif position == "2,3":
        if next_input.upper() == "E":
            position = "3,3"
            possible_directions(False, False, True, True)
        elif next_input.upper() == "W":
            position = "1,3"
            possible_directions(False, True, True, False)
        else:
            print("Not a valid direction!")
            possible_directions(False, True, False, True)
    elif position == "3,3":
        if next_input.upper() == "S":
            pull_lever(levers_pulled, position, choice_lever)
            position = "3,2"
            possible_directions(True, False, True, False)
        elif next_input.upper() == "W":
            pull_lever(levers_pulled, position, choice_lever)
            position = "2,3"
            possible_directions(False, True, False, True)
        else:
            print("Not a valid direction!")
            possible_directions(False, False, True, True)
    elif position == "3,2":
        if next_input.upper() == "N":
            position = "3,3"
            possible_directions(False, False, True, True)
        elif next_input.upper() == "S":
            position = "3,1"
            print(f"Victory! Total coins {len(levers_pulled)}.")
        else:
            print("Not a valid direction!")
            possible_directions(True, False, True, False)
    return position, levers_pulled
    

def play():
    list_of_choice = ["N", "E", "s", "W"]
    lever_choices = ["y", "n"]
    choice_lever = int(input("Input seed: "))
    random.seed(choice_lever)

    position = "1,1"
    possible_directions(True, False, False, False)
    levers_pulled = []

    while position != "3,1":
        next_input = random.choice(list_of_choice)
        next_choice = random.choice(lever_choices)
        position, levers_pulled = move(next_input, position, levers_pulled, next_choice)

def main():
    play_again = "y"
    while play_again.lower() == "y":
        play()
        play_again = input("Play again (y/n): ")


main()