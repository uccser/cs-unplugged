{panel type="ct-algorithm"}

# Algorithmic thinking

We used an algorithm in this lesson to sort the numbers into order using a
parallel processor (normally this processor would be implemented in hardware,
but our chalk network is still actually one!
It’s powered by people instead of electricity).

#### Examples of what you could look for:

-   Do students understand how each node functions (taking in two values and
    swapping them if they are in the wrong order)?
    Are they able to explain to other students how to use the network
    correctly?

-   Do the students see that no matter what numbers or data we put into the
    network we will always get a solution if we follow the algorithm correctly?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

The Sorting Network used in these activities is itself an abstract
representation of how Sorting Networks are implemented in hardware and
software.
It represents the core functionality of a Sorting Network, whilst hiding all
the nitty gritty details of how the hardware and circuitry works.

#### Examples of what you could look for:

-   Can students make the connection between the lines and nodes on this graph
    and the way computers can process information by making comparisons?
-   Can students understand that this representation can be used to model how a
    real parallel processing computer would work?

{panel end}

{panel type="ct-decomposition"}

# Decomposition

The whole process of sorting in this activity is decomposed into a very simple
operation: comparing two values.
This operation alone is very simplistic, but when it is performed many many
times it can be used to build up a solution to a much larger task.

#### Examples of what you could look for:

-   Can students see how to design a Sorting Network to sort just 2 values?
    (It would just be a single comparator node).

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

In this lesson students only worked with one type of information, numbers, so
there wasn’t much use of generalisation.
It is more prominent in the next lesson.

{panel end}

{panel type="ct-evaluation"}

# Evaluation

For this Sorting Network there can be up to three comparisons happening at
once, and the length of the network determines how long it would take to
complete all these comparisons.
Although 12 comparisons need to be made when going through the network, the
network can be completed in the time it takes to an individual node to make 5
comparisons.

#### Examples of what you could look for:

-   Can students identify the longest path that any number would have to go
    through to get to the end?
    (The middle two numbers need to make 5 comparisons).
-   Can students explain that if every comparison were to take, say, 2 seconds,
    then the sorting would be finished in 5x2 seconds, and not 12x2 seconds?

{panel end}

{panel type="ct-logic"}

# Logic

The smallest value will always take the left path at any comparison, and from
every starting point the path that always takes the left branch will lead to
that node, the smallest value will therefore always end up in the left-most
position at the end.

#### Examples of what you could look for:

-   Can students explain where the smallest value will end up regardless of
    what the other values are?
-   Do students understand the function of each node?
    Do they avoid simply going to the final node without doing the comparisons?

{panel end}
