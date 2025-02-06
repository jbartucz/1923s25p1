# Game Title: House
# Goal: Find Mom

import random

def welcome():
    print("\nWelcome to the game HOUSE where you are trying to find MOM.")
    print("MOM is hiding in one of the ten rooms in your HOUSE.")

    print("\nThe rooms in your house are: ")
    print("\t1. Living Room")
    print("\t2. Kitchen")
    print("\t3. Dining Room")
    print("\t4. Bathroom")
    print("\t5. Garage")
    print("\t6. Laundry Room")
    print("\t7. Master Bedroom")
    print("\t8. Bedroom One")
    print("\t9. Bedroom Two")
    print("\t10. Office")

    print("\nThe instructions for game play are: ")
    print("\t1. You can only move into adjacent rooms.")
    print("\t2. You can choose to move North, South, East, or West. No diagonals.")
    print("\t3. If you move in a direction where no room exists, you'll receive an 'Invalid Direction' error for walking into a wall.")
    print("\t4. If you encounter an enemy, you must answer their question correctly before proceeding.")

def choose_character(characters):
    print("\nFirst, please choose your character from the following options: ")
    
    for i, character in enumerate(characters):
        print(f"\t{i+1}. {character}")

    choice = input("Enter the name of your character choice: ")
    choice = choice.lower().strip()

    while(True):
        for character in characters:
            if choice == character.lower():
                return character
        print("Please enter a valid character name.")
        choice = input("Enter the name of your character choice: ")

def mom_location():
    rand_int = random.randint(2,10) # returns a random integer in range [start, end] including the end points.
    if rand_int == 2: return "Kitchen"
    elif rand_int == 3: return "Dining Room"
    elif rand_int == 4: return "Bathroom"
    elif rand_int == 5: return "Garage"
    elif rand_int == 6: return "Laundry Room"
    elif rand_int == 7: return "Master Bedroom"
    elif rand_int == 8: return "Bedroom One"
    elif rand_int == 9: return "Bedroom Two"
    else: return "Office"

def enemy_encounter():
    enemies = ["Dad", "Big Brother", "Little Sister", "Jerry the Dog", "Karl the Cat"]
    rand_idx = random.randint(0,4)
    enemy = enemies[rand_idx]

    rand_int = random.randint(0,3)
    if(rand_int == 0):
        print(f"\nUh oh, you bumped into {enemy}! Answer their question to continue searching for MOM.")
        answer_question()

    return

def answer_question():

    question_bank = {
    "1": {
       "question": "What is 2 + 2? ",
       "choices": {
           "correct": "4",
           "B": "3",
           "C": "1"
       }
    },
    "2": {
       "question": "One atmosphere is approximately equal to: ",
       "choices": {
           "A": "3 psi",
           "B": "4 psi",
           "correct": "14.7 psi"
       }
    },
    "3": {
       "question": "About how many tonnes does a cloud weight? Include commas in answer.",
       "choices": {
           "A": "1",
           "B": "1,000",
           "correct": "1,000,000"
       }
    },
    "4": {
       "question": "How much more likely are giraffes to be struck by lightning compared to people?",
       "choices": {
           "A": "3",
           "correct": "30",
           "C": "300"
       }
    },
    "5": {
       "question": "The oldest person ever to be recorded lived to what age?",
       "choices": {
           "A": "100",
           "correct": "122",
           "C": "112"
       }
    },
    "6": {
       "question": "Which TV show featured the first interracial kiss ever aired?",
       "choices": {
           "correct": "Star Trek",
           "B": "Scooby Doo",
           "C": "The Bachelor"
       }
    },
    "7": {
       "question": "How many keys does a piano have?",
       "choices": {
           "correct": "88",
           "B": "99",
           "C": "111"
       }
    },
    "8": {
       "question": "Which famous Roman leader introduced the leap year?",
       "choices": {
           "A": "Marcus Aurelius",
           "correct": "Julius Caesar",
           "C": "Donald Trump"
       }
    },
    "9": {
       "question": "What war was ended by the signing of the Treaty of Versailles?",
       "choices": {
           "A": "World War Two",
           "correct": "World War One",
           "C": "War of 1812"
       }
    },
    "10": {
       "question": "What kind of fish is Dory from Finding Nemo?",
       "choices": {
           "correct": "Blue tang",
           "B": "Clownfish",
           "C": "Bluefish"
       }
    }
    }

    rand_question = str(random.randint(1,10))

    print()
    print(question_bank[rand_question]["question"])
    
    print("Answer choices: ")
    for choice in question_bank[rand_question]["choices"].values():
        print("\t", choice)

    is_incorrect = True

    while is_incorrect:
        ans = input("Enter the correct answer: ").strip().lower()
        if(ans == question_bank[rand_question]["choices"]["correct"].strip().lower()):
            print("\nCorrect! Please continue searching for MOM.")
            is_incorrect = False
        else:
            print("Incorrect choice. Please try again.")
            print("Note: The enemy is quite picky. You must match spaces and characters EXACTLY or else you cannot proceed.")

    return


# Main program
def run_game():
    '''
    Purpose: Main function to run the game program
    Parameter(s): none
    Return Value: none
    '''

    # Welcome note to player and game instrustucions
    welcome()

    # User chooses a character to play from the given options
    characters = ["John", "Lisa", "Sam", "Payton"]
    my_character = choose_character(characters)
    print(f"\nHello {my_character}! You are currently in the Living Room.")

    # Rooms in game
    rooms = {
   "Living Room": {
       "description": "You are in the Living Room. From here, you can enter the: \n\tKitchen \n\tBathroom \n\tLaundry Room \n\tOffice",
       "choices": {
           "north": "Bathroom",
           "east": "Kitchen",
           "south": "Office",
           "west": "Laundry Room"
       }
    },
    "Kitchen": {
       "description": "You are in the Kitchen. From here, you can enter the: \n\tLiving Room \n\tDining Room.",
       "choices": {
           "south": "Dining Room",
           "west": "Living Room",
       }
    },
    "Dining Room": {
       "description": "You are in the Dining Room. From here, you can enter the: \n\tKitchen \n\tOffice",
       "choices": {
           "north": "Kitchen",
           "west": "Office",
       }
    },
    "Bathroom": {
       "description": "You are in the Bathroom. From here, you can enter the: \n\tMaster Bedroom \n\tLiving Room \n\tBedroom One",
       "choices": {
           "north": "Master Bedroom",
           "south": "Living Room",
           "west": "Bedroom One"
       }
    },
    "Garage": {
       "description": "You are in the Garage. From here, you can enter the: \n\tLaundry Room \n\tOffice",
       "choices": {
           "north": "Laundry Room",
           "east": "Office",
           "south": "Dungeon"
       }
    },
    "Laundry Room": {
       "description": "You are in the Laundry Room. From here, you can enter the: \n\tBedroom One \n\tLiving Room \n\tGarage",
       "choices": {
           "north": "Bedroom One",
           "east": "Living Room",
           "south": "Garage",
           "west": "Front Door"
       }
    },
    "Master Bedroom": {
       "description": "You are in the Master Bedroom. From here, you can enter the: \n\tBathroom \n\tBedroom Two",
       "choices": {
           "south": "Bathroom",
           "west": "Bedroom Two",
       }
    },
    "Bedroom One": {
       "description": "You are in Bedroom One. From here, you can enter the: \n\tBedroom Two \n\tBathroom \n\tLaundry Room",
       "choices": {
           "north": "Bedroom Two",
           "east": "Bathroom",
           "south": "Laundry Room"
       }
    },
    "Bedroom Two": {
       "description": "You are in Bedroom Two. From here, you can enter the: \n\tMaster Bedroom \n\tBedroom One",
       "choices": {
           "east": "Master Bedroom",
           "south": "Bedroom One",
       }
    },
    "Office": {
       "description": "You are in the Office. From here, you can enter the: \n\tLiving Room \n\tDining Room \n\tGarage",
       "choices": {
           "north": "Living Room",
           "east": "Dining Room",
           "west": "Garage"
       }
    },
    "Dungeon": {
        "description": "You have found the DUNGEON. To enter, continue south. To return to the garage, turn around and go north.",
        "choices": {
            "north": "Garage",
            "south": "\nYou have stumbled into the DUNGEON. Unfortunately, the door locked behind you, and you cannot escape. A few weeks go by, and you die of dehydration. You didn't even get to say bye to MOM."
        }
    },
    "Front Door":{
        "description": "You have found the front door! To travel through, go west. To return to the Laundry room, turn around and go east.",
        "choices": {
           "east": "Laundry Room",
           "west": "\nInspired by the Fourth of July, you embark on a jouney of independence into the great big world. Who needs MOM anyway?"
       }
    }
    }

    current_room = "Living Room"
    mom_hidden = True
    mom_loc = mom_location()
    # print("mom location: ", mom_loc)

    while(mom_hidden):
        if(current_room == mom_loc):
            print(f"\nCongraulations {my_character}! You found MOM in the {current_room}!")
            print()
            break
        else:
            enemy_encounter()
            print("\nDarn, MOM is not here.")
            print(rooms[current_room]["description"])

            direction = input("Please enter a direction you would like to go (north, south, east, or west): ").lower()

            while direction not in rooms[current_room]["choices"]: # iterates until user input matches one of the viable choices for a room
                print("Oops! Invalid direction. Either you misspelled something or walked into a wall.")
                direction = input("Please enter a valid direction (north, south, east, or west): ").strip().lower()
            
            if(current_room == "Front Door" and direction == "west") : 
                print(rooms[current_room]["choices"][direction])
                break
            if(current_room == "Dungeon" and direction == "south") : 
                print(rooms[current_room]["choices"][direction])
                break

            current_room = rooms[current_room]["choices"][direction]


    # continue running program until user enters "5" to quit
        

if __name__ == '__main__':

    # run the game program 
    run_game()
