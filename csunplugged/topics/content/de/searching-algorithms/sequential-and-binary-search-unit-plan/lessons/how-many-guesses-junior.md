# How many guesses?

## Key questions

Suppose you lent a friend your favourite book to read and can’t remember who you lent it to. Imagine these 6 houses represent where they live. You need it back urgently because you are going on holiday tomorrow, so you start visiting each house to see if they have your book.

{image file-path="img/topics/houses_randomnumbers.png" alt="Six houses numbered 16, 24, 36, 41, 48, and 56"}

How many houses do you predict you will need to visit to find the one where your book is? Write the number of guesses you think and your initials on a post-it note. Place your post-it on a continuum like the one below.

{image file-path="img/topics/6_guesses.png" alt="A continuum line with marks for 1, 2, 3, 4, 5, and 6 guesses"}

What do you notice about our predictions?

**Mögliche Antworten wären beispielsweise:**

- That we had different numbers of guesses, because you might get lucky and find your book at the first house, but you might also could be unlucky and find your book at the last house.
- Three and four guesses are likely to be popular because that’s approximately half way (this is indeed close to the average that could be expected).
- Some students might choose 6 guesses; that is the most that would ever be needed.

{panel type="teaching"}

# Teaching observations

Students might expect that they could be 'lucky' and find the book early, or they might pessimistically go for the worst case, where it's in the last few houses that they visit. The activity below will illustrate that both of these cases could happen, but the actual number will be randomly distributed, so there's no simple answer to the question.

{panel end}

## Lesson starter

Place the 15 searching squares on a table. Explain that we have 15 different numbers, one on each card. Show that one side has an animal on it and the other a number. Under each of these cards is a number that you can’t see, and they aren’t in order. The numbers range from 1 to 15. Can you find the card with the number 12?

{panel type="teaching"}

# Teaching observations

You can adapt the range to suit what your students are working on in their mathematics lessons. This lesson focuses on unsorted lists so it doesn’t matter if the numbers are all from a sequential range (for example: all the numbers in the range from 1 - 15), as long as the cards are placed in a random order. When you’re using a sorted list in future exercises though it works better to not have all the numbers from a certain range, otherwise students can just count to figure out where the number is! You can generate different sets of cards with various ranges of numbers [here]('resources:resource' 'searching-cards').

{panel end}

## Lektionsaktivitäten

Set up a line of 15 cards, with the animal facing upwards.

Have a payment system ready such as tokens for your classroom, counters, sweets, or marbles. The game could be set to have some real stakes - for example: I have 10 marbles, and each is worth 2 minutes of free time. For every guess you make you have to pay me one marble.

Say to the students: let’s see how many guesses it takes to find the number 4.

Who would like the first guess? (Choose a student). Which animal should I turn over? Tell us why you chose that guess. (There's no particular logic for which card to choose, but students might choose to be methodical and go from left to right, or simply choose cards at random.)

Turn over the chosen card to show the number under it. If it's the correct one, you can stop, otherwise *remove it from the row and put it aside* and have the student pay you with one marble (or with whatever you are using as tokens). Repeat this process until a student chooses the card with your number on it (you should carry on even if they have lost all their tokens). If at the end of the game the student has no tokens left then you have one, and if they found it before using all their marbles then they win the game.

If you find they guessed the number quickly, then shuffle the cards and repeat the game to demonstrate that they might guess on the first guess, but likewise it could be the very last guess as well. At the beginning of a new game the student starts with all their tokens again.

How many guesses did it take to find the number this time?

With each guess, how many cards were eliminated from being a possibility? (Answer one - each question can only get rid of one option).

Did the students win because they guessed within 10 guesses or did you win because it took them longer and they lost all their tokens? Repeat this game until the students have won 3 times or you have won 3 times. You should shuffle the cards each time, and introduce new cards or different sets if necessary to avoid students memorising what is on each card.

{panel type="teaching"}

# Teaching observations

The number of guesses required can be anything from 1 (if you are lucky and find the number on the first guess), to 15 (if you’re very unlucky and have to turn over every card). The number of guesses should be evenly distributed between 1 and 15 - each number is equally likely. Students could also work out the average (which should be close to 7 if enough games are played). This also means that most of the time students won't have any tokens left if you start with 5 for each search.

{panel end}

You can repeat this game using the 0 - 100 searching cards, or you can use the blank searching cards to create your own numbers. You can also use the blank searching cards to make a game which uses letters, words etc. instead of numbers.

## Applying what we have just learnt

This algorithm is a practical one that is sometimes used for searching for data on a computer. It's very useful to be able to predict how long an algorithm will take. In this lesson, it might seem unpredictable, but there are some definite conclusions that can be drawn. For example, if there are 15 cards, you never need to look at more than 15 items, and it's a matter of luck whether you find it very quickly or if it's the last one you look at. A worse algorithm would be to pick a card at random, check it, put it back, and repeat this until you find what you're looking for; this could theoretically go on forever!

## Lesson reflection

The method you have been using is called sequential search - if the values are out of order then we just go through them in some sequence until we find the one we want. What is the algorithm for a sequential search?

- Repeat until the number is found. 
    - Remove one item from the payment system
    - Turn over a card.
    - If it isn’t the card you are searching for then remove that card (or leave the card turned over to show the number).

How much longer will this take if we give the algorithm twice as many cards to search? (It will take twice as long, on average.) We will explore more accurate statistics to measure this at older ages.