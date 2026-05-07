#Made by Justine Ignacio
#Simple Dungeon Game
import random
import traversal
import combat_system
import shop_currency_system

#Player class dictionary [Player Health],[Player Speed],[Player Defense] max 100
#50 is the average
#Every class has 170 points to allocate
#Refer to Skill section in combat_system
player_class = {
    "knight" : (70, 50, 50),
    "paladin" : (85, 25, 60),
    "warrior" : (65, 75, 30)
}

#Weapon dictionary [weapon_damage],[weight] max 99 (speed = player_speed - weight)
weapons = {
    "sword" : (25,15),
    "axe" : (35,30),
    "dagger" : (10, 5)
}

#Enemy dictionary
enemy = {
    "slime" : [40, 10, 20],
    "goblin" : [50, 35, 30],
    "orc" : [70, 20, 50]
}

#Main Menu traversal
paths = {
    "dive" : dive,
    "shop" : shop,
    "flee" : flee
}

#Function 
combat = {
    "attack" : attack,
    "block" : block
}

class_choice = ""
enemy_list = ("slime", "goblin", "orc")

#Global variables
player_health, player_speed, player_defense = player_class.get(class_choice)
enemy_health, enemy_speed, enemy_defense = enemy.get(enemy_spawn)

#Player greeting
player_name = input("Name yourself: ")
print(f"\nGreetings {player_name}\n Welcome to the Dungeon!")

choice = ""

while True:

    print(f"-"*40)
    print("[Dive] Enter the Dungeon\n[Shop] Enter the Shop\n[Flee] Return to your Hometown") #Paths
    choice = input("Choose your path: ")
    paths.get(choice, lambda: print("Thou has chosen a path long forgone, step not into oblivion.")) #Will decide the path, lambda function to catch invalid inputs

