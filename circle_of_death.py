import playerlist.py 
import linked_list.py

class Player:
	def __init__(self, name, username, assassin, target, kill_count, e_mail):
		self.in_game = True
		self.circle = None
		self.name = name
		self.username = username
		self.assassin = assassin
		self.target = target
		self.kill_count = kill_count
		self.e_mail = e_mail

	def __repr__(self):
		return "Player(" + \
			+ repr(self.name) + ", "\
			+ repr(self.username) + ", "\
			+ repr(self.assassin) + ", "\
			+ repr(self.target) + ", "\
			+ repr(self.kill_count) + ", "\
			+ repr(self.e_mail) + ")"
	

	

class CircleOfDeath:
	def __init__(self, players):
		self.death_types = []
		self.circle = LinkedList.create(players)

	def kill_player(self, player, method):
		assert player in self.circle, "Player is not in the game or already dead"
		self.circle.remove(player)
		player.in_game = False
		self.death_types.append(method)

	def bomb(self, players):
		for player in players:
			self.kill_player(player)

