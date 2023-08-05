import os
import random

HP =  40
MHP = 40
Coins = 10
Lvl = 1
XP = 0
NXP = 10
DMG = 5
DEF = 2
Wep = "WoodSword"
Wepbook = {"WoodSword":3}
LvlbookH = {1:40,2:45,3:50,4:60,5:70}
LvlbookD = {1:5,2:6,3:8,4:10}

Name = input("What is Your name?\n ")
os.system("clear")

#Functions
def Lvlcheck():
  global Lvl
  global DMG
  global HP
  global MHP
  MHP = LvlbookH[Lvl]
  HP = MHP
  DMG = LvlbookD[Lvl]
def Battle(Name,EHP,EMHP,EDMG):
  Lvlcheck()
  global NXP
  global XP
  global Coins
  global HP
  global MHP
  global Lvl
  global DMG
  global Wep
  global Wepbook
  global DEF
  earn = 0
  Tdmg = DMG + Wepbook[Wep]
  invalid = 0
  win = 0
  while True:
    print(f"Your HP: {HP}/{MHP}")
    print(f"{Name}'s HP: {EHP}/{EMHP}")
    print(f"Weapon: {Wep}")
    print("Options: 1 = Attack 2 = Defend")
    inp = input("What do you do?: ").strip()
    os.system("clear")
    
    if inp == "1": 
      invalid = 0
      defense = 0 
      f = EHP
      EHP -= random.randint(DMG-2,DMG+2)
      input(f"You attack the {Name} dealing {f-EHP} damage!")
      if EHP < 1:
        input(f"You beat the {Name}!")
        win = 1
        break
    elif inp == "2":
      invalid = 0
      input("You brace Yourself")
      defense = random.randint(DEF - 1,DEF + 2)
    else: 
      invalid = 1

    if invalid == 0:
      dmg = EDMG - defense + random.randint(-2,1)
      input(f"The {Name} attacks you dealing {dmg} damage!")
      
      if dmg  >= 1:
        HP = HP - dmg
      else:
        print(f"The {Name} completely misses.")

    if HP <= 0:
      break
  os.system("clear")
  if win == 1:
    earn = (EMHP + EDMG) / 2
    XE = random.randint(earn-1,earn+2) + 2
    CE = random.randint(earn-1,earn+2)
    Coins += CE
    XP += XE
    input("You win!")
    input(f"You earned {CE} Coins")
    input(f"You earned {XE} XP")
    input(f"You now have {Coins} coins")
    if XP > NXP:
      XP -= NXP
      Lvl += 1
      print(f"You leveled up to level {Lvl}!")
      Lvlcheck()
    input(f"You have {XP}/{NXP} and you're level {Lvl}!")
    input("Press enter")
    return None
  else:
    print("You lost some of your coins")
    Coins -= random.randint(2,EDMG)
    if Coins <= 0:
      Coins = 0
    print(f"You have {Coins} coins")
    input("Press enter")
    return 1
    
#Code
input('''
-----AIM-----
Travel the land upgrading yourself along the way.
You will have to fight fierce and terrifing monsters leading up the to the Darklord good luck and don't die.

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
input("You walk out of the forest to head back home when a old man comes to talk to you ")
os.system("clear")
input("Old Man: You will have to save the land from the darkness. ")
input("You: What. ")
input("Old Man: I'l be off for my travels good luck.")
input("You laugh it off, 'He's lost his marbles!' you say to yourself")
input("press enter to walk into town ")
os.system("clear")
input("half way to the village you come across a evil mushroom that looks like it wants to hurt you")
input("You prepare for battle thinking the Old man wasn't so crazy after all.")
os.system("clear") 

while True:
  if Battle("Mushroom",15,15,5) == None:
    break
    
print("You arrive at the village.")

