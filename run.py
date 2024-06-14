
def intro():
    print("You are standing outside of the house you plan to rob. Do you...")
    
    print("A: Open the door")
    print("B: Kick the door")

    while True:
        answer = str(input())
        if answer == "a" or answer == "A":
            first_room()  
        elif answer == "b" or answer == "B":
            game_over()
        else:
            print("Please choose a valid option")

def first_room():
    print("You are in the first room. Do you...")

    print("A: Proceed to the last room")
    print("B: Go back to the intro")
    print("C: Wake the residents up and surrender")

    while True:
        answer = str(input())
        if answer == "a" or answer == "A":
            last_room()  
        elif answer == "b" or answer == "B":
            intro()
        elif answer == "c" or answer == "C":
            game_over()    
        else:
            print("Please choose a valid option")

def last_room():
    print("You are in the last room. Do you...")

    print("A: Open the safe")
    print("B: Go back to the first room")
    print("C: Wake the residents up and surrender")

    while True:
        answer = str(input())
        if answer == "a" or answer == "A":
            last_room()  
        elif answer == "b" or answer == "B":
            first_room()
        elif answer == "c" or answer == "C":
            game_over()    
        else:
            print("Please choose a valid option")

def game_over():
    print("You have been arrested, game over")
    print("Would you like to play again? Please type Y/N")
    
    while True:
        answer = str(input())
        if answer == "y" or answer == "Y":
            intro()  
        elif answer == "n" or answer == "N":
            main()    
        else:
            print("Please choose a valid option")
    

def main():
    print("Welcome to Word Burglar. In this text-based game you will make choices to pull off a heist.\n Your objective is to find the priceless painting hidden somewhere in the house.")
    print("As you progress through the game, you will be presented with choices A-D as you enter each room.\n Make your choice by typing the letter corresponding to the one you want.")
    name = str(input("To begin, please enter your name: "))
    print(f"Welcome to the game {name}")
    intro()

main()