# Parité magique

## Questions clés

- Have you ever had a DVD not work properly? Or tried to scan a QR code and it didn’t load the website?
- How many of you think that computers correct these sorts of mistakes automatically?

### Les réponses possibles pourraient inclure :

Students may come up with situations where computers won't read a disc or scan a code, but they may also confuse this kind of problem with other kinds of failures such as an error in a program or a flat battery.

{image file-path="img/topics/school-test-error.png" alt="A school test shows every question marked correct but the overall score is 0%."}

Adults use computers for important things like banking, writing school reports, and communicating with each other. If the information being stored got changed without anyone knowing, you'd get the wrong balance in your account (too much or too little), the wrong grade in your report, or the wrong message in an email. Or worst still the website you are wanting to go to for your learning or the DVD you want to play won’t work! This activity will look at how computers correct this automatically.

## Lancement du cours

{panel type="video"}

# See teaching this in action

A demonstration of lesson one ("Parity magic") being taught is available here:

{video url="https://vimeo.com/437726658"}

{panel end}

{panel type="general"}

# Notes sur les ressources

You will require:

{image file-path="img/topics/parity-cards.png" alt="A pile of square cards with black on one side and white on the other side." alignment="right"}

- A set of 36 "fridge magnet" cards, all identical with a different colour on each side (e.g. black and white); or non-magnetic cards, in which case the demonstration should be done on a table-top or the floor. The magnetic ones would need to be magnetic both ways up; sheets of double-sided magnetic material can be purchased, but conventional fridge magnets usually won't stick upside down. Double sided magnetic cards can also be made by sticking single-sided magnetic sheet back to back. Paper (non-magnetic) cards can be made by cutting up a sheet of light card that is a different colour on each side.

- A metal board (ideally a whiteboard) if magnetic cards are being used.

- Each pair of children will need: a set of 36 (non-magnetic) cards as above.

There is also an [online interactive version of the parity cards here](http://csfieldguide.org.nz/en/interactives/parity/index.html), from the Computer Science Field Guide.

{panel end}

1. Teacher to class: "I’ve just learnt a magic trick I want to show you".

2. Teacher to class: "So who will be my assistant?"

3. Teacher to student: Hand the cards to the student and ask them to put up one row of 5 cards with some cards showing black and the other white. Ask them to add another row, but making sure there isn’t a pattern between the 2 rows. Continue to do that until you have a grid of 5 x 5. This is an opportunity to count all the cards, skip count in fives to 25, or to double check there really isn’t any patterns happening.

{panel type="teaching"}

# Observations sur l'enseignement

For teachers: The cards represent bits (binary digits). If they haven't studied binary numbers, you may need to just point out that this is the way everything is represented on computers - the cards here could represent a file, a message, a web page or even a program.

{panel end}

4. Teacher to class: “I’m going to make this a little bit harder by adding another row and another column”.

{panel type="teaching"}

# Observations sur l'enseignement

Of course, you are doing this on purpose because what you want to do is make sure that the number of black sides showing in each row and column is an even number. This is always possible; if the student put an odd number of black cards in a row, you add another black card to the row; if they put an even number in the row, add a white card, to keep it as an even number. Remember that zero is an even number.

The extra cards are called "parity bits" (or parity cards), but there's no need to introduce the terminology yet, since that reveals the "magic"; for the meantime the idea is for the class to think that you are just adding even more random cards to make the task harder.

You should practise this several times before doing it in front of the class, as it becomes a lot easier to make it look casual when you've done it before, and makes the trick more mysterious.

{panel end}

{image file-path="img/topics/parity-cards-6x6-grid-step-1.png" alt="5 rows of 5 parity cards in a random arrangement." caption="true"}

Step 1: Example layout of a 5x5 grid set up by the volunteer.

{image end}

### Step by step adding a parity bit to each row and column

{image file-path="img/topics/parity-cards.gif" alt="An animation of adding a parity bit to each row and column."}

The last parity bit placed is useful because it will always work for both the column and row; if it doesn't match for both the row and column then you'll have made a mistake with one of the cards, and should go back and check them (try to not make it obvious that you're doing that).

{panel type="teaching"}

# Observations sur l'enseignement

Now you have added parity cards to make the number of black squares in every row and every column equal to an even number. Don't point this out to the students at this stage.

{panel end}

## Activités de la leçon

Teacher to student: "I'd like you flip over one card while I cover my eyes".

Teacher to class: "Keep a close eye on which card it is to check if I have done my magic trick correctly!"

{panel type="teaching"}

# Observations sur l'enseignement

You need to emphasise that you want just one card flipped over. This prevents them from turning over too many cards (or none!). Usually students will follow this instruction, and their classmates will be able to confirm to you that, or let you know if one hasn't been turned over yet.

{panel end}

After the class confirms that a single card has been flipped, turn around to look at the cards. Scan the cards looking for the row with an odd number of black squares, and the column that has an odd number of black squares. The card that has been flipped will be at the intersection of these two lines. Turn this card over casually to restore it to the correct colour, saying “it’s this one”.

You can make a fuss that it might have been a fluke, so repeat the trick again. (After you put the card back to how it was originally, look away again and ask for another card to be flipped over.)

{image file-path="img/topics/parity-wizard.png" alt="A wizard holding a magic wand with parity cards on it." alignment="right"}

So is it magic? Or is it a trick?

Teacher to class: "Let’s first look at the cards before one was turned over" (make sure you've restored the card that was just flipped). The following steps will help the students to uncover what you've done:

- "Are there any patterns you can see? Think, pair, share."
- "Let’s break it down into parts"
- "Let’s look at the first row - count the black squares - how many are there?" (4 in the example above)
- "Now the second row - count the black squares - how many are there?" 2
- Note that it could be a row of all white squares - which would be 0 black squares; or it could be a row of all black squares - 6

Teacher to class: “If we group these numbers together, 0, 2, 4, 6, what do we call this group? Even numbers. What about 1, 3, 5? What is the name for this group of numbers? Odd numbers.

Let’s now look at the columns:

- "Does the first column have the same rule as the rows?".
- "What about the other columns?".

Teacher to class: “So how did we end up with an even number in every row and column - did the volunteer choose that?” (they didn't!).

{panel type="teaching"}

# Observations sur l'enseignement

Break these steps down to what is appropriate for your groups numeracy knowledge.

{panel end}

Remove your extra row and column, and have them explain what colour to place at the end of the first row to make sure there is an even number of black cards. For example, if there are 3 black cards, ask what colour you need to add to make it into an even number (black)? If there are 4 black cards, they should work out that you need a white card to keep it even.

Continue doing this for each row; then do it for the columns. This is a good exercise for students thinking about even and odd numbers. For the last (corner) card, ask if you should use the row or column to decide it. They should observe that it's the same for both.

Once the extra row and column have been added, ask “So what happens when I turn a card over from black to white?” (It reduces the number of black cards by one, so it's now an odd number). "What if I change a white card to black?" (it adds one, which also gives an odd number).

The students might work out from this how to find the flipped card, but in either case, have a student come up, and ask them to look away while you flip a card. Then, when they look back, ask "Is the first row ok?" (They should notice that it's still even, so hasn't been changed). Carry on for each row until they identify the one with an odd number of black cards. Draw a box around that row, and say "So one of these cards was flipped?" Now do the same with the columns - ask if each one is correct, then draw around the column that they identify.

Now ask "So which card was flipped?" Usually students will identify the one at the intersection.

{panel type="teaching"}

# Observations sur l'enseignement

Students have now worked out for themselves how this works. The key idea is that we just added a little more data, but could reconstruct the original if one card was changed.

{panel end}

{panel type="math"}

# Liens mathématiques

It also exercises the idea of grids (you can use phrases like "5 by 5") and the language of columns and rows.

For junior students there are a lot of opportunities to practise counting to 5 and recognising the patterns of even and odd numbers.

{panel end}

## Appliquer ce que nous venons d'apprendre

- This kind of method is applied to almost all data that is stored or transmitted on computers (although usually a more sophisticated method is used that is even more reliable). If we didn’t have error detection and correction then unexpected errors in data would be common, and digital devices wouldn't be used to store anything important. The world would be in chaos and people wouldn’t trust computers. Computers wouldn’t be reliable.
- DVDs and CDs wouldn’t work if one fleck of dust was on the disc.
- Backing up wouldn't help much as this would also be unreliable too.
- Transmitting data over long distances (e.g. from space probes) would be particularly unreliable, since it can take minutes, or even days, for data to arrive, and it's not feasible to request it to be retransmitted if it has had interference.

## Réflexion sur la leçon

If each square was a piece of information sent to the computer and there wasn’t any parity data added to it, could the information be received correctly from one computer to another if one of the pieces of data is changed? It can’t because if just one piece of information is incorrect then you have no way of knowing. But when we add the parity data to the information, even if one small piece of information is incorrect (turned off instead of on) then the computer can correct the information and can read it properly.

You could try using other objects. Anything that has two easily distinguished ‘states’ is suitable. For example, you could use playing cards, coins (heads or tails) or counters with two different colours on each side.

What happens if two, or more, cards are flipped? (It is not possible to detect exactly which two cards were flipped, although it is possible to tell that something has been changed. You can usually narrow it down to one of two pairs of cards. With 4 flips it is possible that all the parity bits will be correct afterwards, and so the error could go undetected.)