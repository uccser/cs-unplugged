{panel type="ct-algorithm"}

# Algorithmic thinking

The step by step process of counting the number of black squares in each row
and identifying whether the parity is even, and then repeating the process
with each column, is an example of an algorithm.
The full error detection algorithm includes what to to do when the error is
found as well.

#### Examples of what you could look for:

Can students reliably find the flipped card in a grid?
Can they articulate the algorithm to another student to help them complete the
task?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

Each of the cards in this activity represents a bit inside a digital device.
When we arrange all of our ‘bits’ together in the square this is a
representation of some data (admittedly random data in the magic trick, but it
could be done with real data!).
This means our grid is an abstraction because it is a model that could be used
to represent any piece of data that can be stored on a digital device, for
example a sound file, a video, or even a piece of code!

#### Examples of what you could look for:

Are students able to explain that each card is a bit and that the cards can
represent data?
Can they see the connection between the grid of cards and a piece of data made
up of bytes?

{panel end}

{panel type="ct-decomposition"}

# Decomposition

To accomplish this task students must decompose the process “find the error”
into smaller steps.
The first step students break it down to could be “look at each row, one by
one, until I find an error”.
Students can break it down further, focusing on one row, and asking themselves
whether the row has an even or odd number of black cards.
They are decomposing the bigger problem down to a subtask, which they can then
work through and move closer to completing the full problem.
Likewise when they need to find the column with an error they can break this
down in the same way, focusing on one column, and asking the same question
above: does the column have an even or odd number of black cards?
These processes are much simpler to solve that the big problem “Find the
error”, but if you work through them all then you will have completely solved
that big problem!

#### Examples of what you could look for:

Are students able to break the task down into steps and describe these steps,
without having to have the algorithm described to them first?

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

Once students understand the algorithm to find the card that has been turned,
they will be able to find a (single) flipped card for any size grid; a 10 x 10
grid (100 cards) can be done fairly quickly, and even a 20 x 20 grid is
possible given enough time (and cards!).
They can generalise the problem “find the error in a **6 x 6 grid**” to:
“find the error in **a grid**”.

#### Examples of what you could look for:

Can students find the flipped card on larger grids?

{panel end}

{panel type="ct-evaluation"}

# Evaluation

The parity trick is always able to detect and correct errors if one bit has
been flipped, but it is important to evaluate this algorithm for different
kinds of errors as well.
If more than one card is flipped (i.e. more than one error occurs) then we can
tell something is wrong with the data, but our algorithm can’t tell us how to
fix this!
Even worse, if more than two bits are flipped then sometimes we might not even
be able to detect the error!
It’s important that we evaluate this algorithm, because if it is going to fail
sometimes we need to know.
Computer Scientists evaluate algorithms like these and improve them when they
find problems with them.

#### Examples of what you could look for:

Ask students “What kind of errors can be detected and corrected with the
parity cards?
At what point can you only detect but not correct and error?
Why is that?”

Can students explain what goes wrong when we try to detect the error if two
cards are flipped?

{panel end}

{panel type="ct-logic"}

# Logic

Flipping a card will always change a row/column from odd to even, no matter
what the card is in what the other cards in the row/column are.

Also, the idea that the corner card is correct for both the new row and column
is an advanced concept, but a pattern that some students might recognise.

#### Examples of what you could look for:

Can students explain why a single card flip always changes the number of black
cards to an odd number?

Can students explain why the corner card will be correct for both the row and
column?
(This involves fairly advanced reasoning).

{panel end}
