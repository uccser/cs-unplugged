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

| Original       | Sum of digits  | Last digit of sum |
|----------------|----------------|-------------------|
| 123            | 6              | 6                 |
| 999            | 27             | 7                 |
| 916            | 16             | 6                 |
| 900            | 9              | 9                 |
| 4321           | 10             | 0                 |
| 1234           | 10             | 0                 |
| 37281964       | 40             | 0                 |

{panel type="math"}

# Mathematical links

The right-most digit is actually the modulo 10 value. See the [lesson on modulo](https://csunplugged.org/en/topics/kidbots/unit-plan/modulo/) for more detail on how this idea works..

{panel end}

## Lesson activities

1.  Split the group into two and have one group line up beside their hash table and the other beside their hash table. Ideally you’d have between 4 - 6 in each group, so set up as many hash tables as space or the number of students allows.

2. Explain that the object of the relay race is to be the quickest team to input the data (cards) into their hash table. Students need to count the number of collisions they have in their hash table. A collision is where there is more than one piece of data in the column. If a piece of data is put into the incorrect column, then the table is corrupted. 

3. The team that works together has a higher chance of succeeding. The first runner runs to pick up a card and takes it back to the group. They calculate the hash total together to decide which column to place the card (data).
 
4. Walk through where a player moves up to get a card, then runs back to their team, places the card, then tags the next player and stand at the back of the line.

5. Repeat until all the cards are gone and placed within the hash table. 

6. Count how many collisions your team has.

7. The teams are now going to swap hash tables. Before swapping each team
    -   chooses 5 values that the other team must find in their hash table. 
    -   writes these down on a piece of paper or on a whiteboard. 
    -   turns the numbers over in the hash table so they are facing down. 
They then swap tables and hand over the list of values they are looking for and have another relay race. 

8. A student needs to run to the hola hoop, complete an agreed exercise for example 10 star jumpes and run back again before they can turn another card over. If it's not on the list then they put the number aside. The winning team is the first one to have all 5 values on the list.

{panel type="teaching"}

# Teaching observations

Teams will want to choose numbers in slots that have a large number of collisions, but as values are removed from them, another slot may become the "worst" slot. This forces them to think about the best strategy; from a computer science point of view, this is evaluating what the worst case might be.

{panel end}

{panel type="math"}

# Mathematical links

Statistics: Have the students try to predict the number of guesses they think they will need. (It will depend on the number of cards in the table, but the number of guesses will be between the smallest and largest group sizes, and on average should be the average group size). Gather the raw data of the number of guesses made and graph it on a bar chart. 

{panel end}

## Follow up discusion

1. Collect and discuss the scores. 

2. Which numbers are very quick to find? (The ones that are alone in their column.) Which numbers may take longer to find? (The ones whose columns contain lots of other cards.) 

3. Which of the three searching processes (sequential search, binary search, hash search) is fastest? Why? What are the advantages of each of the three different ways of searching? (The binary search strategy is faster than sequential search, but sequential search doesn’t require the numbers to be sorted into order. The hashing strategy is usually faster than the other two, but it is possible, by chance, for it to be very slow as lots of numbers might end up in the same column. In the worst case, if all the numbers happen to end up in the same group, it is just the same as a sequential search - you need to check all the numbers until you find the right one.) And to use the hashing strategy we also have to first build the hash table, which also takes time.

4. What would happen if you were searching for a value that wasn't there? (You'd end up going through all numbers in the columns, but once you had checked them all you would be done, and would know you wouldn't need to look at any other columns).

## Applying what we have just learnt

The columns of numbers are usually referred to as "buckets" or "slots" in the hash table. The hash tables in this lesson had just 10 slots in them. In practice the number of slots is usually similar to the number of things being searched; if you have 1,000,000 customers, you might have up to 2,000,000 slots in the hash table, which means that most of the time you only have one thing in any slot. This makes for very fast searching - you'll usually go straight to what you're looking for. This is why hashing is so popular.

Working with 10 slots is easy, since we can just take the last digit of the hash total. 100 slots would also be easy - just use the last two digits. In practice, we use the "modulo" function, which converts the hash total to a limited range. For example, if your hash total for an item is 39, and you have 15 slots, the slot number for that item would be 39 modulo 15, which is 9. There's more information about this in the lesson on [modulo arithmetic](https://csunplugged.org/en/topics/kidbots/unit-plan/modulo/).

Hashing a value seems very "random", but in fact it's a very powerful idea for several purposes, including fast searching as it was used for here. It is also used to calculate check digits for error detection, and for important applications in cryptography. Using hashing for searching does have a downside however: with the sorted list for binary search, similar values will be next to each other, but in a hash table similar values can hash to very different places, so it's hard to find things that are close to what you're looking for (such as all the names between L and P). But hashing is very fast and it is the method of choice if you're just needing to look something up like an account number or product code.

## Follow up task

[Hash Table worksheet]("resources:resource" "hash-table-worksheet").

## Lesson reflection

What is the algorithm for finding something in a hash table? (You may need to help students realise that it involves a sequential search after the group has been identified.)
