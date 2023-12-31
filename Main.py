import os
import random

colour = {
  "W": "\033[0m", 
  "GRN": "\033[32m", 
  "P": "\033[35m", 
  "Y": "\033[33m",
  "R": "\033[31m",
  "B":"\033[36m",
  "GRY":"\033[30m"
}
HP =  40
MHP = 40
Coins = 10
Lvl = 1
XP = 0
NXP = 10
DMG = 3
DMGMod = 0
DEF = 4
DEFMod = 0
INV = ["HealthPotionLvl1","HealthPotionLvl1","HealthPotionLvl1"]
Wep = "WoodSword"
Wepbook = {"WoodSword":3,"StoneSword":7}
LvlbookH = {1:40,2:45,3:50,4:60,5:70,6:80}
LvlbookD = {1:4,2:5,3:6,4:7,5:9,6:10}
LvlbookX = {1:15,2:20,3:25,4:30,5:40,6:55}
INVbook = {"HealthPotionLvl1":"H30","MiniBomb":"B25"}
forrestname = ["Mushroom","Wolf","Evil Sapling","Giant Spider"]
lootlvl1 = ["HealthPotionLvl1","MiniBomb"]
ItemDesc = {
  "HealthPotionLvl1":": Heals 20 HP",
  "MiniBomb":": Deals 25 damage"
}
ItemCost = {
  "HealthPotionLvl1":4,
  "MiniBomb":6
}

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
  global colour
  B = colour["B"]
  W = colour["W"]
  G = colour["GRN"]
  R = colour["R"]
  original = HP
  if str.startswith("H"):
    str = str.replace("H","")
    HP += int(str) 
    if HP > MHP:
      HP = MHP 
    print(f"You used the {G}{org}{W} and healed {G}{HP-original}{W} health!")
    print(f"You have {G}{HP}/{MHP}{W} HP")
    return 0
  elif str.startswith("B"):
    str = str.replace("B","")
    dmg = int(str)
    print(f"You threw the {B}{org}{W} and dealt {R}{dmg}{W} damage!")
    return dmg

def Battle(Name,EHP,EDMG):
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
  global lootlvl1
  global colour
  B = colour["B"]
  W = colour["W"]
  G = colour["GRN"]
  R = colour["R"]
  EMHP = EHP
  defense = 0
  earn = 0
  invalid = 0
  win = 0
  f_INV = ""

  while True:
    thing = []
    id = []
    
    print(f"\nYour HP: {G}{HP}/{MHP}{W}")
    print(f"{Name}'s HP: {R}{EHP}/{EMHP}{W}")
    print(f"Weapon: {Wep}")
    print(f"Options: 1 = Attack 2 = Defend {B}3 = Inventory{W}")
    inp = input("What do you do?: ").strip()
    os.system("clear")
    
    if inp == "1": 
      invalid = 0
      defense = 0 
      f = EHP
      EHP -= random.randint(DMG+Wepbook[Wep],DMG+2+Wepbook[Wep])
      input(f"You attack the {Name} dealing {R}{f-EHP}{W} damage!")
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
        print("0.Leave")
        #Health
        if INV.count("HealthPotionLvl1") != 0:
          id.append("HealthPotionLvl1")
          f_INV = INV.count("HealthPotionLvl1")
          print(f"{len(id)}. HealthPotionLvl1({f_INV})")
        #Bomb
        if INV.count("MiniBomb") != 0:
          id.append("MiniBomb")
          f_INV = INV.count("MiniBomb")
          print(f"{len(id)}. MiniBomb({f_INV})")
          
        use = input("What item do you use?(select the number)")
        if use.isnumeric() != False or use.strip() != "":
          use = int(use) -1
          
        else:
          invalid = 1
        for i in range(len(id)):
          thing.append(i)
        
        if use in thing:
          os.system("clear")
          INV.remove(id[use])
          EHP -= Use(id[use],INVbook[id[use]])
          
          if EHP < 1:
            input(f"You beat the {Name}!")
            win = 1
            break
        elif use == 0:
          input("press enter to go back")
          invalid = 1
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
      input(f"The {Name} attacks you dealing {R}{dmg}{W} damage!")
      if defense >= 1:
        input(f"The {Name} gets hurt dealing {R}{defense}{W} damage to itself")
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
    loot = None
    if random.randint(1,5) == 5:
      loot = lootlvl1[random.randint(0,len(lootlvl1)-1)]

    
    earn = int((EMHP + EDMG) / 4)
    XE = random.randint(earn-1,earn+2) + 2
    CE = random.randint(earn-1,earn+2)
    Coins += CE
    XP += XE
    input("You win!")
    input(f"You earned {Y}{CE}{W} Coins")
    input(f"You earned {Y}{XE}{W} XP")
    if loot != None:
      input(f"The {Name} dropped an item!")
      input(f"+1 {B}{loot}{W}")
      INV.append({loot})
    input(f"You now have {Y}{Coins}{W} coins")
    if XP > NXP:
      XP -= NXP
      Lvl += 1
      print("You leveled up!")
      Lvlcheck()
    input(f"You have {Y}{XP}/{NXP}{W} XP and you're {B}level {Lvl}!{W}")
    input("Press enter")
    return None
  else:
    print(f"You lost some of your {Y}coins{B}")
    Coins -= random.randint(2,EDMG)
    if Coins <= 0:
      Coins = 0
    print(f"You have {Y}{Coins}{W} coins")
    input("Press enter")
    return 1

def Forrest(l): 
  global forrestname
  yeet = True
  aH = l*7 +9
  aH = random.randint(aH-3,aH+3)
  aD = int(aH/3)

  input("You enter the forrest")
  while yeet:
    aH = random.randint(aH-2,aH+2)
    aD = int(aH/3)
    H = random.randint(aH-1,aH+5)
    D = random.randint(aD-1,aD+3)
    input("You encounter a creature!")
    os.system("clear")
    Battle(forrestname[random.randint(1,len(forrestname)-1)],H,D)
    os.system("clear")
    yeetb = True
    while yeetb:
      stay = input("do you continue?(n to go home and y to stay)").upper().strip()
      if stay == "N":
        input("You leave the forrest and go to the blacksmith")
        yeetb = False
        yeet = False
      elif stay == "Y":
        input("You stay")
        os.system("clear")
        yeetb = False
        
      else:  
        input("Invalid.")
        os.system("clear")
      
def Shop():
  global Coins
  global INV
  global INVDesc
  global INVCos
  
#Colour Variables
B = colour["B"]
W = colour["W"]
G = colour["GRN"]
R = colour["R"]
Y = colour["Y"]
#Code


input(f'''
-----AIM-----
Travel the land {B}upgrading{W} yourself along the way.
You will have to fight fierce and terrifing {R}monsters{W} leading up the to
the {R}final boss{W}. Good luck and don't die.

-----HOW TO PLAY-----
{G}HP = health{W}
{B}Lvl = your character's Level{W}
{Y}XP = your progress to the next level{W}
when given a choice select the given number.
when fighting a {R}monster{W}, you will earn {Y}coins{W} and {Y}XP{W}. 
You can use these {Y}coins{W} to buy {B}loot{W} to {B}upgrade{W} yourself.

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
input("half way to the village") 
input("you come across a evil mushroom that looks like it wants to hurt you")
input("You prepare for battle thinking the old man wasn't so crazy after all.")
input("At least you took some healing potions")
os.system("clear") 



while True:
  if Battle("Mushroom",15,6) == None:
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
HP = MHP
