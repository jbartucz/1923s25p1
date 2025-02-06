
import random


classes_list = ["Saber", "Archer", "Lancer", "Caster", "Assassin"]
enemies_list = ["slime", "goblin", "skeleton", "troll", "orc"]

classes_d = {
    "Saber": {
        "HP": 130,  
        "ATK": 15,
        "SPEED": 1,
        "LUK":30        
    },
    
    "Archer": {
        "HP": 90,
        "ATK": 10,
        "SPEED": 2,
        "LUK":20
        
    },
    
    "Lancer": {
        "HP": 95,
        "ATK": 12,
        "SPEED": 2,
        "LUK":0
    },
    
    "Caster": {
        "HP": 70,
        "ATK": 30,
        "SPEED": 1,
        "LUK":35
    },
    
    "Assassin": {
        "HP": 100,
        "ATK": 20,
        "SPEED": 1,
        "LUK":60  
    },
    
}

enemies_d = {
    "slime": {
        "HP": 5,
        "ATK": 0,
        "money": 1,
    },
    
    "goblin": {
        "HP": 20,
        "ATK": 2,
        "money": 12,
    },
    
    "skeleton": {
        "HP": 25,
        "ATK": 5,
        "money": 3,
    },
    
    "troll": {
        "HP": 45,
        "ATK": 6,
        "money": 12,
    },
    
    "orc": {
        "HP": 60,
        "ATK": 12,
        "money": 100,
    },
    
    
}


rooms = {
    # roomXY, X is what floor. Y is room number
    "room01": {
        "in_room": "You step into the cave, and now the only light available comes from the entrance, allowing you to confirm that no creatures are near the entrance.",
        "in_room2":"However, you have a torch with you. As you light it, the cave is illuminated, revealing a fork in the path ahead.",
        "in_room3":"Three passageways lead in different directions. It seems that now is the time to make a choice.",
        "have_fight": 0,
        "option1": "1. Go right",
        "option2": "2. Go middle",
        "option3": "3. Go left",
        "go1": "room13",
        "go2": "room12",
        "go3": "room11",       
    },
    
    "room11": {
        "in_room": "You can only see the front. Although the cave is not spacious, this also means you won’t encounter any gigantic monsters.",
        "have_fight": 2,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room21",
        "go2": None,
        "go3": None,       
    },
    
    "room12": {
        "in_room": "You can only see the front. Although the cave is not spacious, this also means you won’t encounter any gigantic monsters.",
        "have_fight": 1,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room22",
        "go2": None,
        "go3": None,       
    },
    
    "room13": {
        "in_room": "The path ahead is very spacious, large enough for an elephant to pass through. This also means that a gigantic monster may be dwelling further inside.",
        "have_fight": 1,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room23",
        "go2": None,
        "go3": None,       
    },
    
    "room21": {
        "in_room": "You can only see the front. Although the cave is not spacious, this also means you won’t encounter any gigantic monsters.",
        "have_fight": 0,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room31",
        "go2": None,
        "go3": None,       
    },
    
    "room22": {
        "in_room": "You can only see the front. Although the cave is not spacious, this also means you won’t encounter any gigantic monsters.",
        "have_fight": 2,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room31",
        "go2": None,
        "go3": None,       
    },
    
    "room23": {
        "in_room": "The path ahead is very spacious, large enough for an elephant to pass through. This also means that a gigantic monster may be dwelling further inside.",
        "have_fight": 2,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room32",
        "go2": None,
        "go3": None,       
    },
    
    "room31": {
        "in_room": "The path ahead is very spacious, large enough for an elephant to pass through. This also means that a gigantic monster may be dwelling further inside.",
        "have_fight": 3,
        "option1": "1. Go right",
        "option2": "2. Go middle",
        "option3": "3. Go left",
        "go1": "room41",
        "go2": "room42",
        "go3": "room43",       
    },
    
    "room32": {
        "in_room": "The path ahead is very spacious, large enough for an elephant to pass through. This also means that a gigantic monster may be dwelling further inside.",
        "have_fight": 1,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room43",
        "go2": None,
        "go3": None,       
    },
    
    "room41": {
        "in_room": "You can only see the front. Although the cave is not spacious, this also means you won’t encounter any gigantic monsters.",
        "have_fight": 0,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room51",
        "go2": None,
        "go3": None,       
    },
    
    "room42": {
        "in_room": "The path ahead is very spacious, large enough for an elephant to pass through. This also means that a gigantic monster may be dwelling further inside.",
        "have_fight": 3,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room52",
        "go2": None,
        "go3": None,       
    },
    
    "room43": {
        "in_room": "The path ahead is very spacious, large enough for an elephant to pass through. This also means that a gigantic monster may be dwelling further inside.",
        "have_fight": 0,
        "option1": "1. moving forward",
        "option2": "",
        "option3": "",
        "go1": "room52",
        "go2": None,
        "go3": None,       
    },
    
    "room51": {
        "in_room": "You see a huge creature ahead of you, and you're ready to destroy it.",
        "have_fight": 5,
        "option1": "1. Go home",
        "option2": "2. Go home",
        "option3": "3. Go home",
        "go1": "room53",
        "go2": "room53",
        "go3": "room53",       
    },
    
    "room52": {
        "in_room": "You see a huge creature ahead of you, and you're ready to destroy it.",
        "have_fight": 5,
        "option1": "1. Go home",
        "option2": "2. Go home",
        "option3": "3. Go home",
        "go1": "room53",
        "go2": "room53",
        "go3": "room53",       
    },
    
    "room53": {
        "in_room": "Go Home bye bye",
        "have_fight": 5,
        "option1": "bye",
        "option2": "bye",
        "option3": "bye",
        "go1": "room53",
        "go2": "room53",
        "go3": "room53",       
    },
}

def game_opening():
    '''
    Purpose: Allow the user to choose a class and introduce the beginning of the story
    Parameter(s): 
    Return Value: user_input_class (int)
    '''
    
    print("\nHello, player! Please choose your class.\n")
    print("You will have the following options:")
    
    num_show = 1
    
    for show_classes in classes_list:
        print(f"{num_show}. {show_classes}: HP:{classes_d[show_classes]['HP']} ATK:{classes_d[show_classes]['ATK']} ", end = "")
        print(f"SEPPD:{classes_d[show_classes]['SPEED']} LUK:{classes_d[show_classes]['LUK']}")
        num_show += 1
    
    
    while True:
        try:
            user_input_class = int(input("\nPlease enter a number from 1 to 5 to select your desired class: "))
            
        except ValueError:
            print("Sorry, pleace try again.")
            continue
        if user_input_class <= 0 or user_input_class >= 6:
            print("Sorry, your input number is too big or small. Pleace try again")
            continue
        else:
            break
    
    print("\n-------------story time-------------")
        
    print("\nYou are an adventurer. Today, you have accepted a quest: a mysterious green creature has appeared in a village.")
    
    print("Please head to the village, investigate the situation, and eliminate the unknown creature.")
        
    return user_input_class - 1

def print_room_inf(current_room):
    '''
    Purpose: print the room information
    Parameter(s): current_room (room name for example: room41)
    Return Value: 0
    '''
    
    print(rooms[current_room]['in_room'])
    
    if rooms[current_room].get('in_room2') != None:
        print(rooms[current_room]['in_room2'])
    
    if rooms[current_room].get('in_room3') != None:
        print(rooms[current_room]['in_room3'])
        
    return 0



def now_fight(current_room, player_class):
    '''
    Purpose: now is fight time. randomly pick an enemy and let the enemy fight will use. Note :LUK
    Parameter(s): current_room (room name for example: room41)
    Return Value: 0
    '''
    now_enemy = {
        "name": "emply",
        "HP": 5,
        "ATK": 0,
        "money": 0,
    }
    
    enemy_name = enemies_list[random.randint(0, rooms[current_room]['have_fight'])]
    
    if current_room == "room51" or current_room == "room52":
        enemy_name = enemies_list[4]
    
    now_enemy["name"] = enemy_name
    now_enemy["HP"] = enemies_d[enemy_name]["HP"]
    now_enemy["ATK"] = enemies_d[enemy_name]["ATK"]
    now_enemy["money"] = enemies_d[enemy_name]["money"]
    
    print(f"\nYou see {now_enemy['name']} in front. It seems that in order to move on, you have no choice but to fight.")
    
    user_type = ""
    
    while now_enemy["HP"] > 0 or user_type != "3":
        
        print("You now have three options: 1. Light attack 2. Heavy attack 3. Escape")
        print(f"You now have {player_class['HP']} HP.")

        while user_type not in ["1", "2", "3"]:
            user_type = str(input("Please type your choice (1, 2, or 3): "))

            if user_type not in ["1", "2", "3"]:
                print("Your input is not vaild, pleace try again.\n")
                
        if user_type == "3":
            print(f"You choose not to fight the {now_enemy['name']}. You ran away.")
            break
                
        now_LUK = random.randint(0, player_class["LUK"] + 75)
        
        you_DMG = 0          
        
        if user_type == "1" and now_LUK >= 50:
            you_DMG = player_class["SPEED"] * random.randint(8, player_class["ATK"] * 2)
            print("critical hit!!")
            
        elif user_type == "2" and now_LUK >= 50:
            you_DMG = random.randint(8, player_class["ATK"] * 3)
            print("critical hit!!")

        elif user_type == "1":
            you_DMG = player_class["SPEED"] * random.randint(1, player_class["ATK"])

        elif user_type == "2":
            you_DMG = random.randint(1, player_class["ATK"] * 2)
    
        now_enemy["HP"] -= you_DMG
        print(f"\nYour attack caused {you_DMG} damage")        
        
        # for the died part: make sure you not print other word if the HP is lower than 0
        if now_enemy["HP"] < 1:
            print(f"\nWIN!! {now_enemy['name']} is died")
            print(f"You get {now_enemy['money']} gold coins from {now_enemy['name']} ")
            player_class["money"] += now_enemy["money"]
            break
        
        player_class["HP"] -=  now_enemy["ATK"]
        if player_class["HP"] < 1:
            break
        print(f"{now_enemy['name']}'s attack caused {now_enemy['ATK']} damage to you. You have {player_class['HP']} HP left")
        
        user_type = "0"
        
    print("\nfight end")
            
    return 0



def game_start(player_class):
    '''
    Purpose: Game start!! let user can move, fight and rest
    Parameter(s): player_class(Dictionary) HP ATK SPEED LUK money
    Return Value: Return "success" or "fail" to confirm whether the adventure was successful.
    '''
    
    print("\nYou arrive at the village and search the surrounding area, eventually discovering a suspicious cave.")
    print("The massive footprints at the cave entrance indicate that a creature larger than a human lives inside.")
    print("However, this does not deter you. Instead, you bravely step into the cave.\n")
    
    s_or_f = "success"
    
    current_room = "room01" #start room
    
    count_rest = 3
    
    while current_room != "room53":
        
        print_room_inf(current_room)
        
        Enter_some = input("Press any key to see if there is an enemy in the front:  ")
        if rooms[current_room]['have_fight'] != 0:
            # print("yes fight!!!!!!!!!!")
            
            now_fight(current_room, player_class)
        else:
            print("No enemy in the front")
        
        # break the while loop adn return fail
        if player_class['HP'] < 1: # died stop while loop
            s_or_f = "fail"
            break
        
        print(f"You now have {player_class['HP']} HP.")
        print("Next, you can...")
        print(f"{rooms[current_room]['option1']}")
        
        if rooms[current_room]["go2"] != None:
            print(f"{rooms[current_room]['option2']}")
        if rooms[current_room]["go3"] != None:
            print(f"{rooms[current_room]['option3']}")
        if count_rest > 0:
            print(f"4. Rest and you can take {count_rest} more breaks")
        
        user_type = "0"
        
        while user_type not in ["1", "2", "3", "4"]:
            user_type = str(input("Please type your choice (1, 2, ,3 ,or 4): "))

            if user_type not in ["1", "2", "3", "4"]:
                print("Your input is not vaild, pleace try again.\n")
            elif rooms[current_room]["go2"] == None and user_type == "2":
                print("Your input is not vaild, pleace try again.\n")
                user_type = "error"
            elif rooms[current_room]["go3"] == None and user_type == "3":       
                print("Your input is not vaild, pleace try again.\n")
                user_type = "error"
            elif user_type == "4" and count_rest > 0:
                print("You decided to take a break")
                HP_add = random.randint(20, 30)
                if player_class["HP"] < 50:
                    HP_add += 30
                player_class["HP"] += HP_add
                print(f"You feel your body filled with strength, and your health has been restored by {HP_add}")
                print(f"You now have {player_class['HP']} HP.")
                count_rest -= 1
                print(f"You can take {count_rest} more breaks")
                
                user_type = "error"
            elif user_type == "4" and count_rest == 0:
                print("Your input is not vaild, pleace try again.\n")
                user_type = "error"
        
        if user_type == "1":
            current_room = rooms[current_room]["go1"]
            
            # print(current_room)
        elif user_type == "2":
            current_room = rooms[current_room]["go2"]
            
            # print(current_room)
        elif user_type == "3":
            current_room = rooms[current_room]["go3"]
            
            # print(current_room)
    
    
    return str(s_or_f)

    
#-------------------------------------main-------------------------------------

if __name__ == '__main__':

    player_class_num = game_opening() #will return a int to let me know what class that user choose
    player_class_str = classes_list[player_class_num] # classes_list[0 to 4] 
    player_class = {
        player_class_str: player_class_str,
        "HP": classes_d[player_class_str]["HP"],
        "ATK": classes_d[player_class_str]["ATK"],
        "SPEED": classes_d[player_class_str]["SPEED"],
        "LUK":classes_d[player_class_str]["LUK"],
        "money":0,
           
    }
    
    
    the_end = ""
    the_end = game_start(player_class)
    
    # print(f"\n{the_end}")

    print(f"You got ${player_class['money']} from the monster")
    
    print("End")

    if player_class["money"] > 100 and the_end == "success":
        print("You flawlessly completed the mission, earning the gratitude of the villagers and a generous reward in return.")
        print("However, your next adventure is already waiting for you.")
    elif the_end == "success":
        print("You completed the quest, but later that day, villagers reported some monsters still lurking in the area.")
        print("Your mission was deemed a failure, and you were even required to pay compensation.")
    elif the_end == "fail":
        print("\nYou failed. Although you considered yourself a lucky person, it seems that the goddess of fortune has turned her gaze away from you today.")
        print("As you miserably fled back home, you discovered that you had taken an arrow to the knee. Because of this, you retired from the adventurer's life.")
        

