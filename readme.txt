o----------Dungeon Game WIP----------o

How it works

o~~~~Dungeon Gameplay code
-Run the main_game.py to play the Game
-dictionaries for player_class, weapons, enemy, and game_state is stored in main_game.py
-main_game.py only runs functions imported from modules

ALL gameplay functions so far is stored in dungeon.gameplay.py (5/8/2026)
-game_state dictionary stores everything the game needs to run instead of global functions for cleaner code


o~~~~Dungeon Dive loop
-Input Name
-Choose a path
-Choose your Class
-(TBD) Equip a weapon 
-Enter Dungeon
-You have 15 hours to clear
    Clearing one floor takes 1 hour then moves to next floor
    Rest takes one hour and you stay in the room
-(TBD) Rest SHOULD only be available after clearing the floor (Add max health system based on player_class)


o~~~~TO BE ADDED
Inside dungeon_gameplay.py 
    Run functions from combat_system.py to facilitate PVE

Finish combat loop in dungeon_gameplay.py

Finish inventory, currency, and shop system

o----------Dungeon Game Progress----------o
As of 5/8/2026
o~~~~Main Game

DONE:
Greeting
Player Classes
Weapons
Game State
Enemies
Dungeon Travel (fight, rest, flee)

WIP:
Access inventory inside dungeon
Enter Shop
    The entire shop lol
Inventory system
    Weapon equipping
    Armor equipping (bonus feature)
    Potions
        Health potions (add hp without consuming 1 hour like rest)
Enemy drops 
    gold 
    rare weapons perhaps?
Boss enemy
    Add boss enemy on floor 5 and floor 10
    Boss enemies should have atleast 150 HP or something ridiculous lol


o~~~~Combat

DONE:
Attack (basic subtraction) to be updated
Block (basic subtraction) to be updated

WIP:
Speed (Order of attacks)
Skills, Cooldown, and Energy system

Shop

DONE:
NEIN

WIP:
List of items
Currency system
Importing bought items into game_state : "inventory"

