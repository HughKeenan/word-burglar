
def intro():
    print("You are standing outside of the house you plan to rob. Do you...")
    
    print("A: Open the door")
    print("B: Kick the door")

    answer = str(input())
    if answer == "a" or "A":
        print("Correct")  
    elif answer == "b" or "B":
        print("wrong")

def game_over():
    print("You have been arrested, game over")

def first_room():
    print("You are in the first room")

def main():
    print("Welcome to Word Burglar. In this text-based game you will make choices to pull off a heist.\n Your objective is to find the priceless painting hidden somewhere in the house.")
    print("As you progress through the game, you will be presented with choices A-D as you enter each room.\n Make your choice by typing the letter corresponding to the one you want.")
    name = str(input("To begin, please enter your name: "))
    print(f"Welcome to the game {name}")
    intro()



main()