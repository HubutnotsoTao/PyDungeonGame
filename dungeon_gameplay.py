#Dungeon System
import random 

def dive():
    #import variables from main game
    import main_game
    player_name = main_game.player_name
    weapon = main_game.weapons
    enemy = main_game.enemy
        
    print("-"*40)

    #Class selection
    class_choice = input("Choose your class: ").lower()

    #Set player attributes
    player_stats = main_game.player_class.get(class_choice)
    player_health = player_stats["health"]
    player_speed = player_stats["speed"]
    player_defense = player_stats["defense"]

    print("-"*40)
    print(f"Your class is {class_choice}\nYou shall be known as {player_name} the {class_choice}")
    print("-"*40)
    print(f"Your attributes are\nHealth: {player_health}\nSpeed: {player_speed}\nDefense: {player_defense}")

    #Entering Dungeon
    print("-"*40)
    print(f"You are now entering the dungeon...\n")
    print("-"*40)
    print(f"{player_name} has entered the dungeon!\n")
    dungeon_floor = 0
    dungeon_hours = 15

    while True:
        #Dungeon procedures and updates
        print("-"*40)
        print("Inside the dungeon...\n")
        print(f"You are currently at floor {dungeon_floor}\n")
        print(f"{dungeon_hours} hours left until dungeon collapses")
        print("-"*40)
        print(f"{main_game.player_name}")
        print(f"{main_game.player_name} ")

        enemy_list = ("slime","goblin","orc")
        enemy_spawn = random.choice(list(enemy.keys()))

        enemy_health = main_game.enemy.get(enemy_spawn)["health"]
        enemy_speed = main_game.enemy.get(enemy_spawn)["speed"]
        enemy_defense = main_game.enemy.get(enemy_spawn)["defense"]


        if dungeon_floor >= 10:
            print(f"Congratulations! {player_name} the {player_class} has cleared the dungeon!")
            break
        else:
            print(f"You have cleared floor {dungeon_floor}!")
            dungeon_choice = input("[dive] Keep going?\n[rest] Rest for one hour\n[flee] Flee from the dungeon!")

            dungeon_floor += 1



def shop():
    print(f"")

def flee():
    import main_game
    print(f"Farewell {main_game.player_name}, your journey ends here.")
    return "flee"