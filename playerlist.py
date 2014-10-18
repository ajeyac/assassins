#creates all of the players from an excel spreadsheet
def make_player_list(filename):
    player_list = []
    spreadsheet = open(filename)
    for line in spreadsheet:
        attributes = line.split(",")
        player = Player(attributes[0], attributes[1], None, None, attributes[2], attributes[3])
        player_list.append(player)

    #randomizes list of names
    from random import choice
    number_of_players = len(player_list)
    randomized_list = []
    for _ in range(len((player_list))):
        current_player = choice(player_list)
        randomized_list.append(current_player)
        player_list.remove(current_player)
    return randomized_list
    


