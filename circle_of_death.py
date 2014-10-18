#creates a player class
class Player:
	def __init__(self, name, username, assassin, target, kill_count, e_mail):
		self.name = name
		self.username = username
		self.assassin = assassin
		self.target = target
		self.kill_count = kill_count
		self.e_mail = e_mail
	def __repr__(self):
		return "Player(" + " "\
			+ repr(self.name) + " "\
			+ repr(self.username) + " "\
			+ repr(self.assassin) + " "\
			+ repr(self.target) + " "\
			+ repr(self.kill_count) + " "\
			+ repr(self.e_mail) + ")"

#creates all of the players from an excel spreadsheet
player_list = []
spreadsheet = open("Sample Assassins Spreadsheet.csv")
for line in spreadsheet:
	attributes = line.split(",")
	player = Player(attributes[0], attributes[1], None, None, attributes[2], attributes[3])
	player_list.append(player)


#randomizes list of names
from random import choice
number_of_players = len(player_list)
randomized_list = []
for i in range(len((player_list))):
	current_player = choice(player_list)
	randomized_list.append(current_player)
	player_list.remove(current_player)
print(randomized_list)

