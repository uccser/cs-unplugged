# Parity Magic

A demonstration of lesson one ("Parity magic") being taught is available [here](https://youtu.be/FnwBratAhfg).

## Learning Outcomes

Students will be able to:

#### DT/CT

- Describe the steps it takes to work out how to find the card that is turned over.
- Identify that the error is at the intersection of an odd row/column
- Explain why they chose each extra card when setting up the parity column/row

#### Curriculum Integration:

- Mathematics: counting, categorising (black/white), even/odd numbers, grids, rows, columns, intersection

## Resources

- A set of 36 “fridge magnet” cards, all identical with a different colour on each side (e.g. black and white); or non-magnetic cards, in which case the demonstration should be done on a table-top or the floor.
  The magnetic ones would need to be magnetic both ways up; sheets of double-sided magnetic material can be purchased, but conventional fridge magnets usually won't stick upside down. Double sided magnetic cards can also be made by sticking single-sided magnetic sheet back to back.
  Paper (non-magnetic) cards can be made by cutting up a sheet of light card that is a different colour on each side.
- A metal board (ideally a whiteboard) if magnetic cards are being used.
- Each pair of children will need: a set of 36 (non-magnetic) cards as above.

There is also an online interactive version of the parity cards [here](http://csfieldguide.org.nz/en/interactives/parity/index.html), from the Computer Science Field Guide.

## Key question

- Why is it important for computers to be able to detect if the data received over the internet is the same as the data that was sent? 
- What if I sent you an email that said you could now have Monday off school, but when you received it, there was some electrical interference and a bit was changed from off to on so that the word "now" became "not". What would your reaction be? 
- Can computers correct these sorts of mistakes automatically, and how would they do that? 

### Potential answers could include:

- We use computers for important things like banking, writing school reports, and communicating with each other.
  If the information being stored got changed without anyone knowing, you'd get the wrong balance in your account (too much or too little), the wrong grade in your report, or the wrong message in an email.
  This activity will look at how to correct this automatically.

## Lesson Starter

1. Teacher to class: “I’ve just learnt a magic trick I want to show you”.

2. Teacher to class: “So who will be my assistant?”

3. Teacher to student: Hand the cards to the student and ask them to make a grid of 5 by 5 cards (calling it "5 rows of 5 cards might be clearer for younger students").  “Don't make any patterns - try to make it as random as possible”. To speed up the setup you could have two students do this task; encourage them to leave a small gap between the cards, and not be too fussy about making them straight.

4. Point out that the cards represent bits (binary digits). If they haven't studied binary numbers, you may need to just point out that this is the way everything is represented on computers - the cards here could represent a file, a message, a web page or even a program.

5. Teacher to class: “I’m going to make this a little bit harder by adding another row and another column”.

{panel type="general" title="Teaching Observations"}

Of course, you are doing this on purpose because what you want to do is make sure that the number of black sides showing in each row and column is an even number.
This is always possible; if the student put an odd number of black cards in a row, you add another black card to the row; if they put an even number in the row, add a white card, to keep it as an even number. Remember that zero is an even number.

The extra cards are called "parity bits" (or parity cards), but there's no need to introduce the terminology yet, since that reveals the "magic"; for the meantime the idea is for the class to think that you are just adding even more random cards to make the task harder.

You should practise this several times before doing it in front of the class, as it becomes a lot easier to make it look casual when you've done it before, and makes the trick more mysterious.

{panel end}
