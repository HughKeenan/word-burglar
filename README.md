Bugs

The function to implement the game over initially did not work
A bug arose with the function to show choices for the first room where the wrong choice still progressed the game. Re examination of the code revealed that the if statement has been phrased wrongly, changing it resolved the issue. 

A bug arose also with the possibility of the player attempting to input a choice that doesn't represent one of the options, as this could create a dead end. Nesting the choices inside a while loop resolved the issue

Fixes:
If statement:
https://www.reddit.com/r/learnpython/comments/u9ts2r/python_ignoring_my_elif_statement/

Invalid choices
https://stackoverflow.com/questions/64070816/how-to-restart-a-loop-if-the-input-is-wrong