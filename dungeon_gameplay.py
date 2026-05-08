#Dungeon System
import random 
import sys

def start_game():
    name = input("Name yourself: ")
    print(f"\nGreetings {name}\nWelcome to the Dungeon!")
    return name

def dive(game_state, player_class, weapons, enemy):

    print("-" * 40)

    class_choice = input("Choose your class: ").lower()

    player_stats = player_class.get(class_choice)

    if not player_stats:
        print("Choose an existing class!")
        return

    #Store stats into game_state
    game_state["player"]["class"] = class_choice
    game_state["player"]["health"] = player_stats["health"]
    game_state["player"]["speed"] = player_stats["speed"]
    game_state["player"]["defense"] = player_stats["defense"]

    print("-" * 40)
    print(f"Your class is {class_choice}")
    print(f"You are {game_state['player']['name']} the {class_choice}")
    print("-" * 40)

    print(f"Stats:\nHealth: {game_state['player']['health']}\nSpeed: {game_state['player']['speed']}\nDefense: {game_state['player']['defense']}")

    print("-" * 40)
    print("You are entering the dungeon...")

    game_state["floor"] = 0
    game_state["hours"] = 15

    # Main game loop
    while True:

        print("-" * 40)
        print(f"Floor: {game_state['floor']}")
        print(f"Hours left: {game_state['hours']}")

        enemy_spawn = random.choice(list(enemy.keys()))
        enemy_stats = enemy[enemy_spawn]

        # store enemy in state
        game_state["enemy"] = {
            "name": enemy_spawn,
            "health": enemy_stats["health"],
            "speed": enemy_stats["speed"],
            "defense": enemy_stats.get("defense", 0)
        }

        print(f"Enemy: {enemy_spawn}")

        # 
        if game_state["floor"] >= 10:
            print(f"The Boss has been vanquished! {game_state['player']['name']} cleared the dungeon!")
            break

        choice = input("[fight] [rest] [flee]: ").lower()

        if choice == "flee":
            print("You fled the dungeon!")
            break

        elif choice == "rest":
            game_state["player"]["health"] += 30
            game_state["hours"] -= 1

        elif choice == "fight":
            game_state["floor"] += 1

        else:
            print("Invalid choice!")



def shop(player_name): #Enter shop WIP
    print(f"")

def flee(game_state): #Flee from the dungeon
    print(f"Farewell {game_state['player']['name']}, your journey ends here.")
    return "flee"