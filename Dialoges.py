from dial_save import *
from Save import *
import time, os

def v1(strs):
    input('You: ' + strs)
    print("")

def v2(strs):
    input('John: ' + strs)
    print("")

def c(strs):
    input(strs)
    print("")

def write(first, first_digit):
    f = open("dial_save.py", "w")
    f.write("first = " + str(first) + "\n")
    f.write("first_digit = '" + str(first_digit) + "'" + "\n")
    f.close()

def transition():
    os.startfile("transition.py")
    exit()

print("")
input("Note: Make sure to press [ENTER] after each dialogue/line :D ")
print("")
time.sleep(2)

if first == True:
  if first_digit == "a":
    write("True", "a")
    c("Returning home, even then trouble couldn't leave you be, it seems it liked to find you...")
    c("Was it trouble that found you, or was it you who found trouble?")
    v2(f"Hey {name}!")
    v1("What, who? Oh, it's you again.")
    v2("I have 2 things to say: ")
    v1("You can speak.")
    v2("Number 1: You look like crap.")
    v1("Yeah, I haven't slept in a while.")
    v2("Number 2: I found a bunker, like the old ones.")
    v1("Wait wait wait: what do you mean the old one?")
    v2("No joke.")
    v1("Are you talking about the one in the jungle? Come on man.")
    v2("Not that one, everyone knows about that one, but there's one near it.")
    v1("What? Where? Why did no one find it?")
    v2("It's 3 miles north-east of the bunker in the jungle, it was hidden under some fake forest flooring.")
    v1("Huh, but why?")
    v2("What?")
    v1("Why'd you tell me?")
    v2("You still owe me for that tiger, remember?")
    v1("Good point, so what do you want me to do? Come with you? You scared?")
    v2("Well I wouldn't put it that way...")
    v1("Is little kitten scared?")
    v2("Okay you can stop now.")
    v1("Scaredy cat.")
    v2("You coming or not?")
    v1("Sure, why not.")
    time.sleep(4)
    c("You kept forgetting, I still remember.")
    c("You shall remember only one thing:")
    time.sleep(2)
    print("Humanity has moved on.")
    time.sleep(4)
    print("Technology is no more")
    time.sleep(4)
    input("Only the zero energy remains.")
    write("True", "b")
    transition()
  if first_digit == "b":
    pass