# Sorting networks unit plan

{panel type="teaching" title="See teaching this in action!"}

A demonstration of sorting networks being taught is available here:

{video url="https://www.youtube.com/embed/M-z5pDjqtZk"}

Some other videos showing different situations using Sorting Networks:

-   [Video 1](https://www.youtube.com/watch?v=LOxfdsBBjKI)
-   [Video 2](https://www.youtube.com/watch?v=30WcPnvfiKE)

{panel end}

## What’s it all about?

As we use computers more and more, and the amount of data we use increases, we
want them to process information as quickly as possible.
One way to increase the speed of a computer is to write programs that use fewer
computational steps (as shown in the lessons on sorting and searching
algorithms).
Another way to solve problems faster is to have several computers work on
different parts of the same task at the same time, which is what this unit
explores.
Unfortunately it's not always that simple to just split the work among separate
processors!

{image file-path="img/topics/sorting-network-many-computers-vs-one.png" alt="An image showing a group of people working on their computers working, compared to one person at their computer."}

Sorting Networks are used to sort values into ascending order by comparing pairs
of values; unlike a conventional sorting algorithm, a Sorting Network can have
more than one comparison happening at the same time.
For example, in the six-number Sorting Network that we use a lot in this unit,
a total of 12 comparisons are used to sort the numbers, but up to three
comparisons can be performed simultaneously.
This means that the time required will the same as what one computer by itself
would take to make only 5 comparison steps.
It's a bit like the situation where you might need to type in 4 pages of
writing; if you have 4 people typing at the same time on 4 computers, then you
can probably get the typing done 4 times faster than if one person did all the
work.

A parallel Sorting Network enables us to explore how much faster we can sort
values into order if we can make simultaneous comparisons.
The main six-way parallel network used in these lessons sorts a list of values
more than twice as quickly as a system that can only perform one comparison at
a time.

{image file-path="img/topics/sorting-network-digging-hole-text-en.png" alt="One person is digging a hole and the other person states they can't start digging until the other person is done."}

Not all tasks can be completed faster by using parallel computation however.
As an analogy, imagine one person digging a ditch ten metres long.
If ten people each dug one metre of the ditch at the same time the task would
be completed much faster.
However, the same strategy could not be applied to a ditch ten metres deep, the
second metre is not accessible until the first metre has been dug.

{image file-path="img/topics/sorting-network-confused-people.png" alt="A group of people are confused in front of computers as they try to coordinate a simple job across many people."}

And for typing our four page document, if you have 400 people helping, you'll
probably spend so much time coordinating all the work that it might not be very
fast at all!
Computer Scientists are still actively trying to find the best ways to break
problems up so that they can be solved by computers working in parallel, finding
out how much, and which parts, of the computation can be done at the same time,
and which parts have to be done one after another.

In these lessons we use a fun team activity to demonstrate an approach to
parallel sorting.
It can be done on paper, but we like to get students to do it on a large scale,
running from node to node in the network.

As an aside, although this is called a "network", it is only one of many
different types of networks that we encounter in Computer Science.
A common kind of “network” is a communication network, such as the
telecommunication networks that mobile phones use, and of course the Internet!
There are also networks for representing things like road maps and airline
routes.
It’s important to recognise that the Sorting Network in this activity is **not**
one of these types of networks, it is called a comparator network, because it’s
a network where each node compares two values, rather than linking different
devices (such as phones and computers) together.

## Digital technologies | Algorithms

{image file-path="img/topics/sorting-network-too-far-kid.png" alt="A child walks too far in the sorting network activity, failing the activity for everyone."}

To use the Sorting Network students need to follow a simple algorithm and should
recognise that if they do not follow this algorithm precisely, the way a
computer would, then they will probably not get to a correct result, or may not
get a result at all!
Students will be working collaboratively to ensure that each part of the
algorithm is coordinated, because if one person moves too far ahead, without
stopping at the nodes they are meant to, it causes the process to fail for
everyone.
There are also many algorithms that are used to construct extremely efficient
Sorting Networks of different sizes, and Computer Scientists study these to try
and create even better ones.
These can be very complex however, so when students construct their own networks
they will be doing this in a simplified way.

## Vocabulary explained

-   **Processor/CPU:** A device that can run computer programs.
-   **Parallel processing:** Using multiple processors to work on different
    parts of a problem at the same time.
-   **Serial processing:** Running a program on a single processor, so all the
    instructions are executed one after the other.
-   **Network:** A series of connected nodes such as a computer network, a road
    map, or a comparator network.
-   **Computational step:** A basic operation that is part of an algorithm.
-   **GPU/Graphics Processing Unit:** A specialised processor in a computer that
    can do simple operations for the many pixels in an image in parallel.
    These are often used for other computations because of their ability to do
    parallel processing.

{panel type="math" title="Mathematical links"}

This activity strongly supports learning about the concept of before and after
(ordering) for numbers, including determining the relationship between two
numbers (greater than, less than).

{panel end}

## Real world implications

{image file-path="img/topics/sorting-network-tortoises-vs-rabbit.png" alt="A group of turtles build a wall quicker than one rabbit."}

Often it's cheaper, and faster, to have a number of slow processors work on a
computational problem, rather than one very fast one.
Companies that have massive cloud servers often find it more economical to have
many slower, cheaper devices rather than fewer expensive ones.
Of course, this requires you to be able to split up a computational task over
several processors.
For some computational problems that's very easy to do, and for others it's
impossible.
The task we will be looking at here is between these extremes.

Having such a small operation (comparing two values) split over multiple
devices means that this kind of algorithm needs to run on special hardware.
It is only used for specialist applications at present, but, for example, it is
sometimes done on the graphics processor (GPU) of a computer, because these
processors are good at doing parallel computation of simple tasks.

{image file-path="img/topics/sorting-network-ancient-sorting-network-text-en.png" alt="A GPU finds a cave painting of an ancient sorting network."}

Sorting Networks were invented long before powerful GPUs came along; this is an
exciting thing about computer science - some of the our discoveries are ahead
of the hardware that is available, so we're ready for the hardware if it does
become commonly available!
Note that the approach explored in these lessons is **not** a conventional
sorting algorithm, as the sorting that is done on a conventional system can make
only one comparison at a time; conventional sorting algorithms are explored in
another lesson.
The main goal of these lessons is to help students explore the tradeoffs between
spreading work over several processors instead of using one processor.

One approach to parallel computation that is currently popular is called
"MapReduce", which is widely used in Cloud Computing systems where large amounts
of computing are spread over a large number of processors.

## Seeing the Computational Thinking connections

{panel type="ct-algorithm" title="Algorithmic thinking"}

In these lessons students will be sorting a variety of things into order, but
the underlying algorithm for performing these tasks will remain the same.
It is an algorithm because it is a step-by-step process that will always give
the right solution, as long as it is followed exactly.
In this case it is a special class of algorithm called a "parallel algorithm".
Students will need to follow this algorithm precisely to get to the correct
solution (this is particularly clear when students try to ‘cheat’ by dashing
straight to the end of the network, and then realise this means other students
are now stuck in the middle!
It’s a great learning opportunity when someone does this).

{panel end}

{panel type="ct-abstraction" title="Abstraction"}

The Sorting Network we use in these activities is a simple representation of
something much more complex: how Sorting Networks are implemented using specific
hardware and software on some computers to perform parallel processing.
The lines, circles, and squares we will use in our Sorting Networks hide the
complicated details of the hardware and software.

Another detail we can ignore when we are using a Sorting Network is what the
data we are sorting actually is, or represents.
It doesn’t matter if we are sorting numbers into order, or words, or musical
notes, we will still follow the same process each time.
The one thing about the data that does matter however is that we can compare
each item and that they have a precise way of being ordered (e.g. alphabetical
order).
This is described further in the section on logic.

The overall idea of a Sorting Network is actually an abstract concept as well,
this is explained under the generalisation heading.

{panel end}

{panel type="ct-decomposition" title="Decomposition"}

{image file-path="img/topics/sorting-network-comparing-apples.png" alt="A person compares a large apple and a small apple."}

In order to create an algorithm that can solve computational problems
effectively using parallel processors, we must first be able decompose the task
into very small and basic operations that, when repeated many times, can build
up a solution to the problem.
This operation is what will be performed by each processor in the network.
For the Sorting Network in these lessons this basic operation is the comparison
of two values that we perform at each node.
These operations need to be so basic that nodes can perform them simultaneously
and independently.
Parallel algorithms work best for tasks that need to do repetitive, and
independent, calculations with large amounts of data.

Decomposition is one of the most important steps in creating parallel processing
algorithms!

{panel end}

{panel type="ct-pattern" title="Generalising and patterns"}

There are many links between this section and the abstraction section above, see
if you can spot them!

The Sorting Networks we will look at are each constructed to take in a specific
number of inputs, and that number only.
We can’t use a Sorting Network that sorts 6 numbers to sort 10 numbers instead.
However the generalised idea of a Sorting Network can be applied to different
problems.
The generalised concept of a Sorting Network is simply a comparator network
(comparator just means it makes comparisons, like how we compare numbers in each
of the circles in the network) that takes in a number of inputs, and sorts them
into order.
This general idea of a Sorting Network can then be applied to solving many
different problems, by creating a Sorting Network for the specific number of
inputs needed for the problem and placing its comparison nodes in a specific
pattern.

There are patterns in the layout of Sorting Networks as well; recognising these
helps us design larger networks.
For example, the (optimal) two-way, four-way and six-way Sorting Networks follow
a similar pattern in their layout.
A simple pattern for generating Sorting Networks is explored at the end of
lesson 3 for ages 11-14 (but this can be used with any age group if the students
are interested!).

There is also a common pattern that students can observe between all the
different types of information we sort with the Sorting Network, which is that
they can be compared and ordered in a precise way.
This is described in the logic section.

{panel end}

{panel type="ct-evaluation" title="Evaluation"}

Parallel systems need to be evaluated for correctness: do they always sort
values correctly?
They also need to be evaluated for efficiency: how much time does this network
arrangement take to sort values, and is there a faster arrangement we could use?
Could this problem be solved easier by a non-parallel system?

{panel end}

{panel type="ct-logic" title="Logic"}

A very important rule for the data that Sorting Networks can process is the data
must have something called a transitive relation.
The transitive relation means: if a is less than b, and b is less than c, then a
is less than c.
For example, numbers have a transitive relation: the number 5 is less than 10,
and 10 is less than 15, which means that 5 must also be less than 15.
Data must have this relation for a Sorting Network to be able to sort it.
If items don’t have this relation then there is no logical way for us to order
it!

We will also see that Sorting Networks can't be evaluated by trying every
possible input (well they could be, but it could take hours, days, or even
hundreds of years for big networks!), unless a very small amount of data is
being sorted.
So instead, we must apply logic and reason to prove why it will always sort the
data correctly.
In these lessons we don't get into the advanced proofs that the whole network
will work, but students can apply their logical thinking skills to prove that
the smallest and largest values will always end up in the correct place.

{panel end}

## Reflection questions

-   What was most surprising about the learning that happened from the teaching
    of this unit?
-   Who were the students that were very systematic when working through the
    activities?
-   Who were the students who were very detailed in their activities?
-   What would I change in my delivery of this unit?
