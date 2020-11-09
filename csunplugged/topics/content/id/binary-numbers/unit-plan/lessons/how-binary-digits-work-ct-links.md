{panel type="ct-algorithm"}

# Algorithmic thinking

We used an algorithm in this lesson to convert a decimal number to a binary one. This is an algorithm because it is a step-by-step process that will always give the right solution for any input you give it as long as the process is followed exactly.

Here’s an algorithm for working out which dot cards should be showing, written in text:

- Find out the number of dots that is to be displayed. (We'll refer to this as the "number of dots remaining", which initially is the total number to be displayed.)
- For each card, from the left to the right (i.e. 16, 8, 4, 2 then 1): 
    - If the number of dots on the card is more than the number of dots remaining: 
        - Hide the card
    - Otherwise: 
        - Show the card
        - Subtract the number of dots on the card from the number of dots remaining

Note that this algorithm (working from right to left) works very well with the cards, but if you look up computer programs for doing this, you may encounter a different one that works from right to left. It's usual to have multiple algorithms that achieve the same thing.

#### Examples of what you could look for:

Which students are methodical when they convert between decimal and binary? Which ones start with the leftmost card and move one card at a time to the right, rather than choosing cards at random and flipping them on and off until they get the right number?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

Binary number representation (just using 0 and 1) is an abstraction that hides the complexity of the electronics and hardware inside a computer that store data. Abstraction helps us simplify things because we can ignore the details we don’t currently need to know.

In this case the details we can ignore include: Computers use physical devices like electronic circuits and voltages in circuits to store and move data, and there are many complex physics and mathematical theories that make this work.

We don’t need to understand how these circuits work to use data and represent things using binary. Using binary is an Abstraction of these circuits and allows us to represent numbers as being made out of bits (0s and 1s), to understand data and work out problems without having to think about what is happening ‘underneath the hood’ of the computer.

Another use of abstraction is considering what is needed to represent any given digit in binary. The answer is all you need are two different things. These things can be anything! Two different colours, two different animals, two different symbols etc. As long as there are two of them, and they are different, you can use these to represent any number, using binary, the same way a computer uses electricity to represent data.

We can use binary digits to represent any type of data stored on a computer. When we represent other forms of data (such as letters, images, and sound) we also use abstraction because we hide the details of all the binary numbers underneath and just look at the whole piece of data. All forms of data end up being represented as numbers (which in turn are really just combinations of bits) - for text we have a number for each letter, for images we use a number for each colour, and so on. We are using multiple layers of abstraction! For example, a familiar form of abstraction is that the month "October" could be represented by the number ten, which in turn is represented by the bits 01010, and if these are stored as voltages in computer memory, it is ultimately "low, high, low, high, low" for the voltages.

#### Examples of what you could look for:

Who are the students that demonstrate converting and representing binary numbers using things other than “1’s and 0’s”, “black and white”, and “off and on” (for example using :) and :(, or using people standing up or sitting down). If you are able to interchange terms like "black" and "white" with 0 and 1 without students being concerned about the difference, they are exercising abstraction.

{panel end}

{panel type="ct-decomposition"}

# Decomposition

An example of decomposition is breaking the conversion of the number to binary into one bit at a time. The questions "Should this be 1 or 0" for each of the dot cards is decomposing the problem to a series of questions.

#### Examples of what you could look for:

Which students recognise that it is important to start with the leftmost card and only consider one bit at a time? Which students focus on each individual bit at a time, rather than being overwhelmed by trying to work them all out in one go?

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

Recognising patterns in the way the binary number system works helps give us a deeper understanding of the concepts involved, and assists us in generalising these concepts and patterns so that we can apply them to other problems.

At a simple level, we started with the numbers 1, 2, and 4, and students generalised that to doubling values. The exercise used 5-bit numbers, but students should be able to generalise that to 8-bit numbers, or larger.

The algorithm for converting a decimal number to a binary one follows a pattern that can be generalised to solve the problem of giving change when someone pays by cash. For binary numbers you start with the largest bit always turn a bit on if you need it, just like when you’re giving change you start with the largest denomination and then always take a coin (or note) whenever you need it. Jargon note: This is called a greedy algorithm - it takes as much as it can each time!

{panel type="math"}

# Mathematical links

Ask students what is special about the decimal to binary conversion, in contrast with the general change giving algorithm, and have them observe that in the general case you may need to give more than one coin of the same denomination, whereas in the binary conversion there is always one (or none) of each.

{panel end}

When counting upwards in binary, there is a pattern for how often particular cards flip. The 1st bit (with 1 dot) turns over every time, the 2nd (with 2 dots) turns for every second number, the 3rd (with 4 dots) turns for every 4th... Is there a pattern like this when we count in decimal numbers?

{image file-path="img/topics/col_binary_counting_pattern.png" alt="Binary counting pattern"}

If you have 5 of the cards and all are visible, you will have the number 31, which is 1 less than the value of the next card, 32. Is this pattern always true?

The amount of numbers you can represent with a certain number of bits is the same as the value of the next bit that can be added. For example, using 4 cards (1, 2, 4, 8) you can represent 16 different numbers (0-15), and the next card in the sequence is the number 16. Each time we add the next card we also double the amount of different numbers we can represent.

Working with these patterns is valuable for working out the relationship between the number of bits being used and the power of what they can represent.

Explain one or more of the following patterns:

- That with a certain number of cards you can make the same amount of different numbers as the number of dots that would be on the next card to be added on the left (remember that 0 is a number).
- When you are counting upwards: the first card (1 dot) turns over every time, the second card (2 dots) turns every two times, the third (4 dots), every four times, and the fourth (8 dots), every eight times...
- That when all the cards you have are visible it will add up to the next binary card number minus 1.

#### Examples of what you could look for:

Which students recognised quickly that each card was doubling the number of dots? Can students see the similarities between this and multiplying place values by 10 when they are using the decimal system?

Which students easily understand the patterns of cards flipping when counting with binary numbers?

{panel end}

{panel type="ct-logic"}

# Logic

Logical thinking means using rules you already know and using logic to deduce more rules and information from these. Once we know what number each of the binary cards represents then we can use this knowledge to figure out how to represent other numbers with the cards. If you memorise how to represent the numbers we can make with 5 cards, does that mean you understand how to represent any number with any number of bits? It doesn’t, but you can understand how to do that if you understand the logic behind how these numbers with the 5 cards are made.

A good example of logical thinking in binary numbers is the reasoning for why each bit "has to" have a particular value (e.g. it has to be 1, or it has to be 0) to represent a given number. This in turn leads to understanding that there is only one representation for each number.

#### Examples of what you could look for:

Do students explicitly explain that the right-most bit needs to be a one because it is the only odd number and therefore is needed so that we are able to make any, and all, odd numbers? Without it we could only make even numbers.

Are students able to explain that each card "has to" be up the way it is for a given number e.g. the 16-dot card is needed for the number 19 because without it you only have 15 dots remaining to its right (not enough); but the 16 card isn't needed for the number 9 because it would give too many dots?

{panel end}

{panel type="ct-evaluation"}

# Evaluation

An example of evaluation is working out how many different values can be represented by a given number of bits (e.g. 5 bits can represent 32 different values), and vice versa (to represent 1000 different values, you need at least 10 bits).

#### Examples of what you could look for:

Can a student work out the range possible with 4 bits? (16)

6 bits? (64)

8 bits? (256)

If we add one more bit to a representation, how much does that increase the range? (it doubles it)

If we add two more bits to a representation, how much does that increase the range? (it is four times as much)

How many bits do we need to represent 1000 different values? (10 is sufficient)

{panel end}