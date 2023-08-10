import os
import random

HP =  40
MHP = 40
Coins = 10
Lvl = 1
XP = 0
NXP = 10
DMG = 6
DEF = 3
INV = ["HealthPotionLvl1","HealthPotionLvl1","HealthPotionLvl1"]
Wep = "WoodSword"
Wepbook = {"WoodSword":3,"StoneSword":7}
LvlbookH = {1:40,2:45,3:50,4:60,5:70}
LvlbookD = {1:5,2:6,3:8,4:10}
LvlbookX = {1:10,2:15,3:20,4:30,5:40}
INVbook = {"HealthPotionLvl1":"H20"}
Gems = 0
forrestname = ["Mushroom","Wolf","Evil Sapling","Giant Spider"]

Name = input("What is Your name?\n ")
os.system("clear")

#Functions
def Lvlcheck():
  global Lvl
  global DMG
  global HP
  global MHP
  global NXP
  NXP = LvlbookX[Lvl]
  MHP = LvlbookH[Lvl]
  DMG = LvlbookD[Lvl]
  
def Use(org,str):
  global HP
  global MHP
  global INVbook
  original = HP
  if str.startswith("H"):
    str = str.replace("H","")
    HP += int(str)
    if HP > MHP:
      HP = MHP 
    print(f"You used the {org} and healed {HP-original} health!")
    print(f"You have {HP}/{MHP} HP")

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
  global INV
  global INVbook
  defense = 0
  earn = 0
  invalid = 0
  win = 0
  f_INV = ""

  while True:
    thing = []
    id = []
    print(f"Your HP: {HP}/{MHP}")
    print(f"{Name}'s HP: {EHP}/{EMHP}")
    print(f"Weapon: {Wep}")
    print("Options: 1 = Attack 2 = Defend 3 = Inventory")
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

    elif inp == "3":
      pass
      if len(INV) == 0:
        invalid = 1
        input("Your inventory is empty")

      else:
        print("Options:")
        if INV.count("HealthPotionLvl1") != 0:
          id.append("HealthPotionLvl1")
          f_INV = INV.count("HealthPotionLvl1")
          print(f"{len(id)}. HealthPotionLvl1({f_INV})")
          
        use = input("What item do you use?(select the number)")
        if use.isnumeric() != False or use.strip() != "":
          use = int(use)-1
          
        else:
          invalid = 1
        for i in range(len(id)):
          thing.append(i)
        
        if use in thing:
          os.system("clear")
          INV.remove(id[use])
          Use(id[use],INVbook[id[use]])
        else:
          invalid = 1 
          input("That does not exist")
          os.system("clear")
          
        
    else: 
      invalid = 1

    if invalid == 0:
      dmg = EDMG - defense + random.randint(-2,1)
      if dmg <= 0:
        dmg = 0
      input(f"The {Name} attacks you dealing {dmg} damage!")
      if defense >= 1:
        input(f"The {Name} gets hurt dealing {defense} damage to itself")
        EHP -= defense
        if EHP < 1:
          input(f"You beat the {Name}!")
          win = 1
          break
        
      if dmg  >= 1:
        HP = HP - dmg
      else:
        print(f"The {Name} completely misses.")

    if HP <= 0:
      break
  os.system("clear")
  if win == 1:
    earn = int((EMHP + EDMG) / 2)
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
      print("You leveled up!")
      Lvlcheck()
    input(f"You have {XP}/{NXP} XP and you're level {Lvl}!")
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

def Forrest(l): 
  global forrestname
  yeet = True
  aH = l*7 + 2
  aH = random.randint(aH-2,aH+2)
  aD = int(aH/3)
  if l == 1:
    n = "your"
  else:
    n = "the"
  input(f"You enter {n} forrest")
  while yeet:
    aH = random.randint(aH-2,aH+2)
    aD = int(aH/3)
    H = random.randint(aH-2,aH+2)
    D = random.randint(aD-2,aD+2)
    input("You encounter a creature!")
    Battle(forrestname[random.randint(1,len(forrestname)-1)],H,H,D)
    if input("do you continue?(y/n)").upper().strip() != "Y":
      input(f"You leave {n} forrest")
      yeet = False
      
  
  
  
#Code
input('''
-----AIM-----
Travel the land upgrading yourself along the way.
You will have to fight fierce and terrifing monsters leading up the to the final boss. Good luck and don't die.

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
input("At least you took some healing potions")
os.system("clear") 



while True:
  if Battle("Mushroom",15,15,6) == None:
    break

os.system("clear")
input("You: *arrives home*")
input("that was weird, you say to yourself")
input("was that strange man right after all? ")
input("You decide to go to the blacksmith\n")
os.system('clear')
print("Blacksmith: An old guy")
input("left this stone sword for you.")
input("You: Oh thanks! \n")
input("New weapon: StoneSword")
Wep = "StoneSword"
input(f"new damage: {DMG + Wepbook[Wep]}")
input("You decide to head back home and rest until morning")
os.system("clear")
input("You wake up in some strange place that's covered in thick fog")
input("You see a strange figure with glowing eyes in the distance, and you call out to it")
input("You: Hello?")
input("???: ...")
input("before you can ask again he dashes towards you")
os.system("clear")
input("you open your eyes sweating")
input("It was just a bad dream, you say in relief")
input("press enter to leave the house")
HP = MHP
os.system("clear")
#Forrest
input("You decide to train in the forrest")
Forrest(1)
HP=MHP