{panel type="ct-algorithm"}

# Pensée algorithmique

The divide and conquer process of repeatedly checking the centre card and deducing which cards can be eliminated, and which ones could still contain the number you are searching for, can be written as an algorithm. When you ask students to say which card to check each time they are actually articulating an algorithm and instructing you on how to follow it.

By describing this method with the following algorithm a computer or person can follow it without needing to know how it works, they can just follow the instructions and not have to think about how to actually do the task. It’s important that algorithms are written like this, because computers can’t figure out how to solve problems by themselves! A possible version of the algorithm is written under the lesson reflection.

#### Examples of what you could look for:

Who are the students who not only can explain the exact process to find the number, but are also the students who don’t deviate from that process?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

We can use the divide and conquer approach for more problems than just searching through an ordered list. We can use it to search through any set of objects that have identifying features.

We can also use it to help us sort things into order, which will be explored in the Sorting Algorithms unit.

#### Examples of what you could look for:

If you repeat this exercise but with the numbers underneath different objects, or maybe use different letters of the alphabet or different coloured discs to search for, who are the students that can see that these differences don’t actually matter and they are still solving the same problem?

{panel end}

{panel type="ct-decomposition"}

# Décomposition

{image file-path="img/topics/marbles.png" alt="The image shows a pile of marbles being halved again and again, until one marble remains."}

The Divide and Conquer method is entirely about decomposition. When we use divide and conquer to solve a problem, we are breaking the problem in half repeatedly, which soon decomposes it to a very simple case: a list of one item, which is very easy to search!

#### Examples of what you could look for:

Who are the students who are able to break the problem down into steps and then explain why each step is important?

{panel end}

{panel type="ct-pattern"}

# Généralisation et motifs

The key pattern to recognise in this activity is the process of eliminating half the possible cards by only looking in one, and that this is repeated over and over to accomplish the task.

Like we talked about in the lesson plan, the divide and conquer strategy is a pattern that appears frequently in computer science, and also in real life! It is an efficient and logical way of attacking many different problems where you are searching for something in a group of objects that have different identifying features.

#### Examples of what you could look for:

Who are the students who quickly identified the pattern?

{panel end}

{panel type="ct-evaluation"}

# Évaluation

{image file-path="img/topics/hand-with-marbles.png" alt="The image shows two hands, one with three marbles and the other with one marble." align="right"}

Students can evaluate how well the divide and conquer method works by looking at how many marbles (or whatever payment you decide to use) they have left at the end of the activity. Older students can further examine the efficiency of this algorithm by calculating the maximum number of checks it would make for a different numbers of cards. You could compare this to the number of checks that a sequential search would need, and how these numbers change as you increase the number of cards.

#### Examples of what you could look for:

Who are the students who can explain the strengths and potential problems of using a binary search to find data? Can they explain why the maximum number of checks a binary search will make is much smaller than the maximum for sequential search?

{panel end}

{panel type="ct-logic"}

# Logique

To retain as many marbles (or whatever payment you decide to use) as possible it makes sense to try and eliminate as many cards as possible with each guess. That way you can cut down the number of cards to 1 as fast as possible. Students will generally be able to logically reason and recognise that the best way to do this is to check the centre card each time. If we check that card and compare it to the number we are searching for what does that tell us about all the cards to the left of that card? All the cards to the right of that card? Students can deduce which cards they can now eliminate based on the card they have checked.

Asking students to explain how they came to this conclusion is a great way to exercise their thinking skills, by getting them to articulate the logical steps they followed to come to this conclusion, and why it makes sense that doubling the number of cards only needs 1 more check. Understanding why divide and conquer will only ever require a specific small number of steps at most (for example it will never take more than 5 checks for 19 cards, or 20 checks for 1,000,000 cards) also requires a high level of logical reasoning.

#### Examples of what you could look for:

Which students instinctively go for the middle square when searching? They are likely logical thinkers who can deduce that since the numbers are sorted then the middle square will tell them the most useful information.

{panel end}