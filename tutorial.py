from Classes import *
from Functions import *
from Enemies import *
from Save import *
from tutorial_save import *
from Lists import *
import time

def t(number):
    time.sleep(number)
def pr(stri):
    print(stri)
def di(stri):
    print(f"You: {stri}")
def i(stri):
    input(stri)
def tu(Instruction):
    input(f"TUTORIAL TIP: {Instruction} Press [ENTER] to continue: ")
def note(stri):
    print("PLEASE NOTE: " + stri)

f = open("tutorial_save.py", "w")
def write(intro, menu, hunt):
    f.write("intro = " + str(intro) + "\n" + "menu = " + str(menu) + "\n" + "hunting = " + str(hunt))
    f.close()

if intro == False:
 t(3)
 pr("Silence...")
 t(3)
 pr("Your eyes are wide open...")
 t(3)
 di("That was a strange dream")
 t(3)
 di("But it's time to wake up now.")
 t(3)
 pr("Welcome to Ground Zero, the land of power...")
 t(3)
 input("TUTORIAL TIP: Press [ENTER] to continue: ")
 t(2)
 i("Humanity has moved on.")
 i("Technology is no more.")
 i("Only the Zero Energy remains")
 pr("")
 pr("You walk out side to place a wooden sign on your yard.")
 pr("The sign reads '" + name + " owns this farm'.")
 pr("")
 t(3)
 di("Time to go hunting now.")
 write(True, False, False)
 t(3)

write(True, False, False)

if menu == False:
    tu("Option menus (such as the one coming up) are what are going to be used to navigate the areas found throughout the game.")
    tu("Right now, we will learn how to hunt, which is the basic way to grind XP.")
    note("The way I designed this is janky, so expect at least 1 small bug, nothing game breaking though :D.")
    loop = True
    while loop == True:
        pr("")
        tu("CHOOSE THE HUNT OPTION.")
        for op in home:
            print(op)
        i = input("Type in the number corrosponding to your choice: ")
        pr("")
        if i == "1":
            print("It seems your wardrobe is empty")
        elif i == "2":
            print("It seems you have all your weapons equipped.")
        elif i == "3":
            print("Complete the tutorial before proceeding to the main world.")
        elif i == "4":
            loop = False
        t(2)

if hunting == False:
    pass