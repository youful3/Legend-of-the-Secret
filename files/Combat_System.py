from Functions import *
from Character_Enemies import *
from Save import *
from Weapons import *
import time, os
from Combat_com_com import *

f = open("files\Combat_com_com.py", "w")
f.write(f"""from Weapons import *
enemyType = {__enemy__}
enemyNum = {enemy_num}
weaponUse = {use_weapon}""")
from Combat_com_com import *