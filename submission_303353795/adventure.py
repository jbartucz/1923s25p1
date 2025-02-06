import random


def instructions():
    print("Game start")

def main():
    rooms={
        "Entrance":{
            "description": "Here is Entrance, The point where game start",
            "choice": {
                "Forward":"common road",
                "exit": "leave"
            }
        },
        "common road":{
            "description": "Here is common road, The road connect treasure room",
            "choice" : {
                "Go next": "treasure room",
                "turn back": "Entrance"
            }
        },
        "treasure room":{
            "description": "Here is treasure room, A room may have treasure",
            "choice" : {
                "Turn left": "dark road",
                "Go back": "common road"
            }
        },
        "dark road":{
            "description": "Here is dark road, connect treasure room and next room",
            "choice" : {
                "Go explore": "secret room",
                "Quit": "treasure room"
            }
        },
        "secret room":{
            "description": "Here is secret room, Something unknown inside",
            "choice" : {
                "Take a rest": "rest ground",
                "Go back": "dark road"
            }
        },
        "rest ground":{
            "description": "Here is rest ground, you can take a rest here",
            "choice" : {
                "Keep explore":"evil room",
                "Keep safe": "secret room"
            }
        },
        "evil room":{
            "description": "Here is evil room, may have devil inside",
            "choice" : {
                "Go for reward": "reward road",
                "That's it": "rest ground"
            }
        },
        "reward road":{
            "description": "reward road, you may suprised here",
            "choice" : {
                "Go next":"Hallway",
                "That's all": "evil room"
            }
        },
        "Hallway":{
            "description": "Hallway, connect to the last room",
            "choice": {
                "Finally": "Final place",
                "I am afraid": "reward room"
            }
        },
        "Final place":{
            "description": "Here is Final place, This room let people feel stressful",
            "choice": {
                "Dance":"end_game",
                "Rest": "Hallway"
            }

        }

    }
    characters=["Sam","Bob","George"]

    enemies=["Bob", "Chris"]

    instructions()
    print("choose character")
    for i, j in enumerate(characters):
        print(f'{i+1}-{j}')

    while True:
        choice= int(input("choose which one you want to be:"))
        if 1<=choice <= len(characters):
            player1= characters[choice-1]
            print(f'You are {player1}')
            break
        else:
            print("input invalid, try again")


    current_location="Entrance"

    while True:
        print(f'\n{rooms[current_location]['description']}')
        print("pls choose")
        for do in rooms[current_location]["choice"]:
            print(f'{do}')
        enemy = random.choice(enemies)
        if enemy == "Bob":
            print("Bob is here, fight start")
            print('you beat him, congratulation')
        elif enemy == "Chris":
            print("Evil Chris is in front of you, let's do a boxing")
        action= input("What you want to do?").strip()
        if action in rooms[current_location]["choice"]:
            current_location=rooms[current_location]["choice"][action]
            if current_location ==  "end_game":
                print('Congratulation, game end')
                break
        else:
            print('invalid input, try again')

if __name__ == "__main__":
    main()