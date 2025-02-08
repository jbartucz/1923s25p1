import os
import math
import random

"""
Function: Class used for weapons
Parameters: String, Integer, Integer(Can be left blank to have no cost if not shop item)
"""


class weapon:      #I know we did not cover classes/objects in class but I do not know how to do this efficiently without utilizing classes and I'm used to Java
    def __init__ (self, name, damage, cost = 0):
        self.name = name
        self.damage = damage
        self.cost = cost
    """
    Function: Getters for cost, damage, and name
    Parameters: None
    Return: Integer or String based on getter
    """
    def get_price(self):
        return self.cost
    def get_damage(self):
        return self.damage
    def get_name(self):
        return self.name
    def type(self):
        return "weapon"

"""
Function: Class for heal items
Parameters: String, Integer, Integer(Can be left blank)
"""


class heal_item:
    def __init__ (self, name, heal_amount, cost):
        if cost == None:
            cost = 0
        self.name = name
        self.heal_amount = heal_amount
        self.cost = cost
    """
    Function: Getters for cost, damage, and name
    Parameters: None
    Return: Integer or String based on getter
    """
    def get_heal(self):
        return self.heal_amount
    def get_cost(self):
        return self.cost
    def type(self):
        return "heal_item"


"""
Function: Class for damage-modifying items
Parameters: String, Integer, Integer
Return: Integer or Damage based on getter
"""

class dmg_modifier_item:
    def __init__ (self, name, dmg, cost):
        if cost == None:
            cost = 0
        self.name = name
        self.dmg = dmg
        self.cost = cost
    def get_damage(self): #Getters, take no paramaters. Returns integer
        return self.dmg
    def get_cost(self): #returns integer
        return self.cost
    def get_name(self): #returns string
        return self.name


#Class for enemy, uses String, int, int parameters. 
class enemy:
    def __init__ (self, name, health, damage):
        self.name = name
        self.damage = damage
        self.health = health
    def get_damage(self):
        return self.damage
    def get_health(self):
        return self.health
    def set_health(self, damage_done):
        self.health = self.health-damage_done
    def get_name(self):
        return self.name


#deprecated
class ability:
    def __init__ (self, name, damage):
        self.name = name
        self.damage = damage


"""
Function: Prints buy menu for user to buy items. They are then added to their inventory and removed from the shop inventory if they have enough gold and space.
Parameters: None
Return: None
"""
def buy_menu():
    global gold
    for i in range(len(shop_inventory)):
        printline()
        print(f"{i+1}. {shop_inventory[i].name} (Cost: {shop_inventory[i].get_price()})")
        print(" 0. to Exit Shop")
        printline()
    buy_selection = int(input("Enter the item you would like to buy: "))
    if buy_selection > len(shop_inventory) or buy_selection < 0:
        print("Invalid input\n")
        buy_menu()
        return
    elif shop_inventory[buy_selection] == "Out of Stock" :
        print("Item is Out of Stock")
        buy_menu()
        return
    elif buy_selection == 0:
        present_game("The Shoppee")
    else:
        if None not in inventory:
            print("Inventory full\n")
            buy_menu()
            return
        elif gold < shop_inventory[buy_selection-1].get_price():
            print("Not enough gold\n")
            buy_menu()
            return
        else:
            empty_slot = inventory.index(None)
            inventory[empty_slot] = shop_inventory[buy_selection-1]
            gold = gold - shop_inventory[buy_selection-1].get_price()
            print(f"You bought {shop_inventory[buy_selection-1].name}")
            buy_menu()
            return


"""
Function: Gets the name of a room based on dictionary items. If it matches then name of room is returned
Parameters: Dictionary
Return: String (returns None should never happen)
"""

def get_room_name(room_dict): #Really annoying I have to add this but Python has no built in method. Searches dictionary for matching data to determine its name.
    for name, data in rooms.items():
        if data == room_dict:
            return name
    return None

"""
Function: Called when attack option is used. Player attacks and then enemy. If enemy is killed, defeat_enemy() is ran, otherwise choices screen is pulled back up
Parameters: Enemy
Return: None
"""

def fight_enemy(enemy):
    global gold
    global player_damage_modifier
    global current_room
    global player_health
    printline()
    damage = player_current_damage()
    enemy.set_health(damage)
    print(f"You attack {enemy.name} for {damage}.")
    
    if enemy.get_health() <= 0:
        defeat_enemy(get_room_name(current_room), enemy)
        return
    else:
        print(f"{enemy.name} attacks you for {enemy.damage} damage")
        player_health = player_health - enemy.damage

    print(f"Your health: {player_health}")

    if player_health <= 0:
        print("You have died. Game Over!")


    player_damage_modifier = 1
    get_player_choice(current_room)
    return

"""
Function: Called when enemy in fight is killed, gives play random amount of gold and will end game once they kill final boss. Updates room's description and choices
Parameters: String, Enemy
Return: None
"""

def defeat_enemy(room_name, enemy):
    global current_room
    global gold
    current_room["description"] = "The floor has been succesfully cleared"
    printline()
    print(f"You have slain the {enemy.name}")
    reward = random.randint(5,15)
    gold = gold + reward
    print(f"You have earned {reward} gold for defeating the enemy.")
    printline()
    if enemy.get_name() == "Cursed Knight":
        print("You have slain the Cursed Knight which has wreaked havoc on the land. You are a hero")
        print("Game Over. You Won!")
        os.wait(3000)
        exit()

    current_room["enemy"] = None
    new_choices = {

        "Head Home": "Home",
        "Head to 'The Shoppee'": "The Shoppee",
        "Head to The Lucky Cave": "Cave"
        }

    if "Level" in room_name and "5" not in room_name:
        current_level = int(room_name.split(" ")[1])
        next_level = f"Level {current_level+1}"
        new_choices[f"Head to {next_level}"] = next_level

    update_room_choices(room_name, new_choices)

    present_game(room_name)

"""
Function: Replaces old items with new items to "choices" key in room
Parameters: String, Dictionary
Return: None
"""

def update_room_choices(room_name, new_choices):
    if room_name in rooms:
        rooms[room_name]["choices"] = new_choices
    

"""
Function: Opens inventory and lets player use item, changes their stat accordingly, and potentially remove item
Parameters: None
Return: None
"""
def use_item():
    global player_current_damage
    global current_room
    global inventory
    global player_damage_modifer
    global player_health
    print(f" 1. {inventory[0]} 2. {inventory[1]} 3. {inventory[2]} 4. {inventory[3]} 5. {inventory[4]} 0. Exit")
    user_choice = int(input("Select the item you would like to use: "))
    
    if(user_choice == 0):
        get_player_choice(current_room)
        return

    if user_choice-1 > 4 or user_choice-1 < 0 or inventory[user_choice-1] == None:
        print("Invalid Selection\n")
        use_item()
        return

    elif inventory[user_choice-1].type() == "heal_item":
        player_health = player_health + inventory[user_choice-1].get_heal()
        inventory[user_choice-1] = None
        get_player_choice(current_room)
        return

    elif inventory[user_choice-1].type() == "damage_modifier_item":
        player_damage_modifier = inventory[user_choice-1].get_damage()
        inventory[user_choice-1] = None
        get_player_choice(current_room)
        return

    elif inventory[user_choice-1].type() == "weapon":
        player_current_damage = inventory[user_choice-1].get_damage()
        get_player_choice(current_room)
        return


"""
Function: Calculates player's current damage based on weapon and modifier
Parameters: None
Return: Int
"""
def player_current_damage():
    return player_current_weapon.get_damage() * player_damage_modifier

"""
Function: Reads player's input and runs function accordingly
Parameters: Dictionary
Return: None
"""

def get_player_choice(current_room):
    global player_health
    choice = int(input("Enter your choice: "))
    choices = current_room["choices"]
    keys_list = list(choices.keys()) #Cast to list so that I can index the dictionaries keys. There was probably an easier way but I was too far deep to figure it out
    

    if choice < 1 or choice > len(keys_list):
        print("Invalid selection\n")
        get_player_choice(current_room)
        return
    
    selected_key = keys_list[choice-1]

    
    if selected_key.find("Head to") != -1 or selected_key.find("Enter The Darkness") != -1:
        present_game(choices[selected_key])
        return
    elif selected_key == "Rest" and player_health < 35:
        player_health = player_health+15
    elif selected_key == "Buy":
        buy_menu()
        return
    elif selected_key == "Attack" and current_room["enemy"]:
        fight_enemy(current_room["enemy"])
        return
    elif selected_key == "Use Item":
        use_item()
        return
    else:
        print("Invalid selection\n")
        get_player_choice(current_room)
        return

"""
Function: Prints 40 lines
Parameters: None
Return: None
"""
def printline():
    print("-"*40)

"""
Function: Prints out room, description, and player's options
Parameters: Dictionary
Return: None
"""

def present_game(room_key):
    global current_room
    current_room = rooms[room_key]
    os.system("cls")
    printline()
    print(room_key + "\n")
    print(rooms[room_key]["description"] + "\n")
    printline()

    if current_room["enemy"] != None:
        print(f"You have encountered {current_room["enemy"].name}.")
        print(f"Health: {current_room["enemy"].get_health()}   Damage: {current_room["enemy"].get_damage()}")
        printline()

    number = 1
    for i in rooms[room_key]["choices"]:
        print(str(number) + ". " + i + "\n")
        number = number+1
    get_player_choice(current_room)
    

shop_inventory = [weapon("Great Axe",15, 25), heal_item("Health Potion",20,15), weapon("Staff of Archimedes", 14, 18), heal_item("Great Health Potion",45,35), dmg_modifier_item("Strength Potion",2,15), dmg_modifier_item("Great Strength Potion",4,30)]
main_characters = ["Orc", "Barbarian", "Wizard"]


selected_character = None
player_current_weapon = None
player_damage_modifier = 1 #Need to edit these when player is chosen
player_health = 15
gold = 0
mana = 50 #deprecated feature
inventory = [None, None, None, None, None]
abilities = [] #deprecated, want to keep in code though in case I come back later
rooms = {
    "Home" : {
        "description" : "A place of comfort for you and your party, you can rest up to regain health.",
       
       "choices" : {
            "Rest" : "rest", 
            "Head to 'The Shoppee'" : "The Shoppee",
            "Head to The Catacombs" : "Catacombs",
            "Head to The Lucky Cave" : "Cave"
            },
       "enemy":None
        },

    "The Shoppee" : {

        "description" : "Behind the counter, a burly dwarf asks in a gruff voice what you want.",

        "choices" : {
            "Buy" : "buy",
            "Head Home" : "Home",
            "Head to The Catacombs" : "Catacombs",
            "Head to The Lucky Cave" : "Cave"
            },
        "enemy":None
        },
    "Cave" : {
        "description" : "Despite its name, there seems to be nothing of intrigue here",

        "choices" : {
            "Head Home" : "Home",
            "Head to The Catacombs" : "Catacombs",
            "Head to 'The Shoppee'" : "The Shoppee"
            },
        "enemy": None
        },
    "Catacombs" : {
        "description" : "The main atrium is eerily silent. Bones litter the floor and increase in volume as you approach the staircase.\nIt is a black abyss and you cannot see what is down there",

        "choices" : {
            "Enter The Darkness" : "Level 1",
            "Head Home" : "Home",
            "Head to The Lucky Cave" : "Cave",
            "Head to 'The Shoppee'" : "The Shoppee"
            },
        "enemy" : None
        },
    #Idea: Go back and edit values of dictionary once enemy has been defeated. That way player can traverse through and leave
    "Level 1" : {
        "description" : "As you finally make your way to the bottom of the staircase, a singular torch dimly lights the room. You just barely notice the arrow flying at you in time to dodge it. A group of skeletons have surrounded you, wielding weapons of the previous warriors who dared to venture down here.",

        "choices" : {
            "Attack": "attack",
            "Use Item": "inventory",
            
            },
        "enemy": enemy("Skeletons", 10, 2)
        
        
        },

    "Level 2": {
        "description" : "As you enter the next room, your boots began to slightly stick to the floor. A gigantic blob slithers towards you.",

        "choices" : {
            "Attack":"attack",
            "Use Item": "inventory"
            
            },
        "enemy":enemy("Blob",15,3)
    },

     "Level 3": {
        "description": "The air thickens with an eerie mist, and a low growl echoes through the chamber. A hulking werewolf lunges from the shadows.",
        "choices": {
            "Attack": "attack",
            "Use Item": "inventory"
        },
        "enemy": enemy("Werewolf", 20, 5)
    },
    "Level 4": {
        "description": "The walls of the cavern seem to pulse with an unnatural energy. In the center, a floating wraith stares at you with hollow eyes.",
        "choices": {
            "Attack": "attack",
            "Use Item": "inventory"
        },
        "enemy": enemy("Wraith", 25, 6)
    },
    "Level 5": {
        "description": "A grand chamber lined with ancient runes hums with power. At the far end, a heavily armored knight grips his sword, ready for battle.",
        "choices": {
            "Attack": "attack",
            "Use Item": "inventory"
        },
        "enemy": enemy("Cursed Knight", 30, 7)
    }
}
current_room = rooms["Home"]
while True:
    printline()
    character_select = input("Choose your character: (1) Orc (2) Barbarian (3) Wizard. Type 'help' for more info.")
    if character_select == "help":
        print("\nOrcs are a balanced build of magic and physical attacks, barbarians are mostly physical focused, and wizards are mainly focused on casting spells.\n")
    elif character_select != "help" and int(character_select) <= 4 and int(character_select) > 0:
        selected_character = main_characters[int(character_select)]
        break
    else:
        print("\nInvalid Input\n")

if selected_character == "Orc":
    inventory[0] = weapon("Brutal Cleaver", 5)
    player_current_weapon = inventory[0]
elif selected_character == "Wizard":
    inventory[0] = weapon("Weak Staff", 3)
    inventory[1] = dmg_modifier_item("Potion of Damage",2)
    player_current_weapon = inventory[0]
elif selected_character == "Barbarian":
    inventory[0] = weapon("Heavy Axe", 8)
    player_current_weapon = inventory[0]

present_game("Home")


