from Save import *

#Combat script
def Combat():
	pass

###Save functions

#Basic Save
def saveStats(gold, dp, hp, weapon, name):
	f = open("Save.py", "w")
	f.write("###Save files for " + name + "\n" + f"name = '{name}'" + "\n" + "gold = " + str(gold) + "\n" + "damage = " + str(dp) + "\n" + "health = " + str(hp) + "\n" + f"main_weapon = '{weapon}'")
	f.close()
	pass

#Special New Game Save
def new_game(TrueOrFalse):
	n = open("spec_save.py", "w")
	n.write(f"new_game = {TrueOrFalse}" + "\n")

#Advanced Enemy Health
def adva(hp):
	return hp * 1.5
