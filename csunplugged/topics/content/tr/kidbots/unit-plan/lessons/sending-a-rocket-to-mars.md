# Sending a rocket to Mars

{image file-path="img/topics/unplugged-programming-icon.png" alt="Students standing around a large checkerboard grid." caption="true"}

This example is a starter lesson with an object in the middle. The girl on the white square is 'The Bot', the girl at the back is 'The Programmer' and the boy in the green and gold is 'the Tester'.

{image end}

## Key questions

Why is it important to give very clear instructions? Have you ever been given unclear instructions and ended up doing the wrong thing? Why do you think computers need clear instructions?

## Lesson starter

Ideally this lesson should take place around a large grid such as:

- An outside painted chess board.
- Grids in your classroom carpet.
- Making masking tape grids one the floor in your classroom.
- Draw a chalk grid either in your classroom or outside.

Ask for two volunteers and give yourself and them the roles of:

**Role 1:** The Developer (who writes the program) - The teacher will model this initially

**Role 2:** The Tester (who instructs the Bot and looks for bugs)

**Role 3:** The Bot (who runs the program)

## Lesson activities

{image file-path="img/topics/kidbots-rocket-1.png" alt="8 x 8 grid with a rocket ship at position (1,5) and Mars at position (4,3). Positions are counted from the top left corner."}

Teacher: "I’m going to be the programmer, but I’m going to need your help. We are programming the Bot, not just remote controlling it, because ALL the instructions are written before the Bot can follow those instructions."

"It’s our job to write down clear instructions for the Bot, who is going to be (say the person’s name). (Student's name) will be the Tester and is going to give the instructions to the Bot. The Tester will be on the lookout for bugs."

"First of all we need to decide, what programming language are we are going to use for this? I’ve chosen arrows to represent move forward, turn left and turn right."

"Debugging is fun because you get a chance to change your program after it’s finished when you notice it’s not working how you thought it should."

"First of all I need to decide, what programming language are we are going to use for this? I’ve chosen arrows to represent move forward, turn left and turn right."

{panel type="teaching"}

# Teaching observations

There will be different ways to express the same instructions (such as drawing an arrow, writing "Forward", or using the printed arrows resource above), and the key is that we need to be consistent. The choices about the exact format of the instructions is what leads to different programming languages, and it's fine that this happens, as long as we know the meaning for the particular language we're using at the moment.

{panel end}

If students aren't sure about the left and right direction, you can print the "left and right hand cards", and stick them to their shoes or have them hold them in their hands.

Have the Bot act out the individual instructions: forward means step one square forward, and left and right mean a 90 degree turn on the spot in the square (not moving to another square).

Teacher: "We’re going to write our own program that gets the rocket to fly to Mars. The goal is to get the rocket to the square that Mars is in. Let’s write the first two steps on the board together." (Draw two forward arrows.)

{panel type="teaching"}

# Teaching observations

To work it out students may initially need to see the program in action, so place the arrows within the grid to demonstrate what the rocket will do. It’s also a great technique to write the first few instructions of the code, test it and then add to it. If you are putting arrows on the grid, the turning arrows will also need a forward arrow in the same box, or you can put the forward arrows on the line between boxes, which makes it clearer what it does.

{panel end}

"So let’s try that, and see what happens.

"Tester - could you please take these instructions and pass them onto the Bot. Be ready to underline what doesn’t work when you see the Bot doing something that doesn’t look right, and hand the whiteboard back to me to figure out how to fix the bug."

{panel type="teaching"}

# Teaching observations

A key point in this activity is that the instructions are all written before they are tested. We don't allow anyone to give additional instructions to the Bot; they must follow exactly what is written (which can sometimes be humorous if they head off in the wrong direction.) This is what happens when programming: you write instructions for a program, and when you run the program, they are all executed without the programmer intervening. A programmer needs to visualise what would happen when they are writing the instructions; during testing they will find out if what they envisaged was correct!

{panel end}

Teacher: "Bot - please pick up the rocket ready to receive the instructions for the tester." (The bot can carry a toy or token representing the rocket; or they can imagine that they are guiding it).

Tester then reads off the board: "move forward, move forward."

**Rocket to Mars program:**

{image file-path="img/topics/kidbots-rocket-2.gif" alt="This animation builds upon the previous grid image. The cell with the rocket ship contains an up arrow, and the cell above the rocket contains an up arrow."}

{panel type="teaching"}

# Teaching observations

At this point you could question whether or not a "Stop" instruction is needed. Students should be able to come up with the reasoning that the program stops automatically because there are no more instructions.

{panel end}

"Tester, did the program run as you expected it to?" Depending on the tester's response, if it did then carry on programming, otherwise fix what didn’t work and run that again. In this example the rocket should be in the square three to the left of Mars.

Now let’s add to it. What would we program next?

Point to where the next piece of code needs to be added and add turn right, turn right. (This is deliberately incorrect.)

**Rocket to Mars program:**

{image file-path="img/topics/kidbots-rocket-3.gif" alt="This animation builds upon the previous grid image. The cell two above the rocket ship contains two turn right arrows."}

I think it’s ready to test now. Tester, please test my program (the programmer hands the program on the whiteboard to the tester and the bot should return to the starting square ready to rerun the program).

Teacher: Remember Tester, it’s your job to find any "bugs" in my program. A bug is when my program isn’t doing what was expected. Your job is to draw a line under the piece of code where you notice the instructions seem to be going wrong. You can stop the Bot at the point that you think there is a bug.

**Tester** then reads the instructions in the program off the board and the Bot executes them as they are read.

1. Move forward
2. Move forward
3. Turn right
4. Turn right

{panel type="teaching"}

# Teaching observations

The tester should underline under the second turn right because the rocket will have turned around twice on the spot rather than turning once and going forward again. (Which is what is needed to get to Mars.)

{panel end}

Teacher: "Excellent, you found a bug! I love finding bugs, so I can start solving them. Now class, let’s work through this together to find my bug. Tester, you’ve done a great job finding it, but it’s the programmer’s job to find and fix the bug."

{panel type="teaching"}

# Teaching observations

If the class can’t identify how the program needs debugging then talk through each step and model it with the rocket. Did move forward make sense? Did move forward a second time make sense? Did turn right make sense? What about turn right again? No? Okay I think we found our bug. Let’s draw a line under that and think about what we would change it to? Move forward? Let’s test it.

{panel end}

Once the bug has been identified then ask the Tester to test again. Ask the Bot to pick up the rocket and go back to the start position, then the Tester reads them the instructions.

{image file-path="img/topics/kidbots-rocket-4.gif" alt="This animation builds upon the previous grid image. The cell two above the rocket ship now contains one turn right arrow and one forward arrow. The cell to the right of this cell contains one forward arrow. The cell to the right of this cell (one left of Mars) contains one forward arrow."}

Did we successfully program the rocket to land on Mars? How do we know?

{panel type="teaching"}

# Teaching observations

We successfully programmed the rocket to land on Mars when the rocket and Mars are in the same square.

{panel end}

Are there other ways we could have programmed the rocket to get to Mars? (There will be lots of ways; for example, Right, Forward, Forward, Forward, Left, Forward, Forward will work.) Discuss the programming options and test each one. What if we want the rocket to get to Mars, and then come back safely?

{panel type="teaching"}

# Teaching observations

In programming, there are numerous ways to program the same thing. Some might be more efficient than others, but all are correct if they achieve the desired result. For example a student might program the rocket to go around the outside of the grid and then go and get to Mars. This is a correct solution, but there’s a lot of extra code that’s not necessary. More commonly, two programmers might come up with programs that take a similar amount of time to achieve the same result, in this case (for example, "Forward, Left, Forward, Right" and "Left, Forward, Right, Forward" get the Bot to the same place and orientation; both are equivalent programs; there is rarely a single solution that is the best one, and this means that if a student’s work looks different to a model answer that might be available, it isn’t necessarily wrong. If it achieves the intended outcome, but gets there in a different way it is still correct.

{panel end}

{panel type="teaching"}

# Teaching observations

Either set up your students to be working around the outside of your large grid, or you can use a smaller grid like a chessboard or the back of a 100s board (or print the grid provided with this lesson), in which case the bot moves a counter on the board instead of walking around the grid.

If you have multiple small grids, students can work independently in groups of three (programmer, tester, bot). If you are using a large grid, one group of students can work on their program while another tests theirs. Each group gets to try their program once, and then the next group has a turn while the previous one starts working on debugging their program.

{panel end}

Have the students choose their own two toys (one to be a space travelling object, the other to be the destination) and have them practise this task, as follows.

1. Place the traveller on a square on the edge of the grid, facing inwards.
2. Place the destination toy inside the grid.
3. The programmer writes down the program on a whiteboard.
4. The tester then takes the whiteboard and a different coloured whiteboard pen. The tester tells the Bot each instruction in the program. The tester puts a tick next to the code that is correct and underlines when the code is different to what the Bot should be doing. If this happens the Tester says "Stop" and the Bot stops and goes back to the start. The Tester gives the whiteboard to the Developer, who then debugs the code, and gives the Tester a revised version.
5. Repeat step 4 until the program is free of bugs and works as intended.
6. Change roles and move the Bot (space travelling object) starting point and the toy that represents the destination until everyone has had a turn.

{panel type="teaching"}

# Teaching observations

If you notice that your students need support to visualise how to write the instructions you could use the arrows (cards) provided on the ground, or for a small desktop grid, use a whiteboard marker or small arrows. This supports students to visualise what they want to program.

{panel end}

### The next challenge

Add barriers to the grid so that the path is more complex because the Bot needs to avoid the barriers. This could be space junk and comets, or you could invent a new scenario for the grid.

{image file-path="img/topics/kidbots-rocket-barriers.png" alt="A grid with various cells containing planets, comets, space junk, etc."}

### Other challenges

Have groups program the trip without using the left hand turn (i.e. the only instructions are Forward and Right turn.) Scaffold the students to realise that a left hand turn can be achieved by doing three Right turn instructions. Then challenge them to program with a Left turn but no Right turn.

Ask if they can write programs with only the Right and Left turn instructions (i.e. no Forward instruction)? (This isn't possible, as you would only be able to turn around on one square.)

{panel type="teaching"}

# Teaching observations

Eliminating one of the turn instructions highlights that different instruction sets can achieve the same thing, although some may be more convenient than others (for example, there are many different programming languages, but they can all do essentially the same kind of computation; it's just that some are better suited to some purposes than others.)

Implementing fewer instructions simplifies building a computer, and this can make it either faster or cheaper. For example, a very simple computer might have an addition instruction, but no multiply instruction; but if you need to do multiplication it can be achieved by doing lots of additions. Many common processors these days tend to have a small number of simple instructions (they are called Reduced Instruction Set Computers, or RISC) because it's more efficient than having lots of instructions (Complex Instruction Set Computers, or CISC).

{panel end}

## Applying what we have just learnt

It’s quite common to think that programming is some kind of special talent that people either have or don’t have, but this couldn’t be further from the truth! Like all skills, programming is something you learn through practise, making mistakes, and learning from them. The most important skill that programmers need is to be able to communicate with others, especially when they are finding and describing bugs. Bugs happen all the time in programming, so being able to identify where the bug occurs and problem solving how to fix it is incredibly important. It doesn’t matter how experienced you are at programming, there will always be bugs that need to be found, and fixed. That’s why the word "debugging" is so important to programmers.

## Lesson reflection

Now that you are all programmers, what did you think was the most challenging part of being a programmer?