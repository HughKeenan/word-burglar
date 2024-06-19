Bugs

The function to implement the game over initially did not work
A bug arose with the function to show choices for the first room where the wrong choice still progressed the game. Re examination of the code revealed that the if statement has been phrased wrongly, changing it resolved the issue. 

A bug arose also with the possibility of the player attempting to input a choice that doesn't represent one of the options, as this could create a dead end. Nesting the choices inside a while loop resolved the issue

The function to call game over initially resulted in a dead end, this was fixed by implementing user input to allow the player to return to the intro screen or restart the game

A bug arose with a list of strings, attempting to index it created an error saying the index was out of range. Re-examination of the code revealed that the list entries had all been set between a single set of quotation marks, meaning the list only had one entry, and nothing beyond that could be accessed 

The lockpicker function when first written displayed the prompt to move the lockpick twice for the second and third prompts.

The function to generate the safe combination initially would not work, 

Fixes:
If statement:
https://www.reddit.com/r/learnpython/comments/u9ts2r/python_ignoring_my_elif_statement/

Invalid choices
https://stackoverflow.com/questions/64070816/how-to-restart-a-loop-if-the-input-is-wrong

Word scramble:
https://www.youtube.com/watch?v=vtjLxNU6eyk

safecracker:
https://www.reddit.com/r/learnpython/comments/1aeofpv/crack_the_safe_code/