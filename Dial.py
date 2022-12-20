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