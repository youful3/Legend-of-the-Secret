from Functions import *
from Character_Enemies import *
from Save import *
from Weapons import *
import time, os

com_data = open("files\Combat_com_com.txt", "r")
use_weapon = com_data.read(3)
__enemy__ = com_data.read(1)
enemy_num = com_data.read(2)
f = open("files\Combat_com_com.py", "w")
f.write(f"""from Weapons import *
enemyType = {__enemy__}
enemyNum = {enemy_num}
weaponUse = {use_weapon}""")
from Combat_com_com import *