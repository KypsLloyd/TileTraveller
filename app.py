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

# Fall kallar á prent á þeim áttum sem eiga við um staðsetningu
def valid_dir_print(pos):
    if pos == [1,1]:
        possible_directions(True, False, False, False)
    elif pos == [1,2]:
        possible_directions(True, True, True, False)
    elif pos == [1,3]:
        possible_directions(False, True, True, False)
    elif pos == [2,1]:
        possible_directions(True, False, False, False)
    elif pos == [2,2]:
        possible_directions(False, False, True, True)
    elif pos == [2,3]:
        possible_directions(False, True, False, True)
    elif pos == [3,2]:
        possible_directions(True, False, True, False)
    elif pos == [3,3]:
        possible_directions(False, False, True, True)

# Fall uppfærir staðsetningu leikmanns ef það er valid átt
def valid_move(next_input, coins, position, valid_spots):
    lever_positions = [[1,2],[2,2],[2,3],[3,2]]
    next_input = next_input.upper()
    if next_input in valid_spots:
        if next_input == "N":
            position[1] += 1
        elif next_input == "E":
            position[0] += 1
        elif next_input == "S":
            position[1] -= 1
        elif next_input == "W":
            position[0] -= 1
        if position in lever_positions:
            coins = pull_lever(coins)
        if position == [3,1]:
            print(f"Victory! Total coins {coins}.")
        else:
            valid_dir_print(position)
        return position, coins
    else:
        print("Not a valid direction!")
        valid_dir_print(position)
        return position, coins

# Fall sér um að gefa notanda valmöguleika um að taka í rofa og bætir honum þá við
def pull_lever(coins):
    choice = input("Pull a lever (y/n): ")
    if choice.lower() == 'y':
        coins += 1
        print(f"You received 1 coin, your total is now {coins}.")
    return coins

# Fall færir leikmann
def move(next_input, position, coins): 
    if position == [1,1]:
        position, coins = valid_move(next_input, coins, position, ["N"])
    elif position == [1,2]:
        position, coins = valid_move(next_input, coins, position, ["E","N","S"])
    elif position == [1,3]:
        position, coins = valid_move(next_input, coins, position, ["E","S"])
    elif position == [2,1]:
        position, coins = valid_move(next_input, coins, position, ["N"])
    elif position == [2,2]:
        position, coins = valid_move(next_input, coins, position, ["W","S"])
    elif position == [2,3]:
        position, coins = valid_move(next_input, coins, position, ["E","W"])
    elif position == [3,2]:
        position, coins = valid_move(next_input, coins, position, ["N","S"])
    elif position == [3,3]:
        position, coins = valid_move(next_input, coins, position, ["S","W"])
    return position, coins
    
position = [1,1]
coins = 0
valid_dir_print(position)

while position != [3,1]:
    next_input = input("Direction: ")
    position, coins = move(next_input, position, coins)