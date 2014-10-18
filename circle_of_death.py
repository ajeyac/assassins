import playerlist.py 
import linked_list.py

class Player:
	def __init__(self, name, username, assassin, target, kill_count, e_mail):
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

class 



