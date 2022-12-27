from Functions import *

#Class for NPCs
class Npc:
	def __init__(self, name, job):
		self.name = name
		self.job = job

#YOU ARE RAINBOWWW
#WHICH IS FAX

#Class for Basic Enemy
class BasicEnemy(Npc):
	def __init__(self, name, job, ene_m, hp, atk_mi, atk_ma):
		super().__init__(name, job)
		self.ene_m = ene_m
		self.hp = hp
		self.a_hp = adva(hp)
		self.atk_mi, self.atk_ma = atk_mi, atk_ma

#Class for Monster/Boss
class Monster(BasicEnemy):
	def __init__(self, name, job, ene_m, hp, atk_mi, atk_ma, super_name, super_dmg):
		super().__init__(name, job, ene_m, hp, atk_mi, atk_ma)
		self.a_hp, self.a_name = adva(hp), "Advanced " + name
		self.super_name = super_name
		self.super_dmg = super_dmg

#Class for FinalEnemy
class FinalEnemy(Monster):
	def __init__(self, name, job, ene_m, hp, atk_mi, atk_ma, super_name, super_dmg, QQQ):
		super().__init__(name, job, ene_m, hp, atk_mi, atk_ma, super_name, super_dmg)
		self.QQQ = QQQ
	
class Weapon():
	def __init__(self, name, damage, defense):
		self.name = name
		self.damage = damage
		self.defense = defense