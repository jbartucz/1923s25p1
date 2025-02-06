import random

# characters & enemies in the game
game_chars = ["The Mage", "The Vamp", "The Soundcloud Rapper", "The Drain Warrior"]
enemy_chars = ["Ken Carson", "Nettspend", "Playboi Carti", "Destroy Lonely", "Osamason"]
player_inventory = [] # player's inventory
# weapons that can be gained 
loot_list = ["magic purple potion", "sword", "powerful microphone that emits death rays", "gun"] 

# dictionary of our rooms
rooms = {
    "Forest": {
        "description": "You are standing at the edge of a dense, eerie forest. A chilling fog surrounds you. You have 2 choices:",
        "choices": {
            "Go straight to the Castle Gates": "Castle Gates",
            "Go back into the forest": "Bad Ending"
        }
    },

    "Castle Gates": { 
        "description": "Castle gates scarily loom over you.",
        "choices": {
            "Go straight and enter the castle": "Main Hall",
            "Go left": "The Cemetery",
        }
    },

    "The Cemetery": {
        "description": "Tombstones line the graveyard. Rats are scampering about and it seems ghouls are out haunting..",
        "choices": {
            "Go deeper into the cemetery and find an open shack": "The Shack",
            "Turn back to the castle gates": "Castle Gates",
        }
    },

    "The Shack": {
        "description": "A random shack with weapons strewn about and blood stains everywhere.",
        "choices": {
            "Turn back into the cemetery": "The Cemetery",
            "Head straight back to the castle": "Castle Gates",
        }
    },

    "The Forest": {
        "description": "The thick heavy fog hangs over the air, but you see a pair of eyes glinting in the dark.",
        "choices": {
            "You approach the figure": "Forest",
            "Turn back to the castle gates": "Castle Gates"
        }
    },

    "Main Hall": {
        "description": "You approach a dark hall that smells like must and death. It seems raided and desolate.",
        "choices": {
            "Go upstairs to explore the second level": "Upper Hall",
            "Go left where you hear noises": "The Dark Corridors",
        }
    },

    "Upper Hall": {
        "description": "You are now on upper level that overlooks the main hall. Here, you have access to the king's chambers.",
        "choices": {
            "Head right toward the chambers": "King's Chambers",
            "Head back downstairs": "Main Hall",
        }
    },

    "The Dark Corridors": {
        "description": "You find yourself at another empty hall lined with cobwebs and the skeletons of past servers. There appears to be more stairs leading down.",
        "choices": {
            "Follow the noises and go downstairs": "The Torture Chambers",
            "Turn back to the main hall": "Main Hall"
        }
    },

    "King's Chambers": {
        "description": "You are now in King Carti's cryptic chamber. You can: ",
        "choices": {
            "Lurk around the room" : "Game End",
            "Leave the room": "Upper Hall"
        }
    },

    "The Torture Chambers": {
        "description": "You notice the torture devices filling the area, deeply unsettled by the blood, coldness, and faint scary noises.",
        "choices": {
            "The torture chamber is filled with poisionous gas. It is too late to escape.": "Bad Ending",
        }
    },

    "Bad Ending": {
        "description": "Unfortunately, your choice lead to an inevitable death.",
        "choices": {} # no more movements can be made
    },

    "Game End": {
        "description": "Playboi Carti is in the rooom you are searching for",
        "choices": {
            "Destroy him with one hit!": "Game End",
            "Try to actually be friends with Carti": "Bad Ending"
        }
    }
}


def init_game():
    '''
    Purpose: Initializes the game setting and first user prompts.
    Parameter(s): none
    Return Value: none
    '''

    # set beginning game location & character HP
    current_location = "Forest"
    char_hp = 100

    print("\n..::|WELCOME|::..\nTO 5 nights of OPIUM... a game of survival against the Opium leaders in their grungy castle.")
    print("\nHOW THE GAME WORKS:\nYou will be exploring 10 rooms in the Opium Castle in hopes to take down King Carti.\nIn each room, you will either get attacked or find loot.\nIf you manage to find Carti in some room without reaching 0 HP (you start with 100), then you win the game.")

    # infinite loop to allow us to reprompt user, if invalid input is given
    while True:
        response = input("\nWould you like to play? Please enter yes or no: ")
        # validate user input
        if response == "yes" or response == "Yes":
            print("\nYou're officially in the game. Here is a list of who you can be:")
            for i, char in enumerate(game_chars, 1): 
                print(i, char)
            
            # allow the player to choose
            user_input = input("\nPlease type the character you would like exactly (ex. The Mage) or type random for a surprise: ")
            if user_input in game_chars:
                print(f"\nYou have chosen {user_input}. Get ready to start your adventure! Spawning you in...\n")
                start_game(current_location, char_hp)
            elif user_input == "random":
                # random character choosing (0-3)
                random_index = random.randint(0, 3)
                user_character = game_chars[random_index]
                print(f"\nYou have chosen {user_character}. Get ready to start your adventure! Spawning you in...\n")
                start_game(current_location, char_hp)
            else:
                print("\nError: Could not find character. Please read directions carefully and enter character's name as is.\n")
                continue
        elif response == "no" or response == "No":
            print("\nSad to see you go. Goodbye!\n")
            return # exit the game
        else:
            # invalid input was supplied
            print("Invalid input. Please enter yes or no. Try again.")
            continue

def print_room_info(current_room):
    '''
    Purpose: We can call this method everytime to print the current room's description and choices.
    Parameter(s): location, which is the starting location (str)
    Return Value: none
    '''
    room_info = rooms[current_room]
    print(room_info["description"])
    
    # convert dictionary to a list to iterate easier
    choices = list(room_info["choices"].keys())
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

def move_rooms(current_room, next_key):
    '''
    Purpose: Handles the movement between rooms.
    Parameter(s): current_room (str): the player's current room.
                  next_key (str): The number corresponding to the user's choice.
                  
    Return Value: the new room to move to
    '''

    # get key value pair of choices 
    choice_list = list(current_room["choices"].items())

    # get the new chosen index
    if len(choice_list) == 0:
        # means we reached "bad" or "good" ending; no next room to go to
        return None
    else:
        # we have a valid chosen key 
        chosen_key = choice_list[next_key - 1]
        # access value
        next_room = chosen_key[1]

        
    print(f"\nOption: {next_key} chosen. Moving you to the {next_room}...")

    # Return the room the player will move to (the value in the choices dictionary)
    return next_room 

def handle_room_event(location, health_bar):
    '''
    Purpose: Handles what happens when the player enters a room (loot or enemy).
    Parameter(s): location (the player's current room)
                  health_bar (current health of player)
    Return Value: new health (after events)
                  new room ocation (after events) 
    '''
    has_enemy = random.choice([True, False])
    enemy_chance = random.randint(0, (len(enemy_chars) - 1))

    if has_enemy:
        chosen_enemy = enemy_chars[enemy_chance]
        while chosen_enemy == "Playboi Carti":
            # regenerate:  we only want carti in king's chambers for the winning outcome
            new_enemy_chance = random.randint(0, len(enemy_chars) - 1)  # re-roll the enemy
            chosen_enemy = enemy_chars[new_enemy_chance]

        print(f"\nOh no. In the room you found {chosen_enemy}.")

        # player must take damage upon encountering an enemy regardless
        damage = random.randint(20, 80)
        health_bar -= damage
        print(f"{chosen_enemy} attacked! You lost {damage} HP. You now have {health_bar} HP.\n")

        # do a health check in case we die
        if health_bar < 0:
            return location, health_bar

        # check if there exists a weapon in player's inventory
        if "sword" in player_inventory or "powerful microphone that emits death rays" in player_inventory or "gun" in player_inventory:
            print(f"You can use your {player_inventory[random.randint(0, (len(player_inventory) - 1))]} to defeat the your chosen enemy!")
            defense_choice = input("\nDo you want to attack? Type yes or no: ") 
            if defense_choice == "Yes" or defense_choice == "yes":
                # assuming weapon is used to defeat enemy; remove from the list
                print("Enemy sucessfully attacked. Enemy died.\n")
                enemy_chars.remove(chosen_enemy)
            elif defense_choice == "No" or defense_choice == "no":
                print(f"You snooze you lose. {chosen_enemy} got you again.")
                health_bar -= damage
                print(f"Your HP is now {health_bar}.\n")
                # do a health check in case we die
                if health_bar < 0:
                    return location, health_bar
                else:
                    return location, health_bar # need to return regardless??
            else:
                print("Invalid input and action. Please enter yes or no next time. Game continuing...\n")

    elif has_enemy == False:
        # we get loot instead
        random_gen = random.randint(0, (len(loot_list) - 1)) # -1 to account for indexing @ 0
        acquired_loot = loot_list[random_gen]

        if acquired_loot not in player_inventory:
            player_inventory.append(acquired_loot) # immediately add
            print(f"ITEM ACQUIRED: You found a {acquired_loot}!\n")
        else:
            # already in inventory
            print(f"ITEM ACQUIRED: You got a {acquired_loot} but it is already in inventory. Not collecting.\n")
        
        if "magic purple potion" in player_inventory:
            health_bar += 35
            player_inventory.remove("magic purple potion")  

            if health_bar > 100:
                # cap health back to 100
                health_bar = 100
            
            print(f"The magic purple potion gave you +35 HP. You're health is now at: {health_bar}\n")  
        
    return location, health_bar  # return the updated health

def start_game(location, health_bar):
    '''
    Purpose: Starts the main game loop; directing user to rooms and encountering choices
    Parameter(s): location, which is the starting location (str)
    Return Value: none
    '''

    # keeps looping, so long that player is alive
    while health_bar > 0:
        room_info = rooms[location]

        # set up the scene
        print_room_info(location)
        room_choice = input("\nWhich option do you choose? Please enter (1, 2, 3, etc): ")
        # validate user input
        if not room_choice.isdigit():
            print("\nInvalid input. Please enter number on choice list.\nRe-prompting you now...\n")
            continue  # keep prompting user

        # num is valid
        if 1 <= int(room_choice) <= len(room_info["choices"]):
            # get the next room
            location = move_rooms(room_info, int(room_choice))
        else:
            print("Invalid input. Please enter number on choice list.\nRe-prompting you now...\n")
            continue

        # game ending conditions
        if location == "Game End":
            print("\nYou found Playboi Carti in the rom and successfully defeated him. Congratulations, you win!")
            break  # quit game
        elif location == "Bad Ending":
            print("\nUnfortunately, your choice led to an inevitable death.")
            break  # quit game
        elif health_bar <= 0:
            print("\nGAME OVER, YOU DIED.\nThanks for playing!")
            break  # Immediately exit the loop
        else:
            # keep playing and update location/health if needed
            location, health_bar = handle_room_event(location, health_bar)
    
    # The game ends here (when HP depletes completely), return to exit the function
    print("GAME OVER: You're health dropped below 0.\nThanks for playing! Please restart game if you want to play again!\n ")
    return

# runs our program.
if __name__ == '__main__':
    init_game()
