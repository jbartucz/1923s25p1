import random

def move(now_place, time_machine):
    '''
    Purpose: to move next world
    Parameter(s): now_place, time_machine
    Return Value: next_place
    '''
    print(f"move to {rooms[now_place]['choices'][time_machine]}")
    next_place = rooms[now_place]['choices'][time_machine]
    return next_place

def get_dice(now_place, dice):
    '''
    Purpose: to get a dice
    Parameter(s): now_place, dice
    Return Value: next_place
    '''
    if now_place == "Emerald World":
        key = 4
        if key in dice:
            print("You have already [4] dice")
        else:
            print("You got dice [4]")
            dice.append(4)
    elif now_place == "Falls World":
        key = 5
        if key in dice:
            print("You have already [5] dice")
        else:
            print("You got dice [5]")
            dice.append(5)
    elif now_place == "Smart World":
        key = 6
        if key in dice:
            print("You have already [6] dice")
        else:
            print("You got dice [6]")
            dice.append(6)
    else:
        print("There is no dice here")
    return now_place

def cow_demon(dice):
    '''
    Purpose: to beat Boss Cow_Demon
    Parameter(s): dice
    Return Value: get_ball
    '''
    print("You met a Boss Cow_Demon.")
    value = random.choice(dice)
    if value >= 2:
        get_ball = 1
        print("You won! You got a ball.")
    else:
        get_ball = 0
        print("You lose, You were sent to the Cold World")
    return get_ball

def mermaid(dice):
    '''
    Purpose: to beat Boss mermaid
    Parameter(s): dice
    Return Value: get_ball
    '''
    print("You met a Boss Mermaid.")
    value = random.choice(dice)
    if value >= 3:
        get_ball = 1
        print("You won! You got a ball.")
    else:
        get_ball = 0
        print("You lose, You were sent to the Cold World")
    return get_ball

def samurai(dice):
    '''
    Purpose: to beat Boss Samurai
    Parameter(s): dice
    Return Value: get_ball
    '''
    print("You met a Boss Samurai.")
    value = random.choice(dice)
    if value >= 3:
        get_ball = 1
        print("You won! You got a ball.")
    else:
        get_ball = 0
        print("You lose, You were sent to the Cold World")
    return get_ball

def final_boss(dice):
    '''
    Purpose: to beat final_boss
    Parameter(s): dice
    Return Value: none
    '''
    broken_leg = 0
    print("You can beat boss if you break two legs")
    while broken_leg < 2:
        value = random.choice(dice)
        if value >= 3:
            print("You broke one leg")
            broken_leg += 1
        else:
            print("You couldn't break a leg")
            broken_leg = 0
    print("Congulaguation! You got a diamond.")
    return None

    


rooms = {
   "Cold World": {
       "description": "Tom lives in this city. Here is really cold place. This is a starting point",
       "choices": {
           "red": "Emerald World",
           "blue": "Jazz World",
           "green": "Falls World" 
       }
   },

   "Jazz World": {
       "description": "This world is famous for delicious food and Jazz.",
       "choices": {
           "red": "Falls World",
           "blue": "Cold World",
           "green": "Gold World"
       }
   },

   "Emerald World": {
       "description": "This world is famous for green nature.",
       "choices": {
           "red": "Dice",
           "blue": "Tech World",
           "green": "Cold World"
       }
   },

   "Falls World": {
       "description": "This world is famous for great fall",
       "choices": {
           "red": "Cold World",
           "blue": "Smart World",
           "green": "Dice"
       }
   },

   "Tech World": {
       "description": "This world is surround by electrical technology",
       "choices": {
           "red": "Jazz World",
           "blue": "Wild World",
           "green": "Cold World"
       }
   },

   "Smart World": {
       "description": "Description of this room and the choices a user can make.",
       "choices": {
           "red": "Sea World",
           "blue": "Jazz World",
           "green": "Dice"
       }
   },

   "Gold World": {
       "description": "Description of this room and the choices a user can make.",
       "choices": {
           "red": "Samurai",
           "blue": "Samurai",
           "green": "Samurai"
       }
   },

   "Wild World": {
       "description": "Description of this room and the choices a user can make.",
       "choices": {
           "red": "Cow_Damon",
           "blue": "Cow_Damon",
           "green": "Cow_Damon"
       }
   },

   "Sea World": {
       "description": "Description of this room and the choices a user can make.",
       "choices": {
           "red": "Mermaid",
           "blue": "Mermaid",
           "green": "Mermaid"
       }
   },

   "New World": {
       "description": "Description of this room and the choices a user can make.",
       "choices": {
           "red": "Final",
           "blue": "Final",
           "green": "Final"
       }
   }


}



def adventure():
    '''
    Purpose: To run the game
    Parameter(s): none
    Return Value: none
    '''
    ball = 0
    time_machine = ["red", "blue", "green"]
    dice = [1, 2, 3]

    beated_cow_damon = 0
    beated_mermaid = 0
    beated_samurai = 0


    now_place = "Cold World"
    print("The king was robbed a diamond by Boss Eagle(which is final boss).")
    print("So the king begged you to take back a diamond. ")
    print("There are 10 world and Eagle is in New World. But you have to get 3 balls to get into the New World.")
    print("There are 3 bosses in some world and you can get one ball if you beat one boss.")
    print("Once you correct 3 balls, the way to the New World will be opened.")

    print("\nYou have a 3 time machine(red, blue, green) that the destination is different based on the color of time machine.")
    print("You can use one time machine at one time.")
    print("And you have dices.(default is 1,2,3). In the boss battle, you can get random number from dice.")
    print("If your number is higher than number the boss has, you can beat bosses.")
    print("You may get a another number of dice when you use any time machines. It will help you in the boss battle.")
    print(" So, the more dice you have, the eaiser to beat bosses.")
    print("To beat a final boss, you have to get a number higher than final boss two times.")

    print("\nSo, you have to beat 3 bosses while moving world and searching another dice, and then beat final boss.")

    while ball < 3:

        print(f"dice{dice}")
        print(f"ball={ball}")
        print(f"\nYou are in {now_place}\n")
        print("Input 1; if you use red time machine")
        print("Input 2; if you use blue time machine")
        print("Input 3; if you use green time machine")
        players_decision = int(input("\nChoose the time machine(1,2,3): "))
        if players_decision == 1:
            status = rooms[now_place]["choices"][time_machine[0]]
            if status == "Dice":
                now_place = get_dice(now_place, dice)
            elif status == "Cow_Damon":
                if beated_cow_damon == 0:
                    beated_cow_damon += cow_demon(dice)
                    ball += beated_cow_damon
                else:
                    print("You have already beated Cow_Damon")
                now_place = "Cold World"
            elif status == "Mermaid":
                if beated_mermaid == 0:
                    beated_mermaid += mermaid(dice)
                    ball += beated_mermaid
                else:
                    print("You have already beated Mermaid")
                now_place = "Cold World"
            elif status == "Samurai":
                if beated_samurai == 0:
                    beated_samurai += samurai(dice)
                    ball += beated_samurai
                else:
                    print("You have already beated Samurai")
                now_place = "Cold World"
            else:
                now_place = move(now_place, time_machine[0])

        elif players_decision == 2:
            status = rooms[now_place]["choices"][time_machine[1]]
            if status == "Dice":
                now_place = get_dice(now_place, dice)
            elif status == "Cow_Damon":
                if beated_cow_damon == 0:
                    beated_cow_damon += cow_demon(dice)
                    ball += beated_cow_damon
                else:
                    print("You have already beated Cow_Damon")
                now_place = "Cold World"
            elif status == "Mermaid":
                if beated_mermaid == 0:
                    beated_mermaid += mermaid(dice)
                    ball += beated_mermaid
                else:
                    print("You have already beated Mermaid")
                now_place = "Cold World"
            elif status == "Samurai":
                if beated_samurai == 0:
                    beated_samurai += samurai(dice)
                    ball += beated_samurai
                else:
                    print("You have already beated Samurai")
                now_place = "Cold World"
            else:
                now_place = move(now_place, time_machine[1])

        elif players_decision == 3:
            status = rooms[now_place]["choices"][time_machine[2]]
            if status == "Dice":
                now_place = get_dice(now_place, dice)
            elif status == "Cow_Damon":
                if beated_cow_damon == 0:
                    beated_cow_damon += cow_demon(dice)
                    ball += beated_cow_damon
                else:
                    print("You have already beated Cow_Damon")
                now_place = "Cold World"
            elif status == "Mermaid":
                if beated_mermaid == 0:
                    beated_mermaid += mermaid(dice)
                    ball += beated_mermaid
                else:
                    print("You have already beated Mermaid")
                now_place = "Cold World"
            elif status == "Samurai":
                if beated_samurai == 0:
                    beated_samurai += samurai(dice)
                    ball += beated_samurai
                else:
                    print("You have already beated Samurai")
                now_place = "Cold World"
            else:
                now_place = move(now_place, time_machine[2])

        else:
            print("\nThere is no this kind of time machine.")

    final_boss(dice)
    return None

adventure()

    