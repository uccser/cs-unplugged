{panel type="ct-algorithm"}

# Pensiero algoritmico

We used multiple algorithms in this lesson: one to convert a letter into a decimal number and then into a binary number, and vice versa. These are algorithms because they are a step-by-step process that will always give the right solution for any input you give it as long as the process is followed exactly.

Here’s an algorithm for converting a letter into a decimal number:

Choose a letter to convert into a decimal number. Find the letter’s numerical position in the alphabet as follows:

- Say A (the first letter in the alphabet)
- Say 1 (the first number in our sequence of numbers) 
    - Repeat the following instructions until you come to the letter you are looking to convert 
        - Say the next letter in the alphabet
        - Say the next number (counting up by 1)
- The number you just said is the decimal number that your letter converts too.

For example, to convert the letter E, the algorithm would have you counting A,1; B, 2; C, 3; D, 4; E, 5.

{image file-path="img/topics/binary_count_girl.png" alt="girl thinking about alphabet and numbers" alignment="right"}

(A more efficient algorithm would have a table to look up, like the one created at the start of the activity, and most programming languages can convert directly from characters to numbers, with the notable exception of Scratch, which needs to use the above algorithm.)

The next algorithm takes the algorithm from lesson 1 which we use to represent a decimal number as a binary number:

- Find out the number of dots that is to be displayed. (We'll refer to this as the "number of dots remaining", which initially is the total number to be displayed.)
- For each card, from the left to the right (i.e. 16, 8, 4, 2, then 1): 
    - If the number of dots on the card is more than the number of dots remaining: 
        - Hide the card
    - Otherwise: 
        - Show the card
        - Subtract the number of dots on the card from the number of dots remaining

#### Examples of what you could look for:

Can students create instructions for, or demonstrate, converting a letter into a decimal number, and then convert a decimal number into binary; are they able to show a systematic solution?

{panel end}

{panel type="ct-abstraction"}

# Astrazione

This activity is particularly relevant to abstraction, since we are representing written text with a simple number, and the number can be represented using binary digits, which, as we know from lesson 1, are an abstraction of the physical electronics and circuits inside a computer. We could also expand our abstraction because we don’t actually have to use 0s and 1s to represent our message. We could use any two values, for example you could represent your message by flashing a torch on and off, or drawing a line of squares and triangles on the whiteboard.

{image file-path="img/topics/binary_torch.png" alt="Flashlight" alignment="right"}

Abstraction helps us simplify things because we can ignore the details we don’t currently need to know. Binary number representation is an abstraction that hides the complexity of the electronics and hardware inside a computer that stores data. Letters are an abstraction that a human can make sense of quickly; talking about the letter H is generally more meaningful than calling it "the 10th letter of the alphabet", and when we are reading or speaking we don’t need to know it is the 10th letter anyway.

#### Examples of what you could look for:

Have students create instructions for, or demonstrate how to represent new language elements, such as a comma.

{panel end}

{panel type="ct-pattern"}

# Generalizzazione e riconoscimento di schemi (pattern)

Recognising patterns in the way the binary number system works helps give us a deeper understanding of the concepts involved, and assists us in generalising these concepts and patterns so that we can apply them to other problems.

#### Examples of what you could look for:

Have students decode a binary message from another student, by converting the binary numbers into text to view the message. Can they recognise patterns in the binary to anticipate what the word is? Can they work with a different set of letters using the same principles?

{panel end}

{panel type="ct-logic"}

# Logica

Logical thinking means recognising what logic you are using to work these things out. If you memorise how to represent that the letter H is represented as binary 01010 it's not as generally applicable as learning the logic that any character can be represented by the process described in this activity.

#### Examples of what you could look for:

Observe the systems students have created to translate their letters into binary and vice versa. What logic has been applied to these? Are they efficient systems?

{panel end}

{panel type="ct-decomposition"}

# Scomposizione

An example of decomposition is breaking a long message such as 00001000100001011001 into 5-bit components (00001 00010 00010 11001), each of which can now be converted to a letter. The 5-bit components are then decomposed into the value of individual bits.

#### Examples of what you could look for:

Can students convert a coded message with no spacing in it?

{panel end}

{panel type="ct-evaluation"}

# Valutazione

An example of evaluation is working out how many different characters can be represented by a given number of bits (e.g. 5 bits can represent 26 characters comfortably, but 6 bits are needed if you have more than 32 characters, and 16 bits are needed for a language with 50,000 characters.

#### Examples of what you could look for:

Can a student work out how many bits are needed to represent the characters in a language with 50 characters? (6 bits are needed) How about represent emojis, if you have about 10 emojis available (10 bits will be needed for each one).

{panel end}