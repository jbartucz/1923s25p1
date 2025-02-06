import random

# function for rolling the dice
def roll_die():
    # force using cursed die first
    if(you["Cursed Dices"] > 0):
        print("You have used Cursed Die!")
        you["Cursed Dices"] = you["Cursed Dices"] - 1
        return cursed_die()
    # choice if player wants to use upgraded die
    elif(you["Upgraded Dices"] > 0):
        print(f"You have upgraded dices in your inventory: ({you['Upgraded Dices']} Available)")
        ans_upg_die = ""
        while True:
            ans_upg_die = input(f"Do you want to use it? (y/n)")
            if ans_upg_die == "y":
                you["Upgraded Dices"] = you["Upgraded Dices"] - 1
                return upgraded_die()
            elif ans_upg_die == "n":
                break
    return random.randint(1,6)

def upgraded_die():
    return random.randint(1,10)

def cursed_die():
    return random.randint(1,4)

# for enemy attack
def enemy_die():
    return random.randint(1,3)

# show inventory function
def check():
    print(f"HP: {you['HP']}")
    print(f"Upgraded Dices: {you['Upgraded Dices']}")
    print(f"Cursed Dices: {you['Cursed Dices']}")
    print(f"Food: {you['Food']}")

def search():
    # Helping valuable for search function
    searching = random.randint(1, 15)
    if (searching == 4 or searching ==  14 or searching == 13):
        you["Cursed Dices"] = you["Cursed Dices"] + 1
        print("Oh no!! you found cursed die!")

    elif (searching % 3 == 0):
        you["Upgraded Dices"] = you["Upgraded Dices"] + 1
        print("Yippee!! You just receive upgraded die")

    elif (searching == 1 or searching == 7 or searching == 10):
        you["HP"] = you["HP"] + 1
        print("Let's gooo!! your HP has increased by 1!!")
    else:
        monster = random.choice(enemy)
        print(f"You found a {monster}! Fight them!")
        monster_fight(monster)

# fighting with monster
def monster_fight(monster):
    # make your attack point, also enemy
    your_attack = roll_die()
    enemy_attack = enemy_die()
    print(f"Your attack: {your_attack}")
    print(f"Enemy attack: {enemy_attack}")
    # win
    if (your_attack > enemy_attack):
        you["HP"] = you["HP"] + 1
        print(f"Yes! you defeat the {monster}! (HP +1)")
    # lose
    elif (your_attack < enemy_attack):
        you["Cursed Dices"] = you["Cursed Dices"] + 1
        you["HP"] = you["HP"] - 1
        print(f"{monster} cursed you! (HP: -1 & 1 Cursed die received!)")
    # tie
    else:
        print("You still have a luck! Nothing happened!")
    

# Boss fight
def boss_fight():
    # your attack
    your_attack = roll_die()
    
    print(f"Your attack is {your_attack}")
    # boss attack
    boss_attack = random.randint(1,5)
    print(f"Boss damage: {boss_attack}")

    # lose
    if(boss_attack > your_attack):
        you["HP"] = you["HP"] - 2
        print(f"Boss attack! Your current HP: {you['HP']}")

    # win
    elif(your_attack > boss_attack):
        print("Victory!! You have won the boss fight and clear the game!")

    # tie
    else:
        print("You blocked the boss's damage!!")
        print("Nothing happened!")

# buying food function
def buy_food():
    if you["Upgraded Dices"] <= 0:
        print("Sorry, you do not have enough upgraded die to buy the food")
    else:
        print("You paid for the food with 1 upgraded die!")
        you["Food"] = you["Food"] + 1
        you["Upgraded Dices"] = you["Upgraded Dices"] - 1

# eat function
def eat():
    if you["Food"] <= 0:
        print("You do not have food")
    else:
        print("You have consumed the food!")
        you["Food"] = you["Food"] - 1
        you["HP"] = you["HP"] + 1

# talk to the spirit function
def talk():
    print("Spirit will bless you everytime you talk to them!")
    print("The Item you get is depending on the spirits")
    spirit_bless()

# spirits = ["Ginny","Santa","White Lady","Org","Fire Spirits", "Golem", "Unicorn"]
# make a spirit bless
def spirit_bless():
    spirit = random.choice(spirits)
    print(f"Random your spirit: {spirit}")
    if spirit == "Ginny":
        print(f"{spirit} gave you 1 upgraded die, 1 HP, and 1 Food!")
        you["Food"] = you["Food"] + 1
        you["HP"] = you["HP"] + 1
        you["Upgraded Dices"] = you["Upgraded Dices"] + 1
    elif spirit == "Santa":
        print(f"{spirit} gave you 3 upgraded die and 2 Food!")
        you["Food"] = you["Food"] + 2
        you["Upgraded Dices"] = you["Upgraded Dices"] + 3
    elif spirit == "White Lady":
        print(f"{spirit} attacks you!! (Minus 1 HP and receive 1 cursed die)")
        you["HP"] = you["HP"] - 1
        you["Cursed Dices"] = you["Cursed Dices"] + 1
    elif spirit == "Org":
        print(f"Ouchh!!' {spirit} hit you with a log! (Minus 2 HP)")
        you["HP"] = you["HP"] - 2
    elif spirit == "Fire Spirits":
        amount = random.randint(1, 3)
        luck = random.choice(["Food", "Upgraded Dices", "HP"])
        print(f"{spirit} gave you {luck}:{amount}")
        you[luck] = you[luck] + amount
    elif spirit == "Golem":
        print(f"{spirit} blocked you! You have to pay 1 Food and 1 Cursed die to the {spirit}")
        if (you["Food"] <= 0 or you["Cursed Dices"] <= 0):
            print("Luckily, you do not have enough food or cursed die...")
            print("Spirit go away~~")
        else:
            print("You paid 1 Food and 1 Cursed die")
            you["Food"] = you["Food"] - 1
            you["Cursed Dices"] = you["Cursed Dices"] - 1
    elif spirit == "Unicorn":
        print("Lucky! Unicorn gave you super bless!")
        print("You receive everything 1 each!")
        you["Food"] = you["Food"] + 1
        you["HP"] = you["HP"] + 1
        you["Upgraded Dices"] = you["Upgraded Dices"] + 1
        you["Cursed Dices"] = you["Cursed Dices"] + 1

# pray function
def pray():
    print("*Praying for the forest spirit*")
    print("Give your offering to receive your new item...")
    # make a loop for praying
    while True:
        print("\n1) Offer Upgraded die")
        print("2) Offer Cursed die")
        print("3) Offer HP")
        print("4) Offer Food")
        print("5) Exit")
        offering = input("What do you want to offer? ")
        # condition on each pray
        if offering == "1":
            if you["Upgraded Dices"] <= 0:
                print("You do not have enough Upgraded Die")
            else:
                you["Upgraded Dices"] = you["Upgraded Dices"] - 1
                amount = random.randint(0, 5)
                luck = random.choice(["Food", "Upgraded Dices", "HP"])
                print(f"Nice charm! God gave you {luck}:{amount}")
                you[luck] = you[luck] + amount
        elif offering == "2":
            if you["Cursed Dices"] <= 0:
                print("You do not have enough Cursed Die")
            else:
                you["Cursed Dices"] = you["Cursed Dices"] - 1
                amount = random.randint(1, 5)
                luck = random.choice(["Food", "Upgraded Dices", "HP"])
                print(f"God is angry!! He took your {luck}:{amount}")
                you[luck] = you[luck] - amount
        elif offering == "3":
            amount = random.randint(0, 10)
            luck = random.choice(["Food", "Upgraded Dices", "HP"])
            print(f"God is proud of you! He gave you {luck}:{amount}")
            you[luck] = you[luck] + amount
        elif offering == "4":
            if you["Food"] <= 0:
                print("You do not have enough food")
            else:
                amount = random.randint(0, 2)
                luck = random.choice(["Food", "Upgraded Dices", "HP"])
                print(f"God like your food! He gave you {luck}:{amount}")
                you[luck] = you[luck] + amount
        elif offering == "5":
            print(f"Thank you for visiting!")
            return
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

def kick():
    print("*You kicked the final boss*")
    print("*But you got injured* (HP: -1)")
    you["HP"] = you["HP"] - 1

def instruction():
    print("\n**********************************************************GAME INSTRUCTION**********************************************************")
    print("- Lobby is the only place you can keep food and eat it anytime you want! (Gain 1 Food by trading 1 Upgraded die & Gain 1 HP/Food)")
    print("- You can check your status by typing 'check'")
    print("- There is an upgraded die and cursed die! Be careful while using!")
    print("- You can leave the game anytime by typing 'exit")
    print("- Type 'command' to see what you can do!")
    print("- Type 'help' to see game instruction!")
    print("**********************************************************GAME INSTRUCTION**********************************************************\n")

def play_game():
    print("Welcome to The treasure adventure!")
    print("This game based on your luck! Roll the dice to see your luck!")
    print("You can choose to keep going without finding or searching anything! But you will still have to fight the boss")
    print("\n**********************************************************GAME INSTRUCTION**********************************************************")
    print("- Lobby is the only place you can keep food and eat it anytime you want! (Gain 1 Food by trading 1 Upgraded die & Gain 1 HP/Food)")
    print("- You can check your status by typing 'check'")
    print("- There is an upgraded die and cursed die! Be careful while using!")
    print("- You can leave the game anytime by typing 'exit")
    print("- Type 'command' to see what you can do!")
    print("- Type 'help' to see game instruction!")
    print("**********************************************************GAME INSTRUCTION**********************************************************\n")
    current_room = "Lobby"
    # Make loop to play game
    while True:
        room = rooms[current_room]
        print(f"\n{room['description']}")
        print("Available actions:")
        for action in room["choices"]:
            print(f"- {action}")
        # Make loop to get an action
        while True:
            # if losing all hp
            if you["HP"] <= 0:
                print("You have been defeated! Game Over!")
                return
            action = input("What do you do? ").lower()
            if action == "exit":
                print("Thank you for playing the game! Goodbye!")
                return
            elif action == "command":
                # make a space for the explanation
                print("")
                print("Available actions:")
                for action in room["choices"]:
                    print(f"- {action}")
            elif action in room["choices"]:
                # check if the key value is a function or not?
                if callable(room["choices"][action]):
                    room["choices"][action]()
                # if not change room
                else:
                    current_room = room["choices"][action]
                    break

            else:
                print("Invalid choice. Try again.")
        
        

# character
spirits = ["Ginny","Santa","White Lady","Org","Fire Spirits", "Golem", "Unicorn"]
# enemy
enemy = ["Fire Chicken", "Water Lizard", "Earth Buffalo", "Air cat", "Metal dog"]

# you dictionary for your stat
you = {
    "HP": 5,
    "Upgraded Dices": 0,
    "Cursed Dices": 0,
    "Food": 0
}

# rooms dictionary for the game
rooms = {
   "Lobby": {
       "description": "*Lobby* This is the lobby for the adventure! This is the only place you can buy food!",
       "choices": {
           "enter": "Cave Entrance",
           "leave": "Mystery Forest",
           "check": check,
           "buy food": buy_food,
           "eat": eat,
           "help": instruction
       }
   },

   "Cave Entrance": {
       "description" : "*Cave Entrance* You have entered the Cave Entrance! The chamber spirit is waiting here! Talk to them to get bless!",
       "choices":{
           "leave": "Lobby",
           "enter": "Main Chamber",
           "check": check,
           "eat": eat,
           "talk": talk,
           "help": instruction
       }
   },

   "Mystery Forest": {
       "description": "*Mystery Forest* This is the place to prepare, Pray for the god and receive your luck! (Entrance fee: 1 random item in your inventory)",
       "choices": {
           "search": search,
           "go back": "Lobby",
           "check": check,
           "eat": eat,
           "pray": pray,
           "help": instruction
       }
   },

   "Main Chamber": {
       "description": "*Main Chamber* You are in the first route to the Treasure Chamber.",
       "choices": {
           "go left": "Crystal Crove",
           "go right": "Underground Forest",
           "retreat": "Cave Entrance",
           "check": check,
           "eat": eat,
           "help": instruction
       }
   },

   "Crystal Crove": {
       "description": "*Crystal Crove* Scooby Doo town?? Check it out!",
       "choices": {
           "search": search,
           "go right": "Underground Forest",
           "go straight": "Dragon Cave",
           "retreat": "Main Chamber",
           "check": check,
           "eat": eat,
           "help": instruction
       }
   },

   "Underground Forest": {
       "description": "*Underground Forest* Forest underground? There might be some food for you to prepare.",
       "choices": {
           "search": search,
           "go left": "Crystal Crove",
           "go straight": "Waterfall Underground",
           "check": check,
           "eat": eat,
           "help": instruction
       }
   },

   "Waterfall Underground": {
       "description": "*Waterfall Underground* Wow waterfall!! Take a rest before you continue",
       "choices": {
           "search": search,
           "go left": "Dragon Cave",
           "go straight": "Boss Gate",
           "check": check,
           "eat": eat,
           "help": instruction
       }
   },

   "Dragon Cave": {
       "description": "*Dragon Cave* Seems like a huge dragon is in a deep sleep. Be careful! and hurry up!",
       "choices": {
           "search": search,
           "go right": "Waterfall Underground",
           "go straight": "Boss Gate",
           "check": check,
           "eat": eat,
           "help": instruction
       }
   },

   "Boss Final Chamber": {
       "description": "*Boss Final Chamber!!!* This is the last boss fight! Go ahead fight the boss and win the game! you need to get more score than the boss!",
       "choices": {
           "fight": boss_fight,
           "flee": "Boss Gate",
           "check": check,
           "eat": eat,
           "kick": kick,
           "help": instruction
       }
   },

   "Boss Gate": {
       "description": "*Boss Gate* This is the last place before fight the boss, and there is portal back to the Main Chamber",
       "choices": {
           "search": search,
           "use portal": "Main Chamber",
           "continue": "Boss Final Chamber",
           "check": check,
           "eat": eat,
           "help": instruction
       }
   }
}

if __name__ == "__main__":
    play_game()