import random

# List of characters the player can choose from
characters = ["Warrior", "Mage", "Archer", "Elf"]

# List of potential enemies
enemies = ["Evil Fairy", "Ruined Kight", "Corrupt Spirit", "Heart Steel Dragon"]

# Dictionary for rooms/locations
rooms = {
    "Cave Entrance": {
        "description": "You stand at the dark cave entrance. You can enter or walk away.",
        "choices": {"enter": "Dark Cave", "leave": "Forest Path"}
    },
    "Dark Cave": {
        "description": "The cave is damp and eerie. You have 3 paths.",
        "choices": {"left": "Treasure Room", "right": "Monster Lair", "leave":"Forest Path"}
    },
    "Forest Path": {
        "description": "You walk into a dense forest. A bridge is ahead, and a hut is nearby.",
        "choices": {"bridge": "River Bank", "hut": "Old Cabin"}
    },
    "Treasure Room": {
        "description": "You find a treasure chest! Open it or leave?",
        "choices": {"open": "Chest", "leave": "Dark Cave"}
    },
    "Monster Lair": {
        "description": "A fierce monster blocks your path! Fight or flee?",
        "choices": {"fight": "Battle", "flee": "Dark Cave"}
    },
    "Old Cabin": {
        "description": "An old cabin filled with mysterious artifacts.",
        "choices": {"search": "Hidden Passage", "leave": "Forest Path"}
    },
    "Hidden Passage": {
        "description": "A secret tunnel leads to an unknown place.",
        "choices": {"follow": "Treasure Room", "back": "Old Cabin"}
    },
    "River Bank": {
        "description": "You reach a river. You can swim across or follow it.",
        "choices": {"swim": "Secret Island", "follow": "The Living Forest"}
    },
    "Secret Island": {
        "description": "An island with strange markings. A portal stands in the center.",
        "choices": {"enter portal": "Victory", "wait": "River Bank"}
    },
    "The Living Forest": {
        "description": "The forest of uncertainty. Will you walk forward or backward?",
        "choices": {"forward": "Teleport", "backward": "Old Cabin"}
    },
    "Teleport": {
        "description": "You will be randomly teleported to another place.",
        "choices": {}  # This will be determined by a random event
    },
    "Chest": {
        "description": "You will open the chest!",
        "choices": {}  # This will be determined by a random event
    },
    "Battle": {
        "description": "You face the enemy! Rolling the dice to determine the outcome...",
        "choices": {}  # This will be determined by a random event
    },
    "Victory": {
        "description": "Congratulations! You have won the adventure!",
        "choices": {}
    }
}

def choose_character():
    print("Choose your character:")
    for index, char in enumerate(characters, 1):
        print(f"{index}. {char}")
    choice = input("Enter the number of your choice: ")
    if choice.isdigit() and 1 <= int(choice) <= len(characters):
        return characters[int(choice) - 1]
    else:
        return "Explorer"

def battle():
    enemy = random.choice(enemies)
    print(f"A {enemy} appears! You must roll a die to fight...")
    if enemy == "Evil Fairy":
        if "yes" == input("Do you still want to fight it? (type yes or no)"):
            roll = random.randint(1, 6)
            if roll >= 2:
                print(f"You rolled a {roll}!")
                print("You defeated the enemy! ")
                return "Treasure Room"
            else:
                print(f"You rolled a {roll}!")
                print("You lost the battle and must retreat!")
                return "Dark Cave"
        else:
            return "Dark Cave"
    elif enemy == "Ruined Kight":
        if "yes" == input("Do you still want to fight it? (type yes or no)"):
            roll = random.randint(1, 6)
            if roll >= 3:
                print(f"You rolled a {roll}!")
                print("You defeated the enemy!")
                return "Treasure Room"
            else:
                print(f"You rolled a {roll}!")
                print("You lost the battle and must retreat!")
                return "Dark Cave"
        else:
            return "Dark Cave"
    elif enemy == "Corrupt Spirit":
        if "yes" == input("Do you still want to fight it? (type yes or no)"):
            roll = random.randint(1, 6)
            if roll >= 4:
                print(f"You rolled a {roll}!")
                print("You defeated the enemy!")
                return "Treasure Room"
            else:
                print(f"You rolled a {roll}!")
                print("You lost the battle and must retreat!")
                return "Dark Cave"
        else: 
            return "Dark Cave"
    elif enemy == "Heart Steel Dragon":
        answer = input("Do you still want to fight it? (type yes or no)")
        if "yes" == answer:
            roll = random.randint(1, 6)
            if roll >= 6:
                print(f"You rolled a {roll}!")
                print("You defeated the enemy!")
                return "Treasure Room"
            else:
                print(f"You rolled a {roll}!")
                print("You lost the battle and must retreat!")
                return "Dark Cave"   
        elif "no" == answer:
            return "Dark Cave"
        
def Teleport():
    first_10_rooms = list(rooms.keys())[:10]
    room = random.choice(first_10_rooms)
    print(f"You have been telelported to {room}")
    return room 

def Treasure():
    roll = random.randint(1,2)
    if roll == 1:
        print("You found the Treasure!")
        return "Victory"
    else:
        print("It was a portal that took you to a random place")
        return "Teleport"

def play_game():
    print("Welcome to the Adventure Game!\nYou have to either find the final portal, or get the treasure from the chest!")
    player = choose_character()
    print(f"You are playing as {player}. Let the adventure begin!")
    
    current_room = "Cave Entrance"
    
    while current_room != "Victory":
        room = rooms[current_room]
        print(f"\n{room['description']}")
        
        if current_room == "Battle":
            current_room = battle()
            continue
        
        if current_room == "Teleport":
            current_room = Teleport()
            continue

        if current_room == "Chest":
            current_room = Treasure()
            continue
        
        choices = room["choices"]
        if not choices:
            break  # End game if no choices are left
        
        print("Options:")
        for action in choices:
            print(f"- {action}")
        
        choice = input("What do you do? ").lower()
        if choice in choices:
            current_room = choices[choice]
        else:
            print("Invalid choice! Try again.")
    
    print("Congratulations! You have won the adventure! Thanks for playing!")

if __name__ == "__main__":
    play_game()
    while input("Do you want to play again? (type yes or no) ") == "yes":
        play_game()
    print("This game has ended.")
        