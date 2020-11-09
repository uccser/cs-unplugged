# Reinforcing numeracy through a Sorting Network

## Key questions

What are examples of tasks that get finished sooner if more people help with them? What are examples of tasks that don't get finished sooner if more people help with them?

### Potential answers could include:

{image file-path="img/topics/sorting-network-office-note-text-en.png" alt="A group of students all carry a note to the office."}

Tasks such as tidying the classroom, picking up rubbish, or reshelving library books may come up as ones that benefit from multiple helpers. Things that don't go faster might include delivering a note to the office (10 people delivering the note won't get it there 10 times faster), or washing dishes if there is only one sink (two people are faster than one, but more people probably can't speed it up).

## Lesson starter

{panel type="video"}

# See teaching this in action

{video url="https://vimeo.com/437722996"}

Some other videos showing different situations using Sorting Networks:

- [Video 1](https://vimeo.com/437726931)
- [Video 2](https://vimeo.com/437726955)

{panel end}

Use the Sorting Network template to draw a 6 person Sorting Network on a paved surface outside using chalk (other alternatives include using masking/painters tape on a carpet or wooden floor, tape on a tarpaulin, or line marking paint on grass). Note that the Sorting Network needn't use different colours or line thicknesses, but if suitable chalk or tape is available, this can help students remember which way to go. It should be large enough that two students can comfortably stand in the rectangles; the more spread out it is, the more effective the exercise is. In a very confined situation, it could be done on a desk top using game counters instead of students moving around, but this is much less engaging.

Show the students the Sorting Network drawn on the ground, and tell them "This chalk computer can do some things very fast, let’s investigate what it does."

{panel type="math"}

# Mathematical links

Supports students understanding of ordering any range of numbers, from ordering single digit numbers to fractions and decimals, or numbers in their millions.

{panel end}

{panel type="exemplars"}

# Exemplars

Here are examples of the kinds of numbers you could use to reinforce number ordering (two of each set of six cards are shown). It's good to start with the single digit numbers to get students used to the system, and then provide more difficult numbers appropriate to the students' ability level.

{image file-path="img/topics/sorting-network-example-cards-1.png" alt="Two pieces of paper with single digit numbers printed on them."}

{image file-path="img/topics/sorting-network-example-cards-2.png" alt="Two pieces of paper with seven digit numbers printed on them."}

{image file-path="img/topics/sorting-network-example-cards-3.png" alt="Two pieces of paper with fractions printed on them."}

{panel end}

## Lesson activities

{image file-path="img/topics/sorting-network-kids.png" alt="A group of children sort items on a Sorting Network drawn on concrete."}

1. Organise students into groups of six. Only one team will use the network at a time.
2. The current team should stand on the circles at the "input" end of the Sorting Network.
3. Give each of the six students a card to hold (initially use the set of cards containing the numbers from 1 to 6; the cards should be given to the students out of order). These cards are the inputs into this cool chalk computer (this is a special kind of computer that can process several operations at the same time).
4. Get the first two students to follow the lines from their circles until they meet at a box (the others should pay attention).
5. When the two have entered the box, they should say “Hello” to each other (this is to make sure that they stop and both engage in this step), and then compare cards to decide who has the lower number and who has the higher number.
6. The student with the lower number should follow the line out to the left and go to the next box, while the person with the higher number follows the line leaving to the right to go to the next box.
7. Now get the next pair of students to do the same, meeting at a box and leaving it with the smaller to the left and the larger to the right.
8. You can now get the remaining pair of students to do this (remind them to say hello when they meet).
9. Once they have the idea, tell them to repeat this process until they get to the end of the network. If someone gets left behind, have the students go back to the beginning; they will need to pay attention when they meet at a square, and ensure that both people who have met know the outcome.
10. When they have all reached the circles at the other end of the network have them turn and face the starting circles and read what’s on their card, from left to right. They should be in the correct order from smallest to largest; if not, they may need to try again and work more carefully.
11. When each group has been through the Sorting Network, introduce a Sorting Network race to see which group can successfully complete the task in the shortest amount of time (either with two Sorting Networks racing teams at the same time, or one network with the times measured using a stopwatch).

{panel type="teaching"}

# Teaching observations

If it didn’t work it may be because a pair incorrectly went to the wrong square or a person raced ahead of everyone else. Have the group repeat the task and check each comparison. If it doesn’t work a second time, bring in student “testers” to confirm that each square has made the right decision which person is to go to the left and the right. Encouraging them to say "hello" when they meet at a square helps to avoid someone heading off before they have made a decision on the values.

{image file-path="img/topics/sorting-network-too-far-kid.png" alt="A child walks too far in the sorting network activity, failing the activity for everyone."}

If a student races to the end ahead of everyone else because they already know where their number will go once the numbers are sorted (this happens quite often!) then some students are going to be left stuck inside the network because they don’t have someone to compare numbers with. This is a good opportunity to remind students that computers need to follow the instructions they are given precisely to make sure they achieve the correct result; it also reinforces the need for teamwork!

{panel end}

## Applying what we have just learnt

This technique with parallel instructions can't run directly in the kind of computer system that students are likely to be learning about, as simpler systems can only compare one pair of values at a time, while this one is comparing up to three pairs of values at the same time. But although this algorithm hasn’t been written to work on a conventional system, there is still an algorithm to be observed, a parallel algorithm, and this can be implemented with specialised hardware and software. The challenge with creating parallel algorithms is to have as many things happening at the same time as possible, so that we can get things done faster. However, it's not always easy to break a problem up so that separate parts can happen at the same time, as often each comparison depends on the results of another. The diagram that we used above happens to be the shortest one we can design for sorting 6 values.

How do we know this Sorting Network is reliable and works every time?

The outcome we want to achieve is that the numbers come out in the correct order with the smallest number being in the left-most box and the second smallest number finishing next to it, right through to the largest number being in the right-most box. If we want to make sure it works for all possible inputs, then we would need to try it for every order that the values might start in - it turns out that there are 720 different orderings that 6 items can start in, so that's a lot of cases to test. For sorting more than 6 items, there are way too many different orderings to try out, so we must make a mathematical proof of why it works. Here are some elements of such a proof:

Let’s disregard the numbers for now and look at the Sorting Network from the point of view of following the paths. If the smallest number was in node 1, what path would it take and does it end up in the leftmost node at the end?

{image file-path="img/topics/sorting-network-node-1.png" alt="An image showing the network with the path the smallest number would take through the network if the smallest number started in node 1."}

Now repeat this by asking if the smallest number was in node 2, what path would it take and does it still end up in the leftmost node at the end?

{image file-path="img/topics/sorting-network-node-2.png" alt="An image showing the network with the path the smallest number would take through the network if the smallest number started in node 2."}

Repeat this until you’ve tested all 6 nodes. If the smallest number ends up in the leftmost node regardless of where it starts, that's part-way to being sure that the structure always works.

You can repeat this with the largest number - no matter where it starts, it will always end up in the right-most node.

Doing this for the other four values (e.g. the second to largest) isn't quite as simple, but computer scientists are able to prove that they will also always end up in their correct position.

## Lesson reflection

- Was there ever a situation where the cards weren’t sorted in the right order? What had happened for that to occur? How was it corrected?
- Can you trace the pathways for the lowest number if it was placed in any position? What about the largest number?