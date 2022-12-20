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

f = open("tutorial_save.py", "w")

if intro == True:
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

if hunting == False:
    tu("The following list is what will be used to navigate the different attacks, areas in the open world, and inventory, through out the game.")
    tu("In the prompt given below the list, you will have to type the number corresponding to your choice.")
    t(3)
    pr("TUTORIAL TIP: Right now, we are about to learn about hunting, so type the number corresponding to the hunting option.")
    loop = True
    while loop == True:
        for option in home:
            print(option)
        option = input("Type the number corresponding to your choice: ")
        if option == '1':
            print("It seems your wardrobe is empty.")
            t(2)
        elif option == '2':
            print("It seems you have all your weapons equipped")
            t(2)
        elif option == '3':
            print("You must complete the tutorial before entering the main world.")
            t(2)
        elif option == '4':
            loop = False
        else:
            print("I didn't understand, make sure there is no typo.")
        i("Press [ENTER] to continue: ")
    