# Binary search trees

## Preparatory knowledge

- [Binary searching and sequential searching lessons]('topics:unit_plan' 'searching-algorithms' 'unit-plan').

**Note:** This activity is about Binary Search Trees, or BSTs.
There is a previous activity about Binary Search, which uses a sorted list of values.
Students often understandably confuse Binary Search and Binary Search Trees.
Both are mentioned below, and although they have elements in common, they are distinct ideas.
We’ll often use the abbreviation BST here to help to make it clear that we’re talking about the trees, and not just Binary Search.

{panel type="general"}

# Notes on resources

This activity requires a "binary search tree" (BST) to be marked out on as large a surface as possible, such as a playground.
The BST consists of lines for the students to follow, and "nodes" (these are typically circles or cards) that have values written on the back of them.
While the activity could be done on a tabletop or indoors, it's much better if it's in a hall or playground, marked out on the ground with chalk, painter's tape, or masking tape (because students will be creating their own layouts, chalk on pavement tends to be a lot easier than tape).
The nodes should also be as large as possible.
For a smaller indoor setup, paper cups, envelopes or sticky notes with numbers underneath are suitable (as for the binary search activity), but it's ideal if they are large, such as rubber squares, paper plates, or discarded CDs.
The writing needs to be invisible when they are upside down.
The left-hand picture below shows what they will look like.
The right-hand picture shows the numbers to put under each disc, but these shouldn't be visible to the students.
The lesson explains how to lay these out.

{image file-path="img/topics/binary-search-tree-hopscotch-tree.png" alt="Binary search tree drawn on the ground in chalk." caption="true"}

An example of what we will be creating. Each binary search tree has a different shape depending on the data.

{image end}

{panel end}

## Key questions

-   When we organised the sequential and binary search, what would happen if we had new data (information) to add? What would we need to do to insert that data? Is one faster to add data to? Is one faster to find the data in?

### Potential answers could include:

With a sequential search it's fine to add information to the end of the list since the order doesn't matter, but with binary search it needs to be inserted in the correct place to keep it in sorted order, so you'd need to find the place to insert it and move everything up.
So with sequential search it's easy to add new data since the order doesn't matter, but it's slow to find things; whereas binary search is slow to add data but quick to find it.
In this lesson we'll look at a method that is fast for adding and finding data.

## Lesson starter

What are the names of the parts of a tree that you can see?

Possible answers are: trunk, branches, leaves... Explain that we’ll use some of these words to talk about a binary search tree.

Let’s look at an example of what happens in the physical world: If a cat or ball is stuck in a tree, and you want to describe where it is, starting at the base (root), could you guide the rescuer by saying which way to go at each fork in a branch?
For example, below is a picture of a tree with a cat - using only "left" and "right", what are the directions you would give someone to climb up to where the cat is?
Can you guide someone to anywhere in the tree just by giving them "left" and "right" directions?

{image file-path="img/topics/binary-search-tree-cat-in-tree.png" alt="A cat stuck in a tree."}

{panel type="teaching"}

# Teaching observations

-   Particular parts of a tree that are technical terms used in this activity are the branches, leaves, and root; but students might also mention the trunk, bark, fruit and other features.
You can probably use these terms without defining them when you look at BSTs; for example, in the exercise above with a real tree, it makes sense to talk about a “left branch” and “right branch”, and students probably won’t need these explained.

-   For the tree drawn, the instructions "right, right, left, right" will get to the cat; note that although the first branch looks like a decision between "left" and "straight", we want to get used to the idea of calling it "left" and "right".
Some students might observe that not all trees have two-way branches, although a two-way fork is common; even something that looks like it is branching three ways can probably be seen as two two-way branches if you look carefully.

{panel end}

{image file-path="img/topics/binary-search-tree-numbers-completed-with-empty.png" alt="Two binary search trees. One with numbers in the nodes and one without."}

Mark out the "tree" above on the ground.
The numbers are shown for your convenience in the left picture, but they would be hidden (turning the disc upside down) as in the picture on the right when the students first see the tree.
(Note that the colours and arrows aren't necessary, but can help to talk about the tree.)

Show the students the "tree" that you have marked out.
(If you are confident with the activity, you can mark out a tree with more than 12 discs - the larger the better.)

If this represented a tree, where would the root be? (It's the single disc nearest you).
Which discs do you think are called the leaves? (These are the disks at the top with no branches coming out of them).

{panel type="teaching"}

# Teaching observations

The term "root" is the technical term for where you start in a "binary search tree".
It's called "binary" because each disc has at most two branches, "search" because we can use it to find things, and "tree" because it has branches.
The technical word for the discs is "node".
The term "branch" is used to refer to each of the lines where the tree splits (at each node), and a "leaf" is a node at the end of the tree.
It's helpful to use these terms with the class so that they get used to them.

{panel end}

## Searching the tree

1.  Reveal what is under the disc at the root, which in the example has the number 40.

    {image file-path="img/topics/binary-search-tree-numbers-step-1.png" alt="A binary search tree with the number 40 at the root."}

2.  Explain that we're looking for the number 25 in this tree.
    There is a simple rule: everything down the left branch of a disc is smaller than the value shown, and everything down the right branch is larger.

3.  Ask which branch the number 25 should be down. (It is smaller than 40, so it must be down the left branch, since everything smaller is down the left).

4.  Turn the first disc back over (so that students don't easily remember what was on it), and follow the left branch, revealing the number under the next disc.
    In this case it is 23. Ask if 25 will be left or right from 23? (It is larger, so it will be down the right branch.)

    {image file-path="img/topics/binary-search-tree-numbers-step-2.png" alt="A binary search tree with the root hidden. The left branch from the root has the number 23 shown."}

5.  Hide the 23 again, and reveal the disc down the right branch, which is 30.
    Ask if we should go left or right? (Left, because 25 is less than 30; students may also observe that there's no choice, but that isn't relevant, as you must go left if the number is smaller.)

    {image file-path="img/topics/binary-search-tree-numbers-step-3.png" alt="The right branch from node 23 shows the number 30."}

6.  Hide the 30, and reveal the disc down the left, which is 25. You have located the disc you were searching for.

    {image file-path="img/topics/binary-search-tree-numbers-step-4.png" alt="The left branch from node 30 shows the number 25."}

## Finding another number

1.  Make sure all the discs are hidden, and return to the root.

2.  This time ask the students for directions to find the number 55.
    (They should work out that this requires going right at 40, right at 44, right at 48, and left at 91.)
    Remember to flip each disc back after looking at it, to avoid students memorising the tree.

## What if the number isn't there?

Ask students to search for the number 35.
(They should flip over 40, 23, 30, but at 30 they will want to go right since 35 is larger than 30. There's no branch, so you can conclude that the number isn't in the tree, despite having looked at only 3 discs.)

## Variations

### Adding a value

To do this, just search for where it should be, and add it on a new disc in the correct direction from the last disc that you got to (the added disc will be a new "leaf").
For example, when you searched for the number 35 in the previous example, it could have been added on a new right branch from number 30.

{image file-path="img/topics/binary-search-tree-numbers-step-5.png" alt="Binary tree with a new leaf added."}

### Build your own tree

You can build your own tree with any numbers that you want to be able to search.
You could either make up some numbers, or use something like the years of historic events.
It’s best to avoid having the same value twice, but we explain how to accommodate this below.

To build a tree, the very first value that you add to the tree will be the root, so just place that data on the ground.
It's a very simple "tree" at this stage, with just one value in it!!
But it gets more interesting as you add more values.
Once the root is put down, students can add each value as for "adding a value" above i.e. search for where it belongs, and when you get to the end of the path, add it as a branch from the disc that you got to.
For example, suppose we're making a tree with the numbers 45, 23, 26 then 76.
The tree would be built up as follows:

{image file-path="img/topics/binary-search-tree-numbers-step-6.png" alt="Constructing a binary search tree with the numbers 45, 23, 26 and 76."}

Initially the tree will seem very simple with just 45 as the root, but it can grow rapidly as values are added.
The shape will depend on the order that the numbers arrive in.
Note that it pays to have the branches from the root drawn to be fairly wide, as the tree may need to be wider further down as more values are added.
The branches needn’t be straight, as long as it’s obvious which is left and which is right.

{panel type="teaching"}

# Teaching observations

Students may ask what happens if two values are the same. This is something they could explore; if they do, here are some ideas that they are likely to come to:

-    If you allow duplicate values in the tree, you need to be consistent about whether an equal value is down the left or right branch (for example, you could make a rule that the right branch is greater than or equal to the value at the branch)

-    Or you could count the number of items at a node, so if you get a second one, you store a count of 2 at that node (this is an example of data associated with the value)

-    In some cases duplicates shouldn't occur; for example, if the value is an ID or account number, there shouldn't be two people with the number.

{panel end}

### Build your own tree with other data

Instead of using numbers, we can put words in a tree.
Discuss what "less than" would mean with words (students should observe that it could be dictionary order, so "less than" means earlier in the dictionary).
Have a set of words written on the back of a card, or old CD (the words could be a spelling list).

Here's an example using animal names; words that are earlier in the alphabet are down the left branch, and vice versa.
This is the final version; below are the instructions for building it up with the class.

{image file-path="img/topics/binary-search-tree-animals-completed.png" alt="An example of a full binary search tree with words as nodes."}

Take a word randomly from a pile you have prepared, and use this as the first value that you add to the tree; or you could have students write down their favourite animal.
The first word chosen becomes the root (in the example it is the word “elephant”).

{image file-path="img/topics/binary-search-tree-animals-step-1.png" alt="The word 'elephant' as the root node."}

Take the next word, to start building your binary search tree.
As a class, decide if it’s a word that starts with a letter that is lower than “e” or higher than “e”.
In this example it’s the word “cow”, so it comes before "elephant" i.e. to the left.
Have a student draw a long branch from the root.
(It’s important to have this drawn out on a shallow angle (around 20 degrees) to leave space for later.
Then place the word down at the end of this branch.

{image file-path="img/topics/binary-search-tree-animals-step-2.png" alt="The word 'cow' is added to the left of the root node."}

Go back to the root word, then compare that with the next word (“dog” in the example).
Is D higher or lower than E? It is lower, so go left, then compare “dog” with “cow”.
Everyone should agree that it’s higher, so draw a long branch to the right.

{image file-path="img/topics/binary-search-tree-animals-step-3.png" alt="The word 'dog' is added to the right of the 'cow' node."}

Repeat this process as a class until students understand how to add a new word correctly.

Once they do, put students into groups of 3, where one person holds the word and makes the decisions, another person draws the branch once a decision is made, and the third person confirms it is correct.
(This is important because if the binary search tree is built incorrectly, then it won’t be reliable).
Once the the teams are ready, have them line up behind the root word and set teams off in 20 second intervals, until all words have been placed on the tree.
Once the binary search tree is set up, then work through different scenarios, including:

-    Adding a new word - how many words can we add to our binary tree search? (There is no limit.)

-    Finding different words and counting how many nodes need to be checked. (Some will be near the root, but usually will be further down the tree.)

-    Can we reliably accept that if a word isn’t found in the binary search tree by following the left/right rule, that it isn’t there? (If it is built accurately, then you can be sure that it's not down another branch of the tree that wasn't explored; if students make a mistake placing a node, this could be a learning point, since that node probably can’t be found in future searches.)

{panel type="teaching"}

# Teaching observations

It's ideal to draw the tree without any branches overlapping, so students need to draw their branches with wide angles, rather than close together.

{panel end}

### Use a much larger tree

Here's a large one that you could use!
Rather than draw it, you could use the blank version, and allow students to point at a node to ask what its value is, which you read off your secret version with the numbers on.
They won’t need to write anything down - at every step they are simply making a left/right decision.
Note that it's important that every value down the left branch of a node is smaller than the value in the node, and every value down the right branch is larger.

{image file-path="img/topics/binary-search-tree-big-tree-blank.png" alt="A large empty binary search tree."}

{panel type="teaching"}

# Teacher's secret version

{image file-path="img/topics/binary-search-tree-big-tree-completed.png" alt="A large binary search tree."}

Note: this large tree can be recreated using these numbers in this order:
53, 86, 61, 27, 88, 30, 49, 23, 28, 55, 91, 12, 21, 72, 90, 32, 10, 99, 81, 60, 45, 20, 93, 97, 3, 31, 41, 58, 76,
84, 73, 18, 92, 7, 47, 36, 74, 5, 48, 98, 19, 15, 46, 75, 14, 16, 17, 96.

{panel end}

{panel type="teaching"}

# Teaching observations

It's easy to make your own binary search tree, but just be sure to start at the root each time you add a new value, which will help to ensure that everything down a left branch is smaller than the node it's branching from.
If something is put down the wrong branch then it will throw off the searching! If you're not sure, just use the examples we've given.
If you run out of room, the tree doesn't have to be too tidy, as long as it's obvious at each node which way the left and right branches are (especially if there's only one branch, the direction needs to be obvious, although it could bend around after leaving the node).

{image file-path="img/topics/binary-search-tree-nine-node-tree.png" alt="An untidy, but readable binary search tree."}

{panel end}

### Use a binary search tree to look up information

In practice, we'd usually have some information associated with the value that we're looking for (such as a person's details).
You could build a binary search tree that looks up the population of cities, dates of historical events, or the definition of foreign words (an example is shown below).
Having students research the content of a disc and then place it provides an integrated learning opportunity.

{image file-path="img/topics/binary-search-tree-cities.png" alt="A binary search tree where the nodes are cities with their population number, sorted in alphabetical order."}


{panel type="teaching"}

# Teaching observations

When creating the nodes for your own tree, write the key (the value that is being searched for) above any other corresponding information for that node.
For example, if you will be searching for cities via alphabetical order, write the city name above the population.
If searching by population write the population above the city name.

{panel end}

### How fast is a binary search tree?

Here is a large binary search tree.
How many nodes (discs) does it have?
How many numbers would you compare getting from the root to the far end of the tree (which is called a leaf)?
(There are 63 nodes, but the maximum number of discs you'll look at is 6 - that's pretty efficient!)
What if there was another layer in the tree? (There would be 127 nodes, but you only need to look at 7 of them).
In fact, every time the number of items being searched doubles, it only takes a little more time to search it.

{image file-path="img/topics/binary-search-tree-balanced-tree.png" alt="A large, balanced binary search tree."}

### When binary search trees go bad

Have students create a new tree where you give them numbers in ascending order (e.g. 2, 12, 21, 23, 41, 45...), instead of random order.
For example, below is a tree where we've added the numbers 5, 10, 15 and so on; as a result, every branch is a right branch.
It works, but if we keep getting new numbers to add in increasing order, they will form a long chain of right branches, and it is slow to find things in it.
As students add numbers like 50, 55, 60, and so on, they will see that it gets to be a long way from the root to a leaf.
Luckily it’s usual for data to arrive in a random order, and you don't get these patterns.
The paradox about binary search trees is that they perform the worst when you give them ordered information, and are much better when it's random!
In practice this situation can be avoided easily using some simple changes to the algorithm for adding nodes.

{image file-path="img/topics/binary-search-tree-unbalanced-tree.png" alt="A binary search tree with only right branches."}

### How does this relate to binary search?

The binary search tree (BST) is a lot like a binary search, but because it uses a tree, it's much easier to add an item to it, because you just add it to the end of the tree as a new leaf.
In contrast, to use binary search you need to have a sorted list, and if you want to add something to a sorted list you can’t just add it to the end - you have to move all the data in that list along one space, so that there is space in the list for the new piece of data.
If a computer program is adding something to a sorted list, this means it has to take everything else in the list and move it to a new place in its memory, and this can take some time!
This is why computer scientists choose to use trees in some situations, and sorted lists in others.

{panel type="math"}

# Mathematical links

This activity relies heavily on comparing values; making one mistake will send students down the wrong branch of the tree!
It can be made more challenging by using larger numbers (e.g. 5 digit numbers such as 32843 and 32480, which look similar, and require some care to compare precisely).

{panel end}

## Applying what we have just learnt

A binary search tree is an elegant way to do searching.
It has a lot in common with doing a binary search of a sorted list, but the two shouldn't be confused.
In particular, a tree makes it very easy to add new values - you just link it to the last node you got to when searching for the value.
In the sorted list for a binary search, you have to move everything up to make space for a new value.
So in practice, binary search trees (and related structures) are more likely to be used than binary search, since data tends to be dynamic, with new values being added frequently.

## Lesson reflection

What surprises did you have with this lesson?
Did you see how your knowledge of a binary search supported your learning about binary search trees?

### Potential answers could include:

-    Being surprised that binary trees work best with random numbers.
-    Like binary search, there is a maximum of two options from each branch and the algorithm for deciding which way to go is the same for every branch.
