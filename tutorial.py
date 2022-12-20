from Classes import *
from Functions import *
from Enemies import *
from tutorial_save import *
import time

def t(number):
    time.sleep(number)
def pr(stri):
    print(stri)
def di(stri):
    print(f"You: {stri}")

if intro == True:
    t(3)
    pr("Silence...")
    t(3)
    pr("Your eyes are wide open...")
    t(3)
    di("That was a strange dream")
    t(3)
    di("But it's time to wake up now.")