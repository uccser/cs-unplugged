# Searching with a Hash Table

## Key questions

Suppose you had to answer questions about a fiction book really quickly for a competition (such as "Where was Charlie when he realised he had the ticket?"), how would you organise it all so that you could answer the questions faster than anyone else?

### Potential answers could include:

-   Make an index of all the main characters and events.

-   Put information in alphabetical order.

-   Reference the page numbers that corresponds to each of these.

## Lesson starter

The binary searching algorithm was much faster and more efficient than the sequential searching algorithm. But there are other searching algorithms used in programs to find the right data even faster! One way is using Hash Tables. You can discover how it works by playing the Hash Table relay game.
It is based on generating a simple number from the longer number on the cards which is called a hash total. In this activity we're going to take the number, and apply a simple formula to it to get a number between 0 and 9. The formula is to add all the digits together, and take the right-most digit of the answer. For example, for the number 9240 you want to calculate the hash total you add the digits together (9+2+4+0 = 15), and take the 5 from the end. The result is referred to as a "hash" of the original number - it's a meaningless value derived from it, but a key point is that given the same original number, you'll always get the same hash value. Hashing a value is when you convert it into a hash total.
Set up the Hash Table relay game outside or in your classroom. 

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |

-   Put 20 numbers faced down in a hula hoop.

-   Draw a chalk table that has 10 compartments (or draw it on a whiteboard if you are running this activity inside).

{panel type="teaching"}

# Teaching observations

The terms "hash total" and "hashing"  are technical terms that comes up often in computer science. It's a fairly simple concept - you convert an input into a unique but fairly meaningless new value. This is surprisingly useful for several purposes. It's useful to introduce the word "hash" here and use it when referring to the total so that students learn this language.

{panel end}

Here are some examples of hashing based on the algorithm mentioned above.

| Original  | Sum of digits  | Last digit of sum |
|-----------|----------------|-------------------|
| 123       | 6              | 6                 |
| 999       | 27             | 7                 |
| 916       | 16             | 6                 |
| 900       | 9              | 9                 |
| 4321      | 10             | 0                 |
| 1234      | 10             | 0                 |
| 37281964  | 40             | 0                 |

{panel type="math"}

# Mathematical links

The right-most digit is actually the modulo 10 value. See the [https://csunplugged.org/en/topics/kidbots/unit-plan/modulo/](lesson on modulo) for more detail on how this idea works..

{panel end}
