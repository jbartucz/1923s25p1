import random
def main():
     
    rooms = {
        "Entrance": {
            "description": "You are standing at the entrance of the dungeon. It's dark, and you can barely make out the path ahead.",
            "choices": {
                "Enter the dungeon": "Dungeon Hall",
                "Leave": "leave_game"
            }
        },
        "Dungeon Hall": {
            "description": "The hallway is dimly lit. You can hear distant sounds echoing through the stone walls.",
            "choices": {
                "Go forward": "Treasure Chamber",
                "Turn back": "Entrance"
            }
        },
        "Treasure Chamber": {
            "description": "You enter a room filled with ancient treasure. But something doesn't feel right...",
            "choices": {
                "Inspect treasure": "trap_room",
                "Exit": "Dungeon Hall"
            }
        },
        "Trap Room": {
            "description": "As you inspect the treasure, a trap is triggered! A hidden door slams shut, trapping you in a room with spikes on the floor.",
            "choices": {
                "Fight the trap": "fight_room",
                "Try to escape": "Dungeon Hall"
            }
        },
        "Fight Room": {
            "description": "You decide to fight! But a group of enemies appear, ready to attack.",
            "choices": {
                "Fight enemies": "battle",
                "Run away": "Dungeon Hall"
            }
        },
        "battle": {
            "description": "You battle the enemies! Your fate depends on your choices and the dice roll...",
            "choices": {
                "Fight hard": "result_battle",
                "Use magic": "result_battle"
            }
        },
        "result_battle": {
            "description": "The battle outcome is determined. If you survive, you can continue your adventure.",
            "choices": {
                "Continue": "Dungeon Hall",
                "Exit": "leave_game"
            }
        },
        "leave_game": {
            "description": "You decided to leave the dungeon. Maybe another time.",
            "choices": {}
        }
    }

    # Lists for characters and enemies
    characters = ["Archer", "Mage", "Warrior"]
    enemies = ["Goblin", "Orc", "Dragon"]

 

    # Player chooses a character
    print("Choose your character:")
    for i, character in enumerate(characters):
        print(f'{i+1}. {character}')

    while True:
        try:
            choice = int(input("Choose a character by entering the number: "))
            if 1 <= choice <= len(characters):
                player = characters[choice - 1]
                print(f"You have chosen {player} as your character.\n")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

    # Starting point of the game
    current_location = "Entrance"

    while True:
        # Display room description and choices
        print(f'\n{rooms[current_location]["description"]}')
        print("What do you want to do?")
        for option in rooms[current_location]["choices"]:
            print(f'- {option}')

        # Random encounter with an enemy
        enemy = random.choice(enemies)
        print(f"\nA wild {enemy} appears!")

        # Random battle outcome
        battle_outcome = random.choice(["You win!", "You lose!"])

        action = input("What is your next move? ").strip()

        # Player chooses a valid action and transitions to another room
        if action in rooms[current_location]["choices"]:
            current_location = rooms[current_location]["choices"][action]
            
            if current_location == "battle":
                print(f"Battle Outcome: {battle_outcome}")
                if battle_outcome == "You lose!":
                    print("Game Over! You were defeated.")
                    break
            elif current_location == "leave_game":
                print("Thank you for playing! Game over.")
                break
        else:
            print("Invalid input, please try again.")
 
if __name__ == "__main__":
    main()