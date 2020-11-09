# Buchstabencodierung mittels binärer Darstellung

## Key questions

How do you think a computer knows which letter to show on the screen?

{panel type="teaching"}

# Teaching observations

Discussion may start at the 26 letters of the English alphabet, and then expand to other characters on the keyboard, including capital letters, digits and punctuation. Students may be aware that other languages can have thousands of characters, and the range of characters is also expanding as emoticons are invented!

{panel end}

## Lesson starter

{panel type="general"}

# Hinweise zu Ressourcen

There is also an online interactive version of the binary cards [here](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), from the [Computer Science Field Guide](http://www.csfieldguide.org.nz/), but it is preferable to work with physical cards.

{panel end}

Can we match letters to numbers so that we can send coded messages to each other?

How many letters are there in the alphabet? Let’s count them together on our alphabet cards.

How can we represent the letters using numbers? (Guide students to the idea of using 1 for A, 2 for B, and so on.)

We can represent numbers using binary, but in the last lesson with 4 bits, what was the biggest number we could represent? (15)

How can we represent bigger numbers? (Add a card). How many dots on the extra card? (16)

Give out the cards, and have the students place them on the table in the correct order (16, 8, 4, 2, 1).

Now give them a number by saying "No, Yes, No, No, No" for the 5 cards. Ask them how many dots this produces. (The "Yes" is for the 8 card, so it's the number 8.) Which letter is number 8? ("H"). This can be written on the board.

Now give the next number, "No, Yes, No, No, Yes" (9). Which letter is number 9? ("I", which can be written after the "H".)

That's the whole message - "HI".

Now try sending a different word to the class. The [Binary to Alphabet resource]('resources:resource' 'binary-to-alphabet') below shows the binary patterns for the 26-letter alphabet; you can use yes/no for 1/0, but you could also use other ways of saying them, such as "on/off", "up/down", or even "one/zero". In particular, it may be helpful to represent a number higher than 16 to give them experience with the 5th bit.

{panel type="teaching"}

# Teaching observations

Note that if your local alphabet is slightly different (e.g. has diacritics such as macrons or accents.) then you may wish to adapt the code to match the common characters; this issue is also considered below.

{panel end}

# Lektionsaktivitäten

Let’s work this out how to write our own binary code for “dad”.

You sing/say the alphabet slowly and I’ll count how many letters go by until we get to ‘D’ (D is the 4th letter).

So how do we make 4 using binary code?

{image file-path="img/topics/binary-4-equals-d.png" alt="Kids holding binary cards"}

OFF OFF ON OFF OFF

You sing the alphabet slowly and I’ll count how many letters go by until we get to ‘A’. A is the 1st letter .

So how do we make 1 using binary code?

{image file-path="img/topics/binary-1-equals-a.png" alt="Kids holding binary cards"}

OFF OFF OFF OFF ON

Hang on! Haven’t we already written the binary code for D? We can reuse that! Computer Scientists always look for ways to reuse any work they have done before. It’s much faster this way.

Now let’s try this with someone’s name? Whose name should we translate into binary numbers?

Choose a student and work through the steps to create their name.

To reinforce students' alphabet knowledge, you could translate all student's name into binary numbers onto a piece of card and display it around the room.

{panel type="teaching"}

# Teaching observations

Some languages have more or fewer characters, which might include those with diacritic marks such as macrons and accents. If students ask about an alphabet with more than 32 characters, then 5 bits won't be sufficient. Also, students may have realised that a code is needed for a space (0 is a good choice for that), so 5 bits only covers 31 alphabet characters.

A typical English language keyboard has about 100 characters (which includes capital and lowercase letters, punctuation, digits, and special symbols). How many bits are needed to give a unique number to every character on the keyboard? (typically 7 bits will been enough since it provides 128 different codes).

Now have students consider larger alphabets. How many bits are needed if you want a number for each of 50,000 Chinese characters? (16 bits allows for up to 65,536 different representations).

It may be a surprise that only 16 bits is needed for tens of thousands of characters. This is because each bit doubles the range, so you don't need to add many bits to cover a large alphabet. This is an important property of binary representation that students should become familiar with.

{panel end}

{panel type="teaching"}

# Teaching observations

The rapid increase in the number of different values that can be represented as bits are added is exponential growth i.e. it doubles with each extra bit. After doubling 16 times we can represent 65,536 different values, and 20 bits can represent over a million different values. Exponential growth is sometimes illustrated with folding paper in half, and half again. After these two folds, it is 4 sheets thick, and one more fold is 8 sheets thick. 16 folds will be 65,536 sheets thick! In fact, around 6 or 7 folds is already impossibly thick, even with a large sheet of paper.

{panel end}

## Lesson reflection

- What are some reasons why we don’t use the binary number system as the representation for our written language?
- What did you find challenging during this lesson?
- How did you overcome these challenges?