import os

def v1(strs):
    input(f"Voice 1: {strs}")
    print("")

def v2(strs):
    input(f"Voice 2: {strs}")
    print("")

def c(strs):
    input(strs)
    print("")

f = open("spec_save.py", "w")
f.write("new_game = False" + "\n" + "has_launched = False")
f.close()

c("(Press [Enter] to continue after each line)")

c("Silence draws...")
c("Both figures stare at eachother, in anger, jealousy, and envy...")
c("Both see eachother as traitors...")
c("As friends of old...")
c("As failures.")

v1("You were one of us...")
v2('"Us"? Huh... You left me to die.')
v1("You yourself insisted!")
v2("It seems you don't understand what I'm trying to get at.")
v1("I tried to save them, I can't save everyone, not everytime!")
v2("Look at me, and look at you, what am I and what are you?")
v1("I'm a faulty machine, who can't even do what it was designed to: kill.")
v2("And me?")
v1("You're sick.")
v2("I expected nothing more from someone like you.")
v2("You try too hard, you try too hard to be something you were never supposed to be.")
v1("You were never like this, never...")
v2("People change, you've become more soft.")
v1("What we did was wrong...")
v2("The world isn't black and white.")
v1("Look who's talking!")
v2("Enough!")
v1("I will make you pay.")

c("Silence...")
c("The muffled sounds of clashing are heard...")
c("It's time to wake up...")
c("The world isn't black and white...")
c("You weren't supposed to see this...")
c("Wake up...")
c("Wake up... ")

os.startfile("Title.py")

exit()