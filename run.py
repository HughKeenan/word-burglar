import random


def intro():
    """
    This function is the beginning of the game
    """
    print("After long preparations, you are finally ready")
    print("Tonight is your heist of the treasure in Mr. Holmes' residence.")
    print("You've heard his house is a bit weird, but that won't stop you.")
    print("You know his schedule and he should be asleep. Let's get to work.")
    print("Approaching the house, you see a window beside the front door.")

    print("Do you...")
    print("A: Kick the door down")
    print("B: Break the window")
    print("C: Open the window quietly")
    print("D: Cut and run")

    # This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("Striding up to the door, you drive a mighty kick at it.")
            print("Your foot goes into the letterbox, where it becomes stuck.")
            print("One of the neighbours sees you and calls the police")
            game_over()
        elif answer == "b" or answer == "B":
            print("Going to the window, you put your elbow through it.")
            print("It shatters, gashing your arm. You to scream in agony.")
            print("One of the nighbours who heard has called the police.")
            game_over()
        elif answer == "c" or answer == "C":
            print("You take a thin knife from your pocket.")
            print("You jemmy open the window and slip inside.")
            first_room()
        elif answer == "d" or answer == "D":
            print("You wuss out at the very first hurdle. Pathetic.")
            wuss_out()
        else:
            print("Please choose a valid option")


def first_room():
    """
    Player choices for the first room
    """
    print("Straightening up, you look around the dark room.\nDo you...")
    print("A: Run to the door. Let's get this over with and get out!")
    print("B: Quietly proceed to the door")
    print("C: Check the room for valuables")
    print("D: Cut and run")

    # This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("You sprint to the door, not noticing the coffee table.")
            print("Tripping over it, you faceplant onto the floor, concussed.")
            game_over()
        elif answer == "b" or answer == "B":
            print("You proceed, taking care not to hit the coffee table.")
            corridor()
        elif answer == "c" or answer == "C":
            print("You crouch down so as not to be seen.")
            print("You do a thorough inventory of the room.")
            print("What you're looking for isn't here.")
            first_room()
        elif answer == "d" or answer == "D":
            print("At least you made it inside.")
            wuss_out()
        else:
            print("Please choose a valid option")


def corridor():
    """
    This function acts as the main hub of the game.
    From here the player can head to the ending
    or try optional challenges
    """
    print("Closing the door, you find yourself in the shadowy corridor.")
    print("Do you...")
    print("A: Go into the nearby bathroom.")
    print("B: Head into the lounge.")
    print("C: Head into the trophy room.")
    print("D: Go further down the corridor.")
    print("E: Cut and run.")

    # This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("What are you doing?!")
            print("This is Word Burglar, not Turd Burlgar!")
            corridor()
        elif answer == "b" or answer == "B":
            print("You head to the door directly opposite.")
            print("You gently open it and slip into the lounge.")
            lounge()
        elif answer == "c" or answer == "C":
            print("Glancing down the corridor, you walk down it a few paces.")
            print("You reach the next door and enter the trophy room.")
            trophy_room()
        elif answer == "d" or answer == "D":
            print("Listening intently, you pad towards another door.")
            saferoom_door()
        elif answer == "e" or answer == "E":
            print("What, scared of the dark?")
            wuss_out()
        else:
            print("Please choose a valid option")


def lounge():
    """
    This function brings the player into the lounge, where they can encounter an optional puzzle
    """
    print("The lounge is richly furnished, you see a book bound in what looks like gold on the mantlepiece.\nDo you...")
    print("A: Pick up the book.")
    print("B: Check out the liquor cabinet.")
    print("C: Sit on the couch and take a load off.")
    print("D: Go back to the corridor, need to stay on task.")

    #This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("Stalking over to the book, you reach out and grasp it with both hands. It doesn't move, and you hear a loud click.")
            lounge_trap()            
        elif answer == "b" or answer == "B":
            print("Heading over to the glass fronted liquor cabinet, you open it and take a huge gulp of brandy from one of the bottles.\nIt immediately goes to your head and you dance around the room singing at the top of your voice.\nYou come to your senses just in time to see the police car outside the window.")
            game_over()           
        elif answer == "c" or answer == "C":
            print("You plonk down on the couch, raising a huge cloud of dust and causing you to erupt into paralysing and cacaphonous coughs and sneezes.\nYou have woken Mr. Holmes and he is now calling the police.")
            game_over()
        elif answer == "d" or answer == "D":
            print("Deciding that such valuables out in the open are probably too good to be true, you turn on your heel and return to the corridor.")
            corridor()
        else:
            print("Please choose a valid option")

def lounge_trap():
    """
    This function activates the trap minigame in the lounge room
    """
    print("A pair of manacles spring from the mantlepiece and snap shut around your wrists. You pull at them to no avail.\nLooking up, you see a metal spike emerging from a hole in the ceiling.")
    print("It looks as though it's preparing to drop down and impale you!\nLooking around in desperation, you see words appear on the mirror:")
    print("You've met your match brigand! I will release you only if you can choose the word that desribes your villany!")

    options = ["PUCKERIER", "PUGILIST", "PULLDEVIL", "PURPURA", "PURFLER"]
    required_word = "PURLOINER" 
    #The choices variable selects 2 entries at random from the options list 
    choices = random.sample(options,2)

    #show_to_player creates an empty list, to which the puzzle solution and 2 wrong choices are added
    show_to_player = []
    show_to_player.append(required_word)
    show_to_player.extend(choices)

    print(show_to_player)

    #This while loop lets the player answer the puzzle
    #string methods contained within ensure answers of upper or lower case will be accepted
    while True:
        answer = str(input("What word best describes you? ")).upper()
        if answer == required_word:
            print("With a grinding of gears, the spike retreats. Your wrists are released and you straighten up.")
            print("Gold or no, that thing isn't worth it. Rubbing at your chafed skin, you retreat to the safety of the corridor.")
            corridor()
        else:
            print("At your incorrect answer, the dull clunk of something unlocking sends a shiver through your spine.\nMoments later the spike follows it, buckling you under the impact.")
            gruesome_death()

def trophy_room():
    """
    This function allows the player to enter the trophy room and choose whether to engage with an optional puzzle 
    """
    print("Closing the door behind you, you see the room is bare, save for the large golden trophy set on a pedastal in the centre.\nDo you...")
    print("A: Look around the room.")
    print("B: Run straight up to the trophy and take it. Shiny!")
    print("C: Cautiously approach the trophy.")
    print("D: Go back to the corridor, this seems off.")

    #This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("You look carefully into every nook and cranny around the edge of the room, but nothing catches your eye.\nMaybe he's just weirdly proud of his trophy.\nYou even open the door and peek out into the corridor but there's nothing there.")
            trophy_room()
        elif answer == "b" or answer == "B":
            print("In your haste to reach it, you don't notice the floor tile that depresses under your tread.\nSuch is your speed that a clever mechanism intended to trap you instead scythes clean through your body, slicing you in two.")
            gruesome_death()
        elif answer == "c" or answer == "C":
            print("Keeping an eye out, you approach the trophy. A tile depresses under your foot and you stumble forward.\nGetting to your feet, you see sawblades coming out of the walls and floor on long arms, preventing you from moving in any direction.")
            trophy_trap()
        elif answer == "d" or answer == "D":
            print("Remembering you've heard this guy's a nutjob, you decide not to risk whatever he cooked up in here and go back to the corridor")
            corridor()     
        else:
            print("Please choose a valid option")

def trophy_trap():
    """
    Provides an optional puzzle by asking the player to solve a word puzzle formed from rearranged letters in a string
    """
    password = "AVARICIOUS"
    #The password_question variable rearranges the password letters at random, creating a puzzle for the player
    password_question = "".join(random.sample(password, len(password)))
    
    print("Starting to panic, you frantically turn around looking for a solution.\nYou notice a placard has descended from the ceiling.")
    print("It says 'Your greed will be your undoing thief! Admit it and decipher my puzzle to be freed! What are you?!'")
    print(f"Beneath the message you see {password_question}.\nIt must be an anagram! Unscramble the letters and find the word to solve it!")
    
    #This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What do you admit to being? ")).upper()
        if answer == password:
            print("The sawblades retract and you heave a sigh of relief.\nDeciding to leave the trophy where it is, you waste no time in leaving the room.")
            corridor()
        else:
            print("Your inability to answer the question signals to the sawblades and they extend on their arms, cutting you to ribbons.")
            gruesome_death()

def saferoom_door():
    print("Your head is on a swivel at this final door.\nThe only other room is Holmes' bedroom, so this must be it!\nYou try the handle but it won't open.\nDo you...")
    print("A: Try the handle again.")
    print("B: Try to pick the lock.")
    print("C: Ask Mr. Holmes to open it.")
    print("D: Cut and run")

    #This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("It's clearly locked, but keep trying, I'm sure it'll open at some stage.")
            saferoom_door()
        elif answer == "b" or answer == "B":
            print("You take your trusty lockpick from your pocket and slip it into the keyhole.\nThis shouldn't be too difficult...")
            lockpicker()            
        elif answer == "c" or answer == "C":
            print("Taking complete leave of your senses, you knock on the bedroom door.\nA bleary eyed Holmes asnwers and you ask him for the key to his study.\nHe responds by punching you squarely in the face, knocking you unconscious.\nYou wake to find yourself locked in the wardrobe and police running through the house.")
            game_over()
        elif answer == "d" or answer == "D":
            print("Quitting just before the end. You utter coward.")
            wuss_out()
        else:
            print("Please choose a valid option")

def lockpicker():
    """
    This function provides a minigame based on player input
    """
    print("Crounching down with the lock at eye level, you prepare to pick the lock, listening intently for any click to tell you it's opening.")
    print("It looks like a normal 3 pin lock, so 3 clicks and it's open.")
    print("If you move the lock in the wrong direction, you'll have to go back to the start.\nGo easy, you only have 1 pick and it's delicate, move it in the wrong direction 3 times and it'll snap.")
    print("Type in the direction you wish to move the pick: 'UP', 'DOWN', 'LEFT' or 'RIGHT' and press ENTER")

    turns_to_break = 3

    pin_one = "UP" 
    pin_two = "LEFT"
    pin_three = "RIGHT"
    
    #This lets the player choose how to move the lockpick to open the door
    #string methods contained within ensure answers of upper or lower case will be accepted
    #on a wrong choice, the player must start again from the beginning
    #if the player answers wrongly 3 times, they lose the game
    while True:
        path_to_open = (input("Which direction do you move the pick: ")).upper()
        if path_to_open == pin_one:
            print("Click!")
            path_to_open_2 = (input("Which direction do you move the pick: ")).upper()
            if path_to_open_2 == pin_two:
                print("Click!")    
                path_to_open_3 = (input("Which direction do you move the pick: ")).upper()
                if path_to_open_3 == pin_three:
                    print("Click!")
                    print("Nice! Silently you open the door and slip inside.")
                    last_room()
                    break
                else:
                    print("Clunk! That's not right!")
                    print("You think back to the rhyme you made up while practicing on locks like this one:\n'The sun came up in the morning, left the east and headed right on to the west'")
                    turns_to_break -=1
                    print(f"{turns_to_break} wrong moves until the pick breaks")
                    if turns_to_break == 0:
                        print("The lockpick snaps in the keyhole.\nYou curse in frustration and kick the door.\nTurning, you see a very angry looking Mr. Holmes, one hand pointing a revolver at you and the other calling the police.")
                        game_over()
            else:
                print("Clunk! That's not right!")
                print("You think back to the rhyme you made up while practicing on locks like this one:\n'The sun came up in the morning, left the east and headed right on to the west'")
                turns_to_break -=1
                print(f"{turns_to_break} wrong moves until the pick breaks")
                if turns_to_break == 0:
                    print("The lockpick snaps in the keyhole.\nYou curse in frustration and kick the door.\nTurning, you see a very angry looking Mr. Holmes, one hand pointing a revolver at you and the other calling the police.")
                    game_over()
        else:
            print("Clunk! That's not right!")
            print("You think back to the rhyme you made up while practicing on locks like this one:\n'The sun came up in the morning, left the east and headed right on to the west'")
            turns_to_break -=1
            print(f"{turns_to_break} wrong moves until the pick breaks")
            if turns_to_break == 0:
                print("The lockpick snaps in the keyhole.\nYou curse in frustration and kick the door.\nTurning, you see a very angry looking Mr. Holmes, one hand pointing a revolver at you and the other calling the police.")
                game_over()

def last_room():
    """
    Player Choices for the last room
    """
    print("Closing the door, you look around the room. It's Holmes' office.\nRemembering what you saw when casing the house, you remove a painting from the back wall, revealing a small safe.\nDo you...")
    print("A: Open the safe")
    print("B: Go back to corridor")
    print("C: Cut and run")

    #This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("Taking a deep breath to steady yourself, you decide it's all or nothing.")
            safecracker()  
        elif answer == "b" or answer == "B":
            print("Thinking you heard a noise outside, you go back out to the corridor and check.\nThere's nothing there, but you hear the office door shut behind you.\nTrying the handle you find it has locked itself automatically, you'll have to open it again.")
            lockpicker()
        elif answer == "c" or answer == "C":
            print("...\nI mean...just why?")
            wuss_out()    
        else:
            print("Please choose a valid option")

def safecracker():
    """
    This function is a random number generator, the player must guess the safe code to win the final prize
    """
    print("You approach the safe. On the front is a keypad showing the numbers 0 - 3.")
    print("You remember from casing the house that the code is 3 digits long and the first one is 2.\nIf you get any digit wrong you'll have to go back to the start of the sequence.")
    print("Be careful! You've seen this kind of safe before!")
    print("If you enter more than 6 wrong numbers, it will set off the alarm and the police will be here in minutes!")

    #The numbers variable is a list comprehension of the numbers 0-3, creating a list of those numbers
    numbers = [x for x in range(4)]
    attempts = 6

    known_number = 2

    code = random.sample(numbers,2)

    #combination creates an empty list, to which the 3 digits of the combination are added
    combination = []
    combination.append(known_number)
    combination.extend(code)

    #This lets the player guess the digits of the combination
    #on a wrong choice, the player must start again from the beginning
    #if the player answers wrongly 6 times, they lose the game
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
    print("The safe door swings open. Hardly daring to believe it, you reach in and grasp the contents with trembling hands")
    print("Finally! After all this time, you can prove that you are the ultimate Word Burglar!")
    print("You hold it up to a shaft of moonlight streaming in through the window, and examine the ultimate prize:")
    print("Mr. Holmes' Thesaurus!")

def game_over():
    """
    Ends the game in a fail state
    """
    print("Blaring sirens ring in your ears as the police burst in.\nResponding to reports of suspicious activity, they tackle you to the ground and cuff your hands behind your back.")
    print("You will be going to prison for a very long time.")
    print("GAME OVER")
    
    #This lets the player choose whether to restart on a game over
    while True:
        answer = str(input("Would you like to play again? Please type Y/N: "))
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
    
    #This lets the player choose whether to restart on a game over
    while True:
        answer = str(input("Would you like to play again? Please type Y/N: "))
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
    
    #This lets the player choose whether to restart on a game over
    while True:
        answer = str(input("Would you like to play again? Please type Y/N: "))
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
    print("Welcome to Word Burglar.\nIn this text-based game you will make choices to try and pull off a heist.\nYour objective is to find the priceless treasure hidden somewhere in the house.")
    print("As you progress through the game, you will be presented with choices as you enter each room.\nMake your choice by typing the letter corresponding to the one you want, followed by ENTER.")
    
    #This lets the player input a name
    #names cannot be longer than 15 characters
    while True:
        name = str(input("To begin, please enter your name: "))
        if len(name) > 15:
            print("You name may be a maximum of 15 characters long")
            continue 
        else:     
            print(f"Welcome to the game {name}")
            intro()

main()