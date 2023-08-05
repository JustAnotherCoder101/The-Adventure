import os
import random

HP =  50
MHP = 50
Coins = 10
Lvl = 1
XP = 0
NXP = 10
DMG = 5


Name = input("What is Your name?\n ")
os.system("clear")

#Functions
def Battle(Name,EHP,EMHP):
  global Coins
  global HP
  global MHP





#Code
input('''
-----AIM-----
travel the land upgrading yourself along the way
fighting fierce and terrifing monsters leading up the to the
Darklord good luck don't die

-----HOW TO PLAY-----
HP = health
Lvl = your character's Level
XP = your progress to the next level
when given a choice select the given number.
when fighting a monster, you will earn coins and XP. 
You can use these coins to buy loot to upgrade yourself.

That's all for now



press enter
''')
os.system("clear")
input("Old Man:You will have to save the land from the darkness ")
input("You: Ok? ")
input("Old Man: I'l be off for my travels good luck")
input("press enter to walk into town ")
os.system("clear")
input('half way there you come across a evil mushroom you decide to fight')
os.system("clear") 
Battle("Mushroom",20,20)


