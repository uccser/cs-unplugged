{panel type="ct-algorithm"}

# Algorithmic thinking

As students find their way around a Binary Search Tree they will be developing very precise algorithms to navigate it.
In this activity the main rule they are given is that items to the left are smaller, and items to the right are larger.
If they can successfully traverse the tree, they will have operationalised this rule as an algorithm equivalent to “compare the key with the value at the current node, and if it is smaller, move to the node on the left, otherwise move to the node on the right; keep doing this until you find the key or reach the end of the tree.”
They may also discover algorithms for finding the smallest value in the whole tree (“keep taking the left branch until the node doesn’t have one”).
Many other algorithms are possible for a binary search tree, including finding all the values within a particular range, displaying the values in increasing order, or deleting a value from the tree, although these aren’t covered in this activity.

#### Examples of what you could look for:

Are students able to confidently find a given value in a tree that they haven’t seen before by only looking at nodes on the path from the root to the node with the value?

Are they able to add a node for a new value in the right place in the tree?

Can they give an algorithm to find the smallest or largest value in the tree without looking at any of the values at all?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

Binary search trees are a type of data structure, and so can be used with any type of data, as long as that data can be put into an order.
When we use a binary search tree its structure also allows us to ignore much of the information it contains, and focus only on the information that we need at the time.
This is because when we use it we only ever have to look at one node at a time, and have no need to look at any others in the tree, until we move on to another. 


#### Examples of what you could look for:

Did students recognise that a binary search tree can also be used to search for words, since we can put them into alphabetical order and compare them?

Did they come up with any other types of data they could put into a binary search tree, such as dates?

{panel end}

{panel type="ct-decomposition"}

# Decomposition

Binary search trees are another example of how we can apply the divide and conquer strategy to simplify a problem, and create an efficient solution.
Each decision made going through the tree eliminates everything down one branch, reducing the size of the problem.

#### Examples of what you could look for:

Did students recognise that each decision eliminated an entire section of the tree?

Did they focus on each step, going from one node to the next, individually?

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

Students who have previously used sorting networks will probably notice many similar patterns between these activities (but it is important to note that these are still very different things!)
As with a sorting network, at each node a comparison is made between two numbers, and the result of this comparison tells you where to go next.
The interesting thing to observe here is that using just one very simple comparison operation (in different ways), we are able to both sort data into order, and search through it.
Another connection between these two activities is the type of data that can be used - the data must have something called a "transitive relation".
This is further explained under logic, and also in the sorting networks unit plan under logic. 
Because it is based on a simple comparison step, any type of data that can be sorted using a sorting network can also be placed into a binary search tree.
As binary search trees are abstract data structures, they can be generalised for use with any type of data that can be put into some kind of order.
The other connection students will likely make is between binary search trees, and binary search! While the names are almost the same, the actual pattern they both follow is subtly different, although they both make use of the divide and conquer strategy.
A curious observation about binary search trees is that if values are added in increasing order, they don't work very well! The order that data is added into the tree has an impact on how efficient the tree is, because the tree will form different shapes.

#### Examples of what you could look for:

Do students recognise that the order we add data into a tree can have an impact on how efficiently the tree performs?

Do students recognise that binary search trees work best if the values are added in a random order i.e. that patterns in the data arriving can make a tree work inefficiently?

Did students make any connections between a binary search tree, and other concepts they have seen before?

{panel end}

{panel type="ct-evaluation"}

# Evaluation

As we have seen, because of the way the algorithm for constructing a binary search tree works, trees can sometimes form long chains rather than an evenly distributed tree.
This can have a big impact on the efficiency of the tree.
As discussed under Decomposition, each time we make a decision at a node we effectively eliminate everything down one branch of the tree.
If a tree contains a lot of nodes that only connect to one other node (so it has long chains in it) then each time we make a decision at a node we eliminate none, or very few, nodes.
When constructing binary search trees we should examine their structure and evaluate them for efficiency.
A well constructed, or balanced, binary search tree will be very efficient to use.
The depth of the tree will also be relatively low compared with the number of nodes in it, as the number of nodes that can be at each layer of the tree doubles with each new layer.
This doubling is also probably a pattern students have seen before if they have covered the binary number lessons.
Evaluating a problem, before creating a tree, is also important because it may not always be the best strategy to use a binary search tree.
If we know we already have all of our data, and so won't need to add in more (or almost never will) then using a sorted list and binary search is likely to be more efficient than creating a binary tree.
However if we need to add more data in the future then a binary search tree is a much better solution, as it is much easier to add data to a tree than it is to add it to a sorted list.

#### Examples of what you could look for:

Can students identify what makes an efficient binary search tree and what makes an inefficient one? 

Can they compare the pros and cons of using sorted lists and trees in different situations?

Did students observe that the number of nodes that can be at each layer of the tree doubles with each step?

{panel end}

{panel type="ct-logic"}

# Logic

These trees rely on the logic that if we are following one branch, then one can safely eliminate everything down the other branch.
This is because of the simple relationship between the nodes in the tree, and the nodes that they connect to.
As with the data we could use in a sorting network, any data can be put into a binary search tree as long as it has what is called a "transitive relation".
For example, numbers have a transitive relation based on "less than": the number 5 is less than 10, and 10 is less than 15, which means that 5 must also be less than 15.
In general, this transitive relation means: if a is less than b, and b is less than c, then a is less than c. 
If items don’t have this relation then there is no logical way for us to figure out where to put it in the tree!
Not all relations are transitive; for example, consider the relation "is standing next to".
If Arnold is standing next to Tim, and Tim is standing next to Caitlin, it doesn't necessarily mean that Arnold is standing next to Caitlin.

#### Examples of what you could look for:

Did students recognise that everything down the left branch from a node must be smaller than the value at that node?

Can students reason about where the smallest value in the tree would be? (You keep taking left branches until there are no more to take; the logic is that anything down a right branch must be larger.)

Can they think of other types of data they could put into a binary search tree?

Can they think of any types of data that don’t have a transitive relation, and that therefore can’t be put into a binary search tree?

{panel end}
