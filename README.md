# WELCOME TO MACGYVER MAZE GAME !

**THE GAME**  
You are MacGyver, trapped in a maze. The exit is watched by a gard. To escape, you must first pick up 3 objects in the maze: a needle, a small tube and some ether. With them, you'll make a syringe to drug the guard and run away. But if you try to escape without the syringe, the guard will kill you !

**HOW TO PLAY**  
Move MacGyver with the direction keys: up, down, left, right.  
To pick up the objects, simply put MacGyver on their place.  
The 3 objects will automatically transform into a syringe once you have picked up all of them.  
Once you have the syringe, all you have to do is rush to the exit.

**SETUP**  
Todo

**CONFIG**  
The maze pattern is in the pattern.txt file and can be modified.  
It is a 15 x 15 structure, in which each cell is represented by a specific character:  
" W " (uppercase) for a piece of wall  
" _ " (key 8 of the keyboard) for a piece of corridor  
" : " for the exit.

*About the exit, please note:*

- the maze must be entirely closed with walls, except for one, and only one, exit.
- DO NOT locate the exit in a corner, since MacGyver cannot move diagonally.

Here is an example of how to represent a small structure of 3 x 3 cells, the exit is in the east wall(depending on the font, the maze may seem to be not square-shaped):  
WWW  
W_:  
WWW
