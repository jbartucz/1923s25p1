import random
rooms1 = {
    "StartingRoom": "Cave",
    "Cave": {
        "Description": "Dark cavern with monsters",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Fields",
            "Choice B": "Cave"
        }
    },
    "Fields": { 
        "Description": "A place full of flowers",
        "MonsterClass": "none",
        "choices": {
            "Choice A": "Forest",
            "Choice B": "Cave"
        }
    },
    "Forest": {
        "Description": "An eerie place with many monsters",
        "MonsterClass": "strong",
        "choices": {
            "Choice A": "Plains",
            "Choice B": "Fields"
        }
    },
    "Plains": {
        "Description": "An empty flatland",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Swamp",
            "Choice B": "Forest"
        }
    },
    "Swamp": {
        "Description": "A muddy and wet land",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Castle",
            "Choice B": "Plains"
        }
    },
    "Castle": {
        "Description": "In the distance you see a castle",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Snowy Plains",
            "Choice B": "Swamp"
        }
    },
    "Snowy Plains": {
        "Description": "An extremely thick snows and flat lands that is extremely cold",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Castle Entrance",
            "Choice B": "Castle"
        }
    },
    "Castle Entrance": {
        "Description": "You see the huge castle infront of you and all its glamour",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Castle Lobby",
            "Choice B": "Snowy Plains"
        }
    },
    "Castle Lobby": {
        "Description": "You enter inside the old and dusty castle go to the Throne",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Throne",
            "Choice B": "Castle Entrance"
        }
    },
    "Throne": {
        "Description": "An old throne still as pristine as always like someone is taking care of it",
        "MonsterClass": "boss",
        "choices": {
            "Choice A": "Throne",
            "Choice B": "Castle Lobby"
        }
    },
}

rooms2 = {
    "StartingRoom": "Cemetary",
    "Cemetary": {
        "Description": "The place is riddled with graves and this cold feeling",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Path",
            "Choice B": "Cemetary"
        }
    },
    "Path": { 
        "Description": "An empty path that begins from right where you stand",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Manor",
            "Choice B": "Cemetary"
        }
    },
    "Manor": {
        "Description": "Very unsettling Manor at the end if the path",
        "MonsterClass": "strong",
        "choices": {
            "Choice A": "Lobby",
            "Choice B": "Path"
        }
    },
    "Lobby": {
        "Description": "Has a chandelier and stairs as well as a kitchen",
        "MonsterClass": "strong",
        "choices": {
            "Choice A": "Kitchen",
            "Choice B": "Manor"
        }
    },
    "Kitchen": {
        "Description": "A kitchen with some knives and other necessaties",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Upstairs",
            "Choice B": "Lobby"
        }
    },
    "Upstairs": {
        "Description": "A strange light is eminating from a rooms",
        "MonsterClass": "weak",
        "choices": {
            "Choice A": "Throne",
            "Choice B": "Kitchen"
        }
    },
    "Throne": {
        "Description": "A throne with many jewels and is weirdly clean and polished",
        "MonsterClass": "boss",
        "choices": {
            "Choice A": "Throne",
            "Choice B": "Upstairs"
        },
    },
}

weakenemies = [
    {
        "name": "slime",
        "damage": 20,
        "health": 20,
        "maxmonsterhp": 15,
        "description": "A slimy creature that looks ready to dissolve you"
    },
    {
        "name": "goblin",
        "damage": 15,
        "health": 30,
        "maxmonsterhp": 30,
        "description": "A creature that carries a club and looks ready to hit you"
    },
    { 
        "name": "dark elf",
        "damage": 15,
        "health": 20,
        "maxmonsterhp": 20,
        "description": "A creature who is nimble and has impeccable accuracy but lacks durability"
    },
]

strongenemies = [
    {
        "name": "Dragon",
        "damage": 25,
        "health": 30,
        "maxmonsterhp": 40,
        "description": "A mighty lizard who spews fire and can fly"
    },
    {
        "name": "Warlord",
        "damage": 20,
        "health": 30,
        "maxmonsterhp": 30,
        "description": "A warrior of power and strength"
    },
    {
        "name": "Lich",
        "damage": 30,
        "health": 20,
        "maxmonsterhp": 20,
        "description": "A foolish wizard that seeks more power in exchange for his life"
    }
    
]

kingrandom_health = random.randint(60,100)
kingrandom_damage = random.randint(20, 40)

bossenemies = [
    {
    "name": "King of Random",
    "damage": kingrandom_damage,
    "health": kingrandom_health,
    "maxmonsterhp": kingrandom_health,
    "description": "A King who has lost thier mind from gambling"
}
]

player = {
    "health": 100,
    "damage": 10,
    "maxplayerhp": 100
}

rooms = [rooms1, rooms2]
room = random.choice(rooms)

currentroom = room["StartingRoom"]
description = room[currentroom]["Description"]
choices = room[currentroom]["choices"]
    
end = False
battle = False
die = False

def heal_player ():
    global player
    heal_amount = random.randint(30,50)
    print()
    player["health"] = min(player["health"] + heal_amount, player["maxplayerhp"])
    print(f"You have healed {heal_amount} HP. Current health: {player['health']}/{player['maxplayerhp']} HP")

# def fullheal_player():    Removed for now may make it random at a later date
#     global player
#     player["health"] = player["maxplayerhp"]
#     print(f"You have been fully healed! Current health: {player['health']}/{player['maxplayerhp']} HP")

def encounter_monster():
    global player, battle, end, die
    
    monster_class = room[currentroom]["MonsterClass"]
    if monster_class == "weak":
        monster = random.choice(weakenemies)
        escape_monster = 0.75
        print(f"You are on your way to {currentroom} and then stumble accross a weak {monster['name']}")
    elif monster_class == "strong":
        monster = random.choice(strongenemies)
        escape_monster = 0.25
        print(f"You are on your way to {currentroom} and then stumble accross a mighty {monster['name']}")
    elif monster_class == "boss":
        monster = random.choice(bossenemies)
        escape_monster = 0.00
        end = True
    else:
        return
    
    monster["health"] = monster["maxmonsterhp"]
    
    print(f"You've encountered a wild {monster['name']}")
    print(f"Description: {monster['description']}")
    battle = True
    
    while battle == True:
        print()
        print(f"Player Health: {player['health']}/{player['maxplayerhp']} HP")
        print(f"{monster['name']} Health: {monster['health']}/{monster['maxmonsterhp']} HP")
        action = input("What will you do? (attack/run/heal): ").lower()
        print()
        if action in ["attack", "atk", "a"]:
            monster["health"] -= player["damage"]
            print(f"You dealt {player['damage']} damage to the {monster['name']}!")
            if monster["health"] <= 0:
                print(f"You have slain {monster['name']}")
                battle = False
                # fullheal_player() Balancing issues
            else:
                player["health"] -= monster["damage"]
                print(f"{monster['name']} has inflicted {monster['damage']} to you")
                if player["health"] <= 0:
                    print(f"You have been defeated by {monster['name']}!")
                    print(f"Game Over!")
                    die = True
                    battle = False
        elif action in ["run", "r"]:
            if random.random() < escape_monster:
                print(f"You have successfully escaped {monster['name']}")
                # fullheal_player() Balancing issues
                return
            else:
                print(f"{monster['name']} has prevented your escape")
                player["health"] -= monster["damage"]
                print(f"{monster['name']} has inflicted {monster['damage']} to you")
                if player["health"] <= 0:
                    print(f"You have been defeated by {monster['name']}!")
                    print(f"Game Over!")
                    die = True
                    battle = False
        elif action in ["heal", "h"]:
            heal_player()
            player["health"] -= monster["damage"]
            print(f"{monster['name']} has inflicted {monster['damage']} to you")
            if player["health"] <= 0:
                print(f"You have been defeated by {monster['name']}!")
                print(f"Game Over!")
                die = True
                battle = False
        else:
            print("Invalid input please try again")
            print("I'll overlook this so your turn won't be wasted")
        
            
    
def view():
    print(f"{currentroom}: {description}")
    print()
    for choice, outcome in choices.items():
        print(f"{choice}: {outcome}")
    print()

def controller(stringinput):
    print()
    global currentroom, description, choices, die, end
    
    stringinput = stringinput.lower()
        
    if stringinput in ["choice a", "a", room[currentroom]["choices"]["Choice A"]]:
        next_room = room[currentroom]["choices"]["Choice A"]
        currentroom = next_room
    elif stringinput in ["choice b", "b", room[currentroom]["choices"]["Choice B"]]:
        previous_room = room[currentroom]["choices"]["Choice B"]
        currentroom = previous_room
    else:
        print(f"Error your input: {stringinput} is not possible")
    description = room[currentroom]["Description"]
    choices = room[currentroom]["choices"]
    
    if currentroom != "Throne" and "MonsterClass" in room[currentroom] and random.random() < 0.5:
        encounter_monster()
    
    if currentroom == "Throne":
        encounter_monster()
        if die == False:
            print()
            print("You have defeated the boss and claimed your rightful Throne!!")
            print("You Win!")
            end = True
    
    if die == True:
        end = True


def adventure():
    # print(room)
    print()
    while end != True:
        view()
        controller(input("What do you want to do? "))
        

adventure()