import random

inventory = []
broom_flying_mastered = False

def main():
    print("Welcome to the Harry Potter Adventure Game!")
    print("You will choose a character and embark on a magical journey.")

    characters = ["Hogwarts Student", "Auror", "Defense Against the Dark Arts Professor", "Auror Trainee", "Quidditch Player"]
    possible_encounters = ["Death Eater", "Dementor", "Voldemort", "Order of the Phoenix Member", "Dobby"]

    print("\nAvailable characters:")
    for i, c in enumerate(characters, 1):
        print(f"{i}. {c}")

    chosen_character = None
    while chosen_character is None:
        try:
            choice = int(input("\nPlease choose your character (enter a number): "))
            if 1 <= choice <= len(characters):
                chosen_character = characters[choice - 1]
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

    print(f"\nYou have chosen: {chosen_character}")
    print("Let's begin!\n")

    rooms = {
        "4 Privet Drive": {
            "description": "This is the childhood home of Harry Potter. You can explore or move on to Diagon Alley.",
            "choices": {
                "Explore the house": "Harrys Old Room",
                "Go to Diagon Alley": "Diagon Alley",
                "Go to Kings Cross Station": "Kings Cross Station"
            }
        },
        "Harrys Old Room": {
            "description": "This is a small cupboard-like room where a young boy once lived. A broken broom is on the floor.",
            "choices": {
                "Pick up the broom": "Pick Broom Event",
                "Do nothing": "Put Broom Event",
                "Go back": "4 Privet Drive"
            }
        },
        "Pick Broom Event": {
            "description": "You pick up the broom and feel a faint magical power. You can practice flying or go back.",
            "choices": {
                "Practice flying": "Flying Practice",
                "Go back": "4 Privet Drive"
            }
        },
        "Put Broom Event": {
            "description": "You decide to leave the broom. Nothing happens here, you can go back.",
            "choices": {
                "Go back": "Harrys Old Room"
            }
        },
        "Flying Practice": {
            "description": "You try to fly the broom. Roll a die: if result >= 4, you succeed.",
            "choices": {
                "Roll the die": "Flying Practice Result",
                "Give up": "Pick Broom Event"
            }
        },
        "Flying Practice Result": {
            "description": "Your practice result depends on the die roll. Then you can go back.",
            "choices": {
                "Go back": "4 Privet Drive"
            }
        },
        "Diagon Alley": {
            "description": "A bustling street full of wizard shops. You can visit Gringotts or the Leaky Cauldron.",
            "choices": {
                "Go to Gringotts": "Gringotts",
                "Go to the Leaky Cauldron": "Leaky Cauldron",
                "Go back": "4 Privet Drive"
            }
        },
        "Gringotts": {
            "description": "The wizard bank run by goblins. You can interact with them or leave.",
            "choices": {
                "Talk to goblin": "Gringotts Talk",
                "Leave": "Diagon Alley"
            }
        },
        "Gringotts Talk": {
            "description": "The goblin seems suspicious of you. You can try to persuade them or give up.",
            "choices": {
                "Persuade": "Gringotts Result",
                "Give up": "Gringotts"
            }
        },
        "Gringotts Result": {
            "description": "The goblin agrees to give you some gold. Then you leave.",
            "choices": {
                "Leave": "Diagon Alley"
            }
        },
        "Leaky Cauldron": {
            "description": "A lively pub with the smell of butterbeer. You can gather information or go back.",
            "choices": {
                "Gather info": "Leaky Info",
                "Go back": "Diagon Alley"
            }
        },
        "Leaky Info": {
            "description": "You hear rumors about some activity at Hogwarts. Maybe you should go to Kings Cross.",
            "choices": {
                "Go back": "Leaky Cauldron"
            }
        },
        "Kings Cross Station": {
            "description": "You arrive at Kings Cross Station. Platform 9¾ is nearby.",
            "choices": {
                "Enter platform 9¾": "Hogwarts Express",
                "Walk around": "4 Privet Drive"
            }
        },
        "Hogwarts Express": {
            "description": "You board the train to Hogwarts. It will take you to the castle.",
            "choices": {
                "Travel to Hogwarts": "Hogwarts Castle Gate",
                "Get off": "Kings Cross Station"
            }
        },
        "Hogwarts Castle Gate": {
            "description": "You stand before the grand gates of Hogwarts. You can enter the Great Hall or go to the Forbidden Forest.",
            "choices": {
                "Enter Great Hall": "Great Hall",
                "Go to the Forbidden Forest": "Forbidden Forest"
            }
        },
        "Forbidden Forest": {
            "description": "Dark and full of potential danger. You can go deeper or go back.",
            "choices": {
                "Go deeper": "Deep Forest",
                "Go back": "Hogwarts Castle Gate"
            }
        },
        "Deep Forest": {
            "description": "You sense dark magic. You may find something or face danger.",
            "choices": {
                "Go back": "Forbidden Forest"
            }
        },
        "Great Hall": {
            "description": "You enter the Great Hall of Hogwarts. It's lively and bright. You can talk to Dumbledore or go back.",
            "choices": {
                "Talk to Dumbledore": "Game Over",
                "Go back": "Hogwarts Castle Gate"
            }
        },
        "Game Over": {
            "description": "Dumbledore smiles at you. Your adventure ends here.",
            "choices": {
                "End": None
            }
        }
    }

    current_room = "4 Privet Drive"

    while True:
        print("\n----------------------------")
        print(f"Location: {current_room}")
        print(rooms[current_room]["description"])

        if random.random() < 0.3:
            encounter = random.choice(possible_encounters)
            print(f"\nSuddenly, you encounter: {encounter}!")
            if encounter in ["Death Eater", "Dementor", "Voldemort"]:
                result = combat_sequence(encounter)
                if not result:
                    print("You have been defeated. Game over.")
                    break
                else:
                    print("You managed to overcome the threat and continue.")
            else:
                print(f"{encounter} nods at you, giving you a sense of strength.")

        if current_room == "Game Over":
            print("\nThe game has ended. Thanks for playing.")
            break

        choices = rooms[current_room]["choices"]
        if not choices:
            print("\nNo more choices. Game over.")
            break

        print("\nPossible actions:")
        for i, act in enumerate(choices.keys(), 1):
            print(f"{i}. {act}")

        user_choice = input("Make your choice (number or text): ").strip()
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if 1 <= user_choice <= len(choices):
                action = list(choices.keys())[user_choice - 1]
                next_room = choices[action]
            else:
                print("Invalid choice, please try again.")
                continue
        else:
            if user_choice in choices:
                next_room = choices[user_choice]
            else:
                print("Invalid choice, please try again.")
                continue

        if next_room == "Pick Broom Event":
            if "Broom" not in inventory:
                print("\nYou put the Broom into your inventory.")
                inventory.append("Broom")
        elif next_room == "Flying Practice Result":
            roll = random.randint(1, 6)
            print(f"\nYou rolled a {roll}.")
            if roll >= 4:
                global broom_flying_mastered
                broom_flying_mastered = True
                print("You have succeeded in basic flying skill. This may help in future battles.")
            else:
                print("You failed to control the broom. More practice is needed.")

        if next_room is None:
            print("\nNo more adventures. Game over.")
            break
        else:
            current_room = next_room

    print("\nThank you for playing. See you next time!")

def combat_sequence(enemy):
    print(f"You have encountered {enemy} and must choose your action.")
    base_success_battle = 4
    base_success_escape = 3

    from __main__ import broom_flying_mastered
    if broom_flying_mastered:
        base_success_battle -= 1
        base_success_escape -= 1

    while True:
        action = input("Choose: 1) Fight  2) Run >>> ").strip()
        if action == "1":
            roll = random.randint(1, 6)
            print(f"\nYou choose to fight {enemy}. You need a roll >= {base_success_battle} to win.")
            print(f"You rolled {roll}.")
            if roll >= base_success_battle:
                print(f"You beat {enemy}!")
                return True
            else:
                print(f"You did not succeed. {enemy} overcame you.")
                return False
        elif action == "2":
            roll = random.randint(1, 6)
            print(f"\nYou choose to run. You need a roll >= {base_success_escape} to escape.")
            print(f"You rolled {roll}.")
            if roll >= base_success_escape:
                print(f"You escaped from {enemy}.")
                return True
            else:
                print(f"You failed to run away from {enemy}.")
                return False
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()
