# The Great Number Hunt (Sorted)

## Key questions

{image file-path="img/topics/binary_search_books.png" alt="A row of books in alphabetical order."}

How would you look for a book in a library if the books were sorted in alphabetical order? Is that easier than if they were out of order?

### Potential answers

Guide students to discuss the algorithm or process that they would use to find a value in a sorted list and how that would be different in an unsorted list. Help them to recognise that the best way to search the sorted list is to do a binary search: it does matter what order they actually look at the books.

## Lesson starter

As with lesson 3, on each sheet are 31 number boxes with lots of money in them. All money has a serial number on it and in each of the number boxes all the notes start with the same serial number. The only problem is there is only one number box that has the real money in it, the rest are fake. You know what the serial number on the real money is, and your challenge is to find the number box with the real money in it, in the least amount of guesses.

Guide students through how the game will work by following the instructions on the [Number Hunt]('resources:resource' 'number-hunt') (although this time the numbers will be in sorted order).

{panel type="math"}

# Mathematical Links

This is a teachable moment for the class to discuss different strategies to ensure the smallest number of guesses is used. It's not essential that they use the "best" method (starting with the middle item), since they will learn the hard way that this would have been a good idea, but it may save some frustration if they become aware of the strategy in advance.

Statistics: Gather the raw data of the number of guesses made and graph it on a bar chart. Repeat the game a number of times to see what the pattern of data is.

Number Knowledge: Read and say numbers between 100 and 9999.

{panel end}

## Lektionsaktivitäten

1. Organise your class into pairs.
2. They need a hard surface to write on and a pencil or pen (or whiteboard pen if you have laminated the sheets).
3. Have students seated back to back.
4. Have everyone come up and get a [Number Hunt printable]('resources:resource' 'number-hunt').
5. Go through the instructions and set up their games.
6. Play the game and have students add up how many guesses it took each of them to find the number box with the correct number in it.
7. Add this data to either a class sheet to graph on paper or add it to a spreadsheet that also displays the graph and what the graph grow as more data becomes available.

## Applying what we have just learnt

{image file-path="img/topics/marbles.png" alt="The number of marbles are halved each time."}

The method you have been using is called binary search - if the values are in order then we can eliminate half of the numbers with each guess until we find the one we want. This is an incredibly efficient algorithm that we can use for searching a sorted list.

It also shows how sometimes algorithms aren’t strongly affected by how big the problem gets - we can search billions of items (e.g. every web site we can find) using this method; if we had 1,000,000,000,000 number boxes, you'd only need to open 40 of them to find a particular one; and doubling the number of boxes only adds one more question to finding a value. This is a pleasant contrast to some other problems where we don't have such efficient algorithms.

## Lesson reflection

{comment Add replacement image of img/topics/binary_search_chests.gif}

What is the algorithm for a binary search for the Number Hunt game?