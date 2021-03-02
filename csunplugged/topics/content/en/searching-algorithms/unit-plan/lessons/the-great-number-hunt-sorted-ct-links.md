{panel type="ct-algorithm"}

# Algorithmic thinking

Binary search works by applying the Divide and Conquer process; we repeatedly check the centre number box and deduce which boxes can then be eliminated, and which ones could still potentially contain the real money you are hunting for. This can be given as an algorithm.

By describing this method with the same algorithm as in lesson 2 a computer or person can follow it without having to think about how to actually do the task.

#### Examples of what you could look for:

Who are the students who not only can explain the exact process to find the real money, but are also the students who don’t deviate from that process?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

As in lesson 2 and lesson 3, we can ignore many details about the items we are searching for.

Also, as discussed in lesson 2, we can use the divide and conquer approach for more problems than just searching through an ordered list of numbers. We can use it to search through any set of objects that can be placed in ascending order (such as words in alphabetical order).

#### Examples of what you could look for:

What questions are students asking about the number boxes? Organise them into useful questions and no as useful questions. Which students can identify quickly what the relevant information is?

{panel end}

{panel type="ct-decomposition"}

# Decomposition

Binary search is a classic method of divide and conquer and is entirely about decomposition. Refer to lesson 2.

#### Examples of what you could look for:

Who are the students who are able to break the problem down into steps and then explain why each step is important?

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

The key pattern to recognise in this activity is the process of eliminating half the possible cards by only looking in one, and that this is repeated over and over to accomplish the task.

Like we talked about in the lesson plan, the divide and conquer strategy is a pattern that appears frequently in computer science, and also in real life!
It is an efficient and logical way of attacking many different problems where you are searching for something in a group of objects that have different identifying features.

#### Examples of what you could look for:

Who are the students who quickly identified the pattern?

{panel end}

{panel type="ct-evaluation"}

# Evaluation

Students will be evaluating binary search in the same way they evaluated the divide and conquer method in lesson 2.

Students can evaluate how well the divide and conquer method works by looking at how many marbles (or whatever payment you decide to use) they have left at the end of the activity.
Older students can further examine the efficiency of this algorithm by calculating the maximum number of checks it would make for a different numbers of cards.
You could compare this to the number of checks that a sequential search would need, and how these numbers change as you increase the number of cards.


#### Examples of what you could look for:

Who are the students who can explain the strengths and potential problems of using a binary search to find data?

{panel end}

{panel type="ct-logic"}

# Logic

To search through the number boxes and guarantee they will find the real money in a low number of guesses students must use the binary search algorithm rather than using a sequential search or just choosing randomly based on where they think the money might be.
This is because they need to eliminate as many boxes as possible with each guess.
Students might think if there are 100 boxes and the number they are looking for is 90 then the logical choice would be to look in a boxes near the right end of the list first, instead of the middle, because they think 90 is likely to be near the 90th box.
But this isn’t actually a more logical choice than dividing the list in half with binary search if you don’t know the range of serial numbers on the money in the boxes, and binary search is so fast that trying to be clever about where a value is doesn't help much even if you're right.
Which students can explain why the logical decision is to always stick with binary search? A good question to prompt them with is:

-   You don’t know what the range of serial numbers on the money is, it could be anything!
    If they were somewhere between 1 and 99,999,999 and you have 100 number boxes would it be a good choice to guess where the money might roughly be?
    Or should you stick to binary search?


#### Examples of what you could look for:

{image file-path="img/topics/numbers-middle-bright.png" alt="The middle item is the important item."}

Which students instinctively go for the middle square when searching?
They are likely logical thinkers who can deduce that since the numbers are sorted then the middle square will tell them the most useful information.

{panel end}
