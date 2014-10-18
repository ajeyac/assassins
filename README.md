assassins
=========

This repository contains code to facilitate an assassins game, specifically a game played with the "circle of death" variant. A player recieves a target, who themself receives a target, and so on, until you have a circular cycle of targets and assassins. When a player is eliminated, their assassin then receives the victim's old target. This continues until only one is left standing.

This code will:

- take your input (from an Excel spreadsheet) containing the names, codenames, and e-mails of everyone in the game and:

	- randomize a circle of assassins and victims

	- keep track of the "circle of death" as players are eliminated
	
	- monitor the kill counts of all players
	
	- keep a tally of the methods of death (for the GM's use, to tweak rules if necessary)

	- (hopefully) inform players, via e-mail or text, of their current game status and new targets