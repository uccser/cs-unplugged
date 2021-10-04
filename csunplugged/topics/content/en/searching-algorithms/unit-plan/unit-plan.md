# Sequential and binary search

{comment Video 1: Sequential search: Random numbered cards with pictures on them. (using numbers from 0 - 31) - SETTING: As if it’s a maths group in a class setting}

{comment Video 2: Binary search using numbered cards with pictures on them ranging from 0 - 999.}

{comment Video 3: Linking the "Number Hunt" activities to statistics.}

{image file-path="img/topics/different-sized-haystacks.png" alt="A farmer can easily find a needle in a small haystack, but can't find it in a large haystack."}

Searching for a keyword, a value, or a specific piece of data (information) is the basis of many computing applications, whether it’s looking up a bank account balance, using an internet search engine, or searching for a file on your laptop.
Computers deal with a lot of information so we need efficient algorithms for searching.
This unit explores some common algorithms that are used to search for data on computers, with the opportunity to integrate this learning with statistics.

Because computers are often required to find information in collections of data that can be very, very large, using the right algorithm for searching is crucial!
A key idea in computer science that we'll be illustrating with searching algorithms is just how fast an algorithm can be; students might think that if you're searching twice as much data then it should take twice as long, but we'll look at a way to search that takes almost the same amount of time to search 2 million items as it would for 1 million.

We'll also look at the kind of steps that algorithms use to solve the important problem of searching data.
When you’re telling a computer how to find exactly what you’re looking for you need to remember that computers are simple machines, they can only look at one piece of data at a time, and check if it is what you’re searching for.
Imagine if every time a computer had to search for something, it had to compare every single piece of information it contained to the information it was searching for before it found what you were looking for? It would take a very long time to find what you wanted.
That’s why computer scientists need to develop quick and efficient ways of doing this.

For computer scientists finding the right algorithm requires analysing the time taken and the amount of memory used.
Some great discussion questions are:

Is it always useful to sort your data so you can complete a binary search?
Let’s look at a word processor, you have 100 pages of text and want to find one word.
Why wouldn’t the word processor sort your words into order to find the word you are looking for?

A consideration that computer scientists take into account is how many times are you likely to search for something.
If it’s only once, then it isn’t worth the effort to sort and then find the item.

## Digital Technologies | Algorithms

This unit demonstrates two different search methods: _sequential_ (sometimes called _linear_) search, and _binary_ search.
We'll see that binary search is remarkably fast, and although there are other search algorithms that are can do even better (such as the _hash table_, which is covered in the unit on Data Structures for search algorithms), the step-up from sequential search to binary search demonstrates how much there is to gain there is to be made by applying the right algorithm to the job.

{image file-path="img/topics/computer_searching.png" alt="Cartoon computer looking around with a magnifying glass"}

People expect computers to find information very quickly, and the speed of search algorithms has a big influence on our experience as users.
A search engine typically searches billions of web pages in less than a second, which is the kind of time-frame that humans are used to working in.
We don’t like seeing the “wheel of doom” appear while the computer is processing/thinking about what to do, and if an app is too slow then people won’t want to use it.

This unit focuses on understanding two simple searching algorithms, and comparing how long they can take to reliably find the correct data (a number or word, for example).

## Vocabulary explained

**Data**: The way information is stored.
Numbers are a type of data you will come across very often (e.g. account numbers, customer numbers, card numbers, serial numbers, product numbers and so on).
It could also be text (such as words that we're searching for), dates, and even images and sound.
You can think of anything stored in a computer's memory as data; it’s all pieces of information.

**Raw data**: Raw data means ‘unprocessed data’ which has been collected from a source, and has not been cleaned up or used yet.
For example, say you had measured the temperature every day of the year, and now you have a bunch of numbers, this could be called your ‘unprocessed data’.
If you then divided this data into each month of the year, and averaged it so you had the average temperature for each month, this would be your ‘processed data’.

**Sequential search**: A sequential search is when you look at each piece of data, one by one, and don’t stop until you find what you are looking for.
You can use a sequential search on any data, whether it is sorted or unsorted (though it would be potentially a slow way to locate what you are looking for if the data is in sorted order!)
However, sequential search is the **only** option you can use when you need to search through data that is **unsorted**.
Say for example you are looking for the word “is” in the following list: “the”, “my”, "it", “is”, “said”, “a”, “from”.
A computer would go to the first word “the” and ask is it the same as “is”.
If it is it will stop searching, if it isn’t, it will go to the next word and repeat this process until it finds the matching data.
In this case it takes 5 guesses to find the word.
It could have taken up to 7 guesses or just 1 guess, depending on which word you were searching for.

Imagine our detective (below) is programmed to do a sequential search to find the word **"said"**. Here’s the process or algorithm he would follow to find it.
Notice he can only compare one word at a time!

Now imagine if he has a million words to search!

{image file-path="img/topics/sequential_detective.gif" alt="A detective looking at words sequentially in a sentence until he finds the word 'said'"}

**Binary search**: An algorithm that tells us how to efficiently find a specific value in an **ordered (sorted)** list.
It is called ‘binary’ search because each time you look at a value in the list you divide the list into 2 parts, one is discarded and the other is kept.
The word "binary" here just means something that has two parts, such as a binary star system (made of two stars); binary search shouldn't be confused with binary numbers.

Suppose our detective is looking for the word **"said"** from the following list, which is in alphabetical order: “a”, “from”, “is”, “it”, “my”, “said”, “the”.
First the computer will go straight to the middle word, “it”  and see if that matches - because it doesn’t, the computer doesn’t need to check the 3 words to the left.
Now the computer finds the middle word of the right half of the list, which is “said”.
Binary search narrows in on the location of the word very quickly.

{image file-path="img/topics/binary_detective.gif" alt="A detective trying to find the word 'said' in a sentence using binary search"}

## Real world implications

We can apply these search strategies ourselves when we are looking to find one thing.
Every time we play games like “guess my number” we can apply the binary search to it.
Likewise if we are searching for a book in the library that hasn’t been returned to the correct place, we’ll need to do a sequential search to find it.
Searching is everywhere in our lives, from finding a person’s address to looking up a phone number in a phone book.
We can apply binary or sequential search methods depending on how the data has been organised to start with.

{panel type="math"}

# Mathematical links

This unit could be taught within a statistics unit at all curriculum levels to support students' understanding of why particular searching methods are faster than others.

{panel end}

## Reflection questions

What was most surprising about the learning that happened from the teaching of this unit?


Who were the students who were very systematic in their activities?


Who were the students who were very detailed in their activities?


What would I change in my delivery of this unit?
