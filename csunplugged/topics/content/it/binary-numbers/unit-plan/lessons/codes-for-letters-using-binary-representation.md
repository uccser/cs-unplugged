# Codes for letters using binary representation

## Key questions

- How many different characters can you type on a computer? (Discussion may start at the 26 letters of the English alphabet, and then expand to other characters on the keyboard, including capital letters, digits and punctuation. Students may be aware that other languages can have thousands of characters, and the range of characters is also expanding as emoticons are invented!)

## Lesson starter

{panel type="general"}

# Notes on resources

There is also an online interactive version of the binary cards [here](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), from the [Computer Science Field Guide](http://www.csfieldguide.org.nz/), but it is preferable to work with physical cards.

{panel end}

{image file-path="img/topics/col_binary_robot_boy_convo.png" alt="Cartoon boy talking to robot" alignment="left"}

Discuss how you would communicate a letter of the alphabet to someone if all you could do is say a number between 0 and 26. *(Students will usually suggest using a code of 1 for a, 2 for b, and so on)*.

Work out and write down the binary numbers using 5 bits from 0 to 26 on the Binary to Alphabet resource, then add the letters of the alphabet.

{panel type="teaching"}

# Teaching observations

- Check their binary code for three is 00011 as students commonly write 00100 as they anticipate the pattern without necessarily checking it is correct.
- Check they are writing the binary code in the correct order with the least significant value on the right - for example some will start with one as 10000 instead of 00001.
- Identify the students who are demonstrating one or all of these computational thinking attributes; being very systematic, have everything lined up exactly, are the first to recognise the pattern and don’t need the cards any more.
- Check that all students can describe back to you how to calculate the number they are up to. This will identify those who are guessing the pattern.
- Note that if your local alphabet is slightly different (e.g. has diacritics, macrons etc.) then you may wish to adapt the code to match the common characters; this issue is also considered below.

{panel end}

## Lesson activities

Using the table that students have created above, give them a message to decode, such as your name or the name of a book author (e.g. 00001 00010 00010 11001 for ABBY).

Now get students to write and communicate their own messages. Remind them that they can write the zeroes and ones using any symbols, such as ticks and crosses.

Consider unusual representations; for example, each bit could be communicated with a sound that is either high pitched or low pitched. Or the 5-bit number could be represented by holding up the five fingers on one hand, one finger corresponding to each bit.

## Adding more characters

Some languages have slightly more or fewer characters, which might include those with diacritic marks. If students consider an alphabet with more than 32 characters, then 5 bits won't be sufficient. Also, students may have realised that a code is needed for a space (0 is a good choice for that), so 5 bits only covers 31 alphabet characters.

Have the students design a system that can handle a few extra characters such as diacritics. (This can usually be done by allocating larger numbers, such as 27 to 31, to the other characters).

A typical English language computer keyboard has about 100 characters (which includes capital and lowercase letters, punctuation, digits, and special symbols). How many bits are needed to give a unique number to every character on the keyboard? (Typically 7 bits will been enough since it provides 128 different codes).

Now have students consider larger alphabets. How many bits are needed if you want a number for each of 50,000 Chinese characters? (16 bits allows for up to 65,536 different representations).

{panel type="teaching"}

# Teaching observations

It may be a surprise that only 16 bits is needed for tens of thousands of characters. This is because each bit doubles the range, so you don't need to add many bits to cover a large alphabet. This is an important property of binary representation that students should become familiar with.

{panel end}

{panel type="math"}

# Mathematical links

The rapid increase in the number of different values that can be represented as bits are added is *exponential* growth i.e. it doubles with each extra bit. After doubling 16 times we can represent 65,536 different values, and 20 bits can represent over a million different values. Exponential growth is sometimes illustrated with folding paper in half, and half again. After these two folds, it is 4 sheets thick, and one more fold is 8 sheets thick. 16 folds will be 65,536 sheets thick! In fact, around 6 or 7 folds is already impossibly thick, even with a large sheet of paper.

{panel end}

{panel type="teaching"}

# Teaching observations

Using a 5-bit code for an alphabet goes back to at least 1870 (the "Baudot" code); many different number to letter correspondences have been used over the years to represent alphabets, but one that was common for some time is "ASCII", which used 7 bits and therefore could represent over 100 different characters. These days "Unicode" is common, which can represent over 100,000 different characters. Nevertheless, each of these codes, including Unicode, still contain elements of the simple code used in this lesson (A is 1, B is 2...). For example, the ASCII code for "A" is 65 and "B" is 66 etc.; if you work out the binary representations of these, and just keep the right-most 5 bits, you've got the code that we've been using above.

{panel end}

## Lesson reflection

- What are some reasons why we don’t use the binary number system as the language for our written language?
- How do you think ancient Egyptians would have converted their hieroglyphics to binary?
- What did you find challenging during this lesson?
- How did you overcome these challenges?