# Data structures for searching

{image file-path="img/topics/searching-table.png" alt="A person searches for an item on a table covered in food."}

The previous lessons in the searching algorithms unit have shown that the way we organise data can affect which algorithms we can use for searching through it.
An unsorted list can't be searched with a binary search; the only way to search through it is to use a sequential search.
A sequential search could be used to search a sorted list, but when the list is sorted we can use a binary search, which is a much faster algorithm.

{image file-path="img/topics/binary-vs-hash.png" alt="The image has a diagram of a hash table and a diagram of a binary tree."}

In computer science, data structures are used to organise data in a way that makes it easier to work with.
A sorted list is a very simple kind of data structure, where the organisation makes binary search possible.
In this unit we'll look at two completely different data structures, hash tables and binary search trees, that are a common basis of searching when it is done in practice on computers.
Both have close ties to sequential and binary search, but they are more flexible in most practical situations.

Computer scientists generally think of a searching problem as being supplied with a "key", such as an account number, person's name, or geographic location, and looking up some values associated with that key, such as the account balance, address, or name of a building.
For example, if you search for a city using an online map, the name of the city is the key, and the data associated with it is its location on the map.
Sometimes you just need to know if the key exists; for example, a spelling checker might search for a word, and if it's not in the dictionary then it can mark it as an error.

A hash table is similar to a list of data, but data is placed at very specific points in the list, rather than being in a random or a sorted order.
The main idea of a hash table is that you can apply a simple calculation (called a hash function) to the key that you're looking for, and that will tell you where to look for it in the hash table.
This means it gives direct access (most of the time) to the information you’re looking for.
Of course, there are a lot of details that we need to get right, but this is the basis of the fastest methods for searching.
The idea of hashing comes up in other areas of computer science, and is even an essential part of how organisations can store passwords securely.

Another structure that we look at in this unit is the binary search tree; these have a lot of the same benefits as sorted lists, but make it a lot easier to keep the data organised.
Trees some up a lot in computer science because they provide a very structured way to keep information organised.
Even the structure of folders used on a personal computer is a type of tree.

## Digital Technologies | Algorithms (and Data representation?)

{panel type="teaching" title="Hashing and hashtags"}

{image file-path="img/topics/hash-vs-hash.png" alt="The image has a diagram of a hash table and a hashtag symbol (#) with a not equals sign separating them."}

Students may try to make a connection between hashing and using hashtags.
They are actually completely different things.
The names have different derivations, and just happen to be the same word (hashtag is from the shape of the # symbol, and hashing is based on making a hash of your data).
Hashing should be treated as a completely new concept.

{panel end}

## Vocabulary explained

**Hashing** - taking a number, word, or other item being searched for, and converting it to a number using a mathematical function.
This number can be used to find out where the data is stored.

{image file-path="img/topics/funnel-water.png" alt="The image shows a teapot pouring water into a funnel, and another teapot pooring water into a funnel that is upside down."}

**One way functions** - a calculation that is easy to do one way, but hard to run backwards.

**Data structure** - a way of organising data so that it can be used more efficiently.

## Real world implications

Hashing, and using hash functions support programmers to make really fast searching algorithms.
This approach seems almost fanciful because it relies a lot on randomness - making a very random value out of the key you're searching for, and hoping that not too many other things come out to the same value.
Fortunately the statistics around this is well understood, and people can design very fast and efficient hash tables.


Binary search trees are also the basis of a commonly used structure where the relationships between the keys are important - especially if you're looking for values similar to the one being searched for.

{image file-path="img/topics/girl-searching.png" alt="A girl uses an online search engine on a computer."}

There are many variations on hash tables and search trees, but chances are that if you are looking something up on a computer system it will be using software based on these ideas, whether it's checking your online account balance, getting the price of a product in a shop, or looking for a web page using a search engine.
