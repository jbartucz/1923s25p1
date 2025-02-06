# DATE: 2/2/25
# OVERVIEW: This program takes a user through a text adventure RPG-style. The user will
#           select a role and stat points that will affect their journey. Every playthrough
#           will begin in the same room, but the following locations will be determined by 
#           the player's actions and luck.

import random

def game_start():
    '''
    Purpose: Introduce the user to the game and setting
    Parameter(s): none
    Return Value: bool (if True, continue adventure. If False, stop adventure)
    '''
    print("\nWelcome to a new adventure! Are you ready to embark on an epic and (hopefully) delicious quest?")
    
    print("\nAs an ambassador from the Kitchen Kingdom, you have been given the honorable task of traveling across the")
    print("Pantry Plains to gather the highest quality sandwich ingredients. With your cutting edge culinary skills,")
    print("you must make the most grand sandwich of all the land to feed the Chef Supreme. If pleased, they will")
    print("bring peace and unity across this Culinary Continent. However, if you fail, there's no telling how sour")
    print("the consequences wil be...")

    choice = str(input("\nTo succeed, you will need both luck and a keen sense of taste. Do you dare continue? (y/n): "))

    isInvalidInput = True
    while isInvalidInput:
        if choice == "y":
            print("You are a brave soul indeed!")
            isInvalidInput = False
            return True
        
        elif choice == "n":
            print("You've abandoned your duties and stayed home... good for you?")
            isInvalidInput = False
            return False
        
        else:
            choice = str(input("I do not understand your response... please clarify, do you wish to continue? (y/n): "))

def rules():
    '''
    Purpose: Tell the user the rules of the game
    Parameter(s): none
    Return Value: none
    '''
    print("\nIn this game, you will choose which villages you want to get ingredients from for the bread, meat, and")
    print("toppings for your epic sandwich. At each location, your success in obtaining these ingredients will be")
    print("determined by adding together your roll of a twenty-sided die and your respective stat for either 'bread',")
    print("'meat', or 'prep'.")

def character_select(pcs, stats):
    '''
    Purpose: Tell the user the roles they can select and have them choose
    Parameter(s): pcs (List containing the playable characters and their stats (dictionaries)), stats (list)
    Return Value: int (0: Baker, 2: Butcher, 4: Prep cook, 6: Sous chef)
    '''
    print("\nYou may choose which adventurer to play as. Here are your options and their stats:")
    for i in range(0, 8, 2):
        print(f"{int(i/2) + 1}) The {pcs[i]}:")
        print(f"    Bread: {pcs[i+1]["bread"]}")
        print(f"    Meat: {pcs[i+1]["meat"]}")
        print(f"    Prep: {pcs[i+1]["prep"]}")
    
    choice = str(input("\nPlease enter an integer between and including 1 through 4 to select your character: "))

    isInvalidInput = True
    while isInvalidInput:
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            print("An excellent choice! You are ready to begin your journey... be prepared!")
            isInvalidInput = False
        else:
            choice = str(input("I do not understand your response... please clarify, who do you wish to play as? (1, 2, 3, or 4): "))

    stats[0] = pcs[(int(choice) - 1) * 2 + 1]["bread"]
    stats[1] = pcs[(int(choice) - 1) * 2 + 1]["meat"]
    stats[2] = pcs[(int(choice) - 1) * 2 + 1]["prep"]

    return (int(choice) - 1) * 2 # index of playable character title in list 'pcs'
                                 # add one to this value to access the corresponding stats

def room_enter(rooms, room, pcs, pc, stats, ingredients):
    '''
    Purpose: Run all events and present choices for a room the user enters
    Parameter(s): rooms (dictionary), room (string), pcs (list), pc (int), stats (list), ingredients (list)
    Return Value: string of next room name
    '''
    print(f"\nYou have entered the {room}")
    print(f"{rooms[room]["description"]}")

    # Run the events (if any)
    if room == "Pantry Plains": # First room
        print("\nBefore you begin to gather ingredients, you decide to train your culinary skills. You can...")
        print(f"1) {rooms[room]["choices"]["action A"]}")
        print(f"2) {rooms[room]["choices"]["action B"]}")
        print(f"3) {rooms[room]["choices"]["action C"]}")
        choice = str(input("\nWhat would you like to do? (1, 2, or 3): "))

        isInvalidInput = True
        while isInvalidInput:
            if choice == "1" or choice == "2" or choice == "3":
                isInvalidInput = False
            else:
                choice = str(input("I do not understand your response... please clarify, what would you like to do? (1, 2, or 3): "))

        statBoost = dice_roll()
        stats[int(choice) - 1] = stats[int(choice) - 1] + statBoost
        print("Your current stats are:")
        print(f"    Bread: {stats[0]}")
        print(f"    Meat: {stats[1]}")
        print(f"    Prep: {stats[2]}")

    elif room == "Castle Chef": # Last room
        print("\nGuy Fieri, in an epic and ethused voice, says:")
        print("We’re takin’ you on a road rockin’ trip down to Flavortown, where the gravitational force of bacon warps the laws of space and time.")
        
        sandwichScore = ingredients[0] + ingredients[1] + ingredients[2]
        print(f"\nYou present him your sandwich, which has a score of: {sandwichScore}")
        print("He takes a bite, and then says...")

        if sandwichScore > 65:
            print("Holy moly, Stromboli!")
            print("\nHe loves your sandwich. You saved the day!")
        elif sandwichScore > 40:
            print("You know what, it might just be a mound of oil-logged Pillsbury crescent dough, but it’s bomb-dot-com tasty, amigo!")
            print("\nYou're confused if he likes it or not... Afterwards, nothing really changes.")
        else:
            print("ALWAYS sauce with authority!")
            print("\nHe's not a big fan of the sandwich. You failed and Kitchen Chaos takes over...")

    else: # Inbetween rooms
        print(f"\nThis is where you obtain your {rooms[room]["stat"]} ingredient.")
        print("You search this place endlessly, and...")

        ingredQuality = dice_roll()
        
        if rooms[room]["stat"] == "bread":
            print(f"Your {rooms[room]["stat"]} score: {stats[0]}") # Current stat
            ingredQuality = ingredQuality + stats[0] # Total ingredient score
            ingredients[0] = ingredQuality # Update ingredient score

        elif rooms[room]["stat"] == "meat":
            print(f"Your {rooms[room]["stat"]} score: {stats[1]}")
            ingredQuality = ingredQuality + stats[1]
            ingredients[1] = ingredQuality

        elif rooms[room]["stat"] == "prep":
            print(f"Your {rooms[room]["stat"]} score: {stats[2]}")
            ingredQuality = ingredQuality + stats[2]
            ingredients[2] = ingredQuality

        print(f"Total ingredient score: {ingredQuality}")
        print("\n...You find what you were looking for!")

        if room == "Vegan Village" and pcs[pc] == "Butcher":
            print("\nAs the Butcher, you're not very fond of Vegans. In fact, you two have... quite the beef.")
            ingredients[1] = ingredients[1] - 15
            print(f"Your current ingredient quality for meat is now: {ingredients[1]}")

    # Decide where to go next (if any)
    if room == "Burger-burg" or room == "Teriyaki Town" or room == "Club Club":
        print("\nYou travel to your final destination to present an epic sandwich to Chef Supreme...")
        return rooms[room]["choices"]["direction A"]
    
    elif room == "Castle Chef":
        print("\nThis marks your journey's end...")
        return []
    
    else:
        print("\nYou come across a fork (not a utensil) in the road. There's three directions to go...")
        print(f"1) {rooms[room]["choices"]["direction A"]}")
        print(f"2) {rooms[room]["choices"]["direction B"]}")
        print(f"3) {rooms[room]["choices"]["direction C"]}")
        nextRoom = str(input("\nWhere would you like to travel to next? (1, 2, or 3): "))

        isInvalidInput = True
        while isInvalidInput:
            if nextRoom == "1" or nextRoom == "2" or nextRoom == "3":
                print("An excellent choice! You continue on your journey...")
                isInvalidInput = False
            else:
                nextRoom = str(input("I do not understand your response... please clarify, where would you like to go? (1, 2, or 3): "))

        if nextRoom == "1":
            return rooms[room]["choices"]["direction A"]
        elif nextRoom == "2":
            return rooms[room]["choices"]["direction B"]
        else:
            return rooms[room]["choices"]["direction C"]

def dice_roll():
    '''
    Purpose: If the user pursues an event, have them roll a d20 to quantify how their luck 
             affects their adventure
    Parameter(s): none
    Return Value: int
    '''
    rollVal = random.randint(1, 20)

    print(f"\nYour roll: {rollVal}")

    return rollVal

# Main program
def adventure_time():
    '''
    Purpose: Main function to run the adventure program
    Parameter(s): none
    Return Value: none
    '''

    # Collection of rooms the user will travel through
    rooms = {
    "Pantry Plains": {
        "description": "You see vast fields of wheat, barley, and other grasses blowing with the wind.",
        "choices": {
            "direction A": "Brioche Base",
            "direction B": "Sourdough Settlement",
            "direction C": "Pumpernickel Pueblo",
            "action A": "Train your baking skills",
            "action B": "Train your rotisseur skills",
            "action C": "Train your preparation skills"
        }
    },
    "Brioche Base": {
        "description": "As you walk through the gates, you begin to bounce on the soft road, which is actually just brioche bread. As is everything else here.",
        "choices": {
            "direction A": "Poultry Place",
            "direction B": "Bovine Borough",
            "direction C": "Vegan Village"
        },
        "stat": "bread"
    },
    "Sourdough Settlement": {
        "description": "You are greeted to a small town who's people seem rough on the outside, but they're just nice and soft on the inside.",
        "choices": {
            "direction A": "Poultry Place",
            "direction B": "Bovine Borough",
            "direction C": "Vegan Village"
        },
        "stat": "bread"
    },
    "Pumpernickel Pueblo": {
        "description": "Ouch! You slipt and fell on a rogue oat that inexplicably covers the entire location. At night time, the buildings and the sky look the same.",
        "choices": {
            "direction A": "Poultry Place",
            "direction B": "Bovine Borough",
            "direction C": "Vegan Village"
        },
        "stat": "bread"
    },
    "Poultry Place": {
        "description": "There are feathers everywhere, you can't seem to get rid of them. And, without noticing, you start walking like a dinosaur.",
        "choices": {
            "direction A": "Burger-burg",
            "direction B": "Teriyaki Town",
            "direction C": "Club Club"
        },
        "stat": "meat"
    },
    "Bovine Borough": {
        "description": "In this fuzzy place, it seems like every step you take is the right MOOve. You also can't stop making cow joke here.",
        "choices": {
            "direction A": "Burger-burg",
            "direction B": "Teriyaki Town",
            "direction C": "Club Club"
        },
        "stat": "meat"
    },
    "Vegan Village": {
        "description": "The scent of soy fills your nose as you walk past many white, rectangular Tofu houses.",
        "choices": {
            "direction A": "Burger-burg",
            "direction B": "Teriyaki Town",
            "direction C": "Club Club"
        },
        "stat": "meat"
    },
    "Burger-burg": {
        "description": "This place has it all! A Culver's, McDonald's, and Five Guys... Oh my!",
        "choices": {
            "direction A": "Castle Chef"
        },
        "stat": "prep"
    },
    "Teriyaki Town": {
        "description": "All the buidlings here shine a dark brown, and its as if you can taste something salty, sweet, and spicy all at once.",
        "choices": {
            "direction A": "Castle Chef"
        },
        "stat": "prep"
    },
    "Club Club": {
        "description": "This party town seems like every other, except there's bacon. Yum!",
        "choices": {
            "direction A": "Castle Chef"
        },
        "stat": "prep"
    },
    "Castle Chef": {
        "description": "You've never seen walls this tall before. As you enter and travel a seemingly endless chamber, you are face-to-face with the Chef Supreme... Who's actually just Guy Fieri.",
        "choices": {
            "action A": ""
        }
    }
    }

    # Playable characters for the user to choose from and their stats
    pcs = [
        "Baker",
        {
            "bread": 10,
            "meat": 0,
            "prep": 5,
        },
        "Butcher",
        {
            "bread": 0,
            "meat": 10,
            "prep": 5,
        },
        "Prep cook",
        {
            "bread": 2,
            "meat": 2,
            "prep": 11,
        },
        "Sous chef",
        {
            "bread": 5,
            "meat": 5,
            "prep": 5,
        }
    ]

    # Current stats of the player, may change according to adventure events
    stats = [0, 0, 0] # bread, meat, prep
    
    # Dynamic list tracking the quality of gathered ingredients
    ingredients = [0, 0, 0] # bread, meat, prep

    begin = game_start()

    if begin == True:
        rules()
        pc = character_select(pcs, stats)
        breadRoom = room_enter(rooms, "Pantry Plains", pcs, pc, stats, ingredients)
        meatRoom = room_enter(rooms, breadRoom, pcs, pc, stats, ingredients)
        prepRoom = room_enter(rooms, meatRoom, pcs, pc, stats, ingredients)
        finalRoom = room_enter(rooms, prepRoom, pcs, pc, stats, ingredients)
        room_enter(rooms, finalRoom, pcs, pc, stats, ingredients)

    print("\nFin.")

if __name__ == '__main__':

    # Let the user embark on an epic journey!
    adventure_time()