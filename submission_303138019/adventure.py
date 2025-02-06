# Gina Pehl CSCI 1923 Project 1

# Adventure of the Sea

import random

characters = ['Dolphin', 'Mermaid', 'Sailor', 'Pirate', 'Shark', 'Jellyfish', 'Crab', 'Octopus']
enemies = ["Shark", "Kraken", "Ghost Pirate", "Sea Serpent", "Leviathan"]

places = {
    "Coral Cove": {
        "description": "A beautiful cove filled with vibrant coral and darting fish. The adventure begins here.",
        "choices": {
            "ride a seahorse east": "Mermaid Lagoon",
            "dive into the abyss": "The Abyssal Trench",
            "follow a school of fish west": "Mystic Tideshore"
        }
    },
    "Mermaid Lagoon": {
        "description": "A shimmering lagoon where mermaids sing songs of the deep.",
        "choices": {
            "join the mermaids' song": "Undersea Kingdom",
            "float back west": "Coral Cove",
            "search for hidden pearls on shore": "Mystic Tideshore"
        }
    },
    "Mystic Tideshore": {
        "description": "A sandy shore with mysterious glowing seashells that whisper secrets of the ocean.",
        "choices": {
            "chase a ghostly light north": "Stormcaller’s Watch",
            "skip over the tidepools east": "Coral Cove",
            "follow a trail of golden sand south": "Golden Coast"
        }
    },
    "The Abyssal Trench": {
        "description": "A deep, dark trench filled with unknown horrors and hidden treasures.",
        "choices": {
            "kick hard and swim up": "Coral Cove",
            "search the eerie depths": "Leviathan's Lair",
            "follow glowing jellyfish south": "The Lost Galleon"
        }
    },
    "The Lost Galleon": {
        "description": "An abandoned pirate ship still carrying ghostly echoes of its crew.",
        "choices": {
            "unlock the captain’s chest": "Treasure Vault",
            "climb the mast for a better view": "Stormcaller’s Watch",
            "descend into the hull north": "The Abyssal Trench"
        }
    },
    "Undersea Kingdom": {
        "description": "A magnificent underwater city ruled by merfolk and guarded by sea creatures.",
        "choices": {
            "surface for air": "Mermaid Lagoon",
            "explore the coral palace": "Treasure Vault",
            "venture into the deep caves east": "Leviathan's Lair"
        }
    },
    "Stormcaller’s Watch": {
        "description": "A towering rock formation where storms gather and secrets are kept.",
        "choices": {
            "slide down a waterfall south": "Golden Coast",
            "scale the cliffs west": "Mystic Tideshore",
            "swing from a broken mast east": "The Lost Galleon"
        }
    },
    "Leviathan's Lair": {
        "description": "The domain of the mighty sea monster, surrounded by shipwrecks and bones.",
        "choices": {
            "sneak past the slumbering beast": "The Abyssal Trench",
            "challenge the monster": "Treasure Vault",
            "find a secret tunnel west": "Undersea Kingdom"
        }
    },
    "Treasure Vault": {
        "description": "A hidden chamber filled with lost treasures and guarded by ancient magic.",
        "choices": {
            "climb a golden staircase north": "Stormcaller’s Watch",
            "escape through a hidden hatch west": "The Lost Galleon",
            "run through a tunnel south": "Golden Coast"
        }
    },
    "Golden Coast": {
        "description": "A peaceful, golden shore that marks the end of the journey.",
        "choices": {
            "watch the sunset and end your adventure": "Game Over"
        }
    }
}

def gameIntro():
    print("Its time for your Sea Adventure!")
    print("Choose your character:")
    
    num = 1
    for character in characters:
        print(f"{num}. {character}")
        num = num + 1
    
    choice = input("Enter the number of your character: ")
    while not choice.isdigit() or int(choice) not in range(1, len(characters) + 1):
        choice = input("Invalid choice. Enter a valid number: ")
    
    playerCharacter = characters[int(choice) - 1]
    print(f"You have chosen {playerCharacter}! Your adventure starts now...\n")
    return playerCharacter

def randomEvent(): 
    if random.random() < 0.2: # %20 chance of an enemy encounter
        enemy = random.choice(enemies)
        print(f"Oh no! A {enemy} appears! You must escape in! \n")

def playGame():
    playerCharacter = gameIntro()
    currentPlace = "Coral Cove"

    while currentPlace != "Game Over":
        print(f"\n{places[currentPlace]['description']}")
        randomEvent()
        print("Your choices: ")
        for action, destination in places[currentPlace]['choices'].items():
            print(f"- {action} (Leads to {destination})")

        move = input("What do you do? ").lower()

        if move in places[currentPlace]['choices']:
            currentPlace = places[currentPlace]['choices'][move]
        else:
            print("Invalid choice. Try again.")
    
    print("Congratulations! You have reached the Golden Coast and completed your adventure!")
    
if __name__ == "__main__":
    playGame()