# Investigating variations using the Sorting Network

## Preparatory knowledge

Students should have completed lesson 1 to introduce Sorting Networks.

## Key questions

-   In the Sorting Network, do you think that we can sort things other than numbers?
    What do you think we could sort?
    (Potential answers could include sorting things by colour, size, age, and height).

## Lesson starter

Show the students the Sorting Network again (if the network needs redrawing then students often enjoy doing this, and drawing it accurately from the diagram is a useful exercise).
Tell them that they will be trying it with some variations this time.

{panel type="math"}

# Mathematical links

Predicting outcomes: By understanding how the Sorting Network works students will be investigating different ways of using the Sorting Network and exploring how the lowest and highest number always ends up in the correct output position.

{panel end}

## Variations

This part of the lesson explores changing the way the numbers are used.

### Variation 1: Identical value

{image file-path="img/topics/sorting-network-equal-3.png" alt="Two people each holding up a card with the number 3 on it."}

In this variation, students try the Sorting Network with a set of cards where some cards have an identical value, such as  1, 2, 3, 3, 4, 5.
They will probably ask what to do when comparing the identical cards - ask them what they think, and they are likely to realise that it won't make any difference (if 3 and 3 meet, then it won't matter which one goes left and which goes right!).
Ask them to predict will happen at the end of the network (they may realise that the identical values will end up adjacent).

Now run the numbers through the network to check.
Here's a brief reminder of the Sorting Network instructions; full details are in lesson 1.

1.  Six students start in the input circles, each holding a card with one of the numbers on it.

2.  They all step forward at the same time, and when they meet someone in a box, they compare their cards.

3.  The person with the smaller card follows the line out to the left, and and the larger card to the right (this is reversed in the second variation for this lesson).

4.  This continues until all the students reach the output circles, at which point they should be in sorted order.

### Variation 2: Larger to the left

This time, the person with the larger number goes to the left instead of the right and follows the line to the next square, while the person with the lower number goes to the right instead of the left and follows the line to the next square.

Ask the students to predict what will happen (they should be able to work out that the values will come out in reverse sorted order i.e. from largest to smallest instead of smallest to largest).

Have them try it out with some numbers to check it.

{panel type="teaching"}

# Teaching observations

By reversing the left/right decision, the final result will be in the reverse order to how it would have been in lesson 1.

{panel end}

### Variation 3: Letters of the alphabet

{image file-path="img/topics/sorting-network-variation-alphabet.png" alt="Cards with letters on them."}

Give the students cards with letters on them.
Ask how we could compare these (students should observe that they could be in alphabetical order).
Have them test this by sorting the cards.

## Using the network backwards

This is an experiment that addresses a question that students may have asked: does the Sorting Network correctly sort the values if we start at the other end?

Have students try this with some simple values (such as the numbers 1 to 6).
Chances are that it will work for many starting orders of the values.
However, encourage them to keep trying until they find an initial order for which it doesn't work.
This will require considerable reasoning to achieve.

If they struggle to find an example, you could give the one below, and then challenge them to find a different one that doesn't come out sorted.

{panel type="teaching"}

# Teaching observations

The Sorting Network is designed to work consistently one way, rather than working both ways.
For example, the first image below shows an input that happens to come out sorted when going through the network backwards, while the second one doesn't.
If it fails on just one input (the second one) then we can't rely on it, even though it sometimes works.
In the other direction, it will always sort correctly.

{image file-path="img/topics/sorting-network-backwards-1.png" alt="This diagram shows that when the Sorting Network is given the input 654321 it happens to come out sorted when ran backwards."}

{image file-path="img/topics/sorting-network-backwards-2.png" alt="This diagram shows that when the Sorting Network is given the input 512364 it does not come out sorted when ran backwards."}

{panel end}

## Applying what we have just learnt

This kind of algorithm needs to run on special hardware to take advantage of doing multiple comparisons at the same time.
It is only used for specialist applications at present, for example it is sometimes done on the graphics processor (GPU) of a computer, because these processors are good at doing parallel computation.
Sorting Networks were invented long before powerful GPUs came along; this is an exciting thing about Computer Science - some of our discoveries are ahead of the hardware that is available, so we're ready to make use of the hardware when it does become commonly available!
Note that this is *not* a conventional sorting algorithm, as the sorting that is done on a conventional system can make only one comparison at a time; conventional sorting algorithms are explored in another lesson.

## Lesson reflection

What did you notice happen with each variation of using the Sorting Network?

Was it what you had expected?
