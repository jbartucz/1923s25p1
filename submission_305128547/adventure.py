import random

rooms = {
    "Cave Entrance": {
        "description": "You wake up at the entrance of a dark cave.",
        "choices": {
            "enter": "Dark Cave",
            "pick other side": "Forest Path"
        }
    },
    "Forest Path": {
        "description": "A winding path through dense woods and strange noises around you.",
        "choices": {
            "go forward": "Waterfall",
            "follow lights": "Ancient Ruins",
            "return": "Cave Entrance",
        }
    },
    "Dark Cave": {
        "description": "The cave is dark and damp. You see glowing eyes staring at you.",
        "choices": {
            "fight": "Battle",
            "run away": "Cave Entrance"
        }
    },
    "Waterfall": {
        "description": "A beautiful waterfall hidden deep in the forest with a weired hut next to it .",
        "choices": {
            "enter hut": "Weird hut",
            "return": "Forest Path"
        }
    },
    "Weird hut": {
        "description": "An old man sits by the fire. He gives you a box.",
        "choices": {
            "open the box": "The world in the box",
            "reject the box": "Waterfall2"
        }
    },
    "Waterfall2": {
        "description": "You were driven out of the hut by the old man. When you turn back, you find that the weird hut has disappeared. .",
        "choices": {
            "return": "Forest Path"
        }
    },
    "The world in the box": {
        "description": "The old man is the guardian of the treasure, and you have fallen into his trap. You will be imprisoned forever in this dark world in the box.",
        "choices": {
            "suicide": "Suicide"
        }
    },
    "Ancient Ruins": {
        "description": "Crumbled stone pillars surround you. You see inscriptions on the walls.",
        "choices": {
            "examine inscriptions": "Secret Chamber",
            "leave": "Forest Path"
        }
    },
    "Secret Chamber": {
        "description": "A hidden chamber filled with treasure and danger.",
        "choices": {
            "take treasure": "Battle",
            "explore deeper": "Lost Catacombs"
        }
    },
    "Lost Catacombs": {
        "description": "An underground labyrinth. Strange sounds echo around you.",
        "choices": {
            "search for exit": "Forest Path",
            "investigate noise": "Battle"
        }
    },
    "Battle": {
        "description": "You face a dangerous creature!",
        "choices": {
            "attack": "Battle Result",
            "defend": "Battle Result"
        }
    },
    "Battle Result": {
        "description": "The battle is over.",
        "choices": {
            "continue": "Treasure Room"
        }
    },
    "Treasure Room": {
        "description": "A room filled with glittering gold and rare artifacts.",
        "choices": {
            "take treasure": "Exit",
            "leave": "Exit"
        }
    },
    "Suicide": {
        "description": "You can't stand the torment and commit suicide. Adventure failure.",
        "choices": {
            "exit": "exit the game"
        }
    },
    "Exit": {
        "description": "You have successfully completed the adventure!",
        "choices": {
            "exit": "exit the game"
        }
    },
    "Null": "Null"
}

characters = ["Warrior", "Assassin", "Buccaneer"]
enemies = ["Goblin", "Dark Spirit", "Forest Beast"]

def choose_character():
    print("Choose your character(enter 1-3):")
    for index, char in enumerate(characters, 1):
        print(f"{index}. {char}")
    
    player_choice = input("Enter the number of your choice: ")
    if player_choice.isdigit() and (0 < int(player_choice) <= len(characters)):
        return characters[int(player_choice) - 1]
    else:
        print("Invalid choice. Try again.")
        player_choice = input("Enter the number of your choice: ")
    return


def random_event():
    events = ["You are healed!", "A hidden trap activates!"]
    return random.choice(events)


def battle(player_health):
    enemy = random.choice(enemies)
    print(f"\n A {enemy} appears! Prepare for battle!")

    enemy_hp = random.randint(1, 10)
    player_hp = player_health
    block = 0
    while player_hp > 0 and enemy_hp > 0:
        print("\n Choose your action:")
        print("1. Attack")
        print("2. Defend")

        battle_choice = input("Enter your choice: ")
        while battle_choice not in ["1", "2"]:
            print("Invalid choice. Try again.")
            battle_choice = input("Enter your choice: ")

        if battle_choice == "1":
            damage = random.randint(2, 5)
            enemy_hp -= damage
            print(f"You attack the {enemy}, dealing {damage} damage!")

        elif battle_choice == "2":
            block = random.randint(1, 3)
            print(f"You block {block} damage from the enemy attack!")

        enemy_attack = random.randint(1, 4)
        if block > 0:
            enemy_attack -= block
        else:
            block = 0
        player_hp -= max(enemy_attack, 0)
        print(f"The {enemy} attacks you, dealing {max(enemy_attack, 0)} damage!")
        print(f"Your HP: {max(player_hp, 0)} | {enemy} HP: {max(enemy_hp, 0)}")

    if player_hp > 0:
        print("\n You defeated the enemy!")
        return "Battle Result"
    else:
        print("\n You have been defeated...")
        return "Cave Entrance"
    


def run_game():
    print("\nWelcome to the Game! Your purpose is to find the treasure. You have to choose your character first. \nHealth point(HP): Buccaneer > Warrior > Assassin")
    player = choose_character()
    print(f"\nYou have chosen to play as a {player}.\n")

    if player == "Warrior":
        player_health = 15
    elif player == "Assassin":
        player_health = 10
    elif player == "Buccaneer":
        player_health = 20
    else:
        player_health = 0
       
    
    current_room = "Cave Entrance"

    while current_room != "NULL":
        room_data = rooms[current_room]
        print(f"\n{room_data['description']}")

        if random.random() < 0.3 and current_room != "Battle":
            event = random_event()
            print(f"Random Event: {event}")
            if event == "You are healed!":
                player_health += 15
            elif event == "A hidden trap activates!":
                player_health -= 5
            
            if player_health <= 0:
                print("\nYou stepped on a trap and lost all your health.")
                print("Game over. Thank you for playing!")
                return


        if current_room == "Battle":
            current_room = battle(player_health)
            continue

        if room_data["choices"]:
            print("\nAvailable actions:")
            for action in room_data["choices"]:
                print(f"- {action}")

            act_choice = input("\nChoice your action: ").lower()
            while act_choice not in room_data["choices"]:
                print("Invalid choice. Try again.")
                act_choice = input("\nChoice your action: ").lower()

            current_room = room_data["choices"][act_choice]
            if current_room == "exit the game":
                print("Game over. Thank you for playing!")
                break


if __name__ == "__main__":
    run_game()
