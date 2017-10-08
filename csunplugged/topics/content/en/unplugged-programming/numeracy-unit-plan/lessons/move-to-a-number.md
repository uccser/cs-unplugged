# Move to a number

{image file-path="img/topics/kidbots-numeracy.png" alt="Students standing around a large checkerboard grid." caption="This example is a starter lesson with an object in the middle. The girl on the white square is "The Bot", the girl at the back is "The Programmer" and the boy in the green and gold is the Tester."}

## Key questions

Why is it important to give very clear instructions?
Have you ever been given unclear instructions and ended up doing the wrong thing?

## Lesson starter

Ideally this lesson should take place around a large grid such as:

-   An outside painted chess board.
-   Grids in your classroom carpet.
-   Masking tape grids on the floor in your classroom.
-   Chalk grid either in your classroom or outside.

Ask for two volunteers and give yourself and them the roles of:

1.  The Developer (who writes the program) - Teacher’s role to model.
2.  The Tester (who instructs the bot and looks for bugs).
3.  The Bot (who runs the program).

## Lesson activity

{image file-path="img/topics/kidbots-numeracy-plane-1.png" alt="8 x 8 grid with various objects across the grid including, ladybugs, different numbers, a plane, and squares with different numbers of dots."}

Teacher: "I’m going to be the programmer, but I’m going to need your help."
"We are  programming "the Bot", not just remote controlling it, because ALL the instructions are written before the Bot can follow those instructions.

"Debugging is fun because you get a chance to change your program after it’s finished when you notice it’s not working how you thought it should."

"It’s my job to write down clear instructions for the Bot, who is going to be (say the person’s name) and "The Tester" (who is...) is going to give the instructions to the Bot and be on the lookout for bugs."

"First of all I need to decide, what programming language are we are going to use for this? I’ve chosen arrows to represent move forward, turn left and turn right."

{panel type="teaching" title="Teaching observations"}

There will be different ways to express the same instructions (such as drawing an arrow, or writing "Forward"), and the key is that we need to be consistent.
The choices about the exact format of the instructions is what leads to different programming languages, and it's fine that this happens, as long as we know the meaning for the particular language we're using at the moment.

Of course, you can place all sorts of numbers on the squares according to the level the students are able to work with.

{panel end}

If students aren't sure about the left and right direction, you can print the "left and right hand cards", and stick them to their shoes or have them hold them in their hands.

Have the Bot act out the individual instructions: forward means step one square forward, and left and right mean a 90 degree turn on the spot in the square (not moving to another square).
When drawing arrows for turning it will pay to use a curved arrow to show the direction of the turn, rather than a straight arrow, which might also mean "move forward".

Teacher: "We’re going to write our own program that gets the bot (represented by the plane on the diagram above) to find 5 counters in one square.
Let’s write the first two steps on the board together."
(Draw two forward arrows.)

{panel type="teaching" title="Teaching observations"}

To work it out students may initially need to see the program in action, so place the arrows within the grid to demonstrate what the plane will do.
It’s also a great technique to write the first few instructions of the code, test it and then add to it.
If you are putting arrows on the grid, the turning arrows will also need a forward arrow in the same box, or you can put the forward arrows on the line between boxes, which makes it clearer what it does.

{panel end}

"So let’s try that, and see what happens."

"Tester - could you please take these instructions and pass them onto the the Bot.
Be ready to underline what doesn’t work when you see the Bot doing something that doesn’t look right and hand the whiteboard back to me to figure out how to fix the bug."

{panel type="teaching" title="Teaching observations"}

A key point in this activity is that the instructions are all written *before* they are tested.
We don't allow anyone to give additional instructions to the Bot; they must follow exactly what is written (which can sometimes be humorous if they head off in the wrong direction).
This is what happens when programming: you write instructions for a program, and when you run the program, they are all executed without the programmer intervening.
A programmer needs to visualise what would happen when they are writing the instructions; during testing they will find out if what they envisaged was correct!

{panel end}

Teacher: "Bot - please get ready to receive the instructions for the tester"
(The bot can carry a toy or token representing the plane; or they can imagine that they are flying the plane).

Tester then reads off the board: "move forward, move forward".

{image file-path="img/topics/kidbots-numeracy-plane-2.gif" alt="This animation shows the plane following two forward commands."}

{panel type="teaching" title="Teaching observations"}

At this point you could question whether or not a "Stop" instruction is needed.
Students should be able to come up with the reasoning that the program stops automatically because there are no more instructions.

{panel end}

"Tester, did the program run as you expected it to?"

Depending on the tester's response, if it did then carry on programming, otherwise fix what didn’t work and run that again.
In this example the plane should be in the square diagonally below the 5 counters square.

Now let’s add to it.
What would we program next?

Point to where the next piece of code needs to be added and add turn left, turn left (this is deliberately incorrect).

{image file-path="img/topics/kidbots-numeracy-plane-3.gif" alt="This animation shows the plane following two forward commands, then two turn left commands."}

Teacher: "I think it’s ready to test now.
Tester, please test my program (the programmer hands the program on the whiteboard to the tester and the bot should return to the starting square ready to rerun the program)"

"Remember Tester, it’s your job to find any "bugs" in my program.
A bug is when my program isn’t doing what was expected.
Your job is to draw a line under the piece of code where they notice the instructions seem to be going wrong.
You can stop the Bot at the point that you think there is a bug."

**Tester** then reads the instructions in the program off the board and the Bot executes them as they are read.

1.  Move forward
2.  Move forward
3.  Turn left
4.  Turn left

{panel type="teaching" title="Teaching observations"}

The tester should underline under the second turn left because the place will have turned around twice on the spot rather than turning once and going forward again (which is what is needed to get to the square with the 5 counters in it).

{panel end}

Teacher: "Excellent, you found a bug!
I love finding bugs, so I can start solving them.
Now class, let’s work through this together to find my bug.
Tester, you’ve done a great job finding it, but it’s the programmer’s job to find and fix the bug."

{panel type="teaching" title="Teaching observations"}

If the class can’t identify how the program needs debugging then talk through each step and model it with the rocket.
Did move forward make sense?
Did move forward a second time make sense?
Did turn left make sense?
What about turn left again?
No?
Okay I think we found our bug.
Let’s draw a line under that and think about what we would change it to?
Move forward?
Let’s test it.

{panel end}

Once the bug has been identified then ask the Tester to test it again; ask the Bot to pick up the plane and go back to the start position, then the Tester reads them the instructions.

{image file-path="img/topics/kidbots-numeracy-plane-4.gif" alt="This animation shows the plane following commands: move forward, move forward, turn left, move forward, turn right, move forward. It finishes on top of the square with the 5 counters."}

Did we successfully program the plane to the square with 5 counters in it?
How do we know?

{panel type="teaching" title="Teaching observations"}

We successfully programmed the plane to the 5 counters because they are in the same square.

{panel end}

Are there other ways we could have programmed the plane to get to the five counters?
(There will be lots of ways; for example, turn left, move forward, turn right, move forward, move forward, move forward will work.)
Discuss the programming options and test each one.
What if we want the plane to get to the counters, and then bring them back to the start?

{panel type="teaching" title="Teaching observations"}

In programming, there are numerous ways to program the same thing.
Some might be more efficient than others, but all are correct if they achieve the desired result.
For example a student might program the plane to go around the outside of the grid and then go and get to the target square.
This is a correct solution, but there’s a lot of extra code that’s not necessary.
More commonly, two programmers might come up with programs that take a similar amount of time to achieve the same result  (for example, "Forward, Left, Forward, Right" and "Left, Forward, Right, Forward" get the Bot to the same place and orientation; both are good answers).
An important concept in programming is that there can be multiple good answers; there is rarely a single solution that is the best one, and this means that if a student's work looks different to a model answer that might be available, it isn't necessarily wrong.
If it achieves the intended outcome, but gets there in a different way it is still correct.

{panel end}

{panel type="teaching" title="Teaching observations"}

Either set up your students to be working around the outside of your large grid, or you can use a smaller grid like a chessboard or the back of a 100s board (or print the one provided with this lesson), in which case the Bot moves a counter on the board instead of walking around the grid.

If you have multiple small grids, students can work independently in groups of three (Programmer, Tester, Bot).
If you are using a large grid, one group of students can work on their program while another tests theirs.
Each group gets to try their program once, and then the next group has a turn while the previous one starts working on debugging their program.

{panel end}

Have the students choose their own ways to represent numbers and a toy to program to find the numbers.

1.  Place the toy on a square on the edge of the grid, facing inwards.
2.  Place the numbers inside the grid.
3.  The Tester says a number for the toy to be programmed to go to.
3.  The Programmer writes down the program on a whiteboard.
4.  The Tester then takes the whiteboard and a different coloured whiteboard pen.
    The Tester tells the Bot each instruction in the program.
    The Tester puts a tick next to the code that is correct and underlines when the code is different to what the Bot should be doing.
    If this happens the Tester says “Stop” and the Bot stops and goes back to the start.
    The Tester gives the whiteboard to the Programmer, who then debugs the code, and gives the Tester a revised version.
5.  Repeat step 6 until the program is free of bugs and works as intended.
6.  Change roles and move the Bot toy and the numbers until everyone has had a turn.

{panel type="teaching" title="Teaching observations"}

If you notice that your students need support to visualise how to write the instructions you could use a whiteboard pen to scaffold the instructions.
Or the arrows provided.
This supports students to visualise what they want to program.

{panel end}

### The next challenge

Program the plane to make 6 by having him move first to the number 3 and then to the ladybird with 3 dots.

{image file-path="img/topics/kidbots-numeracy-plane-1.png" alt="8 x 8 grid with various objects across the grid including, ladybugs, different numbers, a plane, and squares with different numbers of dots."}

### Other challenges

Have groups program getting to a number without using the left hand turn (i.e. the only instructions are forward and right turn).
Scaffold the students to realise that a left hand turn can be achieved by doing three right turn instructions.
Then challenge them to program with a left turn but no right turn.

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
That’s why the word "debugging" is so important to programmers.

### 2D programming challenges

Simple robotic toys like the "Bee-Bot" have a very similar set of commands, and can be used to follow up.

## Lesson reflection

Who are the students who can visualise what needs to be programmed?
