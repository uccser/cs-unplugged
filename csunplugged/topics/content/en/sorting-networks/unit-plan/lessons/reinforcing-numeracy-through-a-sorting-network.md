# Reinforcing numeracy through a Sorting Network

## Key questions

What are examples of tasks get finished sooner if more people help with them?
What are examples of tasks that don't get finished sooner if more people help
with them?

### Potential answers could include:

{image file-path="img/topics/sorting-network-office-note-text-en.png" alt="A group of students all carry a note to the office."}

Tasks such as tidying the classroom, picking up rubbish, or reshelving library
books may come up as ones that benefit from multiple helpers.
Things that don't go faster might include delivering a note to the office (10
people delivering the note won't get it there 10 times faster), or washing
dishes if there is only one sink (two people are faster than one, but more
people probably can't speed it up).

## Lesson starter

Use the Sorting Network template to draw a 6 person Sorting Network on a paved
surface outside using chalk (other alternatives include using masking/painters
tape on a carpet or wooden floor, tape on a tarpaulin, or line marking paint on
grass).
Note that the Sorting Network needn't use different colours or line
thicknesses, but if suitable chalk or tape is available, this can help students
remember which way to go.
It should be large enough that two students can comfortably stand in the
rectangles; the more spread out it is, the more effective the exercise is.
In a very confined situation, it could be done on a desk top using game
counters instead of students moving around, but this is much less engaging.

Show the students the Sorting Network drawn on the ground, and tell them "This
chalk computer can do some things very fast, let’s investigate what it does."

{panel type="math" title="Mathematical links"}

Supports students understanding of ordering any range of numbers, from ordering
single digit numbers to fractions and decimals, or numbers in their millions.

{panel end}

{panel type="exemplars" title="Exemplars"}

Here are examples of the kinds of numbers you could use to reinforce number
ordering (two of each set of six cards are shown).
It's good to start with the single digit numbers to get students used to the
system, and then provide more difficult numbers appropriate to the students'
ability level.

{image file-path="img/topics/sorting-network-example-cards-1.jpg" alt="Two pieces of paper with single digit numbers printed on them."}

{image file-path="img/topics/sorting-network-example-cards-2.jpg" alt="Two pieces of paper with seven digit numbers printed on them."}

{image file-path="img/topics/sorting-network-example-cards-3.jpg" alt="Two pieces of paper with fractions printed on them."}

{panel end}

## Lesson activities

{image file-path="img/topics/sorting-network-kids.png" alt="A group of children sort items on a Sorting Network drawn on concrete."}

1.  Organise students into groups of six.
    Only one team will use the network at a time.
2.  The current team should stand on the circles at the "input" end of
    the Sorting Network.
3.  Give each of the six students a card to hold (initially use the set of
    cards containing the numbers from 1 to 6; the cards should be given to
    the students out of order).
    These cards are the inputs into this cool chalk computer (this is a
    special kind of computer that can process several operations at the same
    time).
4.  Get the first two students to follow the lines from their circles until
    they meet at a box (the others should pay attention).
5.  When the two have entered the box, they should say “Hello” to each other
    (this is to make sure that they stop and both engage in this step), and
    then compare cards to decide who has the lower number and who has the
    higher number.
6.  The student with the lower number should follow the line out to the left
    and go to the next box, while the person with the higher number follows the
    line leaving to the right to go to the next square.
7.  Now get the next pair of students to do the same, meeting at a box and
    leaving it with the smaller to the left and the larger to the right.
8.  You can now get the remaining pair of students to do this (remind them to
    say hello when they meet).
9.  Once they have the idea, tell them to repeat this process until they get to
    the end of the network.
    If someone gets left behind, have the students go back to the beginning;
    they will need to pay attention when they meet at a square, and ensure that
    both people who have met know the outcome.
10. When they have all reached the circles at the other end of the network have
    them turn and face the starting circles and read what’s on their card, from
    left to right.
    They should be in the correct order from smallest to largest; if not, they
    may need to try again and work more carefully.
11. When each group has been through the Sorting Network, introduce a Sorting
    Network race to see which group can successfully complete the task in the
    shortest amount of time (either with two Sorting Networks racing teams at
    the same time, or one network with the times measured using a stopwatch).

{panel type="teaching" title="Teaching observations"}

If it didn’t work it may be because a pair incorrectly went to the wrong square
or a person raced ahead of everyone else.
Have the group repeat the task and check each comparison.
If it doesn’t work a second time, bring in student “testers” to confirm that
each square has made the right decision which person is to go to the left and
the right.
Encouraging them to say "hello" when they meet at a square helps to avoid
someone heading off before they have made a decision on the values.

{image file-path="img/topics/sorting-network-too-far-kid.png" alt="A child walks too far in the sorting network activity, failing the activity for everyone."}

If a student races to the end ahead of everyone else because they already know
where their number will go once the numbers are sorted (this happens quite
often!) then some students are going to be left stuck inside the network
because they don’t have someone to compare numbers with.
This is a good opportunity to remind students that computers need to follow the
instructions they are given precisely to make sure they achieve the correct
result; it also reinforces the need for teamwork!

{panel end}

## Applying what we have just learnt

This technique with parallel instructions can't run directly in the kind of
computer system that students are likely to be learning about, as simpler
systems can only compare one pair of values at a time, while this one is
comparing up to three pairs of values at the same time.
But although this algorithm hasn’t been written to work on a conventional
system, there is still an algorithm to be observed, a parallel algorithm, and
this can be implemented with specialised hardware and software.
The challenge with creating parallel algorithms is to have as many things
happening at the same time as possible, so that we can get things done faster.
However, it's not always easy to break a problem up so that separate parts can
happen at the same time, as often each comparison depends on the results of
another.
The diagram that we used above happens to be the shortest one we can design for
sorting 6 values.

How do we know this Sorting Network is reliable and works every time?

The outcome we want to achieve is that the numbers come out in the correct
order with the smallest number being in the left-most box and the second
smallest number finishing next to it, right through to the largest number being
in the right-most box.
If we want to make sure it works for all possible inputs, then we would need to
try it for every order that the values might start in - it turns out that there
are 720 different orderings that 6 items can start in, so that's a lot of cases
to test.
For sorting more than 6 items, there are way too many different orderings to
try out, so we must make a mathematical proof of why it works.
Here are some elements of such a proof:

Let’s disregard the numbers for now and look at the Sorting Network from the
point of view of following the paths.
If the smallest number was in node 1, what path would it take and does it end
up in the leftmost node at the end?

{image file-path="img/topics/sorting-network-node-1.png" alt="An image showing the network with the path the smallest number would take through the network if the smallest number started in node 1."}

Now repeat this by asking if the smallest number was in node 2, what path would
it take and does it still end up in the leftmost node at the end?

{image file-path="img/topics/sorting-network-node-2.png" alt="An image showing the network with the path the smallest number would take through the network if the smallest number started in node 2."}

Repeat this until you’ve tested all 6 nodes.
If the smallest number ends up in the leftmost node regardless of where it
starts, that's part-way to being sure that the structure always works.

You can repeat this with the largest number - no matter where it starts, it
will always end up in the right-most node.

Doing this for the other four values (e.g. the second to largest) isn't quite
as simple, but computer scientists are able to prove that they will also always
end up in their correct position.

## Lesson reflection

-   Was there ever a situation where the cards weren’t sorted in the right
    order?
    What had happened for that to occur?
    How was it corrected?
-   Can you trace the pathways for the lowest number if it was placed in any
    position?
    What about the largest number?

## Seeing the Computational Thinking connections

{panel type="ct-algorithm" title="Algorithmic thinking"}

We used an algorithm in this lesson to sort the numbers into order using a
parallel processor (normally this processor would be implemented in hardware,
but our chalk network is still actually one!
It’s powered by people instead of electricity).

**What to look for:**

-   Do students understand how each node functions (taking in two values and
    swapping them if they are in the wrong order)?
    Are they able to explain to other students how to use the network
    correctly?

-   Do the students see that no matter what numbers or data we put into the
    network we will always get a solution if we follow the algorithm correctly?

{panel end}

{panel type="ct-abstraction" title="Abstraction"}

The Sorting Network used in these activities is itself an abstract
representation of how Sorting Networks are implemented in hardware and
software.
It represents the core functionality of a Sorting Network, whilst hiding all
the nitty gritty details of how the hardware and circuitry works.

**What to look for:**

-   Can students make the connection between the lines and nodes on this graph
    and the way computers can process information by making comparisons?
-   Can students understand that this representation can be used to model how a
    real parallel processing computer would work?

{panel end}

{panel type="ct-decomposition" title="Decomposition"}

The whole process of sorting in this activity is decomposed into a very simple
operation: comparing two values.
This operation alone is very simplistic, but when it is performed many many
times it can be used to build up a solution to a much larger task.

**What to look for:**

-   Can students see how to design a Sorting Network to sort just 2 values?
    (It would just be a single comparator node).

{panel end}

{panel type="ct-pattern" title="Generalising and patterns"}

In this lesson students only worked with one type of information, numbers, so
there wasn’t much use of generalisation.
It is more prominent in the next lesson.

{panel end}

{panel type="ct-evaluation" title="Evaluation"}

For this Sorting Network there can be up to three comparisons happening at
once, and the length of the network determines how long it would take to
complete all these comparisons.
Although 12 comparisons need to be made when going through the network, the
network can be completed in the time it takes to an individual node to make 5
comparisons.

**What to look for:**

-   Can students identify the longest path that any number would have to go
    through to get to the end?
    (The middle two numbers need to make 5 comparisons).
-   Can students explain that if every comparison were to take, say, 2 seconds,
    then the sorting would be finished in 5x2 seconds, and not 12x2 seconds?

{panel end}

{panel type="ct-logic" title="Logic"}

The smallest value will always take the left path at any comparison, and from
every starting point the path that always takes the left branch will lead to
that node, the smallest value will therefore always end up in the left-most
position at the end.

**What to look for:**

-   Can students explain where the smallest value will end up regardless of
    what the other values are?
-   Do students understand the function of each node?
    Do they avoid simply going to the final node without doing the comparisons?

{panel end}
