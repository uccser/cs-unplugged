Remix the program provided at <https://scratch.mit.edu/projects/159722851/> and change its name to: **KidBots challenge 1.1 Design a Bee-Bot.**

When the green flag is clicked your program should do the following:

- The “cat” sprite; 
    - moves to the position x:50, y:0 on the stage.
    - point in position 90 degrees.
    - clear all the items in the “source code” list.
- The "mouse" sprite; 
    - moves to a random position on the grid. As each tile in the grid is 50x50 steps, to move the “mouse” sprite to a random position in the centre of a tile use this block: `scratch:go to x:((pick random (-1) to (4)) * (50)) y:((pick random (-3) to (3)) * (50))`

Program the buttons on your Bee-Bot to do the following:

- **Forward**: Adds the statement “forward” to the “source code” list.
- **Backward**: Adds the statement “backward” to the “source code” list.
- **Right**: Adds the statement “turn right” to the “source code” list.
- **Left**: Adds the statement “turn left” to the “source code” list.
- **Pause**: Adds the statement “pause” to the “source code” list.
- **Undo**: Removes the last item from the “source code” list.
- **Clear**: Removes all the items in the “source code” list.
- **Home**: Moves the “cat” sprite to position x:50, y:0 on the stage.
- **Go**: Executes all the statements in the “source code” list following below algorithm:
    
    - If the item in the list is “forward”; 
        - If the “cat” sprite touching the “border” sprite; 
            - Display a message “Oh no! Missed it! Press "home" and then "clear" to try again” for 2 secs. Stop all scripts in all sprites.
        - Else 
            - Move the “cat” sprite 50 steps.
    - If the item in the list is “backward”; 
        - If the “cat” sprite touching the “border” sprite; 
            - Display a message “Oh no! Missed it! Press "home" and then "clear" to try again” for 2 secs. Stop all scripts in all sprites.
        - Else 
            - Move the “cat” sprite -50 steps.
    - If the item in the list is “turn right”; 
        - Turn the “cat” sprite 90 degrees to the right.
    - If the item in the list is “turn left”; 
        - Turn the “cat” sprite 90 degrees to the left.
    - If the item in the list is “pause”; 
        - Wait 5 seconds.
    
    When the “go” button is pressed and the “cat” stops (i.e. after all the statements in the “source code” list are executed), check if the “cat” sprite is touching the “mouse” sprite (use the TOUCHING block under the “Sensing” script);
    
    - If it is; 
        - display the message “Gotcha!” for 2 secs.
        - Play a meow sound by using the PLAY SOUND “meow” block under the “Sound” script. To add a sound, click the “Sounds” tab and choose sound from library. Select the sound you wish to add and press “ok”.
    - If it’s not; 
        - Display a message “Oh no! Missed it! Press "home" and then "clear" to try again”.