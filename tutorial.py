from Classes import *
from Functions import *
from Enemies import *
from Save import *
from tutorial_save import *
from Lists import *
import time, os

def t(number):
    time.sleep(number)
def pr(stri):
    print(stri)
def di(stri):
    print(f"You: {stri}")
def i(stri):
    input(stri)
def tu(Instruction):
    print("")
    input(f"TUTORIAL TIP: {Instruction} Press [ENTER] to continue: ")
    print("")
def note(stri):
    input("PLEASE NOTE: " + stri + " Press enter to continue: ")
def tc(stri):
    print(stri)
    time.sleep(4)

def write(intro, menu, hunt):
    f = open("tutorial_save.py", "w")
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
    write(True, True, False)

if hunting == False:
    tu("Hunting is the most basic way to grind XP in this game, so we'll first learn how to do that.")
    tu("In Legend of the Secret, hunting is based on RNG (Randomised), later on you'll find weapons that increase your hunting luck.")
    note("Because this is a tutorial, the hunting system here is scripted and not randomised, because I was too lazy to develop the system, but don't worry, the system in the actual game is RNG, yay gambling!")
    tu("Hunting takes a small amount of gold per session, by that I mean [5] gold per session.")
    tu("Now, let's start with the hunting!")
    i = input("Press [ENTER] to enter the hunting grounds (press N to exit): ")
    print("")
    t(2)
    loop = True
    while loop == True:
        if i == "n" or i == "N":
            print("Sorry, you can't do that during the tutorial, sorry :(.")
            t(3)
        else:
            loop = False
    input("You caught a [Basic Fawn]! Gained [10] gold. Made back [5] gold. Press [ENTER] to continue: ")
    print("")
    input("Press [ENTER] to enter the hunting grounds (press N to exit): ")
    print("")
    print("Grounds Officer: Sorry kid, times up, the hunting grounds are closing.")
    di("Damn, okay I guess, I'll just come back tomorrow.")
    print("Grounds Officer: Thanks for understanding.")
    print("")
    t(2)
    tc("You were returning home...")
    tc("So now it's time...")
    tc("It's time...")
    tc("It's time to move on...")
    tc("It's time to pull the trigger...")
    os.startfile("Dialoges.py")