import os
import random

HP =  50
MHP = 50
Coins = 10
Lvl = 1
XP = 0
NXP = 10
DMG = 5
DEF = 2
Wep = "WoodSword"
Wepbook = {"WoodSword":2}

Name = input("What is Your name?\n ")
os.system("clear")

#Functions
def Battle(Name,EHP,EMHP,EDMG):
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
  Win = 0
  yeet = True
  while yeet:
    print(f"Your HP: {HP}/{MHP}")
    print(f"{Name}'s HP: {EHP}/{EMHP}")
    print(f"Weapon: {Wep}")
    print("Options: 1 = Attack 2 = Defend")
    inp = input("What do you do?: ").strip()
    os.system("clear")
    
    if inp == "1": 
      invalid = 0
      defense = 0 
      EHP -= random.randint(DMG-2,DMG+2)
      input(f"You attack the {Name}")
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
      input(f"The {Name} attacks you!")
      dmg = EDMG - defense
      if dmg  >= 1:
        HP = HP - dmg
      else:
        print(f"The {Name} completely misses.")

    if HP >= 0:
      break
  os.system("clear")
  if win == 1:
    earn = (EMHP + EDMG) / 2
    XE = random.randint(earn-1,earn+2) + 2
    CE = random.randint(earn-1,earn+2)
    input("You win!")
    input(f"You earned {CE} Coins")
    input(f"You earned {XE} XP")
    if XP > NXP:
      XP -= NXP
      Lvl += 1
      print(f"You leveled up to level {Lvl}!")
    input("Press enter")
    return None
  else:
    print("You lost some of your coins")
    Coins -= randint(5,EDMG/2)
    if Coins <= 0:
      Coins = 0
    print(f"You have {Coins} coins")
    input("Press enter")
    return 1
    
#Code
input('''
-----AIM-----
Travel the land upgrading yourself along the way
fighting fierce and terrifing monsters leading up the to the
Darklord good luck and don't die.

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
input("Old Man: You will have to save the land from the darkness ")
input("You: Ok? ")
input("Old Man: I'l be off for my travels good luck")
input("You are very confused. What does he mean?")
input("press enter to walk into town ")
os.system("clear")
input("half way to the village you come across a evil mushroom that you must fight")
os.system("clear") 

while True:
  if Battle("Mushroom",20,20,6) == None:
    break
    
print("You arrive at the village.")

