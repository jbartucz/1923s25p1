import random
import sys

score = 0
#list1
characters = ["Jedi Knight", "Sith Lord", "Bounty Hunter"]
#list2
enemies = ["Stormtrooper", "Droid", "Sith Apprentice", "Wookiee", "Tusken Raider"]
#dict
rooms = {
    "Tatooine": {
        "description": "You are on the desert planet of Tatooine.",
        "choices": {
            "go to Mos Eisley": "Mos Eisley",
            "explore Dune Sea": "Jundland Wastes",
            "head to Lars' Homestead": "Lars' Homestead"
        }
    },
    "Mos Eisley": {
        "description": "You are in the Mos Eisley Cantina. Dangerous people are everywhere.",
        "choices": {
            "talk to bartender": "Jundland Wastes",
            "fight a bounty hunter": "Hoth",
            "leave cantina": "Endor"
        }
    },
    "Jundland Wastes": {
        "description": "A dangerous part of Tatooine.",
        "choices": {
            "head to Dune Sea": "Endor",
            "go to Sandcrawler": "Hoth",
            "search for Jawas": "Endor"
        }
    },
    "Lars' Homestead": {
        "description": "You are at the home planet of Luke Skywalker's family.",
        "choices": {
            "talk to Owen Lars": "Dagobah",
            "look around the farm": "Dagobah"
        }
    },
    "Endor": {
        "description": "You're on the forest moon of Endor. The home of Ewoks.",
        "choices": {
            "talk to Ewok": "Endor",
            "explore forest": "Endor",
            "leave Endor": "Tatooine"
        }
    },
    "Hoth": {
        "description": "You are on the icy planet of Hoth.",
        "choices": {
            "join Rebels": "Hoth",
            "explore icy caverns": "Hoth",
            "leave Hoth": "Coruscant"
        }
    },
    "Dagobah": {
        "description": "The swamps of Dagobah. Yoda’s home.",
        "choices": {
            "train with Yoda": "Dagobah",
            "explore the swamps": "Dagobah",
            "leave Dagobah": "Tatooine"
        }
    },
    "Coruscant": {
        "description": "The capital of the galaxy.",
        "choices": {
            "visit Senate": "Coruscant",
            "talk to a diplomat": "Coruscant",
            "leave Coruscant": "Tatooine"
        }
    },
    "Naboo": {
        "description": "The peaceful planet of Naboo.",
        "choices": {
            "visit Theed": "Naboo",
            "explore the lakes": "Naboo",
            "leave Naboo": "Tatooine"
        }
    },
    "Mustafar": {
        "description": "The volcanic planet of Mustafar..",
        "choices": {
            "search for Darth Vader's castle": "Mustafar",
            "explore lava pits": "Mustafar",
            "leave Mustafar": "Coruscant"
        }
    }
}
#random
def random_event():
    return random.choice([True, False])

def combat_attack(character, enemy):
    print(f"\nYou encounter a {enemy}!")
    global score
    
    if character == "Jedi Knight":
        attack_options = ["Force Push", "Lightsaber Strike", "Use the Force to Defend"]
    elif character == "Sith Lord":
        attack_options = ["Force Choke", "Lightsaber Strike", "Force Lightning"]
    elif character == "Bounty Hunter":
        attack_options = ["Blaster Fire", "Trap Setting", "Quick Escape"]
    
    print("\nChoose your attack:")
    for i, option in enumerate(attack_options, 1):
        print(f"{i}. {option}")
    
    choice = int(input("Enter the number of your choice: "))
    
    success_chance = random.randint(1, 10)
    
    if success_chance <= 3:
        print(f"\nYour attack failed! The {enemy} defeated you.")
        print("Game Over!")
        print("Score: " + str(score))
        sys.exit(0) 
    else:
        print(f"\nYou successfully attack the {enemy} with {attack_options[choice - 1]}!")
        score += 1
#story
def start_game():
    print("Welcome to the Star Wars Adventure Game where the goal is to survive!")
    print("Choose your character:")
    
    print("1. Jedi Knight")
    print("2. Sith Lord")
    print("3. Bounty Hunter")
    
    choice = int(input("Enter the number of your character choice: "))
    
    if choice == 1:
        character = "Jedi Knight"
    elif choice == 2:
        character = "Sith Lord"
    elif choice == 3:
        character = "Bounty Hunter"
    else:
        print("Invalid choice, defaulting to Jedi Knight.")
        character = "Jedi Knight"
    
    print(f"\nYou have chosen the {character}.\n")
    
    current_room = "Tatooine"
    game_loop(current_room, character)

def game_loop(current_room, character):
    while True:
        room = rooms[current_room]
        print(room["description"])
        print("Choices:")
        
        choices = list(room["choices"].keys())
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")
        
        choice = int(input("Enter the number of your choice: "))
        
        if random_event():
            enemy = random.choice(enemies)
            combat_attack(character, enemy)
        
        action = choices[choice - 1]
        current_room = room["choices"][action]
start_game()
