import random 

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
            safecracker()  
        elif answer == "b" or answer == "B":
            first_room()
        elif answer == "c" or answer == "C":
            game_over()    
        else:
            print("Please choose a valid option")

def safecracker():
    print("You approach the safe. On the front is a keypad with numbers 0 - 4.")
    print("You remember from casing the house that the code is 3 digits long and the first one is 2. If you get any digit wrong you'll have to go back to the start of the sequence.")
    print("Be careful! You've seen this kind of safe before, if you enter more than 5 wrong numbers, it will set off the alarm and the police will be here in minutes!")

    numbers = [x for x in range(4)]
    attempts = 5

    known_number = 2

    code = random.sample(numbers,2)

    combination = []
    combination.append(known_number)
    combination.extend(code)
    print(combination)

    while True:
        solution = int(input("Please enter the first digit: "))
        if solution == known_number:
            print("Correct!")
            solution2 = int(input("Please enter the second digit: "))
            if solution2 == combination[1]:
                print("Correct!")    
                solution3 = int(input("Please enter the final digit: "))
                if solution3 == combination[2]:
                    print("You did it!")
                    game_won()
                    break
                else:
                    print("Wrong, start again")
                    attempts -=1
                    print(f"{attempts} attempts remaining")
                if attempts == 0:
                    game_over()    
            else:
                print("Wrong, start again")
                attempts -=1
                print(f"{attempts} attempts remaining")
                if attempts == 0:
                    game_over()
        else:
            print("What are you doing?! You know this one!")
            attempts -=1
            print(f"{attempts} attempts remaining")
            if attempts == 0:
                game_over()               


def game_won():
    print("You Win!")

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
    print("As you progress through the game, you will be presented with choices A-D as you enter each room.\n Make your choice by typing the letter corresponding to the one you want, followed by ENTER.")
    name = str(input("To begin, please enter your name: "))
    print(f"Welcome to the game {name}")
    intro()

safecracker()