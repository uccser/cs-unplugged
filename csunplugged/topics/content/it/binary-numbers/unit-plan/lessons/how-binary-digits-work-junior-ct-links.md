{panel type="ct-algorithm"}

# Pensiero algoritmico

We used an algorithm in this lesson to convert a decimal number to a binary one. This is an algorithm because it is a step-by-step process that will always give the right solution for any input you give it as long as the process is followed exactly.

Here’s an algorithm for working out which dot cards should be showing, written in text:

- Find out the number of dots that is to be displayed. (We'll refer to this as the "number of dots remaining", which initially is the total number to be displayed.)

- For each card, from the left to the right (i.e. 8, 4, 2 then 1):
    
    - If the number of dots on the card is more than the number of dots remaining:
        
        - Hide the card
    
    - Otherwise:
        
        - Show the card
        
        - Subtract the number of dots on the card from the number of dots remaining

#### Examples of what you could look for:

Which students are methodical when they convert between decimal and binary? Which ones start with the leftmost card and move one card at a time to the right, rather than choosing cards at random and flipping them on and off until they get the right number?

{panel end}

{panel type="ct-abstraction"}

# Astrazione

Abstraction and abstract thinking is generally difficult for young students so only a small amount of this section is likely to be applicable for them. We have included the information here however because it is useful background knowledge for teaching this topic.

Abstraction helps us simplify things because we can ignore the details we don’t currently need to know. Binary number representation is an abstraction that hides the complexity of the electronics and hardware inside a computer that store data.

In this case the details we can ignore include: Computers use physical devices like electronic circuits and voltages in circuits to store and move data, and there are many complex physics and mathematical theories that make this work.

We don’t need to understand how these circuits work because we can use the abstraction of binary, as numbers made up of bits (0s and 1s), to understand data and work out problems, without having to think about what is happening ‘underneath the hood’ of the computer.

Another use of abstraction is considering what is needed to represent any given digit in binary. The answer is all you need are two different things. These things can be anything! Two different colours, two animals, two symbols etc. As long as there are two of them, and they are different, you can use these to represent any number, using binary, the same way a computer uses electricity to represent data.

#### Examples of what you could look for:

Who are the students that can demonstrate converting and representing binary numbers using things other than “1’s and 0’s”, “black and white”, and “off and on” (for example using :] and :[, or using people standing up or sitting down). If you are able to interchange terms like "black" and "white" with 0 and 1 without students being concerned about the difference, they are exercising abstraction.

{panel end}

{panel type="ct-decomposition"}

# Scomposizione

An example of decomposition is breaking the conversion of the number to binary into one bit at a time. The questions "Should this be 1 or 0" for each of the dot cards is decomposing the problem to a series of questions.

#### Examples of what you could look for:

Which students recognise that it is important to start with the leftmost card and only consider one bit at a time? Which students focus on each individual bit at a time, rather than being overwhelmed by trying to work them all out in one go?

{panel end}

{panel type="ct-pattern"}

# Generalizzazione e riconoscimento di schemi (pattern)

Recognising patterns in the way the binary number system works helps give us a deeper understanding of the concepts involved, and assists us in generalising these concepts and patterns so that we can apply them to other problems. Generalising these patterns may be more difficult for junior students, but recognising the patterns is a good exercise.

At a simple level, we started with the numbers 1, 2, and 4, and students generalised that to doubling values. In these exercises we converted to 4-bit numbers, but students (who are able to count high enough) may be able to generalise that to more 8-bit numbers, or larger.

The algorithm for converting a decimal number to a binary one follows a pattern that can be generalised to solve the problem of giving change when someone pays by cash. For binary numbers you start with the largest bit and turn it on if it is needed or off if it is not, just like when you’re giving change you start with the largest denomination and then always take a coin (or note) whenever you need it. Jargon note: This is called a greedy algorithm.

{panel type="math"}

# Mathematical links

Ask students what is special about the decimal to binary conversion, in contrast with the general change giving algorithm, and have them observe that in the general case, you may need to give more than one coin of the same denomination, whereas in the binary conversion there is always one (or none) of each.

{panel end}

When counting upwards in binary, there is a pattern for how often particular cards flip. The first bit (with 1 dot) turns over every time we count up by one, the 2nd (with 2 dots) turns for every second number, the 3rd (with 4 dots) turns for every fourth… Is there a pattern like this when we count in decimal numbers?

{image file-path="img/topics/col_binary_counting_pattern.png" alt="Binary counting pattern"}

If you have 4 of the cards and all are visible, you will have the number 15, which is 1 less than the value of the next card, 16. Is this pattern always true?

The amount of numbers you can represent with a certain number of bits is the same as the value of the next bit that can be added. For example, using 4 cards (1, 2, 4, 8) you can represent 16 different numbers (0-15), and the next card in the sequence is the number 16. Each time we add the next card we also double the amount of different numbers we can represent.

Working with these patterns is valuable for working out the relationship between the number of bits being used and the power of what they can represent.

#### Examples of what you could look for:

Which students recognised quickly that each card was doubling the number of dots? Which students easily understand the patterns of cards flipping when counting with binary numbers?

{panel end}

{panel type="ct-logic"}

# Logica

Logical thinking means using rules you already know and using logic to deduce more rules and information from these. Once we know what number each of the binary cards represents then we can use this knowledge to figure out how to represent other numbers with the cards. If you memorise how to represent the numbers we can make with 4 cards, does that mean you understand how to represent any number with any number of bits? It doesn’t, but you can understand how to do that if you understand the logic behind how these numbers with the 4 cards are made.

A good example of logical thinking in binary numbers is the reasoning for why each bit "has to" have a particular value (e.g. it has to be on, or it has to be off) to represent a given number. This in turn leads to an argument that there is only one representation for each number.

#### Examples of what you could look for:

Do students explicitly explain that the first bit needs to be a one because it is the only odd number and therefore is needed so that we are able to make any, and all, odd numbers? Without it we could only make even numbers. Are students able to explain that each card "has to" be up the way it is for a given number e.g. the 8-dot card is needed for the number 9 because without it you only have 7 dots remaining (not enough); but it's not needed for the number 6 because it would give too many dots?

{panel end}

{panel type="ct-evaluation"}

# Valutazione

An example of evaluation is working out how many different values can be represented by a given number of bits (e.g. 4 bits can represent 16 different values), and vice versa (to represent 1000 different values, you need at least 10 bits).

#### Examples of what you could look for:

Can a student work out the range possible with 2 bits? (4)

3 bits? (8)

4 bits? (16)

If we add one more bit to a representation, how much does that increase the range? (it doubles it)

{panel end}