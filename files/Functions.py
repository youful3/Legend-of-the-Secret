from Save import *
import os, time

###Save functions

#Basic Save
def saveStats(gold, dp, hp, weapon, name):
	f = open("files\Save.py", "w")
	f.write("from Weapons import *" + "\n")
	f.write("###Save files for " + name + "\n" + f"name = '{name}'" + "\n" + "gold = " + str(gold) + "\n" + "damage = " + str(dp) + "\n" + "health = " + str(hp) + "\n" + f"main_weapon = '{weapon}'")
	f.close()
	pass

#Special New Game Save
def new_game(TrueOrFalse):
	n = open("files\Spec_save.py", "w")
	n.write(f"new_game = {TrueOrFalse}" + "\n")

#Advanced Enemy Health
def adva(hp):
	return hp * 1.5


#Combat System
def active_combat(enemy1, num):
	f = open("files\Combat_com_com.py", "w")
	f.write("__enemy__ = ", str(enemy1) + "\n")
	f.write("enemy_num = ",str(num) + "\n")
	f.write("use_weapon = ", str(main_weapon) + "\n")
	f.close()
	active_combat_loop = True
	os.startfile("files\Combat_System.py")
	while active_combat_loop == True:
		c = open("files\Combat_com_active.txt", "r")
		check_active = c.read(1)
		if check_active == 'False':
			active_combat_loop = False
		else:
			pass