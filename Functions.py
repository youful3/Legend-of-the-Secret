from Save import *

#Combat script
def Combat():
	pass

def saveStats(gold, dp, hp, weapon, name):
	f = open("Save.py", "w")
	f.write("###Save files for " + name + "\n" + "has_launched = True" + "\n" + f"name = '{name}'" + "\n" + "gold = " + str(gold) + "\n" + "damage = " + str(dp) + "\n" + "health = " + str(hp) + "\n" + f"main_weapon = '{weapon}'")
	f.close()
	pass

#Advanced Enemy Health
def adva(hp):
	return hp * 1.5
