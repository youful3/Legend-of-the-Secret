from Classes import *

John = Npc("John", "Merchant")

#The Machines:
C_Robot = BasicEnemy("C_bot", "Corrupted Robot", "Mercenary", "The Machines", 10, 2, 5)
Cyborg = BasicEnemy( "Cyborg", "Cyborg", "Hunter", "The Machines", 25, 4, 12)
Hybrid = Monster("Hybrid", "Hybrid", "Hive Mind", "The Machines", 30, 10, 16, "Canon Charge", 18)
