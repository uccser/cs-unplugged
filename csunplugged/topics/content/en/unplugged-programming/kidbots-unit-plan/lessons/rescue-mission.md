# Rescue Mission (Sequential programming)

{image file-path="img/topics/unplugged-programming-icon.png" alt="Students standing around a large checkerboard grid." caption="This example is a starter lesson with an object in the middle. The girl on the white square is “The Bot”, the girl at the back is “The Programmer” and the boy in the green and gold is the Tester."}

## Key questions

Why is it important to give very clear instructions?
Have you ever been given unclear instructions and ended up doing the wrong thing?

## Lesson starter

Ideally this lesson should take place around a large grid such as:

-   An outside painted chess board.
-   Grids in your classroom carpet.
-   Making masking tape grids one the floor in your classroom.
-   Draw a chalk grid either in your classroom or outside.

Ask for two volunteers and give yourself and them the roles of:

**Role 1:** The Developer (who writes the program) -  The teacher will model this initially.

**Role 2:** The Tester (who instructs the Bot and looks for bugs).

**Role 3:** The Bot (who runs the program).

## Lesson activities

{image file-path="img/topics/kidbots-little-red-riding-hood-1.png" alt="8 x 8 grid with Grandma's house at position (4,2) and Little Red Riding Hood at position (1,3). Positions are counted from the top left corner, left then down, starting at 1."}

Teacher: “I’m going to be the programmer, but I’m going to need your help.”
“We are  programming “the Bot”, not just remote controlling it, because ALL the instructions are written before the Bot can follow those instructions.

“Debugging is fun because you get a chance to change your program after it’s finished when you notice it’s not working how you thought it should.”

”It’s my job to write down clear instructions for the Bot, who is going to be (say the person’s name) and “The Tester” (who is...) is going to give the instructions to the Bot and be on the lookout for bugs.”

“First of all I need to decide, what programming language are we are going to use for this? I’ve chosen arrows to represent move forward, turn left and turn right.”

{panel type="teaching" title="Teaching observations"}

There will be different ways to express the same instructions (such as drawing an arrow, or writing "Forward"), and the key is that we need to be consistent.
The choices about the exact format of the instructions is what leads to different programming languages, and it's fine that this happens, as long as we know the meaning for the particular language we're using at the moment.

{panel end}

If students aren't sure about the left and right direction, you can print the "left and right hand cards", and stick them to their shoes or have them hold them in their hands.

Have the Bot act out the individual instructions: forward means step one square forward, and left and right mean a 90 degree turn on the spot in the square (not moving to another square).

Teacher: “We’re going to write our own program that gets the Little Red Riding Hood to rescue her Grandma.
The goal is to get Little Red Riding Hood to the square that Grandma is in.
Let’s write the first two steps on the board together.”
(Draw two forward arrows.)

{panel type="teaching" title="Teaching observations"}

To work it out students may initially need to see the program in action, so place the arrows within the grid to demonstrate what the Little Red Riding Hood will do.
It’s also a great technique to write the first few instructions of the code, test it and then add to it.
If you are putting arrows on the grid, the turning arrows will also need a forward arrow in the same box, or you can put the forward arrows on the line between boxes, which makes it clearer what it does.

{panel end}

“So let’s try that, and see what happens.

"Tester - could you please take these instructions and pass them onto the the Bot.
Be ready to underline what doesn’t work when you see the Bot doing something that doesn’t look right, and hand the whiteboard back to me to figure out how to fix the bug. "

{panel type="teaching" title="Teaching observations"}

A key point in this activity is that the instructions are all written *before* they are tested.
We don't allow anyone to give additional instructions to the Bot; they must follow exactly what is written (which can sometimes be humorous if they head off in the wrong direction.)
This is what happens when programming: you write instructions for a program, and when you run the program, they are all executed without the programmer intervening.
A programmer needs to visualise what would happen when they are writing the instructions; during testing they will find out if what they envisaged was correct!

{panel end}

Teacher: “Bot - please pick up Little Red Riding Hood ready to receive the instructions for the tester.”
(The bot can carry a toy or token representing Little Red Riding Hood; or they can imagine that they are guiding her).

Tester then reads off the board: “move forward, move forward.”

**Little Red Riding Hood program:**

<div class="large-text">🡑 🡑</div>
