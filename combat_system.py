#Basic Combat Functions
def attack(atk,dfns):
    dmg = 0
    return max(0, atk - dfns)

def block(atk,dfns):
    dmg = 0
    return max(0, atk - (dfns*1.7))

def combat_speed(player_speed, weapon_weight, enemy_speed):
    class_speed = player_speed - weapon_weight
    if class_speed > enemy_speed:
        print(f"{player_name} hits {enemy_name} first for {dmg} damage!")
    elif class_speed == enemy_speed:
        print("haha") #50/50 random chance
    else:
        print(f"{enemy_name} hits {player_name} first for {dmg} damage")


#Skills
def heavy_attack(atk,dfns):
    dmg = 0
    return max(0, (atk*1.5)-dfns)
    print(f"{player_name} has taken {dmg} damage!")

    #def life_drain(atk,dfns): #WIP
    #    dmg = 0
    #    health = health + (atk/2)
    #    return max(0, (atk*.8)-dfns))

def excalibur(atk,dfns): #LOL 
    dmg = 0
    return max(0, (atk*2)-(dfns/10)),

#Function Testing
#atk = float(input("Input Attack Damage: "))
#dfns = float(input("Input Defense Amount: "))
#action = input("Choose your action: ")
#print(f"You have received {(atk,dfns)} damage!")
