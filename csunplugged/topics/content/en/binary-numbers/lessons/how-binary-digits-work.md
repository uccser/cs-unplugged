# How binary digits work

## Key questions

-   What different number systems do we know about? (Answers might include:
    Roman Numerals; Tally marks; Number bases like binary, octal and
    hexadecimal; Language based systems like Chinese or Ancient Egyptian.)
-   Why do we normally use 10 digits? (Probably because we have 10
    fingers, plus it's a fairly efficient way to write things compared with,
    say, tally marks.)
-   Why do we have different number systems? (They are convenient for
    different things e.g. tally marks are easy if you are counting; Roman
    numerals can be useful for making a number look more mysterious or harder
    to read.)

## Lesson starter

{panel type="video"}

# See teaching this in action

{video url="https://vimeo.com/437725275"}

{panel end}

{panel type="general"}

# Note from the authors

We’ve noticed that once students understand how the binary number system works, they have many questions and are excited to explore the concepts outlined in this lesson further.
We’ve added a lot of information into this lesson, however, it is not our intention that you will teach and cover all the concepts, but that you have at your fingertips the information you need when your students express an interest in learning more.

{panel end}

{panel type="general"}

# Notes on resources

There is also an online interactive version of the binary cards [here](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), from the [Computer Science Field Guide](http://www.csfieldguide.org.nz/), but it is preferable to work with physical cards.

{panel end}

1.  Hold the first 5 cards (1, 2, 4, 8 and 16 dots), but don't let students
    see the dots.
    Ask for 5 students to volunteer to be “bits”, and have them stand in a
    line in front of the class.

2.  Hand out the 1-dot card to the person on the right.
    Explain that they are one "bit" (binary digit), and can be on or off,
    black or white, 0 or 1 dots.
    The only rule is that their card is either completely visible, or not
    visible (i.e. flipped over).
    Hand out the second card to the second person from the right.
    Point out that this card has either 2 dots (visible), or none
    (upside down).

    {image file-path="img/topics/col_binary_2cards.png" alt="2 kids holding binary cards"}

3.  Ask the class what the number of dots on the next card will be.
    Get them to explain why they think that.

    {panel type="teaching"}

    # Teaching observations

    Students will usually suggest it should be three.
    If they suggest 4, they have probably done the activity before (or
    have seen the cards you are holding!)
    If they suggest the wrong number, don't correct them, but continue
    without comment, so that they can construct the rule for themselves.

    {panel end}

4.  Silently give out the four-dot card, and let them try to see the pattern.

    {image file-path="img/topics/col_binary_3cards.png" alt="3 kids holding binary cards"}

    {panel type="teaching"}

    # Teaching observations

    Usually some students will complain that you've missed out the three,
    but simply indicate that you haven't made a mistake.
    This gives them the opportunity to try to construct the pattern for
    themselves.

    {panel end}

5.  Ask what the next card is, and why.

    {panel type="teaching"}

    # Teaching observations

    At this point it is common for students to guess that it is 6
    (since it follows the numbers 2 and 4).
    However, if you let them think about it a little more, some will usually
    come up with 8, and those students should be able to convince the others
    that they are correct (there are several ways a student could explain
    this e.g. that each card is double the previous one, or that if you take
    two of a card, you get the next one)

    {panel end}

6.  Students should be able to work out the fifth card (16 dots) without help:

    {image file-path="img/topics/col_binary_5cards.png" alt="5 kids holding binary cards"}

7.  How many dots would the next card have if we carried on to the left? (32)
    The next...?
    (There's no need to have students hold these cards, as they won't be used
    in the next part of the activity, but you can show them to confirm that
    they are correct).

8.  Continue with 64 and 128 dots.

    {panel type="teaching"}

    # Teaching observations

    At 128 dots there would be 8 cards. This is 8 bits, which is commonly
    referred to as a byte.
    It may be distracting to bring this up at this point, but some students
    may already be familiar with the idea that 8 bits is a byte, and make
    that observation.
    However, in the meantime, we'll work with a 5-bit representation, which
    isn't as useful as a whole byte, but a good size for teaching.
    (A byte is a convenient grouping of bits, and usually computer storage is
    based around bytes rather than individual bits; it's just the same as eggs
    being sold as a dozen; they could be sold individually, but groups of a
    dozen are usually more convenient for everyone concerned.)

    A common mistake is to hand out the cards from left to right, but it's
    convention in number representation that the least significant value is
    on the right, and this is an important idea for students to take away
    from this activity.

    {panel end}

## Lesson activities

1.  Remind the students that the rule is that a card either has the dots fully
    visible, or none of them are visible.
    If we can turn cards on and off by showing the front and back of the card,
    how would we show exactly 9 dots?
    Begin by asking if they want the 16 card (they should observe that it has
    too many dots), then the 8 card (they will likely reason that without it
    there aren't enough dots left), then 4, 2 and 1.
    Without being given any rules other than each card being visible or not,
    students will usually come up with the following representation.

    {image file-path="img/topics/binary-cards-total-9.png" alt="Diagram showing that 2 binary cards make the number 9"}

    {panel type="math"}

    # Mathematical links

    Base 10 (our counting system) has 10 digits, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
    When we count in base 10, we count from 0 to 9 and then run out of digits.
    So we need to add another column; we put a 1 in that column and start
    counting again from 0.
    This makes the number 10, we then repeat that process until the tens
    column is 9 and the ones column is 9 (making 99); from there we then add
    another column.
    Hence we have the familiar place value system that can be shown something
    like this:

    100,000s | 10,000s | 1,000s | 100s |10s | 1

    *Note: Use the appropriate place value example based on what you have
    already taught in your class; this is an extended example.*

    Base 2 (binary) follows the same logic, except it moves a lot quicker
    to the “next” place value, because there are only two digits, 0 and 1.
    The binary place values look like this:

    32 | 16 | 8 | 4 | 2 | 1 |

    Sometimes students confuse the order of digits in a binary representation.
    To support students to understand the correct ordering of binary digits,
    ask the question: If I was going to give you $435.00 which number are you
    most interested in? Is it the 4 or the 5?
    Why is that?
    It’s the same for binary code, the lowest value (least significant digit)
    is on the far right, whereas the most significant digit is on the far left.

    {panel end}

2.  Now ask "How would you make the number 21?"
    (Again, start by asking if they want the 16 card, then the 8 card, and so
    on from left to right).

3.  This is an algorithm for converting numbers to a binary representation. Let’s think through the steps to do this together.

    a. Start with all the numbers switched to on (dots showing).

    {image file-path="img/topics/lightbulb_series_1.png" alt="5 lightbulbs switched on"}

    b. Consider representing the number 10

    c. Does 16 fit into 10? No - so turn it off

    {image file-path="img/topics/lightbulb_series_2.png" alt="4 lightbulbs switched on"}

    d. Does 8 fit into 10? Yes - so keep it on. How many are left over? (2)

    e. Does 4 fit into 2? No - so turn it off

    {image file-path="img/topics/lightbulb_series_3.png" alt="3 lightbulbs switched on"}

    f. Does 2 fit into 2? Yes - so keep it on. How many are left over? (None)

    g. So turn off 1.

    {image file-path="img/topics/lightbulb_series_4.png" alt="2 lightbulbs switched on"}

## Applying what we have just learnt

-   Group students into pairs.
-   Give each pair a set of the smaller binary cards (either 5 or 6 cards,
    depending on the range of numbers they are comfortable with).
-   Starting with just 5 cards, have them practise the algorithm (deciding
    about each card from left to right) for numbers such as 20, 15, and 8.

1.  Explain to students that we're working with just two digits, so they
    are called binary digits.
    They are so common that we have a short name for them: write "binary
    digit" on a piece of paper, then rip off the "bi" at the start, and the
    "t" at the end, put it together and ask what the combined word ("bit")
    spells.
    This is the short name for a binary digit, so the 5 cards that they have
    are actually 5 bits.

2.  Now let’s count from the smallest number we can make up to the highest
    number:

    a. What is the smallest number? (they may suggest 1, then realise
    that it’s 0).

3.  Get the number zero displayed on the cards (i.e. no dots showing).

4.  Now count up 1, 2, 3, 4 …. (each pair should work out these numbers
    between them).

5.  Once they start to get into a routine, ask: how often are we seeing the
    1-dot card? (every second time, which is every odd number)

    a. What other patterns are we seeing?
    (some may observe that the 2-dot card flips on every second count,
    the 4-dot on every 4th and so on; so the 16 dot card doesn't do much!)

6.  Continue until all the cards are switched to “on” and have counted to 31.
    What happens next? (We have to add a new card.)
    How many dots on it? (32)
    What do we have to do to the other 5 cards when we get to 32?
    (we have to turn them all off)

7.  Let’s explore this further ...

    a. So when I have two bits I can make a maximum of? (3)

    b. I add another bit and that has how many dots on it? (4)

    c. I turn off the first two bits to make 4 right?

    d. Now let’s turn on all three bits, so now we have how many? (7)

    e. I add another bit and that has how many dots on it? (8)

    f. Repeat until a pattern is recognised that the number on the next card
    to the left is one more than the total number of dots on all the cards to
    the right (e.g. there are 15 dots on the 8, 4, 2 and 1 cards, so the next
    card to the left is 16).
    This makes it easy to work out the number if all the bits are switched
    on - double the left-hand card, and subtract 1.

    g. How many different numbers can I make with two bits? (4; often students
    will say 3 because they haven’t counted 0)

    h. Let’s add the next bit; how many different numbers can we make now? (8,
    again 7 will often be given as an answer first)

    i. Repeat until a pattern is recognised that each time we add another bit
    we can now represent twice as many numbers.

{panel type="teaching"}

# Teaching observations

A concept that students may struggle with here is that the number of values
is one more than the maximum value (e.g. from 0 to 7, there are 8 different
numbers).
The same observation occurs with the number of digits in conventional decimal
numbers; the largest digit is 9, but there are 10 possible digits (counting 0).
This is sometimes called the fencepost problem (the number of fence posts is
one more than the number of gaps between them), and it comes up a lot in
computing.

{panel end}

## Lesson Reflection

-   Would this activity work if we used white and cream cards? Why? Why not?
    (In principle you could use these, but it wouldn’t be a good idea.
    We are looking for the answer that they are not contrasting colours,
    therefore it would be difficult to see if it is actually on or off.
    This hints why computers use easily distinguished physical
    representations.)
-   What are some contrasting symbols or ways that we can show on and off in
    binary?  

    -   (Ideas could include holding the cards up high, or down low;
        simply holding up a hand; sitting down or standing up; or using a
        different representation such as lights that are on or off.)

-   Computers are cheaper and easier to build if they represent data with just
    two contrasting values, which we represent as the numbers 0 and 1.
    What else could we use to represent two opposites in writing?
    (Perhaps a cross or tick; happy or sad face; or any other pair of symbols.)
-   Extending this idea, the numbers might be represented by a voltage that
    is either close to 5 volts, or close to 0 volts.
    The circuitry is built so that anything less than about 2.5 volts counts
    as 0 and anything over 2.5 volts counts as 1.
    Like the contrasting colours of the cards, this is very easy to recognise.
    We could have had 10 colours of cards to represent the digits from 0 to
    10, and we could have ten voltage ranges (0 to 0.5, 0.5 to 1.0 and so on),
    but it's way more complicated to build fast and accurate circuitry
    for this.
