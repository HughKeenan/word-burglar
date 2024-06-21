Bugs

The function to implement the game over initially did not work
A bug arose with the function to show choices for the first room where the wrong choice still progressed the game. Re examination of the code revealed that the if statement has been phrased wrongly, changing it resolved the issue. 

A bug arose also with the possibility of the player attempting to input a choice that doesn't represent one of the options, as this could create a dead end. Nesting the choices inside a while loop resolved the issue

The function to call game over initially resulted in a dead end, this was fixed by implementing user input to allow the player to return to the intro screen or restart the game

A bug arose with a list of strings, attempting to index it created an error saying the index was out of range. Re-examination of the code revealed that the list entries had all been set between a single set of quotation marks, meaning the list only had one entry, and nothing beyond that could be accessed 

The lockpicker function when first written displayed the prompt to move the lockpick twice for the second and third prompts. This was due to incorrect placement of print commands within the nested if statements.

To prevent the player from using names that are too long, a limit of 15 characters was placed on it. Initially after implementing this, an inifinite loop ran if a sequence that was too long was entered. This was resolved by nesting the name input within the while loop validating the input and using a continue statement on incorrect input.

Where user input was required to be longer than one character, it was initially case sensitive, and any answer other than one exactly matching the variable resulted in a fail outcome. This was fixed by using string methods to change the input case to match the variable.

a bug arose in that some functions continued to run after the game had ended, and the player could enter a choice when they should not be able to. Re-examination of the code revealed that break statements had not been entered in every place they were required. Once this was done, the issue was fixed.

The player was initially able to begin the game by putting in an empty space as their name. To prevent this, the strip method was added to the name input.

Submitting an empty entry or a letter into safecracker initially caused the game to crash. This was solved by nesting the inputs within a try except statement to check for value errors. A similar issue happened with lockpicker. The code was refactored to work along the same lines as safecracker, which resolved the issue

Fixes:
If statement:
https://www.reddit.com/r/learnpython/comments/u9ts2r/python_ignoring_my_elif_statement/

Invalid choices
https://stackoverflow.com/questions/64070816/how-to-restart-a-loop-if-the-input-is-wrong

Word scramble:
https://www.youtube.com/watch?v=vtjLxNU6eyk

safecracker:
https://www.reddit.com/r/learnpython/comments/1aeofpv/crack_the_safe_code/

strip:
https://teamtreehouse.com/community/how-do-you-prevent-an-empty-input-field-being-added-to-my-todo-list