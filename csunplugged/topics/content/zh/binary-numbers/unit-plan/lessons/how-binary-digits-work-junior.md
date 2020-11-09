# How binary digits work

## Key question

- How do you think a digital device stores information?

Accept and record all answers to revisit at the end of the lesson.

## Lesson starter

{panel type="video"}

# See teaching this in action

{video url="https://vimeo.com/437725275"}

{panel end}

{panel type="general"}

# Note from the authors

We’ve noticed that when we teach the binary number system to students ages 5 - 7 we are focusing on number knowledge and number identification rather than how the binary number system works. We also support students to learn to count by one to one matching, because they are counting the dots. Students are motivated to learn because they are learning how computers store information. Students may ask you questions and be excited to explore the concepts outlined in this lesson further. We’ve added a lot of information into this lesson, however, it is not our intention that you will teach and cover all the concepts, but that you have at your fingertips the information you need when your students express an interest in learning more.

{panel end}

{panel type="general"}

# Notes on resources

There is also an online interactive version of the binary cards available (4 card version, corresponding to this activity, or 5 card version if students are comfortable with numbers up to 31), from the [Computer Science Field Guide](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8). However, we strongly recommend using physical cards to start with.

{panel end}

Did you know that right in the inside of any computer there are billions (that’s a really really big number) of little tiny things that can be turned on or off, like a light switch, and that when you have lots of these things together they can display a number or a letter or a movie or make up your favourite game on your device? So let’s look at how they work. Now we need to pretend that we are so incredibly small that we are now inside a computer and we are making the computer show a number. Are you ready?

First of all here’s a card that is the tiny thing that can be turned on or off. The technical word for that is a “bit”.

1. Hold the 4 cards (1, 2, 4, and 8 dots), but don't let students see the dots. Ask for 4 students to volunteer to be “bits”, and have them stand in a line in front of the class.

2. Hand out the 1-dot card to the person on the right. Explain that they are one "bit" (binary digit), and can be on or off, black or white, 0 or 1 dots. The only rule is that their card is either completely visible, or not visible (i.e. flipped over). Hand out the second card so that the first card is on the far right. Point out that this card has either 2 dots, or none.
    
    {image file-path="img/topics/col_binary_4_kids_2_cards.png" alt="2 kids holding binary cards"}

3. Ask the class what the number of dots on the next card will be. Get them to explain why they think that.
    
    {panel type="teaching"}
    
    # Teaching observations
    
    Students will usually suggest it should be three. If they suggest 4, they may have done the activity before (or have seen the cards you are holding!), or they may have very good pattern recognition skills! If they suggest the wrong number, don't correct them, but continue without comment, so that they can construct the rule for themselves.
    
    {panel end}

4. Silently give out the 4-dot card, and let them try to see the pattern. This will be dependent on their level of number knowledge. Mention that each number is doubling (or that if you had two of a card, that would give you the card beside it), and move onto the next step.
    
    {image file-path="img/topics/col_binary_4_kids_3_cards.png" alt="3 kids holding binary cards"}
    
    {panel type="teaching"}
    
    # Teaching observations
    
    Usually some students will point out that you've missed out the three, but simply indicate that you haven't made a mistake, something is happening to the numbers and we will be able to make three by using the cards.
    
    {panel end}

5. Ask what the next card is, and why.
    
    {panel type="teaching"}
    
    # Teaching observations
    
    At this point it is common for students to guess that it is 6 (since it follows the numbers 2 and 4). However, if you let them think about it a little more, some will usually come up with 8, and those students should be able to convince the others that they are correct. There are several ways a student could explain this e.g. that each card is double the previous one, or that if you take two of a card, you get the next one. Some may recite the pattern 1+1=2, 2+2=4, 4+4=8.
    
    If your class are learning to count then show all the cards and count how many dots are on each one. Look for the patterns of doubling and count the dots to prove this.
    
    {panel end}

6. Show the 4th card and hand it out:
    
    {panel type="teaching"}
    
    # Teaching observations
    
    Background information for those who are curious! If we kept handing out cards then once we got to 8 cards we would have 256 dots in total if we added up all the cards. This is 8 bits, which is commonly referred to as a byte. It may be distracting to bring this up at this point, but some students may already be familiar with the idea that 8 bits is a byte, and make that observation. However, in the meantime, we'll work with a 4-bit representation, which isn't as useful as a whole byte, but a good size for teaching younger students. 4 bits is actually called a nibble (sometimes spelt nybble)! This is a fun extra piece of information for interested students.
    
    A common mistake is to hand out the cards from left to right, but it's convention in number representation that the least significant value is on the right, and this is an important idea for students to take away from this activity.
    
    {panel end}

## Lesson activities

1. Tell the students that the rule is that a card either has the dots showing, or hiding. If we can turn cards on (showing) and off (hiding) by showing the front and back of the card, how would we show 3 dots? Begin by asking: how many dots are on the left-most card? Count together that there are 8 dots. Let’s look at the number line. Is 8 bigger than 3? Let’s hide it because it’s too big. Now let’s look at the next card, how many dots can we see? Let’s count them. There are 4, is 4 bigger than 3? Yes, so we need to hide the card. If we didn’t hide the 4 card what would happen? (There would be too many dots). How many dots are on the next card? Let’s count them. There are 2 dots. Let’s look at the number 3, (show it with materials and show that 2 fits into 3, with how many left over?) We need one more dot to make the number 3. So we will leave that card visible.
    
    Without being given any rules other than each card being visible or not, students will usually come up with the following representation.
    
    {image file-path="img/topics/binary_cards_equals_three.png" alt="Diagram showing that 2 binary cards make the number 3"}
    
    {panel type="math"}
    
    # Mathematical links
    
    At a junior level we are focusing on using this counting system to represent numbers and making the association that with these “bits” you can make any number. We’re not going to focus on further knowledge about number base systems. The information below is extra information for you.
    
    For teachers: Base 10 (our normal counting system) has 10 digits, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. When we count in base 10, we count from 0 to 9 and then run out of digits. So we need to add another column; we put a 1 in that column and start counting again from 0. This makes the number 10, we then repeat that process until the tens column is 9 and the ones column is 9 (making 99); from there we then add another column. Hence we have the familiar place value system that can be shown something like this:
    
    100,000s | 10,000s | 1,000s | 100s |10s | 1 **Note: Use the appropriate place value example based on what you have already taught in your class; this is an extended example.**
    
    Base 2 (binary) follows the same logic, except it moves a lot quicker to the “next” place value, because there are only two digits, 0 and 1. The binary place values look like this:
    
    32 | 16 | 8 | 4 | 2 | 1 |
    
    Sometimes students confuse the order of digits in a binary representation. To support students to understand the correct ordering of binary digits, ask the question: If I was going to give you $435.00 which number are you most interested in? Is it the 4 or the 5? Why is that? It’s the same for binary code, the lowest value (least significant digit) is on the far right, whereas the most significant digit is on the far left.
    
    Base 16 is also commonly used on computers - it's called hexadecimal, and has 16 digits. While this is far beyond the scope of this lesson, we wanted to point out that one hexadecimal digit is the equivalent of 4 binary digits (bits), because both can represent 16 different values (from 0 to 15). So this exercise that the students are doing provides a great basis for later understanding another common representation that they will encounter on digital devices.
    
    {panel end}

2. Now ask "How would you make the number 6?" (Again, start by asking if they want the 8 card, and so on from left to right).

3. The process we have been following to make these numbers is an algorithm, which converts our normal counting numbers to a binary representation. Together let’s think through the steps we followed to do this. We'll do this by using the earlier example of representing the number 3 again.
    
    a. Start with all the numbers switched to on (all the dots visible). You could start to introduce abstract representations, like varying the description of the cards (visible/hidden; dots/no-dots; white/black if the backing is black; yes/no; or on/off)
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_4.png" alt="4 lightbulbs switched on"}
    
    b. Does 8 fit into 3? No - so turn it off
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_3.png" alt="3 lightbulbs switched on"}
    
    c. Does 4 fit into 3? No - so turn it off
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_2.png" alt="2 lightbulbs switched on"}
    
    d. Does 2 fit into 3? Yes - so keep it on. How many are left over? (1)
    
    e. Does 1 fit into 1? Yes - so keep it on. How many are left over? (none)
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_2.png" alt="2 lightbulbs switched on"}

## Applying what we have just learnt

- Group students into pairs
- Give each pair a set of the smaller binary cards
- Have them practise the algorithm for numbers below 10.

1. Explain to students that we're working with just two digits, so they are called binary digits. (You could explore the meaning of the "bi" prefix with words like bicycle, biennial, bilingual and bicultural.) Binary digits are so common that we have a short name for them: write "binary digit" on a piece of paper, then rip off the "bi" at the start, and the "t" at the end, put it together and ask what the combined word ("bit") spells. This is the short name for a binary digit, which is why we've been referring to the cards as bits; the 4 cards that they have are actually 4 bits.

2. Now let’s count from the smallest number that we can make, up to the highest number
    
    a. What is the smallest number? (they may suggest 1, then realise that it’s actually 0).

3. Get the number 0 displayed on the cards (i.e. no dots showing)

4. Now count up 1, 2, 3, 4 …. (each pair should work out these numbers between them)

5. Once they start to get into a routine, ask: how often are we seeing the 1-dot card? (every second time, every odd number)
    
    a. What other patterns are we seeing? (the 2-dot card flips on every second count, the 4-dot on every 4th and so on; the 8 dot card doesn't do much; this may be challenging for some students to recognise, and the main goal is that they are aware that the 1-dot card flips every time, and that every second number is an odd number).

6. Continue until all the cards are switched to “on” and have counted to 15. What happens next? (We have to add a new card.) How many dots on it? (16) What do we have to do to the other 4 cards when we get to 16? (we have to turn them all off)

7. Extension ideas ...
    
    a. So when I have two bits I can make a maximum of? (3)
    
    b. I add another bit and that has how many dots on it? (4)
    
    c. I turn off the first two bits to make 4 right?
    
    d. Now let’s turn on all three bits, so now we have how many? (7)
    
    e. I add another bit and that has how many dots on it? (8)
    
    f. Repeat until a pattern is recognised that the number on the next card is one more than the total number of dots on all the cards to the right (e.g. there are 7 dots on the 4, 2 and 1 cards, so the next card to the left is 8). This makes it easy to work out the number if all the bits are switched on - double the left-hand card, and subtract 1.
    
    g. How many different numbers can I make with two bits? (4; often students will say 3 because they haven’t counted 0).
    
    h. Let’s add the next bit; how many different numbers can we make now? (8, again 7 will often be given as an answer first).
    
    i. Repeat until a pattern is recognised that each time we add another bit we can now represent twice as many numbers.

{panel type="teaching"}

# Teaching observations

A concept that students may struggle with here is that the number of values is one more than the maximum value (e.g. from 0 to 7, there are 8 different numbers). The same observation occurs with the number of digits in conventional decimal numbers; the largest digit is 9, but there are 10 possible digits (counting 0). This is sometimes called the fencepost problem (the number of fence posts is one more than the number of gaps between them), and it comes up a lot in computing and in maths.

{panel end}

## Lesson reflection

- Would this activity work if we used white and cream cards? Why? Why not?
    
    - In principle you could use these, but it wouldn’t be a good idea. We are looking for the answer that they are not contrasting colours, therefore it would be difficult to see if it is actually on or off. Computers are easier to build and break less often when we just use two contrasting values.

- What are some other ways we could physically show that each of the bits are on or off?
    
    - Ideas could include holding the cards up high, or down low; simply holding up a hand; sitting down or standing up; or using a different representation such as lights that are on or off.

- What else could we use to represent two opposites, like on and off, in writing?
    
    - Perhaps a cross or tick; happy or sad face; or any other pair of symbols.