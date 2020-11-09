{panel type="ct-algorithm"}

# 算法思维

Searching through data is something computers do all the time, just think about how often we need to search for words in documents and information on the internet! Searching efficiently is a very important problem and that computer scientists have worked on for a long time. To solve this problem we need algorithms, processes that can be followed each time we search for something, and many different ones have been developed (such as binary search). Each of these algorithms can be seen as a solution to a problem.

Students will be learning, using, and describing different algorithms throughout these lessons. They will need to follow clear instructions when doing the activities and when they are doing this they are carrying out algorithms.

The two algorithms we are looking at in this unit, sequential search and binary search, take different amounts of time to complete a search, and sequential search is less efficient than binary search.

The amount of time sequential search takes isn’t very predictable and can vary wildly, from finding something straight away, all the way to having to check every single item we have! On average it will look at half the items, which means the average time it takes is proportional to the number of items being searched; this is why it is also known as linear search, because the time needed is linear in the amount of data being searched. Binary search on the other hand is more predictable and is guaranteed to work within a small number of steps. Since it eliminates half the items we are searching every time we look at an item it works very fast, even with HUGE amounts of data! To search one billion items we would have to look at 30 of them at the very most!

{panel end}

{panel type="ct-abstraction"}

# 抽象

If we have an abstract idea of how the searching algorithms we can use work, then we can apply them to a whole range of situations!

When searching through data it is important to only focus on the information we need to find what we are looking for. When considering general algorithms for searching, one thing we can always abstract away is the nature of the data we are searching through. When we use a searching algorithm we don’t need to know what the data represents, we just need to know what we are searching for, and if we are searching through an ordered list we also need to know how that data is ordered.

{image file-path="img/topics/max_dog.png" alt="A dog with a nametag saying Max"}

For example say we are looking for the number 160 in an unordered list; we don’t need to know whether these numbers represent heights, dollars, or bank account balances, we just need to compare the number we are searching for to the numbers in the list. Now say we are searching for the word “Max” in a list of words which is sorted into alphabetical order; we don’t need to know if we are looking at a list of pets names, or a list of random 3 letter words; we only need to know what alphabetical order means and how we use this to determine if a word is earlier or later in the alphabet. Then the same rules for searching numbers can be applied to words.

{panel end}

{panel type="ct-decomposition"}

# 分解

{image file-path="img/topics/apples_oranges.png" alt="Shows that apples do not equal oranges"}

The most basic step in any searching algorithm is comparing two pieces of data and determining if they are the same or not. Each of the algorithms students will be exploring was created by decomposing the problem of searching down to make use of this very basic step. One of the most important examples of decomposition will be covered in lessons 2 and 4, the Divide and Conquer method. This method is used when we perform a binary search, which is a classic method of decomposition - you divide the list of values into two parts, and then work on each half. In this case, one of the halves will be trivial to "work on" because we know it can't contain what we're searching for, and so we don’t have to do anything with it! Breaking the problem in half repeatedly soon decomposes it to a very simple case: a list of one item, which is very easy to search!

The divide and conquer strategy is a pattern that appears frequently in computer science, and also in real life! It is an efficient and logical way of attacking many different problems where you are searching for something in a group of objects that have different identifying features. For example, if you were trying to guess your friends favourite food you could ask questions like “Is it bananas?”, “Is it chocolate?”, but this would be equivalent to doing a sequential search because with each question you can only eliminate one type of food from all the possible types of food it could be! Instead you could apply divide an conquer and ask questions like “Is it a vegetable?”, “Is it a savoury food?”. These questions eliminate many possible foods just with one question.

{panel end}

{panel type="ct-pattern"}

# 泛化和模式

When doing these lessons look to see if students recognise patterns between the activities. Do they notice that searching through the unsorted number boxes is actually the same task as guessing which cup a number is in when the numbers are in a random order? Do they notice that searching the ordered number boxes is actually exactly the same as the divide and conquer activity? If they do then they might also realise that they can use the same algorithms in each of these similar activities! If we generalise our algorithms (by abstracting away unnecessary information) then we can reuse them in new situations and apply them to new, but similar, problems. They might also start recognising similar problems to these in their everyday lives and applying these strategies, because searching for things is something we all do a lot, whether we’re looking for a book on a bookshelf, or searching your wardrobe for that shirt you want to wear!

{panel end}

{panel type="ct-evaluation"}

# 评估

Evaluation is a key part of these lessons. There can be many different algorithms for the same problem so it is very important that we evaluate these algorithms and figure out which is the best to use in each situation. In these lessons students will look at two different algorithms for searching, each of which performs differently. For each of the search algorithms used the class will be collecting data on how long each method takes, trying to make sense of that data (for example through looking at it all on a graph), and evaluating each of the algorithms based on the data they have collected. This is one of the key points where Computational Thinking and statistics are linked, when we need to evaluate results.

{panel end}

{panel type="ct-logic"}

# 逻辑

By understanding the algorithms, evaluating the data collected, and thinking about how each of the different algorithms work and the differences between them, students will be exercising their logic skills a lot! Logical problem solving skills are exercised when they think about the following:

- Why binary search can only be performed on an ordered list, and why the only algorithm we can use to search an unsorted list is sequential search,
- Why both algorithms are guaranteed to find the item you are searching for (or discover that the item isn’t actually in the list)
- Why halving a list repeatedly (the way you do when using binary search) makes it much faster to search through large amounts of data
- Discuss how the efficiency of the algorithms compares when we use more and more data, i.e as the amount of data sequential search has to look through grows, the amount of time it takes will increase at the same rate (a linear rate), but with binary search the amount of time grows very slowly compared to sequential search.

{panel end}