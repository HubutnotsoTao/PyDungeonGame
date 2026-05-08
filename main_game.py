#Made by Justine Ignacio
#Simple Dungeon Game
import dungeon_gameplay
import combat_system
import shop_system


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

#Game state dictionary
game_state = {
    "player": {
        "name": "",
        "class": "",
        "health": 0,
        "speed": 0,
        "defense": 0
    },

    #Player Currency
    "currency": {
        "gold": 100
    },

    #Player Inventory
    "inventory": {
        "weapons": []
    },

    "floor": 0,
    "hours": 0,
    "enemy": {}
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
choice = ""

#Player greeting
player_name = dungeon_gameplay.start_game()
game_state["player"]["name"] = player_name

while True:
    print("-" * 40)
    print("[Dive] Enter the Dungeon\n[Shop] Enter the Shop\n[Flee] Return")
    print("-" * 40)
    choice = input("Choose your path: ").strip().lower()

    match choice:
        case "dive":
            paths["dive"](game_state, player_class, weapons, enemy)

        case "shop":
            paths["shop"](game_state)

        case "flee":
            paths["flee"](game_state)
            break

        case _:
            print("Thou has chosen a path long forgone, step not into oblivion.")

        
       

