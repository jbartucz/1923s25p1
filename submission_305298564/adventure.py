from random import random
from time import sleep

roomDict = {

    "Entrance" : {

        "description" : "You are floating just outside an old abandoned ship. You don't know how long it's been drifting, but your scans indicated that most of the critical "
                        "components are still good. If you can get to the bridge, you'll likely be able to start the engine and take the ship for yourself.\n\nYou see an airlock you think you could enter through.",

        "choices" : {
            "Enter" : "Storage",
            "Leave" : "Quit"
        }},

    "Storage" : {

        "description" : "It's dusty here. There are old steel crates everywhere, most empty and the rest locked. There's a door stuck open with "
                        "a sign next to it that says MED, and a reinforced bulkhead labeled BARRACKS that you think you could get open.",
        "choices" : {
            "Med" : "Medical",
            "Barracks" : "Barracks"
        }},

    "Medical" : {

        "description" : "A medical bay. Various instruments are strewn across the floor. This is one of the few places in the ship that still has the lights "
                        "on, likely from emergency power. There's a stuck-open door labeled STOR, a heavily worn one labeled ENG, and a sliding glass panel with the word NAV on the wall next to it.",

        "choices" : {
            "Stor" : "Storage",
            "Eng" : "Engineering",
            "Nav" : "Navigation"
        }},

    "Engineering" : {

        "description" : "There are deactivated panels and stations lining the walls of this room. The large engine in the center is eerily silent. You can hear sounds of faint long-term generators in the background, "
                        "and you disturb motes of dust into the air as you walk into the room. There's a door labeled NAV, one labeled MED, and a ladder that goes up through some kind of hatch.",
        
        "choices" : {
            "Ladder" : "Armory",
            "NAV" : "Navigation",
            "MED" : "Medical",
        }},

    "Armory" : {

        "description" : "The hatch is locked, but it has a keypad so you try all the most generic space passwords, eventually getting it open by entering in 0451. You raise the hatch and emerge into what appears to be "
                        "an armory. You see many places where personal arms would've been stored, but all of them seem to be empty.",

        "choices" : {
            "Ladder down to Engineering" : "Engineering"
        }},

    "Navigation" : {

        "description" : "Once-active screens and digital charts used to light this room. Now the only things left are empty chairs and clear course plots. This is truly a stupid, useless room, almost like the ship's architect "
                        "was really phoning it in with the quality of the rooms and just wanted to reach a certain amount of them. To leave here, there's a short tunnel labeled MAINT, a steel door labeled ENG, and a sliding glass panel labeled "
                        "MED that you can access.",

        "choices" : {
            "MAINT" : "Maintenance Hallway",
            "Eng" : "Engineering",
            "Nav" : "Navigation"
        }},

    "Bridge" : {

        "description" : "A doorway to the bridge, blocked by a still-active blue oscillating forcefield.",

        "choices" : {
            "Back away from the field" : "Maintenance Hallway"
        }},

    "Maintenance Hallway" : {

        "description" : "You stand in a decrepit maintenance hallway. There's a door labeled LAB, one labeled NAV, and a forcefield over an entryway labeled BRIDGE.",

        "choices" : {
            "Nav" : "Navigation",
            "Lab" : "Laboratory",
            "Bridge" : "Bridge"
        }},

    "Laboratory" : {

        "description" : "Broken glass and dim light fill this room. Once-white surfaces are now a mixture of gray and brown. "
                        "There's a light door labeled MAINT and a partially shattered bulkhead labeled BARR available from this room.",

        "choices" : {
            "MAINT" : "Maintenance Hallway",
            "BARR" : "Barracks"
        }

    },

    "Barracks" : {

        "description" : "You are in what is very clearly a barracks or crew quarters of some sort. Rows of empty bunk beds in various states of disarray line the room. "
                        "knocked-over desks with forgotten papers strewn around them make navigation difficult through this room. The barracks have a damaged bulkhead labeled LAB and another "
                        "labeled STOR. Interestingly, there's also a ladder that seems to go down through some vertical tunnel. ",

        "choices" : {
            "LAB" : "Laboratory",
            "STOR" : "Storage",
            "Down the ladder" : "Brig"
        }

    },

    "Brig" : {

        "description" : "You climb nearly twenty feet down the ladder in an unlit tunnel. At the bottom is a short walkway that slowly leaks more white light out from behind a "
                        "heavily reinforced bulkhead system.",

        "choices" : {
            "Ladder up to the Barracks" : "Barracks"
        }

    }
    
}

# Once in a room, call get_choice(room["choices"]) to print a simple formatted string of available choices and get input.
# Example: if in storage, choices will read Choices: |[M]ed|[B]arracks|. Lowercase the *first letter* of user input 
# to determine what user chooses. If their choice does not match any, print an error message and repeat choice menu.
def getChoice(choices, userPrompt = "What do you do?"):
    '''
    - Purpose: Once at a decision point, print out all the valid choices available to the player and wait until they choose one.
    - Parameters: choices is a dictionary that has strings as keys. The type of the value does not matter.
    - Return val: the value corresponding to the selected key.
    '''
    
    choiceString = "\n\t|"

    for choice in choices:
        choiceString += f'[{choice[0]}]{choice[1:]}|'

    # Ask for user input. If it matches a valid choice, return the result of that choice
    while (True):
        userChoice = input(f'| {userPrompt}\n{choiceString} ')
        print() # For formatting purposes

        # Check that any valid input was picked up before trying to index it
        if (len(userChoice) != 0):
            for choice in choices:
                if (choice[0].lower() == userChoice[0].lower()):
                    return choices[choice]
            
        print("Invalid choice. Please type one of the valid options below.")
        print(choiceString + "\n")


def changeRoom(room):
    '''
    - Purpose: changes from the current room to another, and triggers any necessary events in the new rooms.
    - Parameters: room (a key in roomDict)
    - Return val: the choice the player makes in that room.
    '''
    global currentPlayer
    global clearedRooms

    print(room + ": " + roomDict[room]["description"])
    # For better readability of the output
    sleep(0.5)

    # If statements for rooms with special events
    if (room == "Storage"):

        if ("Storage" not in clearedRooms):

            print("However, there's something pretty unusual in this room: a Giant Miniature Space Hamster! It's standing (on all fours) "
                  "pretty menacingly.")

            startFight = getChoice({"Yes" : True, "No" : False}, "Do you engage the fiend?")
            if (startFight == True):

                # Check if player died in the fight and stop execution before continuing if so
                if (currentPlayer.attack(Enemy("Giant Miniature Space Hamster")) == False):
                    return "Quit"
                
                print("Right as you turn away from your finished foe, you spot a pile of black devices with bright white "
                      "markings in the shape of many common danger symbols throughout the quadrant. It seems the creature may have been guarding "
                      "or hoarding these. You can comfortably hold one of these devices in your hand, so you grab one just in case you'll need it later.")
                currentPlayer.addItem("Strange Device")
            else:
                print("You decide to let the horrible abomination live another day.")

            print("\nOne way or another, the hamster is dealt with.")
            
            clearedRooms.append("Storage")

        # If I were to do this project again, I would definitely remove this line from every case here and just add it at the end. However, currently
        # I am too exhausted to check for any errors that may cause, so I am leaving it this dumb inefficient way for now.
        return (getChoice(roomDict[room]["choices"], "Where do you want to go?"))
    
    if (room == "Bridge"):

        if ("Keycard" in currentPlayer.inventory):
            print("[KEYCARD] You take out your keycard and hold it up to the reader. The forcefield drops with a descending tone and its unending buzzing finally stops! "
                  "You quickly rush over to the power console to begin turning on the engines and other important systems, and almost immediately after you restore power, "
                  "you hear a knocking sound on the canopy and look over to see a massive glowing eye! It's a squid! An Evil Alien Squid!\nYou hear the squid's thoughts projected "
                  "into your brain!\n")
            sleep(1)
            
            if (len(currentPlayer.slainEnemies) > 1):
                friendsString = ""
                for i in range(0, len(currentPlayer.slainEnemies)):

                    deadEnemy = currentPlayer.slainEnemies[i]
                    if (i == len(currentPlayer.slainEnemies) - 1): # Checks if this is the last element
                        # F-string not used here and for below print statement because the version of Python on Gradescope doesn't like them
                        friendsString += " and " + deadEnemy + "!"
                        
                    # If more than two elements, will need commas for the list of them
                    elif (len(currentPlayer.slainEnemies) > 2):
                        # If this is the second to last element, don't put a space after the comma because then the last element will have a double space
                        if (i == len(currentPlayer.slainEnemies) - 2):
                            friendsString += deadEnemy + ","
                        else:
                            friendsString += deadEnemy + ", "

                    # If only two elements do not place unnecessary comma
                    else:
                        friendsString += deadEnemy

                print("\"You killed my friends " + friendsString + " I must avenge them!")
                currentPlayer.fightSquid()
            
            else:
                print("<<\"What are you doing here? Do you desire to die\">>")
                if (currentPlayer.stats["Wisdom"] >= 5):
                    print("\n[WISDOM] You probably shouldn't threaten this giant alien squid.\n")
                elif (currentPlayer.stats["Wisdom"] < 5):
                    print("\n[WISdom...?] You should totally threaten this giant squid monster thing. Bet it's a wuss!.\n")

                
                result = getChoice({"Persuade" : "Persuade", "Confront" : "Confront", "Deny" : "Deny" })

                if (result == "Persuade"):

                    if (currentPlayer.stats["Persuasion"] > 6):
                        print("[PERSUASION SUCCESS] You tell the squid that not only do you not want to die, but you also think it has a very pretty eye. The squid responds back <<\"Why thank you! I'm very proud of it. "
                              "You may do as you please!\">>\n")
                    else:
                        print("[PERSUASION FAILURE] You can't quite grasp telepathic communication, and end up accidentally comparing the squid to many repugnant things. The squid psychically roars in your head "
                              "and begins its assault on the ship!")
                        currentPlayer.fightSquid()
                        
                elif (result == "Confront"):
                    print("You idiot! You somehow hear the squid laugh telepathically, before it launches an all-out assault on the ship!")
                    currentPlayer.fightSquid()

                elif (result == "Deny"):
                    
                    if (currentPlayer.stats["Intelligence"] > 6):
                        print("[INTELLIGENCE SUCCESS] You weave a long and semantically complex argument about how neither you nor anything else truly exists, and therefore it is impossible for you to \"be\" here! "
                              "The squid gets very confused and tries to understand everything you just said, and its distraction provides you the perfect opportunity to finish initializing the engines and get out of there!\n")
                    else:
                        print("You bravely puff out your chest, stand up straight, and greet the squid with your most powerful of intellectual retorts: \"Nuh uh!\". The squid is rather unamused, and begins an attack on the ship!")
                        currentPlayer.fightSquid()

            # Is the player still alive? Means they either beat squid in combat or talked their way out of the situation.
            if (currentPlayer.ended == False):
                print("=!=!=!=!=!=!=!= You are victorious! You escape with your life and in control of a new ship! =!=!=!=!=!=!=!=\n\n\n\n")

            # Don't need a special message for the other case, because the player already knows they died.
            return("Quit")
   
        else:
            print("You can't find any way to get past the forcefield. You notice what appears to be a keycard reader next to the frame, however. Maybe "
                  "you could find the bridge card somewhere else on the ship.")
            return (getChoice(roomDict[room]["choices"], "Where do you want to go?"))
        
    if (room == "Engineering"):

        if ("Engineering" not in clearedRooms):
            print("Amidst all this relative piece, you hardly notice the figure standing dead still in the corner of the room until he runs out and lunges "
                  "at you. It's an Evil Space Person!")
            
            if (currentPlayer.profession == "Geriatric"):

                startFight = getChoice({"Attack the young man!" : True, "Scold him for such unruly behavior. Treating the elderly like this? He should be ashamed!" : False})
                if (startFight == True):
                    if (currentPlayer.attack(Enemy("Evil Space Person")) == False):
                        return "Quit"
                else:
                    print("The Evil Space Person is now stricken by guilt for his poor behavior. To apologize, he reaches into his pocket and hands you something that looks like a keycard.")
                    currentPlayer.addItem("Keycard")

            else:
                print() # To make up for the lost line in spacing because we don't have a getChoice call in this path
                if (currentPlayer.attack(Enemy("Evil Space Person")) == False):
                    return "Quit"
                else:
                    print("After he's finished with, you notice a card sticking out of one of his pockets. You take it. It seems to be some kind of keycard.")
                    currentPlayer.addItem("Keycard")
                
            print("The Evil Space Person is no longer a threat.")
            clearedRooms.append("Engineering")

        return (getChoice(roomDict[room]["choices"], "Where do you want to go?"))
    
    if (room == "Armory"):

        if ("Armory" not in clearedRooms):
            print("Slumped on the floor just next to the hatch appears to be another Evil Space Person... but this time they're armed! It's an Evil Space Person (with a) Gun! Luckily, he seems to be asleep right now.")

            takeGun = getChoice({"Take the gun" : "Take", "Leave him" : "Leave", "End him" : "End"}, "Do you try and take his gun without waking him up, leave him be, or launch a surprise attack and end him now before he can do the same to you?")

            if (takeGun == "End"):
                print("[SUCCESS] Rather unscrupulous of you. I suppose you'll inherit his moral ambiguity as well as his weapon. He expired, and his gun you acquired!\n\t+5 POWER!")
                currentPlayer.addItem("Gun")
                currentPlayer.stats["Power"] += 5
                currentPlayer.addSlainEnemy("Morally Questionable Space Person (with a Gun)")
            elif (takeGun == "Take"):
                print("[SUCCESS] Very carefully, you sneak the gun from him without waking him up.\n\t+5 POWER!")
                currentPlayer.addItem("Gun")
                currentPlayer.stats["Power"] += 5
            else:
                print("You slowly walk away. Best to let sleeping Space People (with guns) lie.")
            
            print("There's nothing else of value in the armory.")
            clearedRooms.append("Armory")
        
        return (getChoice(roomDict[room]["choices"], "Where do you want to go?"))
    
    if (room == "Laboratory"):

        if ("Laboratory" not in clearedRooms):

            print("You do find a weird space-syringe. Who knows how old it is. It's pretty rusty. Should you inject yourself with it?")

            if (currentPlayer.stats["Wisdom"] >= 5):
                print("\n[WISDOM] Do NOT inject yourself with the syringe. DO NOT DO IT. Also, just because something is "
                      "on a spaceship does not mean it is a \"space\" something! It's just a random syringe, don't do it!\n")
            if (currentPlayer.stats["Wisdom"] < 5):
                print("\n[WISdom...?] You should totally stab yourself with that thing. It'll be rad. You'll probably get "
                      "sweet space-superpowers-- why else would the needle be in a lab if not for crazy mad space-science "
                      "experimentation? Doooo ittt. Everyone will think you're so cool!\n")
                
            inject = getChoice({"Yeah!" : True, "No! Absolutely not!" : False}, "Do you inject yourself with the syringe?")
            if (inject == True):
                rand = random()
                if (rand < 0.75): 

                    print("[WHY?] You chose... poorly. On the plus side, they might name a disease after you. Great job, genius.\n\t-3 WIS, -3 INTELLIGENCE, -5 DURABILITY")

                    currentPlayer.stats["Wisdom"] -= 3
                    currentPlayer.stats["Intelligence"] -= 3
                    currentPlayer.takeDamage(5)
                    # To check if player dies from the damage
                    if (currentPlayer.ended) == True:
                        return "Quit"
                    
                elif (rand > 0.75):
                    print("[YOU GOT LUCKY THIS TIME] Against all logic, rhyme, and reason, the syringe somehow did seem to give you superpowers. That was still "
                          "a pretty dumb decision though.\n\t+1 WISDOM, +2 INTELLIGENCE, +5 DURABILITY, +4 PERSUASION")
                    currentPlayer.stats["Wisdom"] += 1
                    currentPlayer.stats["Intelligence"] += 2
                    currentPlayer.stats["Durability"] += 5
                    currentPlayer.stats["Persuasion"] += 4
            else:
                print("Smart choice.\n\t+1 WISDOM")
                currentPlayer.stats["Wisdom"] += 1

            clearedRooms.append("Laboratory")
            print("There is no longer anything of note in the lab.")

        return (getChoice(roomDict[room]["choices"], "Where do you want to go?"))

    if (room == "Barracks"):

        if ("Barracks" not in clearedRooms):
            print("\nYou accidentally trip over a file of old papers, most of which promptly disintegrate. However, when you picked yourself up from the floor "
                  "you noticed a cylindrical key with a plastic tag attached under one of the desks. You grab it, and on closer inspection the plastic tag holds "
                  "a cartoonish illustration of an old black powder era cannon. Odd.")
            currentPlayer.addItem("Cannon Key")
            clearedRooms.append("Barracks")
            
        return (getChoice(roomDict[room]["choices"], "Where do you want to go?"))
        
    if (room == "Brig"):

        if ("Brig" not in clearedRooms):
            print("The bulkhead however is ajar, and with great effort you push it fully open and step into an almost blindingly white room. It's clear "
                  "that this room is using quite a bit of the ship's remaining power generation. This room is roughly shaped like a cube, and each corner points a floodlight towards the "
                  "center of the chamber, which appears to house what looks like a cell. This must be the ship's brig, though everything else about it is pretty odd.\n")
            sleep(1)
            
            print("Interestingly, the cell is currently occupied-- this must be who all the lights and reinforcements are for. Perplexingly, however, the cell is home "
                  "to a... Harmless Old Lady? She notices you immediately and walks closer to the translucent bars of her cage. \"Have you seen my grandson? I have a gift "
                  "for him! I need to find him so he can get his gift on time, but I got lost and I got stuck here. Can you help me out? Be a dear and pull that large black "
                  "and red lever on the wall over there for me, will you?\"\n")
            sleep(1)
            
            if (currentPlayer.profession == "Security"):
                print("[SECURITY] You notice the wrinkles on her skin seem to fill themselves will a shiny black fluid every so often. The way she moves around isn't "
                      "right either, it's too elastic-- like she's merely pretending to have bones. You suddenly remember something you heard about all the way back in "
                      "training but never saw: shapeshifters! A hostile alien species, their true form is an amorphous black substance that they shape on macro and microscopic levels "
                      "to assume any form they want. That substance however is very vulnerable to high amounts of direct light, weakening them in moderate light and even destroying "
                      "them with enough direct exposure. You're lucky you remembered how to identify shapeshifters all the way back from your training!\n\n...The fact that the lever "
                      "is labeled \"light switch, DO NOT TURN OFF (!!SHAPESHIFTER!!)\" helps too.\n")
                
            letOut = getChoice({"Yes" : True, "No" : False}, "Do you pull the level to let her out?")
            if (letOut == True):
                print("\"Why thank you, dear!\" she gratefully says. She walks through her open cell door and her smile grows larger and larger until it appears very much inhuman. "
                      "Shiny black tendrils burst from all over her body, each snaking towards and putting out one of the lights in the room simultaneously, plunging you into complete "
                      "darkness. You can hear slithering, sticky sounds from all around you, and then a voice right behind your ear whispers \"I haven't known freedom for years... to "
                      "express my utmost appreciation for your selfless act, I'll ensure your unwise demise is relatively quick.\"\n")
                sleep(1)

                # This block of code could be somewhat compacted by making the ellipsis animation thing a function, but I only ever use it here so I'm not sure if it's worth having
                # basically a static helper function in the code to do this instead of just manually repeating it one more time.
                print("it slithers closer.", end="", flush = True)
                sleep(1)
                print(".", end="", flush = True)
                sleep(1)
                print(".", end="", flush = True)
                sleep(1)
                print("Closer.", end = "", flush = True)
                sleep(1)
                print(".", end="", flush = True)
                sleep(1)
                print(".", end="", flush = True)
                sleep(2)
                print(">>>TOO CLOSE<<<")
                sleep(2)

                if ("Strange Device" in currentPlayer.inventory):
                    print("\nYou suddenly remember the device you picked up in the storage room from earlier! Black with white markings of danger-- it could be a light grenade! The only issue is "
                          "that you have no idea how to activate it... as you feel more of the viscous gooey substance surround you, you frantically try every motion and action you can think "
                          "to activate the strange object, until finally you give up on real plans and just squeeze it as hard as you can... which somehow works! Blindingly bright white light seeps "
                          "from the cracks between your fingers and palm in your hand as the device slowly engages, and then in an instant you are completely blinded when it fully detonates. \n\n"
                          "You aren't deaf, however, and you hear the most horrific shrieking coming from all angles around you. Like a buzzsaw on cement. After several minutes, your vision slowly "
                          "returns and you can see that the entire brig and some of the hallways is covered in a grey cemented form of the amorphous creature, waves of black liquid petrified in time "
                          "in almost a static yet fluid expression of pain. \n\nBut the old lady's dead and you aren't, so that part's pretty awesome! Probably time to leave the brig now.")
                    currentPlayer.addSlainEnemy("Harmless Old Lady")
                else:
                    print("\nYou are defenseless against this unique horror. You try to fight, but the alien seems unaffected by your best efforts and it swiftly envelops you in the darkness. You are defeated.")
                    sleep(1)
                    currentPlayer.takeDamage(100)
                    return("Quit")
            else:
                print("\"Oh, I understand. Why would you ever help an old woman in need? Kids these days.\" All the 'friendly old woman' accent now drops from her speech, replaced instead by a metallic and "
                      "nearly liquid intonation. \"Don't worry, I'll be sure to visit you when I get out,\" she oozes at you. You might be crazy, but you're pretty sure as you walked away that you started to "
                      "see her eyes slide down her face. That was weird.")
                
            clearedRooms.append("Brig")

        return (getChoice(roomDict[room]["choices"], "Where do you want to go?"))

    else:
        #print(f"Room is {room}")
        return (getChoice(roomDict[room]["choices"], "Where do you want to go?"))


class Player:
    def __init__(self, profession):
        '''
        - Purpose: initialize a player object with the given profession's statblock.
        - Parameters: profession is a string that has a corresponding statblock in DictHelper
        - Return val: None
        '''
        self.stats = DictHelper.statBlocks[profession]
        self.profession = profession
        # Used to determine when game is over (usually used if player dies)
        self.ended = False
        # These two will be added two by external code and will be used in event checks later
        self.slainEnemies = []
        self.inventory = []

    def addItem(self, item):
        '''
        - Purpose: just a fancy way of appending to the inventory list in a way that prints a string announcing the item's acquisition to be extra clear
                   to the player when they get a new item.
        - Parameters: item is just a string for the name of the item.
        - Return val: None
        '''
        self.inventory.append(item)
        print(f'\n| ITEM ACQUIRED: {item}')

    def addSlainEnemy(self, enemyName):
        '''
        - Purpose: just a fancy way of appending to the slainEnemies list in a way that checks for existing entries so as to avoid duplicates. Would just use a set
                   but then would fail the "use two lists" requirement.
        - Parameters: enemyName is the string name of the enemy.
        - Return val: None
        '''
        if (enemyName not in self.slainEnemies):
                self.slainEnemies.append(enemyName)

    def attack(self, enemy):
        '''
        - Purpose: based on the stats of enemy and player, calculate results of fighting an enemy
        - Parameters: enemy is an object of the Enemy class
        - Return val: True if the player is still alive, False if they die in the fight.
        '''
        #global player
        playerPower = self.stats["Power"]
        enemyPower = enemy.stats["Power"]
        
        enemyStatus = "Alive"

        while((enemyStatus != "Dead") and (self.ended == False)):

            if (enemy.name != "Evil Alien Squid"):
                # Check for critical hit before normal attacks
                    if (random() < 0.1):
                        print(f"You critically hit the {enemy.name}, hurting them extra while avoiding their counterattack!")
                        enemyStatus = enemy.takeDamage(int(playerPower * 1.3))
                        print() # To make up for a lack of spacing because player is not injured when performing a crit

                    elif (playerPower > enemyPower):
                        print(f'The {enemy.name} attacks, but they are feeble compared to you!')
                        self.takeDamage(int(enemyPower * 0.5))
                        enemyStatus = enemy.takeDamage(playerPower)

                    elif (playerPower < enemyPower):
                        print(f'The {enemy.name} attacks, overpowering you!')
                        self.takeDamage(enemyPower)
                        enemyStatus = enemy.takeDamage(int(playerPower * 0.5))

            # The player is fighting the final boss, Evil Alien Squid
            else:
                if (random() < 0.1):
                    print("Critical! You hit the Evil Alien Squid right in the eye! It can't see you well enough to fight back!")
                    enemyStatus = enemy.takeDamage(int(playerPower * 1.5))
                    print() # To make up for a lack of spacing because player is not injured when performing a crit

                elif (playerPower > enemyPower):
                    print("The Evil Alien Squid attacks, but it was not prepared for cannon fire! You blast it as it swipes its tentacles "
                          "at the ship and tries to break through the glass with its beak!")
                    self.takeDamage(int(enemyPower * 0.5))
                    enemyStatus = enemy.takeDamage(playerPower)

                elif (playerPower < enemyPower):
                    print("The Evil Alien Squid easily crushes the ship with its lithe tentacles and powerful beak!")
                    self.takeDamage(enemyPower)
                    enemyStatus = enemy.takeDamage(int(playerPower * 0.5))

        self.addSlainEnemy(enemy.name)

        return (self.ended == False)

    def takeDamage(self, amount):
        '''
        - Purpose: subtract amount from player health. If health reaches or goes past 0, set ended = True and print their death message.
        - Parameters: amount is an int of how much damage they received.
        - Return val: None
        '''
        # Helps with pacing during combat and other times damage is received, so there's a slight progression of text instead
        # of just having all the info spit out at once.
        sleep(1)

        # Check to ensure no negative damage numbers
        if (amount < 0):
            amount = 0
        
        self.stats["Durability"] -= amount

        health = self.stats["Durability"]
        print(f'\n > You took {amount} point{"s" if amount != 1 else ""} of damage. You have {health} durability left.')

        if (health <= 0):
            print("You died! Game over.")
            self.ended = True

    def fightSquid(self):
        '''
        - Purpose: set up the specific boss fight with the Evil Alien Squid, checking for some conditions that will affect the battle.
        - Params: None
        - Return val: True if the player is victorious, False if they died in the fight.
        '''

        if (self.profession == "Captain"):
            print("\n[CAPTAIN] You can use your knowledge of evasive maneuvers to partially mitigate the squid's attacks!\n\t+10 DURABILITY!\n")
            self.stats["Durability"] += 10

        if ("Cannon Key" in self.inventory):
            print("\n[CANNON KEY] You remember the key to the cannons you found earlier! You insert it into a slot on the weaponry station and the ship's weapons activate. "
                  "Now you can fight back against the squid!\n\t+15 POWER! +10 DURABILITY!\n")
            self.stats["Power"] += 15
            self.stats["Durability"] += 10

        if (("Cannon Key" not in self.inventory) and (self.profession != "Captain")):
            print("\nYou have nothing to stop the Evil Alien Squid. You can try to harm it with the ship's anti-asteroid turrets, but you have little hope of survival.\n")

        return(self.attack(Enemy("Evil Alien Squid")))

class Enemy:

    def __init__(self, profession):
        '''
        - Purpose: initialize an enemy object with the given enemy's statblock. Slightly different than Player class in what functions exactly do and because it allows for unique enemy events.
        - Parameters: profession is a string that has a corresponding statblock in DictHelper. Uses same name as Player's parameter because their statblocks are formatted the same.
        - Return val: None
        '''
        self.stats = DictHelper.statBlocks[profession]
        self.name = profession
        #self.specialEvent = getEvent(name)

    def takeDamage(self, amount):
        '''
        - Purpose: used in combat situations with the player. May result in enemy death or event triggering.
        - Parameters: amount of damage (int) received
        - Return val: "Dead" if enemy defeated, "Alive" if not. I know there are infinitely better ways to do this than
                      to return strings, but I am forgetting those best practices for this situation and the string solution works ok.
        '''

        # Due to particular damage combos sometimes player can die the same turn they hit an enemy. When player dies, instead just end the current game execution.
        if (currentPlayer.ended == True):
            return "Alive"

        # Helps with pacing. See the same part of Player.takeDamage() for a more detailed explanation.
        sleep(1)

        # If event occurs, the fight is over regardless of damage sustained.
        if (self.stats["Durability"] <= 3):
            if (random() < 0.5):
                self.runEnemyEvent()
                return("Dead")
            
        # Check to ensure no negative damage numbers
        if (amount < 0):
            amount = 0

        self.stats["Durability"] -= amount
        print(f' > You dealt {amount} points of damage to the {self.name}!')

        if (self.stats["Durability"] <= 0):
            print("\n\t>>You have vanquished the foe!<<\n")
            return("Dead")
        else:
            return("Alive")

    def runEnemyEvent(self):
        '''
        - Purpose: some enemies have unique events that occur when they are at low health. This function handles those interactions.
        - Parameters: None
        - Return val: None
        '''

        # Currently, only these two enemies have events tied to them, so this block is just a placeholder event for
        # the other enemies.
        if (self.name != "Giant Miniature Space Hamster" and self.name != "Evil Space Person"):
            print("You surprise the enemy with a sudden lethal blow! They now lie defeated.")

        print("\n-/-/-/-/-/-|-|-EVENT-|-|-\-\-\-\-\-\n")

        # If health goes to 0 or below, enemy events can still trigger by design which means we have to make sure they aren't added in to slainEnemies twice.
        # Realistically we'd just use a set to fix this problem, but then that would fail the "use two list" part of the assignment.
        if (self.name == "Giant Miniature Space Hamster"):
            currentPlayer.addSlainEnemy(self.name)

            print("The Giant Miniature Space Hamster knows its end is nigh, and it ceases "
                  "all aggressive action immediately! It collapses and looks up at you with pleading, "
                  "beady eyes. It seems like it's asking to be spared.")
            if (currentPlayer.stats["Intelligence"] > 5):
                print("\n[INTELLIGENCE] You've read about these creatures before. They are famously very deceptive. It may be best "
                      "not to trust this devious beast.\n")
                    
            success = getChoice({"Accept" : False, "Crush" : True}, "Do you accept its surrender, or crush this foul beast under your heel?")
            if (success == False):
                print("You are but a fool! As soon as your guard is down, the hamster pulls a perfectly-hidden explosive out from behind its "
                      "furry back! It lets out a maniacal cackle as it flips a lever on the device, detonating it in a final blaze of glory!")
                currentPlayer.takeDamage(10)
            else:
                print("You have ended this horror. The Giant Miniature Space hamster shall threaten innocents no more.")

        elif (self.name == "Evil Space Person"):
            print("\"H-h-hey I quit! This sucks! I don't know what I was expecting living on a derelict ship (I never was a \"big picture\" kinda guy), but it wasn't this! "
                  "Call it a truce and I'll give you some useful information, alright? I know why you're really here, trust me you'll want to know this!")
            if (currentPlayer.stats["Wisdom"] > 5):
                print("\n[WISDOM] He seems to be genuine in his plea.\n")

            listen = getChoice({"Hear him out" : True, "Finish him off" : False}, "Hear him out or finish him off before he can stab you in the back?")
            if (listen == False):
                print("\"Silence, scoundrel!\" You command as you strike him down without letting him finish the sentence. It would've been just another trick, anyways. "
                      "what kind of reputable person lives in an abandoned spacecraft with no resources whatsoever? Regardless, you search through his pockets to see if he "
                      "was actually onto something. And you do find \"something\"-- over a dozen loose razorblades in his back pocket. Why? Why? This can't possibly have "
                      "any purpose other than hurting you. How long has he been keeping those in his pocket, ready to slightly annoy someone looting his corspe? Ow, you "
                      "cut yourself in several different places when you removed your hand from his trapped pocket. That's definitely going to make it a bit tougher to fight.\n\t-2 POWER")
                
                currentPlayer.addSlainEnemy(self.name)
                currentPlayer.stats["Power"] -= 2
            else:
                print("\"Thank you! Ok, so I know you're trying to get to the bridge and take the ship, 'cause that's the only reason anyone would come here. But first, make real "
                      "sure you stop by the barracks and look for a key with a little cannon on it. You'll need that to activate the main guns on this thing, and without those guns "
                      "you'd be practically defenseless against any big monsters or anyone else that wants to take this ship from you-- and a moving derelict is going to attract "
                      "a whole lotta space critters, so it's more likely than not you're gonna need those guns. Now leave me alone, please! Let me get back to doin' whatever it is I do!\"")
                if ("Cannon Key" in currentPlayer.inventory):
                    print("\n\"You... you've already got one? Oh. My bad then, honestly I was really riding on that one thing being valuable information. Uh, thanks for not killing me I guess? No takebacks!\"")
                

            

class DictHelper:

    # Dict to easily access statblocks for player classes and enemy types
    def makeStatDict(Power, Intelligence, Persuasion, Wisdom, Durability):
        '''
        - Purpose: Just a faster way to create a standardized dict of stats for players, enemies, and anything else that may need them.
        - Parameters: Each parameter is an integer that will be stored in statDict. Keys for each value are abbreviations of the param names.
        - Return val: The statDict or None if any of the values are not integers.
        '''
        
        # Attribute meanings:
        # Power: both combat strength and physical ability.
        # Intelligence: amount of pre-existing knowledge and ability to learn new things.
        # Persuasion: ability to convince and sway others.
        # Wisdom: decision-making skills and ability to predict outcomes of certain actions.
        # Durability: effectively acts as "hit points". Only attribute that will change (done in other functions). Dur of 0 = dead.

        statDict = {"Power": Power, "Intelligence": Intelligence, "Persuasion": Persuasion, "Wisdom": Wisdom, "Durability": Durability}
        # Ensure all values are ints to avoid any value errors later
        if all(isinstance(value, int) for value in statDict.values()) == False:
            print("ERROR: Tried to create stat dictionary with non-integer values.")
            return None
        
        return statDict
    
    # If I were to do this project again, I would definitely make this an enum using abbreviated terms for enum elements
    # and then somehow give each element two values (full name and statblock). I am unfamiliar with how to easily do this 
    # in Python, however.
    statBlocks = {
        # Player classes
        "Captain" : makeStatDict(6, 8, 5, 4, 13),
        "Geriatric" : makeStatDict(3, 7, 7, 10, 8),
        "Security" : makeStatDict(8, 4, 2, 6, 18),

        # Enemy classes
        "Giant Miniature Space Hamster" : makeStatDict(3, 1, 6, 1, 2),
        "Evil Space Person" : makeStatDict(6, 5, 3, 3, 9),
        "Harmless Old Lady" : makeStatDict(1, 5, 9, 9, 1),
        "Morally Questionable Space Person (with a Gun)" : makeStatDict(9, 5, 6, 3, 9),
        "Evil Alien Squid" : makeStatDict(14, 5, 1, 3, 35)
    }

def runGame():
    '''
    - Purpose: effectively acts as the main function for this program, actually runs the game. Very few actions are actually done in this function.
    - Parameters: None
    - Return val: None
    '''
    global currentPlayer
    global clearedRooms
    clearedRooms = []

    print("Instructions for the game: All you have to do is type any of the choices displayed to you. You'll see options formatted "
          "like |aChoice|bChoice|cChoice| and all you need to do is type the first letter (emphasized with []) of the one you want to choose and that's it.\n")

    # Let player select a class
    print("Now, Choose a class for your adventure!\n\n"
          "Attributes to consider:\n"
        '''
        Power: both combat strength and physical ability.
        Intelligence: amount of pre-existing knowledge and ability to learn new things.
        Persuasion: ability to convince and sway others.
        Wisdom: decision-making skills and ability to predict outcomes of certain actions.
        Durability: how much health you have.''')
    
    print("\n- Captain       - Geriatric       - Security"
   "\n  - Pow 6         - Pow 3           - Pow 8 "
   "\n  - Int 8         - Int 7           - Int 4"
   "\n  - Per 5         - Per 7           - Per 2"
   "\n  - Wis 4         - Wis 10          - Wis 6"
   "\n  - Dur 13        - Dur 8           - Dur 18\n")
    chosenProfession = getChoice({"Captain" : "Captain", "Geriatric" : "Geriatric", "Security" : "Security"}, "Which class do you choose?")
    currentPlayer = Player(chosenProfession)
    print(f'\nClass chosen: {currentPlayer.profession}!\n')

    currentRoom = "Entrance"

    while (currentPlayer.ended == False):
        currentRoom = changeRoom(currentRoom)
        if (currentRoom == "Quit"):
            currentPlayer.ended = True

    return

if __name__ == '__main__':
    runGame()
