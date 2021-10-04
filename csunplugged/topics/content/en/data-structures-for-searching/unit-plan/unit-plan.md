# Data structures for searching

{image file-path="img/topics/data-structures-for-searching-search-icon.png" alt="Searching through items."}

The previous lessons in the Searching algorithms unit have shown that the way we organise data can affect which algorithms we can use for searching through it.
An unsorted list can't be searched with a binary search; the only way to search through it is to use a sequential search.
A sequential search could be used to search a sorted list, but when the list is sorted we can use a binary search, which is a much faster algorithm.

{image file-path="img/topics/data-structures-for-searching-binary-vs-hash.png" alt="Binary search tree vs hash table."}

In computer science, the way we organise data to make it easier to work with is called a data structure.
A sorted list is a very simple kind of data structure, where the way it is organised makes binary search possible.
In this unit we'll look at two completely different data structures, binary search trees and hash tables, that are commonly used as the basis for searching when it is done in practice on computers.
Both have close ties to sequential and binary search, but they are more flexible in most practical situations.

It’s great to study these, because they give insights into unexpected ways that we can make programs work better.
In practice they are often built into programming languages, so you don’t need to write your own code for them, but even if you don’t need to build one yourself, it’s good to understand how they work, and what their strengths and weaknesses are.

Computer scientists generally think of a searching problem as being supplied with a "key", such as an account number, person's name, or geographic location, and looking up some values associated with that key, such as the account balance, address, or name of a building.
For example, if you search for a city using an online map, the name of the city is the key, and the data associated with it is its location on the map.
Sometimes you just need to know if the key exists; for example, a spelling checker might search for a word, and if it's not in the dictionary then it can mark it as an error.

## Digital Technologies | Data Structures

One of the data structures that will be explained in this unit is the **binary search tree**; these have a lot of the same benefits as sorted lists, but make it a lot easier to keep the data organised.
Trees in general come up a lot in computer science because they provide a very structured way to keep information organised - even the structure of folders used on a personal computer is a type of tree - so studying a particular kind of tree called a binary search tree is a good introduction to ideas that keep coming up when developing software.
Another structure that we introduce in this unit is a **hash table**.
These are similar to a list of data, but data is placed at very specific points in the list, rather than being in a completely random or a completely sorted order.
The main idea of a hash table is that you can apply a simple calculation (called a hash function) to the key that you're looking for, and that will tell you where to look for it in the hash table.
This means it gives instant access (most of the time) to the information you’re looking for.
Of course, there are a lot of details that we need to get right to make this work well, but hashing is the basis of the fastest methods for searching.
The idea of hashing comes up in other areas of computer science too, and is even an essential part of how organisations can store passwords securely.

{panel type="teaching"}

# Teaching observations

{image file-path="img/topics/data-structures-for-searching-hash-vs-hash.png" alt="Hashtags are not the same as hash tables."}

Students may try to make a connection between hashing and using hashtags.
They are actually completely different things.
The names have different derivations, and just happen to be the same word (hashtag is from the shape of the # symbol, which in turn is probably related to the word “hatch”, whereas hashing is based on mixing up the symbols that represent a value, which is more related to the usage in “hash browns”, derived from the French word “hacher”, which means to chop up).
Hashing when dealing with searching data should be treated as a completely new concept from hashtags, although confusingly, when you search for a hashtag, it may well be found using a hash table!

{panel end}

##  Vocabulary Explained

### Hashing

Taking a number, word, or other item being searched for, and converting it to a number using a mathematical function.
This number can be used to find out where the data is stored.
For example, a simple way to hash a word into a number is to convert each letter to a number (e.g. a=1, b=2...), and add up those numbers.

{image file-path="img/topics/data-structures-for-searching-funnel-water.png" alt="A funnel is much easier to use when you pour the water into the wider end!"}

### One way function

A calculation that is easy to do one way, but hard to run backwards.
For example, you might be able to work out 2,111 x 3,709 by hand, but can you work out which two values multiply together to give 55,315,681?

### Data structure

A way of organising data so that it can be accessed more efficiently.

### Tree

Any structure where you can start at a “root” and follow branches to access information.
As well as search trees (which we focus on here), the same kind of structures occur in many other situations, including family trees, organisational charts and file systems.

### Key

The value that we want the computer to search for.
Typically it’s a login name, customer number, product name, or anything that someone might type into a search box in an app or web site.

## Real World Implications

Binary search trees are also the basis of a commonly used structure where the relationships between the keys are important - especially if you're looking for values similar to the one being searched for.
Hashing, and using hash functions supports programmers to make really fast searching algorithms.
This approach might seem almost fanciful at first because it relies a lot on randomness - making a very random value by chopping up and mixing the key you're searching for, and hoping that not too many other things come out to the same value.
Fortunately the statistics around this are well understood, and people can design very fast and efficient hash tables. 

{image file-path="img/topics/data-structures-for-searching-searching-girl.png" alt="Using a search engine."}

There are many variations on hash tables and search trees, but chances are that if you are looking something up on a computer system it will be using software based on these ideas, whether it's checking your online account balance, getting the price of a product in a shop, or looking for a web page using a search engine.

## Reflection Questions

- What was most surprising about the learning that happened from the teaching of this unit?
- Who were the students who were very systematic in their activities?
- Who were the students who were very detailed in their activities?
- What would I change in my delivery of this unit?
