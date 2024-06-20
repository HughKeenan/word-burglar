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
            break
        elif answer == "b" or answer == "B":
            print("Going to the window, you put your elbow through it.")
            print("It shatters, gashing your arm. You to scream in agony.")
            print("One of the nighbours who heard has called the police.")
            game_over()
            break
        elif answer == "c" or answer == "C":
            print("You take a thin knife from your pocket.")
            print("You jemmy open the window and slip inside.")
            first_room()
            break
        elif answer == "d" or answer == "D":
            print("You wuss out at the very first hurdle. Pathetic.")
            wuss_out()
            break
        else:
            print("Please choose one of the options shown")


def first_room():
    """
    Player choices for the first room
    """
    print("Straightening up, you look around the dark room.")
    print("Do you...")

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
            break
        elif answer == "b" or answer == "B":
            print("You proceed, taking care not to hit the coffee table.")
            corridor()
            break
        elif answer == "c" or answer == "C":
            print("You crouch down so as not to be seen.")
            print("You do a thorough inventory of the room.")
            print("What you're looking for isn't here.")
            first_room()
            break
        elif answer == "d" or answer == "D":
            print("At least you made it inside.")
            wuss_out()
            break
        else:
            print("Please choose one of the options shown")


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
            break
        elif answer == "b" or answer == "B":
            print("You head to the door directly opposite.")
            print("You gently open it and slip into the lounge.")
            lounge()
            break
        elif answer == "c" or answer == "C":
            print("Glancing down the corridor, you walk down it a few paces.")
            print("You reach the next door and enter the trophy room.")
            trophy_room()
            break
        elif answer == "d" or answer == "D":
            print("Listening intently, you pad towards another door.")
            saferoom_door()
            break
        elif answer == "e" or answer == "E":
            print("What, scared of the dark?")
            wuss_out()
            break
        else:
            print("Please choose one of the options shown")


def lounge():
    """
    This function brings the player into the lounge.
    Here they can encounter an optional puzzle
    """
    print("The lounge is richly furnished.")
    print("You see a book bound in gold on the mantlepiece.")
    print("Do you...")

    print("A: Pick up the book.")
    print("B: Check out the liquor cabinet.")
    print("C: Sit on the couch and take a load off.")
    print("D: Go back to the corridor, need to stay on task.")

    # This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("Stalking to the book, you reach out and grasp it.")
            print("It doesn't move, and you hear a loud click.")
            lounge_trap()
            break
        elif answer == "b" or answer == "B":
            print("You head over to the glass fronted liquor cabinet.")
            print("You open it and take a big gulp of brandy from one bottle.")
            print("It immediately goes to your head.")
            print("You dance around the room singing like an idiot.")
            print("You recover just in time to see the police car outside.")
            game_over()
            break
        elif answer == "c" or answer == "C":
            print("You plonk down on the couch, raising a huge cloud of dust.")
            print("You to erupt into paralysing and loud coughs and sneezes.")
            print("You have woken Mr. Holmes and he is calling the police.")
            game_over()
            break
        elif answer == "d" or answer == "D":
            print("Valuables in the open are probably too good to be true.")
            print("You turn on your heel and return to the corridor.")
            corridor()
            break
        else:
            print("Please choose one of the options shown")


def lounge_trap():
    """
    This function activates the trap minigame in the lounge room
    """
    print("Manacles spring from the mantlepiece and close around your wrists.")
    print("You pull at them to no avail.")
    print("Looking up, you see a metal spike emerge from the ceiling.")
    print("It looks as though it's preparing to drop down and impale you!")
    print("Looking around in desperation, you see words appear on the mirror:")
    print("You've met your match brigand!")
    print("I will release you only if you choose the word that describes you!")

    options = ["PUCKERIER", "PUGILIST", "PULLDEVIL", "PURPURA", "PURFLER"]
    required_word = "PURLOINER"

    # The choices variable selects 2 entries at random from the options list
    choices = random.sample(options, 2)

    # show_to_player creates an empty list
    # to which the puzzle solution and 2 wrong choices are added
    show_to_player = []
    show_to_player.append(required_word)
    show_to_player.extend(choices)

    print(show_to_player)

    # This while loop lets the player answer the puzzle.
    # String methods ensure answers of upper or lower case will work
    while True:
        ans = str(input("What word describes you? ")).upper()
        if ans == required_word:
            print("With a grinding of gears, the spike retreats.")
            print("Your wrists are released and you straighten up.")
            print("Gold or no, that thing isn't worth it.")
            print("Rubbing at your wrists, you retreat to the corridor.")
            corridor()
            break
        else:
            print("This was incorrect.")
            print("A dull clunk sends a shiver through your spine.")
            print("Instantly the spike follows, buckling you with the impact.")
            gruesome_death()


def trophy_room():
    """
    This function allows the player to enter the trophy room
    Here, they choose whether to engage with an optional puzzle
    """
    print("Closing the door behind you, you see the room is bare.")
    print("Save the golden trophy set on a pedastal in the centre.")
    print("Do you...")

    print("A: Look around the room.")
    print("B: Run straight up to the trophy and take it. Shiny!")
    print("C: Cautiously approach the trophy.")
    print("D: Go back to the corridor, this seems off.")

    # This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("You peer into each nook and cranny around the room's edge.")
            print("Nothing catches your eye.")
            print("You open the door and peek into the corridor. Nothing.")
            trophy_room()
            break
        elif answer == "b" or answer == "B":
            print("Hurrying to it, you don't notice a tile sink underfoot.")
            print("You ran too fast.")
            print("A mechanism intended to trap you instead cuts you in two.")
            gruesome_death()
            break
        elif answer == "c" or answer == "C":
            print("Keeping an eye out, you approach the trophy.")
            print("A tile depresses under your foot and you stumble forward.")
            print("Rising, you see saws coming out of the walls and floor.")
            print("You're prevented from moving in any direction.")
            trophy_trap()
            break
        elif answer == "d" or answer == "D":
            print("You decide not to risk it and go back to the corridor.")
            corridor()
            break
        else:
            print("Please choose one of the options shown")


def trophy_trap():
    """
    Provides an optional puzzle by asking the player to
    solve a word puzzle formed from rearranged letters in a string
    """
    password = "AVARICIOUS"

    # password_question rearranges the password letters
    # this creates a puzzle for the player
    password_question = "".join(random.sample(password, len(password)))

    print("Starting to panic, you look for a solution.")
    print("You notice a placard has descended from the ceiling.")
    print("It says 'Your greed will be your undoing thief!")
    print("Admit it and decipher my puzzle to be freed! What are you?!'")
    print(f"Beneath the message you see {password_question}")
    print("It must be an anagram!")
    print("Unscramble the letters and find the word to solve it!")

    # This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What do you admit to being? ")).upper()
        if answer == password:
            print("The sawblades retract and you sigh in relief.")
            print("Deciding to leave the trophy, you leave the room.")
            corridor()
            break
        else:
            print("Your wrong answer the question signals to the sawblades.")
            print("They extend on their arms, cutting you to ribbons.")
            gruesome_death()


def saferoom_door():
    print("Your head is on a swivel at this final door.")
    print("The only other room is Holmes' bedroom, so this must be it!")
    print("You try the handle but it won't open.")
    print("Do you...")

    print("A: Try the handle again.")
    print("B: Try to pick the lock.")
    print("C: Ask Mr. Holmes to open it.")
    print("D: Cut and run")

    # This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("It's clearly locked, but keep trying.")
            print("I'm sure it'll open at some stage.")
            saferoom_door()
            break
        elif answer == "b" or answer == "B":
            print("You take your trusty lockpick from your pocket.")
            print("This shouldn't be too difficult...")
            lockpicker()
            break
        elif answer == "c" or answer == "C":
            print("Taking leave of your senses, you bang on the bedroom door.")
            print("A bleary eyed Holmes answers and you ask him for the key.")
            print("He responds by punching you in the face, knocking you out.")
            print("You wake, locked in the wardrobe with police on the scene.")
            game_over()
            break
        elif answer == "d" or answer == "D":
            print("Quitting just before the end. You utter coward.")
            wuss_out()
            break
        else:
            print("Please choose one of the options shown")


def lockpicker():
    """
    This function provides a minigame based on player input
    """
    print("You prepare to pick the lock")
    print("You listen intently for any click to tell you it's opening.")
    print("It looks like a normal 3 pin lock; 3 clicks and it's open.")
    print("Move the pick the wrong way and you'll have to start over.")
    print("Go easy, you only have 1 pick and it's delicate.")
    print("Move it in the wrong direction 3 times and it'll snap.")
    print("Type in the way you wish to move the pick:")
    print("'UP', 'DOWN', 'LEFT' or 'RIGHT' and press ENTER")

    turns_to_break = 3

    pin_one = "UP"
    pin_two = "LEFT"
    pin_three = "RIGHT"

    # This lets the player choose how to move the lockpick to open the door
    # String methods ensure answers of upper or lower case will work
    # On a wrong choice, the player must start again from the beginning
    # If the player answers wrongly 3 times, they lose the game
    while True:
        open_path = (input("How do you move the pick: ")).upper()
        if open_path == pin_one:
            print("Click!")
            open_path_2 = (input("How do you move the pick: ")).upper()
            if open_path_2 == pin_two:
                print("Click!")
                open_path_3 = (input("How do you move the pick: ")).upper()
                if open_path_3 == pin_three:
                    print("Click!")
                    print("Nice! Silently you open the door and slip inside.")
                    last_room()
                    break
                else:
                    print("Clunk! That's not right!")
                    print("You remember the rhyme you made up while training:")
                    print("'Sun up, left the east and headed right on west'")
                    turns_to_break -= 1
                    print(f"{turns_to_break} wrong moves and the pick breaks")
                    if turns_to_break == 0:
                        print("The lockpick snaps in the keyhole.")
                        print("You curse in frustration and kick the door.")
                        print("Turning, you see a furious looking Mr. Holmes.")
                        print("Pointing a gun at you, he calls the police.")
                        game_over()
            else:
                print("Clunk! That's not right!")
                print("You remember the rhyme you made up while training:")
                print("'Sun up, left the east and headed right on west'")
                turns_to_break -= 1
                print(f"{turns_to_break} wrong moves and the pick breaks")
                if turns_to_break == 0:
                    print("The lockpick snaps in the keyhole.")
                    print("You curse in frustration and kick the door.")
                    print("Turning, you see a furious looking Mr. Holmes.")
                    print("Pointing a gun at you, he calls the police.")
                    game_over()
        else:
            print("Clunk! That's not right!")
            print("You remember the rhyme you made up while training:")
            print("'Sun up, left the east and headed right on west'")
            turns_to_break -= 1
            print(f"{turns_to_break} wrong moves and the pick breaks")
            if turns_to_break == 0:
                print("The lockpick snaps in the keyhole.")
                print("You curse in frustration and kick the door.")
                print("Turning, you see a furious looking Mr. Holmes.")
                print("Pointing a gun at you, he calls the police.")
                game_over()


def last_room():
    """
    Player Choices for the last room
    """
    print("Closing the door, you look around the room. It's Holmes' office.")
    print("Remembering casing the house, you take a painting off the wall.")
    print("It reveals a small safe.")
    print("Do you...")

    print("A: Open the safe")
    print("B: Go back to corridor")
    print("C: Cut and run")

    # This while loop lets the player choose how they want to proceed
    while True:
        answer = str(input("What is your choice? "))
        if answer == "a" or answer == "A":
            print("You steady yourself, and decide it's all or nothing.")
            safecracker()
            break
        elif answer == "b" or answer == "B":
            print("You heard a noise and go back to the corridor to check.")
            print("Nothing, but you hear the office door shut behind you.")
            print("It has locked itself, you'll have to reopen it.")
            lockpicker()
            break
        elif answer == "c" or answer == "C":
            print("...\nI mean...just why?")
            wuss_out()
            break
        else:
            print("Please choose one of the options shown")


def safecracker():
    """
    This function is a random number generator.
    The player must guess the safe code to win the final prize
    """
    print("You approach the safe.")
    print("On the front is a keypad showing the numbers 0 - 3.")
    print("You remember from casing the house that the code is 3 digits long.")
    print("The first one is 2.")
    print("If you get any digit wrong you'll have to start again.")
    print("Be careful! You've seen this kind of safe before!")
    print("Don't enter more than 6 wrong numbers!")
    print("That will trip the alarm and the police will be here in minutes!")

    # The numbers variable is a list comprehension of the numbers 0-3
    # It creates a list of those numbers
    numbers = [x for x in range(4)]
    attempts = 6

    known_number = 2

    code = random.sample(numbers, 2)

    # combination creates an empty list
    # The 3 digits of the combination are added to this
    combination = []
    combination.append(known_number)
    combination.extend(code)

    # This lets the player guess the digits of the combination
    # on a wrong choice, the player must start again
    # if the player answers wrongly 6 times, they lose the game
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
                    attempts -= 1
                    print(f"{attempts} attempts remaining")
                if attempts == 0:
                    game_over()
            else:
                print("Wrong, start again")
                attempts -= 1
                print(f"{attempts} attempts remaining")
                if attempts == 0:
                    game_over()
        else:
            print("What are you doing?! You know this one!")
            attempts -= 1
            print(f"{attempts} attempts remaining")
            if attempts == 0:
                game_over()


def game_won():
    """
    Ends the game in a victory state
    """
    print("The safe door swings open.")
    print("Hardly daring to believe, you grasp the prize with trembling hands")
    print("Finally! You can prove that you are the ultimate Word Burglar!")
    print("You hold it up to a shaft of moonlight.")
    print("You can clearly see the ultimate prize:")
    print("Mr. Holmes' Thesaurus!")


def game_over():
    """
    Ends the game in a fail state
    """
    print("Blaring sirens ring in your ears as the police burst in.")
    print("They're responding to reports of suspicious activity.")
    print("They tackle you and cuff your hands behind your back.")
    print("You will be going to prison for a very long time.")
    print("GAME OVER")

    # This lets the player choose whether to restart on a game over
    while True:
        answer = str(input("Would you like to play again? Please type Y/N: "))
        if answer == "y" or answer == "Y":
            intro()
        elif answer == "n" or answer == "N":
            main()
        else:
            print("Please choose one of the options shown")


def gruesome_death():
    """
    This function ends the game if the player dies
    """
    print("You lie on the floor as your blood pools around you.")
    print("You wish you had listened when people said this wasn't worth it.")

    # This lets the player choose whether to restart on a game over
    while True:
        answer = str(input("Would you like to play again? Please type Y/N: "))
        if answer == "y" or answer == "Y":
            intro()
        elif answer == "n" or answer == "N":
            main()
        else:
            print("Please choose one of the options shown")


def wuss_out():
    """
    Runs if the player chooses to end the run voluntarily
    """
    print("Red faced and blinded by tears of humiliation, you slink away.")
    print("Defeated, you know you never had what it took to pull this off.")

    # This lets the player choose whether to restart on a game over
    while True:
        answer = str(input("Would you like to play again? Please type Y/N: "))
        if answer == "y" or answer == "Y":
            intro()
        elif answer == "n" or answer == "N":
            main()
        else:
            print("Please choose one of the options shown")


def main():
    """
    The main function serving as the game's menu
    This allows the player to input their name and start playing
    """
    print("Welcome to Word Burglar.")
    print("In this text-based game you will make choices to pull off a heist.")
    print("Your objective is to find the treasure hidden in the house.")
    print("As you progress, you will be presented with choices in each room.")
    print("Make your choice by typing the corresponding letter, then ENTER")

    # This lets the player input a name
    # Names cannot be longer than 15 characters
    while True:
        name = str(input("To begin, please enter your name: "))
        if len(name) > 15:
            print("You name may be a maximum of 15 characters long.")
            continue
        elif len(name) < 1:
            print("You must enter a name to play.")
        else:
            print(f"Welcome to the game {name}")
            intro()
            break


main()
