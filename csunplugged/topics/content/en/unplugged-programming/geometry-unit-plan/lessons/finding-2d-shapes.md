# Finding 2D shapes

## Key questions

Why is it important to give very clear instructions?
Have you ever been given unclear instructions and ended up doing the wrong thing?

## Lesson starter

{panel type="general" title="Notes on resources"}

For the squared grid, this works on painted chess boards, snakes and ladders, or can be marked on the pavement/floor with chalk/tape.
If there isn't space for a large grid, the activity could be done on a small board, such as a chess board, the blank side of 100s boards, or a printed grid.

{panel end}

{image file-path="img/topics/geo-grid.png" caption="This example is a starter lesson with an object in the middle. The girl on the white grid is “The Bot”, the girl at the back is “The Programmer” and the boy in the green and gold is the Tester." alt="Kids standing on and around a grid looking at shapes."}

Ideally this lesson should take place around a large grid such as:

-   An outside painted chess board.
-   Grids in your classroom carpet
-   Making masking tape grids one the floor in your classroom
-   Draw a chalk grid either in your classroom or outside

Ask for two volunteers and give yourself and them the roles of:

**Role 1:** The Developer (who writes the program) - Teacher’s role to model

**Role 2:** The Tester (who instructs the bot and looks for bugs)

**Role 3:** The Bot (who runs the program)

## Lesson activities

{image file-path="img/topics/geo-grid-parrot-1.png" alt="Grid with parrot in (0,1)"}

Teacher: “I’m going to be the programmer, but I’m going to need your help.”
“We are  programming “the Bot”, not just remote controlling it, because ALL the instructions are written before the Bot can follow those instructions.

“Debugging is fun because you get a chance to change your program after it’s finished when you notice it’s not working how you thought it should.”

” It’s my job to write down clear instructions for the Bot, who is going to be (say the person’s name) and “The Tester” (who is...) is going to give the instructions to the Bot and be on the lookout for bugs.”

“First of all I need to decide, what programming language are we are going to use for this?
I’ve chosen arrows to represent move forward, turn left and turn right.”

{panel type="teaching" title="Teaching observations"}

There will be different ways to express the same instructions (such as drawing an arrow, or writing "Forward"), and the key is that we need to be consistent.
The choices about the exact format of the instructions is what leads to different programming languages, and it's fine that this happens, as long as we know the meaning for the particular language we're using at the moment.

{panel end}

If students aren't sure about the left and right direction, you can print the "left and right hand cards", and stick them to their shoes or have them hold them in their hands.

Have the Bot act out the individual instructions: forward means step one square forward, and left and right mean a 90 degree turn on the spot in the square (not moving to another square).

Teacher: “We’re going to write our own program that gets Arnold to find a triangle.
The goal is to get Arnold to the square that the triangle  is in.
Let’s write the first two steps on the board together.”
(Draw two forward arrows.)

{panel type="teaching" title="Teaching observations"}

To work it out students may initially need to see the program in action, so place the arrows within the grid to demonstrate what Arnold will do.
It’s also a great technique to write the first few instructions of the code, test it and then add to it.
If you are putting arrows on the grid, the turning arrows will also need a forward arrow in the same box, or you can put the forward arrows on the line between boxes, which makes it clearer what it does.

{panel end}

“So let’s try that, and see what happens.

Tester - could you please take these instructions and pass them onto the the Bot.
Be ready to underline what doesn’t work when you see the Bot doing something that doesn’t look right and hand the whiteboard back to me to figure out how to fix the bug.

{panel type="teaching" title="Teaching observations"}

A key point in this activity is that the instructions are all written before they are tested.
We don't allow anyone to give additional instructions to the Bot; they must follow exactly what is written (which can sometimes be humorous if they head off in the wrong direction.)
This is what happens when programming: you write instructions for a program, and when you run the program, they are all executed without the programmer intervening.
A programmer needs to visualise what would happen when they are writing the instructions; during testing they will find out if what they envisaged was correct!

{panel end}

Teacher: “Bot - please get ready to receive the instructions for the tester.”
(The bot can carry a toy or token representing Arnold; or they can imagine that they are guiding him).

Tester then reads off the board: “move forward, move forward.”

**2D shapes program:**

<div class="large-text">🡑 🡑 🡑</div>

{image file-path="img/topics/geo-grid-parrot-2.png" alt="Grid with parrot in (0,1) and three right arrows"}

{panel type="teaching" title="Teaching observations"}

At this point you could question whether or not a “Stop” instruction is needed. Students should be able to come up with the reasoning that the program stops automatically because there are no more instructions.

{panel end}

“Tester,  did the program run as you expected it to?"

-  *Depending on the tester's response, if it did then carry on programming, otherwise fix what didn’t work and run that again.
   In this example Arnold should be in the square diagonally below the triangle.*

Now let’s add to it. What would we program next?

Point to where the next piece of code needs to be added and add a move forward and turn left, turn left.

**Arnold program:**

<div class="large-text">🡑 🡑 🡑 ↰ ↰</div>

{image file-path="img/topics/geo-grid-parrot-3.png" alt="Grid with parrot in (0,1) and arrows"}

I think it’s ready to test now.
Tester please test my program (the programmer hands the program on the whiteboard to the tester and the bot should return to the starting square ready to rerun the program).

Teacher:  Remember Tester, it’s your job to find any “bugs” in my program.
A bug is when my program isn’t doing what was expected.
Your job is to draw a line under the piece of code where they notice the instructions seem to be going wrong. You can stop the Bot at the point that you think there is a bug.

**Tester** then reads the instructions in the program off the board and the Bot executes them as they are read.

Move forward

Move forward

Move forward

Turn left

Turn left

{panel type="teaching" title="Teaching observations"}

The tester should underline under the second turn left because Arnold will have turned around twice on the spot rather than turning once and going forward again.
(Which is what is needed to get to the triangle.)

{panel end}

Teacher: “Excellent, you found a bug! I love finding bugs, so I can start solving them.
Now class, let’s work through this together to find my bug.
Tester, you’ve done a great job finding it, but it’s the programmer’s job to find and fix the bug.”

{panel type="teaching" title="Teaching observations"}

If the class can’t identify how the program needs debugging then talk through each step and model it with Arnold.
Did move forward make sense?
Did move forward a second time make sense?
Did move forward a third time make sense? Did turn left make sense?
What about turn left again?
No?
Okay I think we found our bug.
Let’s draw a line under that and think about what we would change it to? Move forward?
Let’s test it.

{panel end}

Once the bug has been identified then ask the Tester to test it again; ask the Bot to pick up Arnold and go back to the start position, then the Tester reads them the instructions.

{image file-path="img/topics/geo-grid-parrot-4.png" alt="Grid with parrot in (0,1) and arrows"}

Did we successfully program Arnold to get to the triangle? How do we know?

{panel type="teaching" title="Teaching observations"}

We successfully programmed Arnold to find the triangle because Arnold and the triangle are in the same square.

{panel end}

Are there other ways we could have programmed Arnold to get to the triangle?
(There will be lots of ways; for example, Left, Forward, Right, Forward, Forward, Forward will work.)
Discuss the programming options and test each one.
What if we want Arnold to get to the triangle, and then bring them back to safety?

{panel type="teaching" title="Teaching observations"}

In programming, there are numerous ways to program the same thing.
Some might be more efficient than others, but all are correct if they achieve the desired result.
For example a student might program Arnold to go around the outside of the grid and then go and get to the triangle.
This is a correct solution, but there’s a lot of extra code that’s not necessary.
More commonly, two programmers might come up with programs that take a similar amount of time to achieve the same result (for example, "Forward, Left, Forward, Right" and "Left, Forward, Right, Forward" get the Bot to the same place and orientation; both are good answers).
An important concept in programming is that there can be multiple good answers; there is rarely a single solution that is the best one, and this means that if a student's work looks different to a model answer that might be available, it isn't necessarily wrong.
If it achieves the intended outcome, but gets there in a different way it is still correct.

{panel end}

{panel type="teaching" title="Teaching observations"}

Either set up your students to be working around the outside of your large grid, or you can use a smaller grid like a chessboard or the back of a 100s board (or print the one provided with this lesson), in which case the Bot moves a counter on the board instead of walking around the grid.

If you have multiple small grids, students can work independently in groups of three (Programmer, Tester, Bot).
If you are using a large grid, one group of students can work on their program while another tests theirs.
Each group gets to try their program once, and then the next group has a turn while the previous one starts working on debugging their program.

{panel end}

Have the students choose their own 2D shapes and a toy to program to find the shapes.

1.  Place the toy on a square on the edge of the grid, facing inwards.

2.  Place the 2D shapes inside the grid.

3.  The Tester says a shape for the toy to be programmed to go to.

3.  The Programmer writes down the program on a whiteboard.

4.  The Tester then takes the whiteboard and a different coloured whiteboard pen.
    The Tester tells the Bot each instruction in the program.
    The Tester puts a tick next to the code that is correct and underlines when the code is different to what the Bot should be doing.
    If this happens the Tester says “Stop” and the Bot stops and goes back to the start.
    The Tester gives the whiteboard to the Programmer, who then debugs the code, and gives the Tester a revised version.

5.  Repeat step 6 until the program is free of bugs and works as intended.

6.  Change roles and move the Bot toy and the 2D shapes until everyone has had a turn.

{panel type="teaching" title="Teaching observations"}

If you notice that your students need support to visualise how to write the instructions you could use a whiteboard pen to scaffold the instructions, or the arrows provided.
This supports students to visualise what they want to program.

{panel end}

## The next challenge:

Add barriers to the grid so that the path is more complex because it needs to avoid the barriers.
This could be blocks blocking the way.

{image file-path="img/topics/geo-grid-parrot-5.png" alt="Grid with parrot in (0,1) and barriers"}

## Other challenges:

Have groups program the rescue without using the left hand turn (i.e. the only instructions are forward and right turn.)
Scaffold the students to realise that a left hand turn can be achieved by doing three right turn instructions.
Then challenge them to program with a Left turn but no right turn.

Ask if they can write programs with only the right and left turn instructions (i.e. no forward instruction)?
(This isn't possible, as you would only be able to turn around on one square.)

{panel type="teaching" title="Teaching observations"}

Eliminating one of the turn instructions highlights that different instruction sets can achieve the same thing, although some may be more convenient than others (for example, there are many different programming languages, but they can all do essentially the same kind of computation; it's just that some are better suited to some purposes than others.)

Implementing fewer instructions simplifies building a computer, and this can make it either faster or cheaper.
For example, a very simple computer might have an addition instruction, but no multiply instruction; but if you need to do multiplication it can be achieved by doing lots of additions.
Many common processors these days tend to have a small number of simple instructions (they are called Reduced Instruction Set Computers, or RISC) because it's more efficient than having lots of instructions (Complex Instruction Set Computers, or CISC).

{panel end}

## Applying what we have just learnt

It’s quite common to think that programming is some kind of special talent that people either have or don’t have, but this isn't so!
Like all skills, programming is something you learn through practise, making mistakes, and learning from them.
An important skill that programmers need is to be able to communicate with others, especially when they are working out what the program should do; they also need to be persistent when finding and fixing bugs.
Bugs happen all the time in programming, so being able to identify where the bug occurs and problem solving how to fix it is incredibly important.
It doesn’t matter how experienced you are at programming, there will always be bugs that need to be found, and fixed.
That’s why the word “debugging” is so important to programmers.

## 2D programming challenges

Simple robotic toys like the "Bee-Bot" have a very similar set of commands, and can be used to follow up.

## Lesson reflection

Who are the students who can visualise what needs to be programmed?
