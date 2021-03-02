# Binary search trees

## Preparatory knowledge

[Binary searching and sequential searching lessons]('topics:unit_plan' 'searching-algorithms' 'unit-plan').

Note: this activity is about Binary Search Trees, or BSTs.
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

{image file-path="img/topics/data-structures-for-searching-overview.png" alt="Binary search tree drawn on the ground in chalk." caption="An example of what we will be creating. Each binary search tree has a different shape depending on the data"}

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

{image file-path="img/topics/data-structures-for-searching-cat-tree.png" alt="A cat stuck in a tree."}

{panel type="teaching"}

# Teaching observations

-   Particular parts of a tree that are technical terms used in this activity are the branches, leaves, and root; but students might also mention the trunk, bark, fruit and other features.
You can probably use these terms without defining them when you look at BSTs; for example, in the exercise above with a real tree, it makes sense to talk about a “left branch” and “right branch”, and students probably won’t need these explained.

-   For the tree drawn, the instructions "right, right, left, right" will get to the cat; note that although the first branch looks like a decision between "left" and "straight", we want to get used to the idea of calling it "left" and "right".
Some students might observe that not all trees have two-way branches, although a two-way fork is common; even something that looks like it is branching three ways can probably be seen as two two-way branches if you look carefully.

{panel end}

{image file-path="img/topics/data-structures-for-searching-binary-search-trees.png" alt="Two binary search trees. One with numbers in the nodes and one without."}

Mark out the "tree" above on the ground.
The numbers are shown for your convenience in the left picture, but they would be hidden (turning the disc upside down) as in the picture on the right when the students first see the tree.
(Note that the colours and arrows aren't necessary, but can help to talk about the tree.)
Show the students the "tree" that you have marked out.
(If you are confident with the activity, you can mark out a tree with more than 12 discs - the larger the better.)

    1. If this represented a tree, where would the root be? (It's the single disc nearest you). 
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

1. Reveal what is under the disc at the root, which in the example has the number 40.

{image file-path="img/topics/data-structures-for-searching-binary-search-tree-2.png" alt="A binary search tree with the number 40 at the root."}

2. Explain that we're looking for the number 25 in this tree.
   There is a simple rule: everything down the left branch of a disc is smaller than the value shown, and everything down the right branch is larger.

3. Ask which branch the number 25 should be down. (It is smaller than 40, so it must be down the left branch, since everything smaller is down the left).

4. Turn the first disc back over (so that students don't easily remember what was on it), and follow the left branch, revealing the number under the next disc.
   In this case it is 23. Ask if 25 will be left or right from 23? (It is larger, so it will be down the right branch.)

{image file-path="img/topics/data-structures-for-searching-binary-search-tree-3.png" alt="A binary search tree with the root hidden. The left branch from the root has the number 23 shown."}

5. Hide the 23 again, and reveal the disc down the right branch, which is 30.
   Ask if we should go left or right? (Left, because 25 is less than 30; students may also observe that there's no choice, but that isn't relevant, as you must go left if the number is smaller).

{image file-path="img/topics/data-structures-for-searching-binary-search-tree-4.png" alt="The right branch from node 23 shows the number 30."}

6. Hide the 30, and reveal the disc down the left, which is 25. You have located the disc you were searching for.

{image file-path="img/topics/data-structures-for-searching-binary-search-tree-5.png" alt="The left branch from node 30 shows the number 25."}

## Finding another number

8. Make sure all the discs are hidden, and return to the root.

9. This time ask the students for directions to find the number 55.
   (They should work out that this requires going right at 40, right at 44, right at 48, and left at 91.)
   Remember to flip each disc back after looking at it, to avoid students memorising the tree.

## What if the number isn't there?

Ask students to search for the number 35.
(They should flip over 40, 23, 30, but at 30 they will want to go right since 35 is larger than 30. There's no branch, so you can conclude that the number isn't in the tree, despite having looked at only 3 discs.)

## Variations

**Adding a value**

To do this, just search for where it should be, and add it on a new disc in the correct direction from the last disc that you got to (the added disc will be a new "leaf").
For example, when you searched for the number 35 in the previous example, it could have been added on a new right branch from number 30.

{image file-path="img/topics/data-structures-for-searching-binary-search-tree-6.png" alt="Binary tree with a new leaf added."}

**Build your own tree**

You can build your own tree with any numbers that you want to be able to search.
You could either make up some numbers, or use something like the years of historic events.
It’s best to avoid having the same value twice, but we explain how to accommodate this below. 
To build a tree, the very first value that you add to the tree will be the root, so just place that data on the ground.
It's a very simple "tree" at this stage, with just one value in it!!
But it gets more interesting as you add more values.
Once the root is put down, students can add each value as for "adding a value" above i.e. search for where it belongs, and when you get to the end of the path, add it as a branch from the disc that you got to.
For example, suppose we're making a tree with the numbers 45, 23, 26 then 76.
The tree would be built up as follows. Initially the tree will seem very simple with just 45 as the root, but it can grow rapidly as values are added.
The shape will depend on the order that the numbers arrive in.
Note that it pays to have the branches from the root drawn to be fairly wide, as the tree may need to be wide further down as more values are added.
The branches needn’t be straight, as long as it’s obvious which is left and which is right.
