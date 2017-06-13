# Codes for Letters Using Binary Representation

## Learning Outcomes

Students will be able to:

#### DT/CT

- Recognise how computers represent alphabet characters as bits using a simplified method.
- Create their own message using binary code.
- Interpret a message using binary code.
- Explain how codes for larger alphabets could be created.
- Explain how they would adapt the representation to include more characters, such as diacritics, capital letters or different symbols.

#### Curriculum Integration

- Identify that mistakes lead to new learning.
- English: alphabet, special characters such as diacritics and capitals
- Maths: doubling, range of values


## CSUnplugged Provided Resources

- [1 set of large binary cards from 1 to 128 dots (8 cards)](https://drive.google.com/file/d/0B-SN1PgPBbCYV0ZQc3VmaEs4ZXM/view?usp=sharing)
- [1 set per pair of students of student binary cards from 1 to 32 dots (6 cards)](https://drive.google.com/file/d/0B-SN1PgPBbCYQW1xcmVkekg2S1k/view?usp=sharing)

There is also an online interactive version of the binary cards [here](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), from the [Computer Science Field Guide](http://www.csfieldguide.org.nz/), but it is preferable to work with physical cards.

## Key Questions

How many different characters can you type on a computer?
(Discussion may start at the 26 letters of the English alphabet, and then expand to other characters on the keyboard, including capital letters, digits and punctuation.
Students may be aware that other languages can have thousands of characters, and the range of characters is also expanding as emoticons are invented!)

## Lesson Starter

Discuss how you would communicate a letter of the alphabet to someone if all you could do is say a number between 0 and 26.
(Students will usually suggest using a code of 1 or a, 2 for b, and so on)

Work out and write down the binary numbers using 5 bits from 0 to 26 on the worksheet, then add the letters of the alphabet.

{image file-path="img/topics/col_binary_robot_boy_convo.png"}

## Student Worksheet

## Teacher Answer

{panel type="teaching" title="Teaching observations"}

- Check their binary code for three is 00011 as students commonly write 00100 as they anticipate the pattern without necessarily checking it is correct.
- Check they are writing the binary code in the correct order with the least significant value on the right - for example some will start with one as 10000 instead of 00001.
- Identify the students who are demonstrating one or all of these computational thinking attributes; being very systematic, have everything lined up exactly, are the first to recognise the pattern and don’t need the cards any more.
- Check that all students can describe back to you how to calculate the number they are up to. This will identify those who are guessing the pattern.
- Note that if your local alphabet is slightly different (e.g. has diacritics, macrons etc.) then you may wish to adapt the code to match the common characters; this issue is also considered below.

{panel end}


## Lesson Activities

Using the table that students have created above, give them a message to decode, such as your name or the name of a book author (e.g. 00001 00010 00010 11001 for ABBY).

Now get students to write and communicate their own messages. Remind them that they can write the zeroes and ones using any symbols, such as ticks and crosses.

Consider unusual representations; for example, each bit could be communicated with a sound that is either high pitched or low pitched. Or the 5-bit number could be represented by holding up the five fingers on one hand, one finger corresponding to each bit.

## Adding More Characters

Some languages have slightly more or fewer characters, which might include those with diacritic marks. If students consider an alphabet with more than 32 characters, then 5 bits won't be sufficient.
Also, students may have realised that a code is needed for a space (0 is a good choice for that), so 5 bits only covers 31 alphabet characters.

Have the students design a system that can handle a few extra characters such as diacritics. (This can usually be done by allocating larger numbers, such as 27 to 31, to the other characters).

A typical English language computer keyboard has about 100 characters (which includes capital and lowercase letters, punctuation, digits, and special symbols).
How many bits are needed to give a unique number to every character on the keyboard? (Typically 7 bits will been enough since it provides 128 different codes).

Now have students consider larger alphabets. How many bits are needed if you want a number for each of 50,000 Chinese characters? (16 bits allows for up to 65,536 different representations).

{panel type="teaching" title="Teaching observations"}

It may be a surprise that only 16 bits is needed for tens of thousands of characters. This is because each bit doubles the range, so you don't need to add many bits to cover a large alphabet. This is an important property of binary representation that students should become familiar with.

{panel end}

{panel type="math" title="Mathematical links"}

The rapid increase in the number of different values that can be represented as bits are added is exponential growth i.e. it doubles with each extra bit.
After doubling 16 times we can represent 65,536 different values, and 20 bits can represent over a million different values.
Exponential growth is sometimes illustrated with folding paper in half, and half again.
After these two folds, it is 4 sheets thick, and one more fold is 8 sheets thick. 16 folds will be 65,536 sheets thick!
In fact, around 6 or 7 folds is already impossibly thick, even with a large sheet of paper.

{panel end}

{panel type="teaching" title="Teaching observations"}

Using a 5-bit code for an alphabet goes back to at least 1870 (the "Baudot" code); many different number to letter correspondences have been used over the years to represent alphabets, but one that was common for some time is "ASCII", which used 7 bits and therefore could represent over 100 different characters.
These days "Unicode" is common, which can represent over 100,000 different characters.
Nevertheless, each of these codes, including Unicode, still contain elements of the simple code used in this lesson (A is 1, B is 2...).
For example, the ASCII code for "A" is 65 and "B" is 66 etc.; if you work out the binary representations of these, and just keep the right-most 5 bits, you've got the code that we've been using above.

{panel end}

## Lesson Reflection

- What are some reasons why we don’t use the binary number system as the language for our written language?
- How do you think ancient Egyptians would have converted their hieroglyphics to binary?
- What did you find challenging during this lesson?
- How did you overcome these challenges?

## Computational Thinking links

{panel type="ct-algorithm" title="Algorithmic thinking"}

We used two algorithms in this lesson: one to convert a letter into a decimal number and then into a binary number, and vice versa.
These are algorithms because they are a step-by-step process that will always give the right solution for any input you give it as long as the process is followed exactly.

Here’s an algorithm for converting a letter into a decimal number:

Choose a letter to convert into a decimal number. Find the letter’s numerical position in the alphabet as follows:

- Say “A” (the first letter in the alphabet)
- Say “1” (the first letter in our sequence of numbers)
    - Repeat the following instructions until you come to the letter you are looking to convert
        - Say the next letter in the alphabet
        - Say the next number (counting up by 1)
- The number you just said is the decimal number that your letter converts too.

For example, to convert the letter E, the algorithm would have you counting A,1; B, 2; C, 3; D, 4; E, 5.

{image file-path="img/topics/binary_count_girl.png"}

(A more efficient algorithm would have a table to look up, like the one created at the start of the activity, and most programming languages can convert directly from characters to numbers, with the notable exception of Scratch, which needs to use the above algorithm.)

The next algorithm is the same algorithm we used in lesson 1, which we use to convert a decimal number to a binary number:

- Find out the number of dots that is to be displayed. (We'll refer to this as the "number of dots remaining", which initially is the total number to be displayed.)
- For each card, from the left to the right (i.e. 16, 8, 4, 2, then 1):
  - If the number of dots on the card is more than the number of dots remaining:
      - Hide the card
  - Otherwise:
      - Show the card
      - Subtract the number of dots on the card from the number of dots remaining

#### What to look for:

Have students create instructions for, or demonstrate, converting a letter into a decimal number (with or without the table), and then convert a decimal number into binary; are they able to show a systematic solution?
Can they explain what they are doing at each step and why?

{panel end}

{panel type="ct-abstraction" title="Abstraction"}

This activity is particularly relevant to abstraction, since we are representing written text with a simple number, and the number can be represented using binary digits, which, as we know from lesson 1, are an abstraction of the physical electronics and circuits inside a computer.
We could also expand our abstraction because we could use any two symbols other than 0s and 1s to represent our message (although while students are first learning this we recommend sticking with 1s and 0s).
For example, you could represent your message by flashing a torch on and off (this gives an idea of how information might be sent over a fibre-optic cable!), or drawing a line of squares and triangles on the whiteboard.

{image file-path="img/topics/binary_torch.png"}

Abstraction helps us simplify things because we can ignore the details we don’t currently need to know.
Binary number representation is an abstraction that hides the complexity of the electronics and hardware inside a computer that stores data.
Letters are an abstraction that a human can make sense of quickly; talking about the letter H is generally more meaningful than calling it "the 10th letter of the alphabet", and when we are reading or speaking we don’t need to know it is the 10th letter anyway.

####  What to look for:

When you use a different representation for binary, such as turning the torch on and off, who are the students who quickly see that this is equivalent to when they previously used 0s and 1s?
They will probably feel comfortable working with this new representation quickly, and other students may be very confused by this change.
Look for students who then decide to create their own representations of binary numbers.

{panel end}

{panel type="ct-decomposition" title="Decomposition"}

The core example of decomposition in this activity is understanding that in computing we have to break down all information into tiny chunks so that computers can store and send this data as bits and bytes. Everything we store inside a computer and see appear on the screen has to have been, in some way, broken down into binary digits.

In this lesson students have performed several steps of decomposition as they have taken the task of encoding a message and broken it down into simple steps. To write a message in binary we have to first look at the message one letter at a time and convert each of these, one-by-one, into decimal numbers, and then convert each of these numbers, one-by-one, into binary numbers. Students perform these same steps in reverse to convert the message back to text.

#### What to look for:

Can students explain why it is important that we can use binary to represent letters? Ask them why it is useful each separate letter into binary, rather than choosing a decimal and binary number for each different word.

{panel end}

{panel type="ct-pattern" title="Generalising and patterns"}

Recognising patterns in the way the binary number system works helps give us a deeper understanding of the concepts involved, and assists us in generalising these concepts and patterns so that we can apply them to other problems.

#### What to look for:

Have students decode a binary message from another student, by converting the binary numbers into decimal numbers, and then to text to view the message. Ask them what they would do if they wanted to include other characters in their message: what if we wanted upper and lower case letters? What if we want to use exclamation and question marks?
Observe which students see that we can simply generalise the method they are already using and can match other characters to bigger decimal numbers, e.g a-z can be 1-26, and A-Z can be 27-52.
If we can represent 32 different characters in binary when we use 5 bits for each character, then how many would we need for 64? Which students can see the pattern of binary and doubling in this situation, and see that we simply need to use 1 more bit to do this?

{panel end}

{panel type="ct-logic" title="Logic"}

Logical thinking involves making decisions based on knowledge you have, and these decisions should be sensible and well thought out. If you memorise that the letter H is represented as binary 01010 it's not as useful as learning how to represent any character using the process described in this activity. If you can understand the logical steps we take as we convert a letter into a binary number, and how we can convert it back, then you will be able to represent any character as binary, and more importantly, you understand the process, since you're more likely to get a computer to do it for you rather than always do it manually. This is especially relevant if we want to represent a large number of characters. What if we wanted to represent every Chinese character? There are over 50,000 of them so trying to memorise them all would take a long time!
When we choose the decimal numbers to use for each of the letters we didn’t have to choose 1 to 26, we could have decided to start at 17 instead and go from 17 to 42, or we could have chosen completely random numbers! What if we decide that A = 82, B = 5, C = 42… Would this be a logical decision to make? 1 to 26 makes much more sense because it is much easier to describe and remember.

#### What to look for:

Observe the systems students have created to translate their letters into binary and vice versa. What logic has been applied to these? Are they efficient systems? Can they explain what they are doing at each step?
Ask students why we are using the numbers 1 to 26 to represent our letters, or if they think there could be a better choice. Ask them how they would choose numbers for other characters, such as choosing a number to represent a space. Which ones give logical answers and can explain why their solution is a good choice?

{panel end}

{panel type="ct-evaluation" title="Evaluation"}

An example of evaluation is working out how many different characters can be represented by a given number of bits e.g. 5 bits can represent 26 characters comfortably, but 16 bits are needed for a language with 50,000 characters. When thinking about how many bits to use to represent something Computer Scientists also have to think about are how much space this is going to take up on a computer (16-bit characters take up twice the space of 8-bit characters), and if we should have some extra bits in case we want to add more characters in the future. Evaluating the benefits and costs of using a certain number of bits is also an idea students can explore.

#### What to look for:

Can a student work out how many bits are needed to represent the characters in a language with 100 characters? (7 bits are needed)
How about representing emojis, when you have about 4000 emojis available (12 bits will be needed for each one).

{panel end}
