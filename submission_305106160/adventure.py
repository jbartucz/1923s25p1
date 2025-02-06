import random

rooms = { 
         
         "Kitchen": { 
                    
                    "description": 
                      ("This is a room that contains a industrial fridge (with various foods) and all the tools one would need to make a 5 course meal at a resturant"), 
                    
                    "choices": { 
                      
                      "A": "Dining Room", 
                      "B": "Pantry Room", 
                      "C": "Mudroom", 
                         
                      }
                    }, 
         
         "Dining Room": { 
                    
                    "description": ("This is an expansive dining room that exudes sophistication with its soaring ceilings, and grand chandelier, and an elongated table that seats 12+. Large arched windows bathe the space with antural light, while intricate crown molding and polished hardwood floors add a timeless charm."), 
                    
                    "choices": { 
                      
                      "A": "Kitchen", 
                      "B": "Living Room", 
                      "C": "Foyer/Entryway", #maybe mudroom
                         
                      } 
                    }, 
         
         "Pantry Room": { 
                    
                    "description": ("This well stocked pantry is a haven of organization and effiency, featuring floor-to-celing shelves brimming with neatly labeled jars of gains, spices, and preserves. Ample storage bins and pull-out drawers house dry goods, while a dedicated section for canned goods, baking essentials, and gourmet ingredients esures everything is within easy reach. Soft, under-shelf lighting adds warmth, making it a chef's dream space."), 
                    
                    "choices": { 
                      
                      "A": "Kitchen", 
                      "B": "Butler's Room", 
                      "C": "Wine Room", 
                         
                      }
                    },
          
         "Mudroom": { 
                    
                    "description": ("Stepping inside, the mudroom greets you with timeless elegance and effortless charm. Built-in cabinetry in a refined hue, brass hooks, and a custom bench create a seamless blend of beauty and function. Artisan tiles underfoot add a touch of sophistication, while open shelving with woven baskets keeps the space airy and organized. A reclaimed wood accent or vintage hall tree infuses character, making this more than just a passage—its a warm, welcoming experience that sets the tone for the home."), 
                    
                    "choices": { 
                      
                      "A": "Kitchen", 
                      "B": "Laundry Room", 
                      "C": "Storage Room", 
                         
                      }
                    }, 
         
         "Living Room": { 
                    
                    "description": ("Stepping into the living room, a sense of calm immediately washes over you. Soft natural light filters through sheer drapes, casting a warm glow over plush seating designed for both relatation and converation. A statement fireplace or central coffee table anchors the space, inviting quiet moments with a book or lively discussion with loved ones."), 
                    
                    "choices": { 
                      
                      "A": "Dining Room", 
                      "B": "Foyer/Entryway", 
                      "C": "Mudroom", 
                         
                      }
                    }, 
         
         "Wine Room": { 
                    
                    "description": ("Though intimate in scale, this wine cellar bridges old-world elegance with modern experimentation, Floor-to-celing racks showcase a curated mix of  time-honored classics and bold new blends, all kept in optimal conditions. Soft, ambient lighting highlights the labels and invities quite moments of tasting, making each visit a small yet memorable escape."), 
                    
                    "choices": { 
                      
                      "A": "Butler's Room", 
                      "B": "Pantry Room", 
                         
                      }
                    
                    },
         
         "Foyer/Entryway": { 
                    
                    "description": ("Inside the Entryway you're greeted by warmth and refinement, echoing the mudroom's charm. A pendant light illumicates paneled walls, while subtle reclaimed wood or fine millworks add timeless character. Underfoot, artisan tile (or possibly hardwood) extends a gracious welcome toward a small bench or console. Mirrors and understated decore amplify natural light, and a single statement piece, like an heirloom mirror, completes the scene, hinting at the thoughtful design found throughout the home."), 
                    
                    "choices": { 
                      
                      "A": "Living Room", 
                      "B": "Dining Room", 
                      "C": "Kitchen", 
                         
                      }
                    }, 
         
         "Butler's Room": { 
                    
                    "description": ("The butler's room offers a sophisticated yet highly functional space for seamless entertainment. Elegant cabinetry, finished in a timeless hue, neatly stores fine china and linens. A polished countertop provides ample room for plating or staging dishes before they journey to the dining room. Sof lighting and suble decorative flourises lend an air of quiet luxury, ensuring thatevery detail, from service to style, exudes effortless grace."), 
                    
                    "choices": { 
                      
                      "A": "Pantry Room", 
                      "B": "Wine Room",  
                         
                      }
                    }, 
         
         "Laundry Room": { 
                    
                    "description": ("Echoing the home's refined charm, the laundry merges from and functino in a light-filled space. SOft, neutral tones pair with warm wood accents and modern hardaware, while built-in cabinetry keeps essentials neatly tucked away. A generous utility sink stands out as both practical and elegant, and thoughtfully chosen lighting brightens every corner. Subtle decorative touches, like a chic backsplash or a tasteful piece of art, transform daily chores into a serene, reenergizing ritual."), 
                    
                    "choices": { 
                      
                      "A": "Mudroom", 
                      "B": "Storage Room", 
                         
                      }
                    },
         
         "Storage Room": { 
                    
                    "description": ("Discrete yet indispensible, the storage room simplifies home organization with floor-to-celing shelving, neatly labeled bins, and a neutral palette that echoes the house's overall sernity. Subtle lighting ensures every item is easy to locate, turing what could be a cramped catch-all a well ordered, calming extension of the home."), 
                    
                    "choices": { 
                      
                      "A": "Pantry Room", 
                      "B": "Laundry Room", 
                      "C": "Mudroom", 
                         
                      }
                    
                    }
         
         }

my_animals = ["Tina The Cat", "Chucky The Dog", "Donald The Duck", "Jack The Fish"]


my_toys = {
    "Tina The Cat": ["Catnip toys", "Spring toys", "Cardboard Box"],
    "Chucky The Dog": ["Tug Rope", "Chew Toys", "Fetch Ball", "Frisbee"],
    "Donald The Duck": ["Mirror", "Hanging Bells", "Floating Pool Toys", "Treat-Dispensing toys"]
}

def printInstructions(): 
  print("\n What would you like to do?")
  print(" - look            : Show the rooms description and any items present.")
  print(" - go <room>       : Moves you to a connected room")
  print(" - take random    : Picks up an item (if available  in present room).")
  print(" - inventory       : Shows items you are carrying")
  print(" - exit            : Quits the game.\n")

def showRoom(playerState): 
  currentRoom = playerState["currentRoom"]
  roomInfo = rooms[currentRoom]
  print(f"\nYou are in the {currentRoom}.\n")
  
  print(roomInfo["description"])
  print("\n", roomInfo["choices"])
  
  print("\nExits:")
  for key, value in roomInfo["choices"].items(): 
    print(f" {key}: {value}")
  
def changeRooms(playerState, chosenRoom):  
  currentRoom = playerState["currentRoom"]
  if chosenRoom in rooms[currentRoom]["choices"].values(): 
    playerState["currentRoom"] = chosenRoom
    showRoom(playerState)
  else: 
    print(f"Unfortunately, you cannot go to {chosenRoom} from here.")
    
def takeRandomItem(playerState, my_toys): 
    animal = playerState.get("animal")
    
    if animal not in my_toys: 
       print(f"No toys available for {animal}")
       return
    
    toy = random.choice(my_toys[animal])
    
    playerState["inventory"].append(toy)
    
    return print(f"You have added {toy} to your inventory!")
    
    
def startGame(): 
  print("Welcome to the House Exploration Game!")

  print("\nChoose your animal: ")
  for animal in my_animals:
    print(f"- {animal}")
    
  while True:
   
    
    while True:
      animalChoice = input("> ").strip().title()
      if animalChoice in my_animals:
          break
      else:
          print("Invalid choice. Please select from the list below:")
          for animal in my_animals:
              print(f"- {animal}")

    playerState = {
        "animal": animalChoice,
        "currentRoom": "Foyer/Entryway",
        "inventory": []
    }

    print(f"\nYou are a {playerState['animal']} exploring this house!")
    printInstructions()
    
    print("\nToys available: ")
    for animal, toys in my_toys.items(): 
      print(f"{animal}: {', '.join(toys)}")
    
    showRoom(playerState)
    
    
    while True: 
      command = input("\n> ").strip().lower()
      
      if command == "exit": 
        print("Thanks for Playing! Goodbye.")
        break
      elif command == "look":
        showRoom(playerState)
      elif command.startswith("go "): 
        _, chosenRoom = command.split(" ", 1)
        chosenRoom = chosenRoom.title()
        changeRooms(playerState, chosenRoom)
        printInstructions()
      elif command.startswith("take random"): 
         takeRandomItem(playerState, my_toys)
      elif command == "inventory": 
        if playerState["inventory"]: 
          print("You are carrying: ")
          for item in playerState["inventory"]: 
            print(f" - {item}")
        else: 
          print("You are not carrying any items.")
      else: 
        print("Invalid command. Type 'look' to examine the room or 'exit to quit.")
        
if __name__ == "__main__":
    startGame()
          
    
    

  



