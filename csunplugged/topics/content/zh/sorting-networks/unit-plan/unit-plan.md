# Sorting networks

{panel type="video"}

# See teaching this in action

A demonstration of sorting networks being taught is available here:

{video url="https://vimeo.com/437722996"}

Some other videos showing different situations using Sorting Networks:

- [Video 1](https://vimeo.com/437726931)
- [Video 2](https://vimeo.com/437726955)

{panel end}

As we use computers more and more, and the amount of data we use increases, we want them to process information as quickly as possible. One way to increase the speed of a computer is to write programs that use fewer computational steps (as shown in the lessons on sorting and searching algorithms). Another way to solve problems faster is to have several computers work on different parts of the same task at the same time, which is what this unit explores. Unfortunately it's not always that simple to just split the work among separate processors!

{image file-path="img/topics/sorting-network-many-computers-vs-one.png" alt="An image showing a group of people working on their computers working, compared to one person at their computer."}

Sorting Networks are used to sort values into ascending order by comparing pairs of values; unlike a conventional sorting algorithm, a Sorting Network can have more than one comparison happening at the same time. For example, in the six-number Sorting Network that we use a lot in this unit, a total of 12 comparisons are used to sort the numbers, but up to three comparisons can be performed simultaneously. This means that the time required will be the same as what one computer by itself would take to make only 5 comparison steps. It's a bit like the situation where you might need to type in 4 pages of writing; if you have 4 people typing at the same time on 4 computers, then you can probably get the typing done 4 times faster than if one person did all the work.

A parallel Sorting Network enables us to explore how much faster we can sort values into order if we can make simultaneous comparisons. The main six-way parallel network used in these lessons sorts a list of values more than twice as quickly as a system that can only perform one comparison at a time.

{image file-path="img/topics/sorting-network-digging-hole-text-en.png" alt="One person is digging a hole and the other person states they can't start digging until the other person is done."}

Not all tasks can be completed faster by using parallel computation however. As an analogy, imagine one person digging a ditch ten metres long. If ten people each dug one metre of the ditch at the same time the task would be completed much faster. However, the same strategy could not be applied to a ditch ten metres deep, the second metre is not accessible until the first metre has been dug.

{image file-path="img/topics/sorting-network-confused-people.png" alt="A group of people are confused in front of computers as they try to coordinate a simple job across many people."}

And for typing our four page document, if you have 400 people helping, you'll probably spend so much time coordinating all the work that it might not be very fast at all! Computer Scientists are still actively trying to find the best ways to break problems up so that they can be solved by computers working in parallel, finding out how much, and which parts, of the computation can be done at the same time, and which parts have to be done one after another.

In these lessons we use a fun team activity to demonstrate an approach to parallel sorting. It can be done on paper, but we like to get students to do it on a large scale, running from node to node in the network.

As an aside, although this is called a "network", it is only one of many different types of networks that we encounter in Computer Science. A common kind of “network” is a communication network, such as the telecommunication networks that mobile phones use, and of course the Internet! There are also networks for representing things like road maps and airline routes. It’s important to recognise that the Sorting Network in this activity is **not** one of these types of networks, it is called a comparator network, because it’s a network where each node compares two values, rather than linking different devices (such as phones and computers) together.

## Digital Technologies | Algorithms

{image file-path="img/topics/sorting-network-too-far-kid.png" alt="A child walks too far in the sorting network activity, failing the activity for everyone."}

To use the Sorting Network students need to follow a simple algorithm and should recognise that if they do not follow this algorithm precisely, the way a computer would, then they will probably not get to a correct result, or may not get a result at all! Students will be working collaboratively to ensure that each part of the algorithm is coordinated, because if one person moves too far ahead, without stopping at the nodes they are meant to, it causes the process to fail for everyone. There are also many algorithms that are used to construct extremely efficient Sorting Networks of different sizes, and Computer Scientists study these to try and create even better ones. These can be very complex however, so when students construct their own networks they will be doing this in a simplified way.

## Vocabulary explained

- **Processor/CPU:** A device that can run computer programs.
- **Parallel processing:** Using multiple processors to work on different parts of a problem at the same time.
- **Serial processing:** Running a program on a single processor, so all the instructions are executed one after the other.
- **Network:** A series of connected nodes such as a computer network, a road map, or a comparator network.
- **Computational step:** A basic operation that is part of an algorithm.
- **GPU/Graphics Processing Unit:** A specialised processor in a computer that can do simple operations for the many pixels in an image in parallel. These are often used for other computations because of their ability to do parallel processing.

{panel type="math"}

# Mathematical links

This activity strongly supports learning about the concept of before and after (ordering) for numbers, including determining the relationship between two numbers (greater than, less than).

{panel end}

## Real world implications

{image file-path="img/topics/sorting-network-tortoises-vs-rabbit.png" alt="A group of turtles build a wall quicker than one rabbit."}

Often it's cheaper, and faster, to have a number of slow processors work on a computational problem, rather than one very fast one. Companies that have massive cloud servers often find it more economical to have many slower, cheaper devices rather than fewer expensive ones. Of course, this requires you to be able to split up a computational task over several processors. For some computational problems that's very easy to do, and for others it's impossible. The task we will be looking at here is between these extremes.

Having such a small operation (comparing two values) split over multiple devices means that this kind of algorithm needs to run on special hardware. It is only used for specialist applications at present, but, for example, it is sometimes done on the graphics processor (GPU) of a computer, because these processors are good at doing parallel computation of simple tasks.

{image file-path="img/topics/sorting-network-ancient-sorting-network-text-en.png" alt="A GPU finds a cave painting of an ancient sorting network."}

Sorting Networks were invented long before powerful GPUs came along; this is an exciting thing about Computer Science - some of our discoveries are ahead of the hardware that is available, so we're ready for the hardware if it does become commonly available! Note that the approach explored in these lessons is **not** a conventional sorting algorithm, as the sorting that is done on a conventional system can make only one comparison at a time; conventional sorting algorithms are explored in another lesson. The main goal of these lessons is to help students explore the tradeoffs between spreading work over several processors instead of using one processor.

One approach to parallel computation that is currently popular is called "MapReduce", which is widely used in Cloud Computing systems where large amounts of computing are spread over a large number of processors.

## Reflection questions

- What was most surprising about the learning that happened from the teaching of this unit?
- Who were the students that were very systematic when working through the activities?
- 在活动中，哪些学生非常关注细节。
- 我将如何改进本单元教学？