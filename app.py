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

# Fall færir leikmann
def move(next_input, position): 
    if position == "1,1":
        if next_input.upper() == "N":
            position = "1,2"
            possible_directions(True, True, True, False)
        else:
            print("Not a valid direction!")
    elif position == "1,2":
        if next_input.upper() == "E":
            position = "2,2"
            possible_directions(False, False, True, True)
        elif next_input.upper() == "N":
            position = "1,3"
            possible_directions(False, True, False, True)
        elif next_input.upper() == "S":
            position = "1,1"
            possible_directions(True, False, False, False)
        else:
            print("Not a valid direction!")
    elif position == "2,2":
        if next_input.upper() == "W":
            position = "1,2"
            possible_directions(True, True, True, False)
        elif next_input.upper() == "S":
            position = "2,1"
            possible_directions(True, False, False, False)
        else:
            print("Not a valid direction!")
    elif position == "2,1":
        if next_input.upper() == "N":
            position = "2,2"
            possible_directions(False, False, True, True)
        else:
            print("Not a valid direction!")
    elif position == "1,3":
        if next_input.upper() == "E":
            position = "2,3"
            possible_directions(False, True, False, True)
        elif next_input.upper() == "S":
            position = "1,2"
            possible_directions(True, True, True, False)
        else:
            print("Not a valid direction!")
    elif position == "2,3":
        if next_input.upper() == "E":
            position = "3,3"
            possible_directions(False, False, True, True)
        elif next_input.upper() == "W":
            position = "1,3"
            possible_directions(False, True, True, False)
        else:
            print("Not a valid direction!")
    elif position == "3,3":
        if next_input.upper() == "S":
            position = "3,2"
            possible_directions(True, False, True, False)
        elif next_input.upper() == "W":
            position = "2,3"
            possible_directions(False, True, False, True)
        else:
            print("Not a valid direction!")
    elif position == "3,2":
        if next_input.upper() == "N":
            position = "3,3"
            possible_directions(False, False, True, True)
        elif next_input.upper() == "S":
            position = "3,1"
            print("Victory!")
        else:
            print("Not a valid direction!")
    return position
    

position = "1,1"

possible_directions(True, False, False, False)
next_input = input("Direction: ")

while True:
    position = move(next_input, position)

    if position != "3,1":
        next_input = input("Direction: ")
    else:
        break