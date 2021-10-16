# The Great Number Hunt (Unsorted)

## Key questions

{image file-path="img/topics/child_searches_book.png" alt="A child searches through some unsorted books on a shelf"}

How would you find the a book on a bookshelf, when all the books aren’t in any particular order?
Are there any other methods you could use?

### Potential answers

{image file-path="img/topics/linear_search.gif" alt="This animation shows that the only way to search the unsorted list is to go through every item (whether they choose randomly or look at the first, then second, then third…) because they are still just checking and eliminating one at a time."}

Guide students to discuss the algorithm or process that they would use to find a value in an unsorted list and how that would be harder than in a sorted list.
Help them to recognise that the only way to search the unsorted list is to go through every item (whether they choose randomly or look at the first, then second, then third…) because they are still just checking and eliminating one at a time.

## Lesson starter

On each sheet are 31 number boxes with lots of money in them. All money has a serial number on it and in each of the number boxes all the notes start with the same serial number.
The only problem is there is only one number box that has the real money in it, the rest are fake.
You know what the serial number on the real money is, and your challenge is to find the number box with the real money in it, but you should "open" as few number boxes as possible.

Guide students through how the game will work by following the instructions on the [Number Hunt]('resources:resource' 'number-hunt').

{panel type="teaching"}

# Teaching observations

If students make the connection that the real money serial could have a check digit, they would be correct in that what they learnt in the error detection and correction unit would apply in knowing if the serial number represents real money or fake money.
Here’s a link to the [Error Detection and Correction unit]('topics:unit_plan' 'error-detection-and-correction' 'unit-plan') for more information.
However, this isn't the purpose of this exercise; the goal is to find a number in the number boxes.

{panel end}

{panel type="math"}

# Mathematical Links

This is a teachable moment for the class to discuss different strategies to ensure the least number of guesses are needed.
The only useful strategy in this case is to make sure that you don't ask for the same box twice i.e. record which ones you have looked at.
This will give a number of guesses between 1 and the total number of boxes.

Statistics: Gather the raw data of the number of guesses made by each student and graph it on a bar chart.
Repeat the game a number of times to see what the pattern of data is.

Number Knowledge: Read and say numbers between 100 and 9999.

{panel end}

## Lesson activities

1.  Organise your class into pairs.
2.  They need a hard surface to write on and a pencil or pen (or whiteboard pen if you have laminated the sheets).
3.  Have students seated back to back.
4.  Have everyone come up and get a [Number Hunt printable]('resources:resource' 'number-hunt').
5.  Go through the instructions and set up their games.
6.  Play the game and have students add up how many guesses it took each of them to find the number box with the correct number in it.
7.  Add this data to either a class sheet to graph on paper or add it to a spreadsheet that also displays the graph and what the graph grow as more data becomes available.

{panel type="teaching"}

# Teaching observations

It is recommended to have the activity from lesson one and lesson two set up for students to move on to when they have both finished guessing their numbers, or else new sheets with different numbers on for them to try again.
As the range of guesses could be the first guess through to 31 guesses, the time delay for everyone finishing means that some students will have nothing to do for 10 or 15 minutes.
Having the other searching algorithm games available helps with classroom management.

{panel end}

## Applying what we have just learnt

{comment Add replacement image of img/topics/linear_search_chests.gif}

The method you have been using is called sequential search - if the values are out of order then we just go through them one-by-one, in some sequence, until we find the one we want.
Some people probably found the number in one or two questions, while others may have "opened" most of the 31 boxes before they found it.
This algorithm is very variable in the time taken - sometimes it's instant, sometimes it's slow, and on average, you'll go halfway through the list of values.

## Lesson reflection

Can you write down the algorithm for a sequential search for the Number Hunt game?
