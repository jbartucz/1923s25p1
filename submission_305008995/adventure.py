# define room dictionary
rooms = {
    "Space Shuttle Control Room" : {"Description": """    You wake up after an emergency crash landing on an unknown planet. 
    Your entire team has disappeared and foliage from the planet's forest like environment has broken through. 
    Some plants have even started growing. You look around and pick up a weapon from your surroundings.""",
        "Weapons": { "Broken Glass": "Shard from the shattered control room window - grab it and make your way to the escape hatch", "Blaster": "Pistol that fires a beam of energy - grab it and make your way to the escape hatch?",
                    "Sword": "Heavy Broadsword forged by your friend Gale renound the blacksmith - grab it and make your way to the escape hatch?"
        }
    }
    , 
        "Primeval Forest": {"Description":"Old Foggy Forest filled with Kings and critters, random encounter, choose the river or the path",
                            "Choices": {"A": "The River",
                                        "B": "The Path"}}
    ,
        "The River":{"Description": "A Lazy, bubbling float down The River to a mysterious lake shrouded by fog",
                     "Choices": {"A": "The Dock",
                                 "B": "The Lake"}}
    ,
        "The Path":{"Description": "An arduous hike along a scraggly, yet beaten, path leading to the Mountain. This path follows the river, be careful not to fall in! Along the way, you meet a playful dragon named Frank. Frank decides to join you on your adventure. Together, you and Frank discover a large, seemingly bottomless pit as you near the base of the mountain",
                    "Choices": {"A: The Pit",
                                "B: The Mountain",
                                "C: The River"}}
    ,
        "The Dock":{"Description": "A lamp lit dock with a hooded figure. Talk to the figure or push past.",
                    "Choices":{"A":"The Lake",
                               "B": "The Night King's Throne Room"}}
    ,
        "The Lake":{"Description": "Fight a sea monster in the middle of the lake. Random Roll to determine its age.",
                    "Choices":{"A": "The Cave"}}
    ,
        "The Cave":{"Description": "A damp, muchy environment filled with trolls. You see three large trolls and a smaller fourth figure slumped over one of their shoulders. Your friend and crewmate, Gale, has been taken captive by the trolls and must be rescued!",
                    "Choices":{"A":"The Night King's Throne Room"}}
    ,
        "The Pit":{"Description": "A bottomless pit, a secondary enterance to the Night King's Throne Room",
                   "Choices": {"A":"The Night King's Throne Room"}}
    ,
        "The Mountain": {"Description": "Along the path, you meet a friendly dwarf who asks you to help save their people from the goblins (he can pay handsomely). Currently there is a battle raging on the mountainside and the dwarves are greatly outnumbered. You are thrust into the fight and must survive"}
    ,
        "The Night King's Throne Room": {"Description": "A cavernous hall with gothic structures and large pillars. The King of darkness awaits you..."}
    
}

# import necessary libraries
import random
import sys

# define functions
def randomRoll():
    '''
    Purpose: random roll a six sided die to determine actions in the game
    Parameter(s): none
    Return Value: number 1-6
    '''
    
    diceRoll = random.randint(1,6)
    return diceRoll

def randEnemy():
    '''
    Purpose: random roll a six sided die to determine what enemy you will face in the game
    Parameter(s): none
    Return Value: troll, wizard, goblin
    '''
    
    diceRoll = random.randint(1,6)
    
    if diceRoll < 3:
        enemy = 'wizard'
    elif diceRoll > 2 and diceRoll < 5:
        enemy = 'troll'
    else:
        enemy = 'goblin'
    print(f"Enemy:  {diceRoll} .... A {enemy}!!!")
    return enemy

# main
if __name__ == '__main__':
    # initialize finalChoice variable to avoid errors
    finalChoice = 0
    # initialize inventory
    inventory = []
    
    # Space Shuttle Control Room
    print(rooms["Space Shuttle Control Room"]["Description"])
    weaponSelection = input("\nPlease input weapon choice: Blaster, Sword, or Broken Glass: ")
    weaponDecision = input(f"\nYou have selected the {rooms["Space Shuttle Control Room"]["Weapons"][weaponSelection]}. Answer Yes or No: ")
   
    while weaponDecision != 'Yes':
        weaponSelection = input("\nPlease, select your weaopn please: Blaster, Sword, or Broken Glass: ")
        weaponDecision = input(f"\nYou have selected the {rooms["Space Shuttle Control Room"]["Weapons"][weaponSelection]}. Answer Yes or No: ")
        if weaponDecision == '1':
            weaponDecision == 'Yes'
    inventory.append(weaponSelection)
    print(f"Added {weaponSelection} to inventory")        
    # Primeval Forest
    print(f"\nAfter prying open the hatch, you step out into the Primeval Forest. Immediately, you are surprised by a rusttling in the bushes. Roll the dice to see if it is a friend or foe.")
    print("A 1-3 will produce a friendly while a 4-6 means an enemy. Ready?!?! Roll...")
    RollForStone = randomRoll()
    enemy = randEnemy()
    print(f"Roll: ",RollForStone)
    if RollForStone < 4:
        print(f"A small {enemy} pops out of the bushes. WaruGNitang! The {enemy} offers his salutations in a language you do not understand. Perplexed, you look on as the {enemy} waddles over and hands you a small stone with a rune engraved in it. You get the feeling this will be helpful in the future.")
        stone = 'stone'
        inventory.append(stone)
        print("Added (stone) to inventory")
    elif RollForStone > 3:
        print(f"A(n) {enemy} pops out and attacks you (he has mistaken you for a warrior under the Night King!! You defend yourself with your {weaponSelection} and the {enemy} bursts into confetti. How strange.")

    print(f"After your encounter, you take a moment to take in your surroundings. Which path will you choose? {rooms["Primeval Forest"]["Choices"]}")
    pathOrRiver = input("Choice: ")
    
    # initialize pathChoice, riverChoice, and riverEnd choice
    pathChoice = ''
    riverChoice = ''
    riverEnd = 0
    
    if pathOrRiver == 'B':
        # The Path
        pathChoice = input(f"\nYou chose the Path {rooms["The Path"]}. Where will you go next? Climb down to The River(C)? Jump into The Pit(A)? Summit the Mountian(B)? Enter A, B or C: ")
        if pathChoice =='C':
            pathOrRiver = 'A'

    if pathOrRiver == 'A':
        # The River
        print("Great choice!")
        riverChoice = input(f"You took {rooms["The River"]["Description"]}. You see {rooms["The Dock"]["Description"]} (A to push past, B to land): ")

    # The Lake
    
    if riverChoice == 'A':
        print(f"\nYou slowly swim past the dock and into the open water of the lake. Suddenly, a huge snake like monster leaps our of the water and plunges toward you!!")
        if weaponSelection != 'Broken Glass':
            print(f"\nYour quickly draw your {weaponSelection} and slay the snake. Slowly the lake begins to drain and you are pulled down into {rooms["The Cave"]["Description"]}")
            riverEnd = 1
        elif weaponSelection == 'Broken Glass' and RollForStone < 4:
            print(f"\nYou are gobbled up by the Serpent of the Lake. The runestone you got earlier begins to glow. It explodes in a volley of light and blows a hole in the serpent. YOU ARE FREE!")
            print(f"Slowly the lake begins to drain and you are pulled down into {rooms["The Cave"]["Description"]}")
            inventory.remove(stone)
            print("Removed stone from inventory")
            riverEnd = 1
        elif weaponSelection == 'Broken Glass' and RollForStone > 3:
            print(f"\nYou are eaten by the Lake Serpent. Better luck next time!")
            sys.exit()

    elif riverChoice == 'B':
        dockChoice = input(f"\nYou pull yourself up out of the water and approach the hooded figure. What will you do: A(Fight) or B(Talk): ")
        if dockChoice == 'A':
            print(f"The figure slowly stands up and his cloak falls from his head revealing a glistening silver crown with red rubies. A low rumbling begins and the very earth begins to shake. Before you can draw your {weaponSelection}, one punch sends you flying backwards into the lake.")
            print(f"Suddenly, a huge snake like monster leaps our of the water and plunges toward you!!")
            if weaponSelection == 'Sword' or 'Blaster':
                print(f"\nYour quickly draw your {weaponSelection} and slay the snake. Slowly the lake begins to drain and you are pulled down into {rooms["The Cave"]["Description"]}")
                riverEnd = 1
            elif weaponSelection == 'Broken Glass' and RollForStone < 4:
                print(f"\nYou are gobbled up by the Serpent of the Lake. The runestone you got earlier begins to glow. It explodes in a volley of light and blows a hole in the serpent. YOU ARE FREE!")
                print(f"Slowly the lake begins to drain and you are pulled down into {rooms["The Cave"]["Description"]}")
                riverEnd = 1
            elif weaponSelection == 'Broken Glass' and RollForStone > 3:
                print(f"\nYou are eaten by the Lake Serpent. Better luck next time!")
                sys.exit()
        if dockChoice == 'B':
            print(f"\nThe figure slowly stands up and his cloak falls from his head revealing a glistening silver crown with red rubies. The figure claims to be the ruler of an underground city and is angry you have interrupted his peaceful day off. A low rumbling begins and the very earth begins to shake. You are knocked unconcious. Everything fades to black.... ")
            riverEnd = 2

    # The Cave
    
    if riverEnd == 1:
        print(f"(You have entered The Cave)")
        if weaponSelection == 'Sword':
            print("You expertly swing your sword and decapitate all three trolls in one slice. Gale, who was only pretending to be knocked out, can't believe his eyes. He starts crying tears of joy. After you two catch up, he tells you that the rest of the crew has been taken by the Night King, a hooded figure who wears a crown of silver. Together, you and Gale head further into the cave, eventually reaching a large cavern. An entire city sprawls before you. Miles away, a castle is visible. That is where you head.")
            finalChoice = 1
        elif weaponSelection == 'Blaster':
             print("You expertly shoot your blaster, putting holes in all three trolls. Gale, who was only pretending to be knocked out, can't believe his eyes. He starts crying tears of joy. After you two catch up, he tells you that the rest of the crew has been taken by the Night King, a hooded figure who wears a crown of silver. Together, you and Gale head further into the cave, eventually reaching a large cavern. An entire city sprawls before you. Miles away, a castle is visible. That is where you head.")
             finalChoice = 1
        elif weaponSelection == 'Broken Glass':
            print("You startle all three trolls but your weapon is too weak to defeat them. Try again with a better weapon!")
            sys.exit()
    # The Pit
    if pathChoice == 'A':
        print(f"\nYou have chosen The Pit: {rooms["The Pit"]["Description"]}. Luckily for you, Frank is able to fly you down safely!")
        print(f"\nYou fly down through a skylight into {rooms["The Night King's Throne Room"]["Description"]}")
        finalChoice = 1
    # The Mountain
    if pathChoice == 'B':
        
        print(f"{rooms["The Mountain"]["Description"]}")
        goblins = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        count = 0
        while count < 10:
            rollCommand = input("Roll Again to see how many goblins you can kill (enter): ")
            roll = randomRoll()
            print(f"You got {roll} goblins!")
           
            
            count += roll
            for i in range(roll):
                goblins.remove(1)
        print("The goblins fell back")
        print(f"In exchange for your heroism, the dwarves crowned you their leader. You and Frank go on to have many adventures together. However, the mystery of what happened to your crew hangs over your head. Try another path to find the answer!")
    # The Night King's Throne room
    if finalChoice == 1:
        print(f"Finally, you reach {rooms["The Night King's Throne Room"]["Description"]}")
        print("First you must defeat the horde(at least 5) of goblins to get to the Night King and save your crew.")

        goblins = [1,1,1,1,1,1,1,1,1,1,1,1]
        count = 0
        while count < 5:
            rollCommand = input("Roll Again to see how many goblins you can kill (enter): ")
            roll = randomRoll()
            print(f"You got {roll} goblins!")
            
            count += roll
            for i in range(roll):
                goblins.remove(1)

        print("The goblins scatter as the King steps down from his throne")
        print("Now its time to fight the King!")
        print(f"The Kinge emmense power is chilling. You are beaten back and forth but you won't give up. After a long arduous battle, you finally overpower the king with your {weaponSelection}. Luckily for you {weaponSelection}(s) is(are) actually his kryptonite. You find your missing crew locked in the dungeon and set them free! Congratualtions you have won!")


            










    