# Parity magic

## Key questions

-   Why is it important for computers to be able to detect if the data received
    over the internet is the same as the data that was sent?
-   What if I sent you an email that said you could now have Monday off school,
    but when you received it, there was some electrical interference and a
    **bit** was changed from off to on so that the word "now" became "not".
    What would your reaction be?
-   Can computers correct these sorts of mistakes automatically, and how would
    they do that?

### Potential answers could include:

Students may come up with situations where computers won't read a disc or scan a code, but they may also confuse this kind of problem with other kinds of failures such as an error in a program or a flat battery.

{image file-path="img/topics/school-test-error.png" alt="A school test shows every question marked correct but the overall score is 0%."}

Adults use computers for important things like banking, writing school reports, and communicating with each other.
If the information being stored got changed without anyone knowing, you'd get the wrong balance in your account (too much or too little), the wrong grade in your report, or the wrong message in an email.
Or worst still the website you are wanting to go to for your learning or the DVD you want to play won’t work!
This activity will look at how computers correct this automatically.

## Lesson starter

{panel type="video"}

# See teaching this in action

{video url="https://vimeo.com/437726658"}

{panel end}

{panel type="general"}

# Notes on resources

{image file-path="img/topics/parity-cards.png" alt="A pile of square cards with black on one side and white on the other side."}

You will require:

-   A set of 36 "fridge magnet" cards, all identical with a different colour on
    each side (e.g. black and white); or non-magnetic cards, in which case the
    demonstration should be done on a table-top or the floor.
    The magnetic ones would need to be magnetic both ways up; sheets of
    double-sided magnetic material can be purchased, but conventional fridge
    magnets usually won't stick upside down.
    Double sided magnetic cards can also be made by sticking single-sided
    magnetic sheet back to back.
    Paper (non-magnetic) cards can be made by cutting up a sheet of light card
    that is a different colour on each side.
-   A metal board (ideally a whiteboard) if magnetic cards are being used.
-   Each pair of children will need: a set of 36 (non-magnetic) cards as above.

There is also an
[online interactive version of the parity cards here](http://csfieldguide.org.nz/en/interactives/parity/index.html),
from the Computer Science Field Guide.

{panel end}

1.  Teacher to class: "I’ve just learnt a magic trick I want to show you".

2.  Teacher to class: "So who will be my assistant?"

3.  Teacher to student: Hand the cards to the student and ask them to make a
    grid of 5 by 5 cards (calling it "5 rows of 5 cards might be clearer for
    younger students").
    "Don't make any patterns - try to make it as random as possible".
    To speed up the setup you could have two students do this task; encourage
    them to leave a small gap between the cards, and not be too fussy about
    making them straight.

4.  Point out that the cards represent bits (binary digits).
    If they haven't studied binary numbers, you may need to just point out that
    this is the way everything is represented on computers - the cards here
    could represent a file, a message, a web page or even a program.

5.  Teacher to class: "I’m going to make this a little bit harder by adding
    another row and another column".

{panel type="teaching"}

# Teaching observations

Of course, you are doing this on purpose because what you want to do is make
sure that the number of black sides showing in each row and column is an even
number.
This is always possible; if the student put an odd number of black cards in a
row, you add another black card to the row; if they put an even number in the
row, add a white card, to keep it as an even number.
Remember that zero is an even number.

The extra cards are called "parity bits" (or parity cards), but there's no
need to introduce the terminology yet, since that reveals the "magic"; for the
meantime the idea is for the class to think that you are just adding even more
random cards to make the task harder.

You should practise this several times before doing it in front of the class,
as it becomes a lot easier to make it look casual when you've done it before,
and makes the trick more mysterious.

{panel end}

{image file-path="img/topics/parity-cards-6x6-grid-step-1.png" alt="5 rows of 5 parity cards in a random arrangement." caption="true"}

Step 1: Example layout of a 5x5 grid set up by the volunteer.

{image end}

### Step by step adding a parity bit to each row and column

{image file-path="img/topics/parity-cards.gif" alt="An animation of adding a parity bit to each row and column."}

The last parity bit placed is useful because it will always work for both the
column and row; if it doesn't match for both the row and column then you'll
have made a mistake with one of the cards, and should go back and check them
(try to not make it obvious that you're doing that).

{panel type="teaching"}

# Teaching observations

Now you have added parity cards to make the number of black squares in every
row and every column equal to an even number.
Don't point this out to the students at this stage.

{panel end}

## Lesson activities

Teacher to student: "I'd like you flip over one card while I cover my eyes".

Teacher to class: "Keep a close eye on which card it is to check if I have done
my magic trick correctly!"

{panel type="teaching"}

# Teaching observations

You need to emphasise that you want just one card flipped over.
This prevents them from turning over too many cards (or none!).
Usually students will follow this instruction, and their classmates will be
able to confirm to you that, or let you know if one hasn't been turned over
yet.

{panel end}

After the class confirms that a single card has been flipped, turn around to
look at the cards.
Scan the cards looking for the row with an odd number of black squares, and the
column that has an odd number of black squares.
The card that has been flipped will be at the intersection of these two lines.
Turn this card over casually to restore it to the correct colour, saying “it’s
this one”.

You can make a fuss that it might have been a fluke, so repeat the trick again.
(After you put the card back to how it was originally, look away again and ask
for another card to be flipped over.)

{image file-path="img/topics/parity-wizard.png" alt="A wizard holding a magic wand with parity cards on it." alignment="right"}

So is it magic? Or is it a trick?

Teacher to class: "Let’s first look at the cards before one was turned over"
(make sure you've restored the card that was just flipped).
The following steps will help the students to uncover what you've done:

-   "Are there any patterns you can see? Think, pair, share".
-   "Let’s break it down into parts".
-   "Let’s look at the first row - count the black squares - how many are
    there?" 4 (in the example above).
-   "Now the second row - count the black squares - how many are there?" 2.
-   Note that it could be a row of all white squares - which would be 0 black
    squares; or it could be a row of all black squares - 6.

Teacher to class: “What do these numbers have in common?”.
Students should be able to observe that they are all even numbers.
If they need a hint, you could ask if there are any odd numbers there.

Let’s now look at the columns:

- "Does the first column have the same rule as the rows?".
- "What about the other columns?".

Teacher to class: “So how did we end up with an even number in every row and
column - did the volunteer choose that?” (they didn't!).

Remove your extra row and column, and have them explain what colour to place at
the end of the first row to make sure there is an even number of black cards.
For example, if there are 3 black cards, ask what colour you need to add to
make it into an even number (black)?
If there are 4 black cards, they should work out that you need a white card to
keep it even.

Continue doing this for each row; then do it for the columns.
This is a good exercise for students thinking about even and odd numbers.
For the last (corner) card, ask if you should use the row or column to decide
it.
They should observe that it's the same for both.

Once the extra row and column have been added, ask “So what happens when I turn
a card over from black to white?” (It reduces the number of black cards by one,
so it's now an odd number).
"What if I change a white card to black?" (it adds one, which also gives an odd
number).

The students might work out from this how to find the flipped card, but in
either case, have a student come up, and ask them to look away while you flip
a card.
Then, when they look back, ask "Is the first row ok?" (They should notice that
it's still even, so hasn't been changed).
Carry on for each row until they identify the one with an odd number of black
cards.
Draw a box around that row, and say "So one of these cards was flipped?".
Now do the same with the columns - ask if each one is correct, then draw around
the column that they identify.

Now ask "So which card was flipped?" Usually students will identify the one at
the intersection.

{panel type="teaching"}

# Teaching observations

Students have now worked out for themselves how this works.
The key idea is that we just added a little more data, but could reconstruct
the original if one card was changed.

{panel end}

{panel type="math"}

# Mathematical links

This lesson would be useful for students learning about what even and odd
numbers are.

It also exercises the idea of grids (you can use phrases like "5 by 5") and
the language of columns and rows.

{panel end}

## Applying what we have just learnt

-   This kind of method is applied to almost all data that is stored or
    transmitted on computers (although usually a more sophisticated method is
    used that is even more reliable).
    If we didn’t have error detection and correction then unexpected errors in
    data would be common, and digital devices wouldn't be used to store
    anything important.
    The world would be in chaos and people wouldn’t trust computers.
    Computers wouldn’t be reliable.
-   DVDs and CDs wouldn’t work if one fleck of dust was on the disc.
-   Backing up wouldn't help much as this would also be unreliable too.
-   Transmitting data over long distances (e.g. from space probes) would be
    particularly unreliable, since it can take minutes, or even days, for data
    to arrive, and it's not feasible to request it to be retransmitted if it
    has had interference.

## Lesson reflection

Try using other objects.
Anything that has two easily distinguished 'states' is suitable.
For example, you could use playing cards, coins (heads or tails) or cards with
0 or 1 printed on them (to relate to the binary number system).

What happens if two, or more, cards are flipped?
(It is not possible to detect exactly which two cards were flipped, although
it is possible to tell that something has been changed.
You can usually narrow it down to one of two pairs of cards.
With 4 flips it is possible that all the parity bits will be correct
afterwards, and so the error could go undetected.)

Another interesting exercise is to consider the lower right-hand card.
If you choose it to be the correct one for the column above, then will it be
correct for the row to its left? (The answer is yes, always.
In this card exercise we have used even parity—using an even number of black
cards.
Can we do it with odd parity?
(This is possible, but the lower right-hand card only works out the same for
its row and column if the numbers of rows and columns are both even or both
odd.
For example, a 5 × 9 layout will work fine, or a 4 × 6, but a 3 × 4 layout
won’t.)
