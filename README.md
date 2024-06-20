Bugs

The function to implement the game over initially did not work
A bug arose with the function to show choices for the first room where the wrong choice still progressed the game. Re examination of the code revealed that the if statement has been phrased wrongly, changing it resolved the issue. 

A bug arose also with the possibility of the player attempting to input a choice that doesn't represent one of the options, as this could create a dead end. Nesting the choices inside a while loop resolved the issue

The function to call game over initially resulted in a dead end, this was fixed by implementing user input to allow the player to return to the intro screen or restart the game

A bug arose with a list of strings, attempting to index it created an error saying the index was out of range. Re-examination of the code revealed that the list entries had all been set between a single set of quotation marks, meaning the list only had one entry, and nothing beyond that could be accessed 

The lockpicker function when first written displayed the prompt to move the lockpick twice for the second and third prompts. This was due to incorrect placement of print commands within the nested if statements.

To prevent the player from using names that are too long, a limit of 15 characters was placed on it. Initially after implementing this, an inifinite loop ran if a sequence that was too long was entered. This was resolved by nesting the name input within the while loop validating the input and using a continue statement on incorrect input.

Where user input was required to be longer than one character, it was initially case sensitive, and any answer other than one exactly matching the variable resulted in a fail outcome. This was fixed by using string methods to change the input case to match the variable.

The function to generate the safe combination initially would not work,

a bug arose in that the last_room function continued to run after the game had ended, and the player could enter a choice when they should not be able to

Fixes:
If statement:
https://www.reddit.com/r/learnpython/comments/u9ts2r/python_ignoring_my_elif_statement/

Invalid choices
https://stackoverflow.com/questions/64070816/how-to-restart-a-loop-if-the-input-is-wrong

Word scramble:
https://www.youtube.com/watch?v=vtjLxNU6eyk

safecracker:
https://www.reddit.com/r/learnpython/comments/1aeofpv/crack_the_safe_code/