import time
from Functions import *
from Save import *
from spec_save import *
import os

new = 0

print("Legend of the Secret")
time.sleep(2)
nlc = input("Press enter to continue from last save (Write 'N' for new game): ")

if nlc == "N" or nlc == "n" or has_launched == False:
	if has_launched == True:
		y = input("Are you sure you want to continue? All save data will be lost (Press Y for yes): ")
		y = y.strip()
		if y == "Y" or y == "y" or y == "yes" or y == "Yes":
			name = input("Hello warrior! What is your name? ")
			saveStats(0, 0, 0, "default", name)
			new_game = True
	elif has_launched == False:
		name = input("Hello warrior! What is your name? ")
		saveStats(0, 0, 0, "default", name)
		print(f"Welcome, {name}.")
elif has_launched == True:
	print("Welcome back " + name)

input("Press [Enter] to enter the main world... ")

if new_game == False:
	os.startfile("Dial.py")
else:
	os.startfile(r"Main world.py")

exit()