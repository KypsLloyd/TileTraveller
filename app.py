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
    

position = "1,1"

next_input = input("Direction: ")

if position == "1,1":
    if next_input.upper() == "N":
        position = "1,2"
        possible_directions(True, True, True, False)
        