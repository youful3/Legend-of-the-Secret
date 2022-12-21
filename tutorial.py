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
def write(intro, hunt):
    f.write("intro = " + str(intro) + "\n" + "hunting = " + str(hunt))
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
 write(True, False)
 t(3)

write(True, False)

if hunting == False:
    for option in home:
        print(option)