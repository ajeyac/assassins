

from random import choice
player_list = ["Alex", "Beth", "Courtney", "David", "Eloise", "Francis", "Graham", "Henry"]
number_of_players = len(player_list)
randomized_list = [""] * number_of_players
for i in range(len((player_list))):
	current_player = choice(player_list)
	randomized_list[i] = current_player
	player_list.remove(current_player)
print(randomized_list)