{panel type="ct-algorithm"}

# Algorithmisches Denken

When you ask students to say which card to check each time they are actually articulating an algorithm and instructing you on how to follow it.

By describing binary search with an algorithm a computer or person can follow it without needing to know how it works; they can just follow the instructions and not have to think about how to actually do the task. It’s important that algorithms are written like this, because computers can’t figure out how to solve problems by themselves! A possible version of the algorithm is written under the lesson reflection

#### Worauf Sie beispielsweise achten können:

Who are the students who not only can explain the exact process to find the number, they also don’t deviate from that process?

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

We can use the divide and conquer approach for more problems than just searching through an ordered list. We can use it to search through any set of objects that have identifying features.

We can also use it to help us sort things into order as well, which will be explored in the Sorting Algorithms unit.

Like with sequential search, it doesn’t matter what we are searching for (as long as that data can be put into an order), it wouldn’t change the algorithm if we were searching for something other than numbers, for example letters of the alphabet.

#### Worauf Sie beispielsweise achten können:

{image file-path="img/topics/digits-alpha-items.png" alt="The image shows three types of data, one is numbers, one is letters, and one is different sized circles."}

If you repeat this exercise but with the numbers underneath different objects, or maybe use different letters of the alphabet or different coloured discs to search for, who are the students that can see that these differences don’t actually matter and they are still solving the same problem? Which students immediately apply the same searching strategy?

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

{image file-path="img/topics/marbles.png" alt="The image shows a pile of marbles being halved again and again, until one marble remains."}

The Divide and Conquer method is entirely about decomposition. When we use divide and conquer to solve a problem, we are breaking the problem in half repeatedly, which soon decomposes it to a very simple case: a list of one item, which is very easy to search!

#### Worauf Sie beispielsweise achten können:

Who are the students who are able to break the problem down into steps and then explain why each step is important?

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

The key pattern to recognise in this activity is the process of eliminating half the possible cards by only looking in one, and that this is repeated over and over to accomplish the task.

Like we talked about in the lesson plan, the divide and conquer strategy is a pattern that appears frequently in computer science, and also in real life! It is an efficient and logical way of attacking many different problems where you are searching for something in a group of objects that have different identifying features.

#### Worauf Sie beispielsweise achten können:

Who are the students who quickly identified the pattern?

{panel end}

{panel type="ct-evaluation"}

# Auswertung

{image file-path="img/topics/hand-with-marbles.png" alt="The image shows two hands, one with three marbles and the other with one marble." align="right"}

Students can evaluate how well the divide and conquer method works by looking at how many marbles (or whatever payment you decide to use) they have left at the end of the activity. They could compare this to the number of marbles they have left at the end of a sequential search.

#### Worauf Sie beispielsweise achten können:

Who are the students who can explain that binary search is more efficient than sequential search? Did any of them see that the disadvantage of binary search is that we need the numbers to be in order first?

{panel end}

{panel type="ct-logic"}

# Logik

To retain as many marbles (or whatever payment you decide to use) as possible it makes sense to try and eliminate as many cards as possible with each guess. That way you can cut down the number of cards to 1 as fast as possible. Students will generally be able to logically reason and recognise that the best way to do this is to check the centre card each time, but depending on their age may not be able to articulate how they know that.

To help them articulate it you could ask them: If we check the centre card and compare it to the number we are searching for what does that tell us about all the cards to the left of that card? All the cards to the right of that card? Students may be able to deduce which cards they can now eliminate, based on the card they have checked.

Asking students to explain how they came to this conclusion is a great way to exercise their thinking skills.

#### Worauf Sie beispielsweise achten können:

{image file-path="img/topics/numbers-middle-bright.png" alt="The image shows a five by five grid of numbers in sorted order, with the center number highlighted."}

Which students instinctively go for the middle square when searching? They are likely logical thinkers who can deduce that since the numbers are sorted then the middle square will tell them the most useful information.

{panel end}