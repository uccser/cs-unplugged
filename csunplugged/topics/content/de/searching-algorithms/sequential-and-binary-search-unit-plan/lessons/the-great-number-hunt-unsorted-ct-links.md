{panel type="ct-algorithm"}

# Algorithmisches Denken

In this lesson we used the same algorithm and algorithmic thinking as we did in lesson 1, but applied it to number boxes instead of the numbers being guessed. Just like in lesson 1, if we check in every number box then we are guaranteed to find the real money at some stage (unless all the money is fake!)

From lesson 1: We used an algorithm in this lesson to find the number we were searching for. This is an algorithm because it is a step-by-step process that will always give the right solution for any input you give it as long as the process is followed exactly; if we check every card in the list we are guaranteed to find the right number (as long as it is in the list!)

#### Worauf Sie beispielsweise achten können:

Who are the students who not only can explain the exact process to find the real money, but are also the students who don’t deviate from that process? Do they realise that if the value isn't there, then every box will have to be opened to find that out?

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

As in lesson 1, we can ignore many details about the items we are searching for. For example it doesn’t matter if the money is in New Zealand dollars/$, Japanese yen/¥, or pounds/£. You only need to focus on the serial numbers and remember that the boxes are in order, as this is all the information you need to solve the problem.

#### Worauf Sie beispielsweise achten können:

What questions are students asking about the number boxes? Organise them into useful questions and no as useful questions. Which students can identify quickly what the relevant information is?

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

The larger task of “find my number” is broken down into a series of small steps, each of which is simply “check one of the cards to see if your number is there" and eliminate that card if it isn’t the correct one. This is important because when a computer searches through data this is the most basic step it performs, it can only compare two things at a time so our algorithm must only compare two things at a time.

#### Worauf Sie beispielsweise achten können:

Who are the students who are able to break the problem down into steps and then explain why each step is important?

Which students can articulate that the computer is only checking one number at a time, and so can only eliminate one number at a time.

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

The generalised idea of this activity is that any searching problem where the data being searched is not organised into some structure or order can only be approached using sequential search. Recognising this pattern can save students, and programmers, time because when they encounter this problem in the future they are aware that they do not need to spend their time trying to come up with an especially clever solution. This situation can be generalised to apply to any type of data.

#### Worauf Sie beispielsweise achten können:

Which students quickly understand that this is actually no different to playing the “how many guesses game” in lesson one?

{panel end}

{panel type="ct-evaluation"}

# Auswertung

Students will be evaluating sequential search when they collect and examine the statistics of how many boxes they had to check. They can further evaluate it by collecting the number of guesses it takes to search through larger numbers of boxes and examining these statistics. For example, what do students think will happen if there are twice as many boxes to search through? 10 times as many? 1,000,000 as many? Would this algorithm be efficient for this many boxes?

#### Worauf Sie beispielsweise achten können:

How much longer would this take if there were twice as many cards? 10 times as many cards? Search engines routinely search through billions of web pages to find the term you're looking for, would this algorithm be efficient for this application? Discuss other ideas on how you could find a number more effectively.

{panel end}

{panel type="ct-logic"}

# Logik

Let's think about the problem logically: The cards have been placed in a random order, therefore all we learn when we look at a card is what is on that card, we don’t learn anything at all about what is on the other cards. Since all we can learn from checking a card is whether or not that card is the one we are searching for, it doesn’t matter what order we check the cards in because it won’t change the fact that we have to check each card, one-by-one, until we find the correct one.

#### Worauf Sie beispielsweise achten können:

Which students can explain why it would be easier to find the money if the boxes where in sorted order?

Ask the students if it would be worth sorting these boxes into order, and look for the students who can identify why this might not be worth it if you're only doing the search once (we only need to search through the boxes once because once we’ve found the money there is no point looking for it again! So sorting them wouldn’t be helpful, it would actually slow things down).

{panel end}