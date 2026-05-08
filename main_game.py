#Made by Justine Ignacio
#Simple Dungeon Game
import random
import dungeon_gameplay
import combat_system

#Player class dictionary [Player Health],[Player Speed],[Player Defense] max 100
#50 is the average
#Every class has 170 points to allocate
#Refer to Skill section in combat_system
player_class = {
    "knight" : {
        "health" : 70,
        "speed" : 50,
        "defense" : 50
    },

    "paladin" : {
        "health" : 90,
        "speed" : 20,
        "defense" : 60
    },

    "warrior" : {
        "health" : 65,
        "speed" : 75,
        "defense" : 30
    }
}

#Weapon dictionary [weapon_damage],[weight] max 99 (speed = player_speed - weight)
weapons = {
    "sword" : {
        "damage" : 25,
        "weight" : 15
    },
    "axe" : {
        "damage" : 35,
        "weight" : 30,
    },
    "dagger" : {
        "damage" : 15,
        "weight" : 5,
    }
}

#Enemy dictionary
enemy = {
    "slime" : {
        "health" : 40,
        "speed" : 10,
        "defense" : 20,
    },
    "goblin" : {
        "health" : 50,
        "speed" : 35,
    },
    "orc" : {
        "health" : 70,
        "speed" : 20,
        "defense" : 50
    }
}

#Main Menu dungeon_gameplay
paths = {
    "dive" : dungeon_gameplay.dive,
    "shop" : dungeon_gameplay.shop,
    "flee" : dungeon_gameplay.flee
}

#Function 
combat = {
    "attack" : combat_system.attack,
    "block" : combat_system.block
}

class_choice = ""

player_name = ""
choice = ""



#Player greeting
player_name = input("Name yourself: ")
print(f"\nGreetings {player_name}\n Welcome to the Dungeon!")

while True:
        print(f"-"*40)
        print("[Dive] Enter the Dungeon\n[Shop] Enter the Shop\n[Flee] Return to your Hometown") #Paths
        choice = input("Choose your path: ").lower()

        if choice.lower() != "flee":
            dungeon_gameplay.paths.get("choice")
            
        elif choice.lower() == "flee":
            dungeon_gameplay.flee()
            break
        else:
            paths.get(choice, lambda: print("Thou has chosen a path long forgone, step not into oblivion."))()

        
       

