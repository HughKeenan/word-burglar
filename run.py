import random 

def intro():
    """
    This function is the beginning of the game
    """
    print("After long preparations, you are finally ready to pull off your heist of the great treasure in Mr. Holmes' residence.")
    print("You know his schedule and he should be asleep by now. Time to get to work.")
    print("Approaching the house, you see a window beside the front door. Do you...")
    print("A: Kick the door down")
    print("B: Break the window")
    print("C: Open the window quietly")
    print("D: Cut and run")

    while True:
        answer = str(input())
        if answer == "a" or answer == "A":
            print("Boldly striding up to the front door, you aim a mighty kick at it and drive your foot home.\n Your foot goes straight into the letterbox, whereupon it becomes stuck.")
            game_over()  
        elif answer == "b" or answer == "B":
            print("Sneaking around to the side of the house, you put your elbow through the window. It shatters and slices a deep gash in your arm, causing you to scream in agony.")
            game_over()
        elif answer == "c" or answer == "C":     
            print("Taking a thin knife from your pocket, you jemmy open the window quietly and slip inside.")
            first_room()
        elif answer == "d" or answer == "D":
            print("For reasons known only to yourself, you wuss out at the very first hurdle. Pathetic.")
            wuss_out()
        else:
            print("Please choose a valid option")

def first_room():
    """
    Player choices for the first room
    """
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
    """
    Player Choices for the last room
    """
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
    """
    This function is a random number generator, the player must guess the safe code to win the final prize
    """
    print("You approach the safe. On the front is a keypad with numbers 0 - 4.")
    print("You remember from casing the house that the code is 3 digits long and the first one is 2. If you get any digit wrong you'll have to go back to the start of the sequence.")
    print("Be careful! You've seen this kind of safe before!")
    print("If you enter more than 5 wrong numbers, it will set off the alarm and the police will be here in minutes!")

    numbers = [x for x in range(4)]
    attempts = 6

    known_number = 2

    code = random.sample(numbers,2)

    combination = []
    combination.append(known_number)
    combination.extend(code)
    print(numbers)
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
    """
    Ends the game in a victory state
    """
    print("You Win!")

def game_over():
    """
    Ends the game in a fail state
    """
    print("Blaring sirens ring in your ears as the police, responding to reports to suspicious activity,\n tackle you to the ground and cuff your hands behind your back.")
    print("You will be going to prison for a very long time.")
    print("GAME OVER")
    print("Would you like to play again? Please type Y/N")
    
    while True:
        answer = str(input())
        if answer == "y" or answer == "Y":
            intro()  
        elif answer == "n" or answer == "N":
            main()    
        else:
            print("Please choose a valid option")

def wuss_out():
    """
    Runs if the player chooses to end the run voluntarily
    """
    print("Red faced and blinded by tears of humiliation, you slink away defeated, knowing you didn't have what it takes to claim the ultimate prize.")
    while True:
        answer = str(input())
        if answer == "y" or answer == "Y":
            intro()  
        elif answer == "n" or answer == "N":
            main()    
        else:
            print("Please choose a valid option")

def main():
    """
    The main function serving as the game's menu, allowing the player to input their name and start playing
    """
    print("Welcome to Word Burglar. In this text-based game you will make choices to pull off a heist.\n Your objective is to find the priceless treasure hidden somewhere in the house.")
    print("As you progress through the game, you will be presented with choices A-D as you enter each room.\n Make your choice by typing the letter corresponding to the one you want, followed by ENTER.")
    name = str(input("To begin, please enter your name: "))
    print(f"Welcome to the game {name}")
    intro()

main()