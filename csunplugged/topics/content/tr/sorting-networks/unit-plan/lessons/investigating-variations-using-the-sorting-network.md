# Investigating variations using the Sorting Network

## Preparatory knowledge

Students should have completed lesson 1 to introduce Sorting Networks.

## Key questions

- In the Sorting Network, what do we think will happen if the smaller card goes right instead of left at each box and vice versa? (Students should be able to reason that the values will come out in reverse sorted order.)

- Will it work if we try to use the Sorting Network backwards, starting with the mixed-up numbers at the output end, and working backwards? (Students may have different views on this; it appears to work most of the time, but in this lesson we will find an example that doesn't.)

## Lesson starter

Show the students the Sorting Network again (if the network needs redrawing then students often enjoy doing this, and drawing it accurately from the diagram is a useful exercise). Tell them that they will be trying it with some variations this time.

Several variations are shown below, and you can choose the ones that suit the students, or you may come up with other items that could be sorted. The key is that the comparisons obey the transitive rule: that if a is smaller than b, and b is smaller than c, then a is smaller than c. Sorting by student height or other personal attributes can be problematic - not only might it be a sensitive issue, but comparing two students to find the highest might not give a consistent result if they are a similar height.

{panel type="math"}

# Mathematical links

Predicting outcomes: by understanding how the Sorting Network works students will be investigating different ways of using the Sorting Network and exploring how the outputs are affected by these changes.

{panel end}

## Variations with numbers

This part of the lesson explores changing the way the numbers are used.

### Variation 1: Identical value

{image file-path="img/topics/sorting-network-equal-3.png" alt="Two people each holding up a card with the number 3 on it."}

In this variation, students try the Sorting Network with a set of cards where some cards have an identical value, such as 1, 2, 3, 3, 4, 5. They will probably ask what to do when comparing the identical cards - ask them what they think, and they are likely to realise that it won't make any difference (if 3 and 3 meet, then it won't matter which one goes left and which goes right!) Ask them to predict will happen at the end of the network (they may realise that the identical values will end up adjacent).

Now run the numbers through the network to check. Here's a brief reminder of the Sorting Network instructions; full details are in lesson 1.

1. Six students start in the input circles, each holding a card with one of the numbers on it.

2. They all step forward at the same time, and when they meet someone in a box, they compare their cards.

3. The person with the smaller card follows the line out to the left, and and the larger card to the right (this is reversed in the second variation for this lesson).

4. This continues until all the students reach the output circles, at which point they should be in sorted order.

### Variation 2: Larger to the left

This time, the person with the larger number goes to the left instead of the right and follows the line to the next square, while the person with the lower number goes to the right instead of the left and follows the line to the next square.

Ask the students to predict what will happen (they should be able to work out that the values will come out in reverse sorted order i.e. from largest to smallest instead of smallest to largest).

Have them try it out with some numbers to check it.

{panel type="teaching"}

# Teaching observations

By reversing the left/right decision, the final result will be in the reverse order to how it would have been in lesson 1.

{panel end}

### Variation 3: Letters of the alphabet

{image file-path="img/topics/sorting-network-variation-alphabet.png" alt="Cards with letters on them."}

Give the students cards with letters on them. Ask how we could compare these (students should observe that they could be in alphabetical order). Have them test this by sorting the cards.

### Variation 4: Words made of letters in alphabetical order

As an interesting variation of sorting letters, there are some English words that have the letters in alphabetical order, such as BIOPSY. If you give the students the letters out of order (such as P, O, I, B, Y, and S) and have them sort them in the Sorting Network, it will form the world BIOPSY at the end. There are few common words with this property; other examples include ALMOST and ABHORS. Have the students try the Sorting Network with some of these words (note that you will need to read the sorted letters from the direction of the starting position to see the word in the correct order).

There is also a number of words that have the letters in reverse alphabetical order, such as SPONGE and ZONKED (these can be sorted using the "larger to the left" variation, or can be read from the far side of the Sorting Network). Some words with this property have double letters in them, such as BELLOW; these will sort correctly, since the order of the double letters is immaterial.

{panel type="general"}

# List of words with letters in alphabetical order

Here is a longer list of 6-letter words that can be used for this exercise. They are all from a dictionary, although some are rather obscure!

{image file-path="img/topics/sorting-network-toffees-cellos-sponge.png" align="right" alt="2 toffees, 2 cellos and a sponge."}

AFFLUX, AGLOOS, ALMOST, BEGILT, BEGINS, BEGIRT, BEKNOT, BELLOW, BIJOUX, BILLOW, BIOPSY, BLOOPS, BLOTTY, CELLOS, CHIKOR, CHILLS, CHILLY, CHIMPS, CHINOS, CHINTZ, CHIPPY, CHIRRS, CHITTY, CHIVVY, CHOOSY, CHOPPY, CLOOPS, CLOTTY, DEFFLY, DEHORT, DEKKOS, DIKKOP, DIMPSY, EFFLUX, EFFORT, ELLOPS, FILLOS, FLOORS, FLOOSY, FLOPPY, FLOSSY, GHOSTY, GIMMOR, GLOOPS, GLOOPY, GLOPPY, GLOSSY, HILLOS, KNOTTY, JIGGED, LIGGED, MIFFED, NIFFED, PIGGED, POLKED, POLLED, POLLEE, POMMEE, POMMIE, PONGED, PONGEE, PONIED, PONKED, POOHED, POOLED, RIFFED, RIGGED, ROLFED, ROLLED, RONNIE, ROOFED, ROOKED, ROOKIE, ROOMED, ROOMIE, SOGGED, SOOGEE, SOOKED, SOOLED, SOOMED, SPLIFF, SPOKED, SPONGE, TIFFED, TIGGED, TOFFEE, TOGGED, TOLLED, TOLLIE, TOMMED, TONGED, TONKED, TOOLED, TOOMED, TOONIE, TROKED, UNFEED, VOMICA, VUMMED, WIGGED, WOLFED, WONNED, WOOFED, WOOLED, WOOLIE, WOONED, WULLED, WURLIE, YOKKED, YOLKED, YONNIE, YTTRIA, YTTRIC, YUKKED, YUPPIE, YWROKE, ZIGGED, ZONKED, ZOOMED, ZOONED, ZOONIC.

{panel end}

### Variation 5: Sorting words in dictionary order

{image file-path="img/topics/sorting-network-variation-words.png" alt="The words crochet and crocodile."}

Give the students cards with dictionary words on them, and ask how these might be compared. Students should observe that they could be placed in dictionary order. A variation is to give them books and have them sort them in order of the authors' names.

{image file-path="img/topics/sorting-network-crochet-v-crocodile.png" alt="Crochet vs crocodile."}

Comparing two words or names is challenging; they will need to know to compare each character until two differ (e.g. for "crochet" and "crocodile", the "croc" prefix is the same, so it is the "h" and "o" that determine their order; this process is an algorithm in itself!)

{image file-path="img/topics/sorting-network-variation-words-2.png" alt="The words kowhai and kākāriki."}

The words being compared could also be used to reinforce spelling or meaning; for example, the words above are the colours in Te Reo Māori, so the student with the word "kowhai" would be reinforcing that it means the colour yellow. The use of macrons and other diacritical marks also gives the opportunity to explore the order that is used in the such languages for those letters.

### Variation 6: Music notation

{image file-path="img/topics/sorting-network-variation-music.png" alt="Two treble clefs."}

Students can compare the pitch of music notation, with higher notes going to the right. If all the cards have the same clef (such as the treble clef here) then it reinforces that the height on the stave corresponds to the pitch. Advanced music students can do the comparisons with different clefs (bass, alto and/or tenor) to exercise note reading.

### Variation 7: Music pitch - aural

{image file-path="img/topics/sorting-network-variation-aural.jpg" alt="Two students compare the pitch of their bells."}

In this variation, students compare the pitch of simple instruments that they are carrying. The bells shown above are ideal because they are all the same size, and force students to compare them by listening. This variation can be challenging because students need to learn what high and low notes are; it can help to have a teacher or music student help with any comparisons that the students aren't sure about, and it may pay to start with notes that aren't close in pitch.

Choosing the 6 notes from a pentatonic scale (e.g. C, D, E, G, A, C) happens to work well, as the sound of all 6 being compared at the same time is a little more pleasant!

## Using the network backwards

This is an experiment that addresses a question that students may have asked: does the Sorting Network correctly sort the values if we start at the other end?

Have students try this with some simple values (such as the numbers 1 to 6). Chances are that it will work for many starting orders of the values. However, encourage them to keep trying until they find an initial order for which it doesn't work. This will require considerable reasoning to achieve.

If they struggle to find an example, you could give the one below, and then challenge them to find a different one that doesn't come out sorted.

{panel type="teaching"}

# Teaching observations

The Sorting Network is designed to work consistently one way, rather than working both ways. For example, the first image below shows an input that happens to come out sorted when going through the network backwards, while the second one doesn't. If it fails on just one input (the second one) then we can't rely on it, even though it sometimes works. In the other direction, it will always sort correctly.

{image file-path="img/topics/sorting-network-backwards-1.png" alt="This diagram shows that when the Sorting Network is given the input 654321 it happens to come out sorted when ran backwards."}

{image file-path="img/topics/sorting-network-backwards-2.png" alt="This diagram shows that when the Sorting Network is given the input 512364 it does not come out sorted when ran backwards."}

{panel end}

## Applying what we have just learnt

This kind of algorithm needs to run on special hardware to take advantage of doing multiple comparisons at the same time. It is only used for specialist applications at present, for example it is sometimes done on the graphics processor (GPU) of a computer, because these processors are good at doing parallel computation. Sorting Networks were invented long before powerful GPUs came along; this is an exciting thing about Computer Science - some of our discoveries are ahead of the hardware that is available, so we're ready to make use of the hardware when it does become commonly available! Note that this is *not* a conventional sorting algorithm, as the sorting that is done on a conventional system can make only one comparison at a time; conventional sorting algorithms are explored in another lesson.

## Lesson reflection

What did you notice happen with each variation of using the Sorting Network?

Was it what you had expected?