import random

def enterCasino(money, inventory, rooms, actionsComplete):
    '''
    Purpose: Only allow entry to casino if allowed
    Parameter(s): current money
    Return Value: location string
    '''
    
    #Secret ending if you have both parts of golden ticket
    if "Left Ticket" and "Right Ticket" in inventory and "leverFlipped" in actionsComplete:
        rooms["Casino"]["choices"]["Use golden ticket"] = lambda: ending3()
    if(money[0] >= 100000):
        return "Casino"
    else:
        
        print("Cant enter Casino until you have $100,000")
        return None
    
def garbage(actionsComplete: list, money):
    '''
    Purpose: Look through garbage can if possible
    Parameter(s): actionComplete list
    Return Value: none

    '''
    if "garbage" in actionsComplete:
        print("Already looked through garbage can, nothing here")
    else:
        actionsComplete.insert(0, "garbage")
        money[0] += 5
        print("You find a crispy $5 bill")
        
        
def luckyCoin(inventory, money):
    '''
    Purpose: Deal with the purchasing of lucky coin  
    Parameter(s): player inventory list,current money
    Return Value: none
    '''
    if money[0] >= 5000 and "Lucky Coin" not in inventory:
        print("You now have a lucky coin(+1 to dice rolls)")
        inventory.insert(0, "Lucky Coin")
        money[0] -= 5000
    elif "Lucky Coin" in inventory:
        print("Already have lucky coin")
    else:
        print("Not enough money sorry")
    
        
def leftTicket(inventory, money):
    '''
    Purpose: Deal with the purchasing of left part of golden ticket
    Parameter(s): player inventory list,current money
    Return Value: none
    '''
    if money[0] >= 10000 and "Left Ticket" not in inventory:
        print("You now have the left part of the golden ticket")
        inventory.insert(0, "Left Ticket")
        money[0] -= 10000
    elif "Left Ticket" in inventory:
        print("Already have left ticket")
    else:
        print("Not enough money sorry")
def flashlight(inventory, money, rooms, actionsComplete):
    '''
    Purpose: Deal with the purchasing of flashlight 
    Parameter(s): player inventory list,current money, rooms dictionary, and actionsComplete list
    Return Value: none
    '''
    if money[0] >= 500 and "Flashlight" not in inventory:
        print("You now have the Flashlight")
        inventory.insert(0, "Flashlight")
        #Adds the ability to now see in Deep forest
        rooms["Deep Forest"]["choices"]["Flip golden lever"] = lambda: goldenLever(actionsComplete)
        money[0] -= 500
    elif "Flashlight" in inventory:
        print("Already have Flashlight")
    else:
        print("Not enough money sorry")
 

def grabDollar(money):
    '''
    Purpose: Allows the user to grab the dollar by the rocks in case they ever run out of money
    Parameter(s): current money
    Return Value: none
    '''
    print("You grab a dollar(Thing must be rough)")
    money[0] += 1
    
def guessingGame(inventory):
    '''
    Purpose: Guessing game used to obtain the right side of golden ticket 
    Parameter(s): inventory 
    Return Value: none
    '''
    if "Right Ticket" in inventory:
        print("Richard: I already gave you my ticket")
        return
    print("Richard: Howdy there fellow, I'm Richard")
    userInput = input("Richard: Wanna play a game to get this right part of a golden ticket I got(Y/N): ")
    if userInput == "y" or userInput == "Y":
        print("I am thinking of a number between 0 and 1000")
        print("I'll tell you each round if you are higher or lower than my current value")
        print("Input -1 to leave")
        randomNumber = random.randint(1, 999)
        while(True):
            while(True):
                try:
                   userInput = int(input("Whats your number: "))
                   break
                except ValueError:
                    print("Invalid input try again please")
            if(userInput == -1):
                break
            if(userInput <= 0 or userInput >= 1000):
                print("Richard: Not a valid guess try again")
                continue
            if(userInput == randomNumber):
                print("Richard: Wow, you got it")
                print("Richard: I am a man of my word, so here you go")
                inventory.insert(0, "Right Ticket")
                break
            if(userInput < randomNumber):
                print("Richard: Too low")
            elif(userInput > randomNumber):
                print("Richard: Too high")
    print("Richard: See you around")
    return

def goldenLever(actionsComplete):
    '''
    Purpose: Allow user to flip the lever and prompt if already complete  
    Parameter(s): actionsComplete list 
    Return Value: none
    '''
    if "leverFlipped" in actionsComplete:
        print("You already flipped the lever")
    else:
        print("You hear mechanical noises coming from the casino")
        actionsComplete.insert(0, "leverFlipped")
def diceGame(money, inventory):
    '''
    Purpose: Allow the user to play the dice game to make money
    Parameter(s): current money, and player inventory
    Return Value: none
    '''
    print("WELCOME TO LUCKY LANE GAMES")
    print("In this game you roll two dice and can win or lose money depending on the roll")
    print("Rules: # = any number")
    print("1, 1 = lose all of bet")
    print("1, # = lose 50% of bet")
    print("2, 2 = 2x bet")
    print("2, # = lose 25% of bet")
    print("3, # = break even")
    print("4, 4 = 4x bet")
    print("4, # = make 25% bet")
    print("5, 5 = win 1000$")
    print("5, # = 50% bet")
    print("6, 6 = 10x bet")
    print("6, # = 2x bet")
    print("Input -1 in bet amount to leave")
    while(True):
        print(f"Current Money: ${money[0]}")
        while(True):
            try:
                userInput = int(input("Whats your number: "))
                break
            except ValueError:
                print("Invalid input try again please")
        if(userInput == -1):
            print("Fairwell!!!!")
            break
        if(userInput > money[0]):
            print("You don't have that much money")
        elif(userInput == 0):
            print("You can't bet 0")
        elif(userInput <= -2):
            print("You can't bet this much")
        else:
            diceRoll_1 = random.randint(1, 6)
            diceRoll_2 = random.randint(1, 6)
            winAmount = 0
            if "Lucky Coin" in inventory:
                diceRoll_1 += 1
                diceRoll_1 = 6 if diceRoll_1 > 6 else diceRoll_1
                diceRoll_2 += 1
                diceRoll_2 = 6 if diceRoll_2 > 6 else diceRoll_2
            if(diceRoll_1 == 1 and diceRoll_2 == 1):
                winAmount = userInput * -1
            elif(diceRoll_1 == 1):
                winAmount = userInput * -.5
            elif(diceRoll_1 == 2 and diceRoll_2 == 2):
                winAmount = userInput * 2
            elif(diceRoll_1 == 2):
                winAmount = userInput * -.25
            elif(diceRoll_1 == 3):
                winAmount = 0
            elif(diceRoll_1 == 4 and diceRoll_2 == 4):
                winAmount = userInput * 4
            elif(diceRoll_1 == 4):
                winAmount = userInput * .25           
            elif(diceRoll_1 == 5 and diceRoll_2 == 5):
                winAmount = 1000
            elif(diceRoll_1 == 5):
                winAmount = userInput * .5
            elif(diceRoll_1 == 6 and diceRoll_2 == 6):
                winAmount = userInput * 10
            elif(diceRoll_1 == 6):
                winAmount = userInput * 2
            print(f"Roll was: \nDice-1 = {diceRoll_1}\nDice-2 = {diceRoll_2}")
            winAmount = int(winAmount)
            if winAmount <= 0:
                print(f"You lost ${winAmount}")
            else:
                print(f"You won ${winAmount}")
            
            money[0] += winAmount
            money[0] = 0 if money[0] < 0 else money[0]
def ending1():
    print("Stuck in the cycle you continue to gamble at the same casino")
    print("In the end you lose everything again and again")
    print("Ending 1 - Bad Ending")
    quit()
def ending2():
    print("Finally deciding to quit the cycle you leave the")
    print("Casino with your $100,000")
    print("Ending 2 - Good Ending")
    quit()
def ending3():
    print("Walking into the golden door you see a slot to put in the golden ticket pieces")
    print("Out of a golden enjeweled machine spits out thousands of dollars")
    print("You now have $1,000,000")
    print("Ending 3 - Golden Ticket Secret Ending")
    quit()
        
if __name__ == '__main__':
    #A list for telling which actions have been done before to prevent repeats
    actionsComplete = []
    #A list of all players inventory items
    inventory = []
    #In a list to allow for pass by reference
    money = [0]

    currLocation = "Alley"
    
    rooms = {
        "Alley": {
            "description": "A dark and gloomy allyway outside of the casino",
            "choices": {
                "Enter casino": lambda: enterCasino(money, inventory, rooms, actionsComplete),
                "Enter street": "Street",
                "Look in garbage bin": lambda: garbage(actionsComplete, money)
            }
        },
        "Casino": {
            "description": "A rich and luxurious palace filled with slot machines and tables, a gold door is in the corner",
            "choices": {
                "Gamble it all away": lambda: ending1(),
                "Leave for good": lambda: ending2()
                }
        },
        "Store": {
            "description": "A good old standard general store, with some usefull trinkets\nLucky Coin($5000)\nLeft part of a Golden Ticket($10000)\nFlashlight($500)",
            "choices": {
                "Buy Lucky Coin": lambda: luckyCoin(inventory, money),
                "Buy Left Golden Ticket": lambda: leftTicket(inventory, money),
                "Buy Flashlight": lambda: flashlight(inventory, money, rooms, actionsComplete),
                "Leave": "Street"
            }
        },
        "Street": {
            "description": "A long stretch of street down central part of town",
            "choices": {
                "Enter store": "Store",
                "Enter forest": "Forest",
                "Enter lucky lane": "Lucky Lane",
                "Enter bar": "Bar",
                "Enter alley": "Alley"
            }
        },
        "Lucky Lane": {
            "description": "A rival casino that is running out of buisness, but still has some games running",
            "choices": {
                "Play dice game": lambda: diceGame(money, inventory),
                "Leave": "Street"
            }
        },
        "Forest": {
            "description": "The trees cover the moonlight on this winding path, there is some weird rocks by the path",
            "choices": {
                "Investigate rocks": "Suspicous Rocks",
                "Enter dark path": "Dark Path",
                "Enter street": "Street"
            }
        },
        "Suspicous Rocks": {
            "description": "There seems to be some $1 dollar bills stuck under some rocks",
            "choices": {
                "Grab $1": lambda: grabDollar(money),
                "Leave": "Forest"
            }
        },
        "Bar": {
            "description": "There is a musk of alcholol in the air, and people sitting around drinking",
            "choices": {
                "Talk to man at counter": lambda: guessingGame(inventory),
                "Leave": "Street",
           }
        },
        "Deep Forest": {
            "description": "You can barley see a few feet infront of you, try getting some light",
            "choices": {
                "Leave": "Dark Path"
            }
        },
        "Dark Path": {
            "description": "Even shadows look bright here",
            "choices": {
                "Turn back": "Forest",
                "Keep going": "Deep Forest"
            }
        }
    }
    
    print("------------------------")
    print("You Have Lost Everything")
    print("  Time to WIN it back")
    print("------------------------")
    print("You have been thrown out of casino late at night \nfor gambling everything that you have.")
    print("Now you must try to win back all the money you lost.\n")
    print("======GOAL======")
    print("  Make $100,000\n")
    input("Press anything to continue:")
    print("\n\n")
    
    
    while(True):
        print(currLocation)
        print("-------------------------")
        print(rooms[currLocation]["description"])
        print(f"CURRENT MONEY: ${money[0]}")
        print(f"Inventory: {inventory}")
        print("-------------------------")
        for choice in rooms[currLocation]["choices"]:
            print(" - " + choice)
        while(True):
            userInput = input("Input a command: ")
            if userInput in rooms[currLocation]["choices"]:
                if type(rooms[currLocation]["choices"][userInput]) is str:
                    #swaps location only if it is a string option
                    currLocation = rooms[currLocation]["choices"][userInput]
                    break
                else:
                    #Runs function associated with command
                    print("=====================")
                    temp =rooms[currLocation]["choices"][userInput]()
                    if temp is not None:
                        currLocation = temp
                    print("=====================")
                    break

            else:
                print("That is not an option try again")
