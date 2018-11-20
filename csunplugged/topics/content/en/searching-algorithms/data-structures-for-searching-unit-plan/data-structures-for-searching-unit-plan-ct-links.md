{panel type="ct-algorithm"}

# Algorithmic thinking

Searching through data is something computers do all the time, just think about how often we need to search for words in documents and information on the internet!
Searching efficiently is a very important problem, and computer scientists have worked for a long time on solving this.
To solve this problem we need algorithms, processes that can be followed each time we search for something, and many different ones have been developed.
Each of these algorithms can be seen as a solution to a problem.

In this unit students will be exploring algorithms for using two different data structures: hash tables, and binary search trees.
For each of these data structures they will be learning, and following algorithms for creating the structures, searching through them, and adding data to them.
These algorithms are different for each of these data structures, but they are also linked to sequential search, and binary search.

{panel end}

{panel type="ct-abstraction"}

# Abstraction

We often have to deal with large amounts of data and complexity when we are working on computational problems.
To help us manage that complexity we can use data structures to organise and represent data in a certain way. Using data structures is a way of encapsulating the data so that we can focus on what the data represents, rather than the details of how each individual piece of data is used.

The two data structures explored in this unit are hash tables, and binary search trees.
These data structures each store and organise data in different ways and have different structures, but both allow you to do the same thing - search for, and find data very quickly.
If you simply want to use one of these data structures (rather than creating one and implementing it on a computational device) to find data, you don’t need to think about every small step it goes through to find the data for you, this information is hidden.
All you need to focus on is that when you search for something, it will be found quickly for you.

{image file-path="img/topics/old-computer-child-computer.png" alt="A older computer passes a book labelled pre-programmed data structures to a child computer."}

When programmers develop software they often use libraries, which contain lots of pre-programmed data structures (such as hash tables) that they can use in their own programs.
This is very helpful because it means they don’t need to spend their time re-implementing these data structures, they don’t need to worry about all the nitty-gritty details, and the code in these libraries has already been very thoroughly tested.

{panel end}

{panel type="ct-decomposition"}

# Decomposition

Using data structures allows us to view a problem from a higher level, without having to focus on each individual part of how the problem, and it’s solution, work.
But to create good data structures and understand how, and why they work, we need to break them down into their components and see how each of these functions and how they fit together.
To implement these data structures we have to focus on smaller details, and the step-by-step processes that are carried out when we create one of these structures, add data into it, search for data, and remove it.

In this unit there is also an important example of the divide and conquer method, which we looked at in the sequential and binary search unit.
Binary search trees can be highly efficient because they are based on using the divide and conquer method to search for data, and do this in a very similar way to binary search.

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

There are many patterns (some algorithmic, some mathematical, and some abstract concepts) that appear throughout this unit.
We have included several in our explanations, but it’s possible that students will come across more as well!

Hashing, and using hash functions, is a strategy that appears in many different areas in Computer Science.
Along with searching, it is common in error detection and correction, in cryptography, and in security.
In fact, if you have learnt about check digits in the error detection and correction unit, then you have already used hash functions.
The way formula we use to calculate a check digit is a hash function.
When we use hash tables for searching we use hash functions to locate data, and in these other areas it is used to validate data and check it is correct.

Some of the hash functions used in this unit, for specific sized hash tables, follow a pattern.
This pattern can be used to make an algorithm that means we can apply these hash functions to hash tables of any size.
This means we can generalise our hash function so it is applicable in a range of situations.

Another familiar pattern you will come across is the divide and conquer strategy.
We used this strategy when we explored binary search, and will use it again when we learn about binary search trees

There are many different types of data structures - in fact, people create them all the time to fit with specific problems or types of data, but there are several well established ones which most other data structures are based on.
Often students learn the general properties of various structures to help choose between them.

{panel end}

{panel type="ct-evaluation"}

# Evaluation

{image file-path="img/topics/kid-thinking-data.png" alt="A child thinks about data."}

Different data structures have different strengths and weaknesses, there is no magical data structure that will perfectly suit any problem!
So when we decide which data structure(s) to use when solving a problem we need to take into account several factors, for example: what type(s) of data are we going to be using?
Is speed important for this task?
Is it important that we don’t use too much computer memory?
Is it more important for our data structure to work very fast, or use a small amount of memory?

The factors you need to think about will be different for different problems, and in some cases there are factors which will only matter if you are actually programming your solution (such as how much memory it uses).

When we select which data structures to use we must evaluate them based on these factors, and choose the one we think is most suitable for the problem.
When we create our data structures we also have to evaluate the individual parts of them to ensure they function well.
For example it is important to evaluate the hash function that a hash table uses, which is described in the logic section.

{panel end}

{panel type="ct-logic"}

# Logic

To design data structures to work well we must use our logic skills.
For example, we need to design the hash function we choose to use for a hash table, as it has a large impact on how we store data in the hash table, and this in turn has a large impact on how quickly we can search through it.

{image file-path="img/topics/bad-cubbyhole.png" alt="A computer has placed all the data in one spot on the hash table and a person is frustrated with the computer's actions."}

What are some things a good hash function should do?
If we want to be able to find things in the hash table quickly then it won’t be a good thing if our hash functions places everything in the same slot in the table, because then we will have to search through all the data in that slot.
This would make our hash table rather pointless.
But if the data is spread out within the table then it is much more likely that we will find the correct piece of data on our first check.
Therefore a good hash function should ensure that every piece of data will end up in a different slot in the table.
In some of the examples we added the digits of a value together to get a hash value.
But what would happen if we multiply them together?
This might appear to produce a better range of values, but (applying some logic) we can realise that if any of the digits is a zero, then the hash total will be zero, so this value will become more likely to occur.
There are many other combinations of arithmetic we could apply, but good reasoning needs to be applied to make sure that it doesn't turn out to hash lots of values to the same place.

{panel end}
