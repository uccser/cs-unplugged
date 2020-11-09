{panel type="ct-algorithm"}

# Algorithmic thinking

In these lessons students will be sorting a variety of things into order, but the underlying algorithm for performing these tasks will remain the same. It is an algorithm because it is a step-by-step process that will always give the right solution, as long as it is followed exactly. In this case it is a special class of algorithm called a "parallel algorithm". Students will need to follow this algorithm precisely to get to the correct solution (this is particularly clear when students try to ‘cheat’ by dashing straight to the end of the network, and then realise this means other students are now stuck in the middle! It’s a great learning opportunity when someone does this).

{panel end}

{panel type="ct-abstraction"}

# Abstraction

The Sorting Network we use in these activities is a simple representation of something much more complex: how Sorting Networks are implemented using specific hardware and software on some computers to perform parallel processing. The lines, circles, and squares we will use in our Sorting Networks hide the complicated details of the hardware and software.

Another detail we can ignore when we are using a Sorting Network is what the data we are sorting actually is, or represents. It doesn’t matter if we are sorting numbers into order, or words, or musical notes, we will still follow the same process each time. The one thing about the data that does matter however is that we can compare each item and that they have a precise way of being ordered (e.g. alphabetical order). This is described further in the section on logic.

The overall idea of a Sorting Network is actually an abstract concept as well, this is explained under the generalisation heading.

{panel end}

{panel type="ct-decomposition"}

# Decomposition

{image file-path="img/topics/sorting-network-comparing-apples.png" alt="A person compares a large apple and a small apple." alignment="right"}

In order to create an algorithm that can solve computational problems effectively using parallel processors, we must first be able decompose the task into very small and basic operations that, when repeated many times, can build up a solution to the problem. This operation is what will be performed by each processor in the network. For the Sorting Network in these lessons this basic operation is the comparison of two values that we perform at each node. These operations need to be so basic that nodes can perform them simultaneously and independently. Parallel algorithms work best for tasks that need to do repetitive, and independent, calculations with large amounts of data.

Decomposition is one of the most important steps in creating parallel processing algorithms!

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

There are many links between this section and the abstraction section above, see if you can spot them!

The Sorting Networks we will look at are each constructed to take in a specific number of inputs, and that number only. We can’t use a Sorting Network that sorts 6 numbers to sort 10 numbers instead. However the generalised idea of a Sorting Network can be applied to different problems. The generalised concept of a Sorting Network is simply a comparator network (comparator just means it makes comparisons, like how we compare numbers in each of the circles in the network) that takes in a number of inputs, and sorts them into order. This general idea of a Sorting Network can then be applied to solving many different problems, by creating a Sorting Network for the specific number of inputs needed for the problem and placing its comparison nodes in a specific pattern.

There are patterns in the layout of Sorting Networks as well; recognising these helps us design larger networks. For example, the (optimal) two-way, four-way and six-way Sorting Networks follow a similar pattern in their layout. A simple pattern for generating Sorting Networks is explored at the end of lesson 3 for ages 11-14 (but this can be used with any age group if the students are interested!).

There is also a common pattern that students can observe between all the different types of information we sort with the Sorting Network, which is that they can be compared and ordered in a precise way. This is described in the logic section.

{panel end}

{panel type="ct-evaluation"}

# Evaluation

Parallel systems need to be evaluated for correctness: do they always sort values correctly? They also need to be evaluated for efficiency: how much time does this network arrangement take to sort values, and is there a faster arrangement we could use? Could this problem be solved easier by a non-parallel system?

{panel end}

{panel type="ct-logic"}

# Logic

A very important rule for the data that Sorting Networks can process is the data must have something called a transitive relation. The transitive relation means: if a is less than b, and b is less than c, then a is less than c. For example, numbers have a transitive relation: the number 5 is less than 10, and 10 is less than 15, which means that 5 must also be less than 15. Data must have this relation for a Sorting Network to be able to sort it. If items don’t have this relation then there is no logical way for us to order it!

We will also see that Sorting Networks can't be evaluated by trying every possible input (well they could be, but it could take hours, days, or even hundreds of years for big networks!), unless a very small amount of data is being sorted. So instead, we must apply logic and reason to prove why it will always sort the data correctly. In these lessons we don't get into the advanced proofs that the whole network will work, but students can apply their logical thinking skills to prove that the smallest and largest values will always end up in the correct place.

{panel end}