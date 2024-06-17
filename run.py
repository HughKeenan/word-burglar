import random 

def intro():
    """
    This function is the beginning of the game
    """
    print("After long preparations, you are finally ready to pull off your heist of the great treasure in Mr. Holmes' residence.")
    print("You've heard his house is a bit weird, but that won't stop you. You know his schedule and he should be asleep by now. Time to get to work.")
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
    print("Straightening up, you look around the dark room. Do you...")

    print("A: Run to the door. Let's get this over with and get out!")
    print("B: Check the room for valuables")
    print("C: Quietly proceed to the door")
    print("D: Cut and run")

    while True:
        answer = str(input())
        if answer == "a" or answer == "A":
            print("Sprinting towards the door, you fail to notice the coffee table a few feet in front of you. Tripping over it, you fall face first into the floor and suffer a severe concussion.")
            game_over()  
        elif answer == "b" or answer == "B":
            print("Crouching down so as not to be seen, you do a thorough inventory of the room, but what you're looking for isn't here.")
            first_room()
        elif answer == "c" or answer == "C":
            print("Carefully you proceed to the door, taking care not to hit off the coffee table and make a noise.")
            corridor()   
        elif answer == "d" or answer == "D":
            print("At least you made it inside.")
            wuss_out()     
        else:
            print("Please choose a valid option")

def corridor():
    """
    This function acts as the main hub of the game, from which the player can head to the ending or try optional challenges
    """
    print("Closing the door softly behind you, you find yourself in the house's shadowy corridor. Do you...")
    print("A: Go into the nearby bathroom.")
    print("B: Head into the lounge.")
    print("C: Head into the trophy room.")
    print("D: Go further down the corridor.")
    print("E: Cut and run.")

    while True:
        answer = str(input())
        if answer == "a" or answer == "A":
            print("What are you doing?! This is Word Burglar, not Turd Burlgar!")
            corridor()
        elif answer == "b" or answer == "B":
            print("Heading to the door directly opposite you, you gently open it and slip into the lounge")
            lounge()
        elif answer == "c" or answer == "C":
            print("Glancing down the corridor, you walk down it a few paces to the next door and enter the trophy room.")
            trophy_room()
        elif answer == "d" or answer == "D":
            print("Listening intently, you pad down the corridor towards your real prize.")
            saferoom_door()
        elif answer == "e" or answer == "E":
            print("What, scared of the dark?")
            wuss_out()     
        else:
            print("Please choose a valid option")

def lounge():
    """
    This function provides a puzzle for the player to solve
    """

def trophy_room():
    """
    This function allows the player to enter the trophy room and choose whether to engage with an optional puzzle 
    """
    print("Closing the door behind you, you see the room is bare, save for the large golden trophy set on a pedastal in the centre. Do you...")
    print("A: Look around the room.")
    print("B: Run straight up to the trophy and take it. Shiny!")
    print("C: Cautiously approach the trophy.")
    print("D: Go back to the corridor, this seems off.")
    while True:
        answer = str(input())
        if answer == "a" or answer == "A":
            print("You look carefully into every nook and cranny around the edge of the room, but nothing catches your eye.\n Maybe he's just weirdly proud of his trophy.\n You even open the door and peek out into the corridor but there's nothing there.")
            trophy_room()
        elif answer == "b" or answer == "B":
            print("In your haste to reach it, you don't notice the floor tile that depresses under your tread.\n Such is your speed that a clever mechanism intended to trap you instead scythes clean through your body, slicing you in two.")
            gruesome_death()
        elif answer == "c" or answer == "C":
            print("Keeping an eye out, you approach the trophy. A tile depresses under your foot and you stumble forward.\n Getting to your feet, you see sawblades coming out of the hold and floor on long arms, preventing you from moving in any direction.")
            trophy_trap()
        elif answer == "d" or answer == "D":
            print("Remembering you've heard this guy's a nutjob, you decide not to risk whatever he cooked up in here and go back to the corridor")
            corridor()     
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
    print("You approach the safe. On the front is a keypad with numbers 0 - 3.")
    print("You remember from casing the house that the code is 3 digits long and the first one is 2. If you get any digit wrong you'll have to go back to the start of the sequence.")
    print("Be careful! You've seen this kind of safe before!")
    print("If you enter more than 6 wrong numbers, it will set off the alarm and the police will be here in minutes!")

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

def gruesome_death():
    """
    This function ends the game if the player dies
    """
    print("You lie on the floor as your blood pools around you, wishing you had listened when people told you this wasn't worth it.")
    print("Would you like to play again? Please type Y/N.")
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
    """
    The main function serving as the game's menu, allowing the player to input their name and start playing
    """
    print("Welcome to Word Burglar. In this text-based game you will make choices to pull off a heist.\n Your objective is to find the priceless treasure hidden somewhere in the house.")
    print("As you progress through the game, you will be presented with choices A-D as you enter each room.\n Make your choice by typing the letter corresponding to the one you want, followed by ENTER.")
    name = str(input("To begin, please enter your name: "))
    print(f"Welcome to the game {name}")
    intro()

trophy_room()