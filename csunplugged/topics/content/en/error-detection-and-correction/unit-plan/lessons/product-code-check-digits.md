# Product code check digits

{panel type="general" title="Preparatory knowledge"}

It is helpful, but not essential, for students to have done the lesson on the
Modulo operator before doing this lesson.

{panel end}

## Key questions

How many people do you know check their dockets at the supermarket or in a shop to be sure that what they purchased matches the docket?

## Potential answers could include:

- Typically it’s not many, and that is because the barcode system is so reliable that we trust that it works.

## Lesson starter

{image file-path="img/topics/error-correction-paint-tin.png" alt="A black paint tin with paint across the name and barcode."}

Explain to your class that you can calculate what the last digit will be on a
12 or 13 digit product code (the number on a bar code).
Have someone find a barcode on a product for you (e.g. some stationery or food
item) and tell you all the digits except the last one (sometimes the digits
have gaps or are before and after the bar code, so they may need to read
carefully to get all digits in the right order; also, some small items have
8-digit codes, and it's best to avoid these for now).

If 13-digit codes are common in your country, use the following guide,
otherwise skip to the 12-digit guide below.

## Lesson activities

### 13-digit instructions

Here’s an example of how to calculate the last digit on a 13-digit barcode.
It's a somewhat odd process of adding and multiplying numbers, but the same
formula will always give you the correct value for the 13th digit, as long as
there isn't an error in the number!

{image file-path="img/topics/barcode-13.jpg"}

The above example barcode is from a product that a student might have selected,
so they would give you these 12 digits (they should keep the 13th digit
secret):

{image file-path="img/topics/barcode-13-step-1.png"}

However, instead of writing it out as above, write it on the board with every
second digit on alternating lines:

{image file-path="img/topics/barcode-13-step-2.png"}

What you are doing is writing the numbers in an odd position at the top and
the even positions in the second row.

Now add up all the numbers in the first row (= 29) and take the number in
the ones column only.
(Later we will introduce a shortcut, where you only need to keep the last
digit after each addition e.g. 9+5 gives 4; for older classes you could
introduce this now through the lesson on modulo arithmetic.
Using only the last digit can seem too easy to them, and can challenge their
thinking!)

{image file-path="img/topics/barcode-13-step-3.png"}

Next add up all the numbers in the second row (to get 24), and again take the
number in the ones column only.

{image file-path="img/topics/barcode-13-step-4.png"}

Multiply the digit from the second sum by three i.e. the 4 in the 24 is
multiplied by 3, but take the ones column answer only (the 2).
With 13-digit barcodes, the units digit from the second row sum is always
multiplied by three.

{image file-path="img/topics/barcode-13-step-5.png"}

Add the result from the first sum to the multiplied answer (in this case,
  the 9 from the 29 to the 2 from the 12):

{image file-path="img/topics/barcode-13-step-6.png"}

Once again, we only need the last digit; in the example it's a 1.
Now ask what you need to add to that digit to get a 0 in the ones column (i.e.
it will add up to either 0 or 10).
In this case, we ask what plus 1 = 10?
The answer, 9, gives us the checksum, which is the 13th number in the product
code.
If the brown total above had ended with a 0, then the checksum would be 0
(since that adds to give a 0 in the ones digit).

{image file-path="img/topics/barcode-13-step-7.png"}

This number should be the final digit on the product code.
Ask the student if you got the right one.
Of course, at this stage there's a small chance you guessed it, but now they
can explore the codes themselves, and they'll soon find out that it always
works if the number is copied correctly.

{panel type="teaching" title="Teaching observations"}

Check that students notice to multiply the second line by 3 and take the last
digit of that number.
If the final number doesn't match the one that was expected, then the product
code had an error in it (which is a nice illustration of error detection at
work - either you wrote it wrong, or the student read it out incorrectly),
or you had an error in the calculations (which wouldn't happen on a computer,
but at least it provides a chance for the class to use their basic maths
facts!).

{panel end}

### 12-digit instructions

Here’s an example of how to calculate the last digit on a 12-digit barcode.
It's a somewhat odd process of adding and multiplying numbers, but the same
formula will always give you the correct value for the 12th digit, as long as
there isn't an error in the number!

{image file-path="img/topics/barcode-12.jpg"}

The above example barcode is from a product that a student might have
selected, so they would give you these 11 digits:

{image file-path="img/topics/barcode-12-step-1.png"}

However, instead of writing as above, write it on the board with every
second digit on alternating lines:

{image file-path="img/topics/barcode-12-step-2.png"}

What you are doing is writing the numbers in an odd position at top and the
even positions in the second row.

Now add up all the numbers in the first row by drawing plus signs between
each digit (in the example this will give 17), and take the number in the
ones column only.
(Later we will introduce a shortcut, where you only need to keep the last
  digit after each addition e.g. 6+4 gives 0; for older classes you could
  introduce this now through the lesson on modulo arithmetic.
Using only the last digit can seem too easy to them, and can challenge
their thinking!)

{image file-path="img/topics/barcode-12-step-3.png"}

Next add up all the numbers in the second row (to get 27), and again take
the number in the ones column only.

{image file-path="img/topics/barcode-12-step-4.png"}

Multiply the digit from the first sum by three i.e. the 7 in the 17 is
multiplied by 3, but take the ones column answer only (the 1 from the 21).
With 12-digit barcodes, the units digit from the first row sum is always
multiplied by three.

{image file-path="img/topics/barcode-12-step-5.png"}

Add the multiplied answer to the second sum (in this case, the 9 from the
29 to the 7 from the 27):

{image file-path="img/topics/barcode-12-step-6.png"}

Once again, we only need the last digit; in the example it's a single
digit already (8).
Now ask what you need to add to that digit to get a 0 in the ones column
(i.e. it will add up to either 0 or 10).
In this case, we ask what plus 8 = 10?
The answer, 2, gives us the checksum, which is the 12th number in
the product code.
If the brown total above had ended with a 0, then the check digit would be
0 (since that adds to give a 0 in the ones digit).

{image file-path="img/topics/barcode-12-step-7.png"}

This number should be the final digit on the product code.
Ask the student if you got the right one.
Of course, at this stage there's a small chance you guessed it, but now
they can explore the codes themselves, and they'll soon find out that it
always works if the number is copied correctly.

{panel type="teaching" title="Teaching observations"}

Check that students notice to multiply the first line by 3 and take the
last digit of that number.
If the final number doesn't match the one that was expected, then the
product code had an error in it (which is a nice illustration of error
detection at work - either you wrote it wrong, or the student read it
out incorrectly), or you had an error in the calculations (which wouldn't
happen on a computer, but at least it provides a chance for the class to use
their basic maths facts!)

{panel end}

## Checking a barcode

In the activity above we worked out the value of the final digit.
When a barcode is scanned, an easy way to check the digits is to add the check
digit to the total, and make sure that the sum ends with a 0
(since that's how the check digit was calculated).

This time you can ask students to check some product codes - ask them to
choose a product with a product code on it (typically a stationery item around
the room will be suitable; many books have 13-digit product codes that
are suitable too).
To simplify how we think about this, we will now express it by adding the
values up backwards.
(This approach will work for both 12- and 13-digit barcodes).

Have students start at the end of the barcode, and write down every second
digit (starting with the last one).
That line is added up (you only need to keep the last digit, but out of
  interest, keep the whole sum).

Then write down every second digit starting at the second to last one.
These digits are summed and multiplied by three, again keeping the whole sum.

Now add the two sums together. If the digits are correct then the total should
sum to a number ending with 0.

Try out different product codes to check that they sum to a number ending in
zero (or if you keep only the last digit from each calculation along the way,
the final value will be zero.)

Now try changing one digit in a valid product code, and see if the total is
non-zero i.e. you can detect the error.
Is there any single digit that you can change in a product code that will
still result in the zero as the total? (This won't be possible).
Are there any two digits that you can change that will give a zero total?
(If one digit change happens to counteract another one, then this can happen,
but it's a rare situation).
If two wrong digits do happen to counteract each other, the error will go
undetected, although the product code will be so incorrect that when the
computer goes to look it up, chances are it's not going to find a product with
that number anyway.

Have students check more product codes. Do they all add up to a multiple of 10?

## Applying what we have just learnt

There needs to be a system around the checksum to make sure that the people
using it know when the checksum worked and when it didn’t.
How do checkout systems let the operator know if there was an error in the
scanning?
(Typically with an error sound).

If the packaging has been damaged or is bent, it may not be possible to read
the bars accurately (it keeps giving errors), so the operator has to type in
the numbers.

What kind of errors can be made if a person types in the numbers?
The main type of answers to look for are:

-   A digit has its value changed.
-   Two adjacent digits are swapped with each other.
-   A digit is inserted in the number.
-   A digit is removed from the number.

## Seeing the Computational Thinking connections

{panel type="ct-algorithm" title="Algorithmic thinking"}

The steps we follow to calculate the barcode checksum is an Algorithm.
We follow this same Algorithm every time we want to create a checksum for a
barcode, and every time we want to check if there is an error in a barcode.
It specifies exactly how we should do this, and students practice algorithmic
thinking as they follow and articulate this algorithm.

#### What to look for:

Can your students write instructions that allow someone else to calculate the
barcode checksum of different products with the same number of digits in their
barcodes (e.g. 12)?
What about instructions that can be used for any different product, regardless
of the number of digits?

{panel end}

{panel type="ct-abstraction" title="Abstraction"}

When a barcode goes through a scanner the scanner reads the black and white
bars on the barcode, whereas when a human looks at a barcode they will read
the digits.
The numbers on the barcode and the black and white bars both represent the
same thing though - a numeric code that identifies a product, and the bars
are an abstracted representation of these numbers.

When we are calculating the checksum we also don’t need to think about what
product it actually represents is, we just want to find out whether or not
the barcode is correct and all we need to do that is the barcode itself.

#### What to look for:

Can your students explain how both of these represent the product?
Can they explain the reason for the different representations?

{panel end}

{panel type="ct-decomposition" title="Decomposition"}

To check the product code, the task of calculating the checksum is broken
down into individual steps: adding one number at a time; doing that for
each subset of digits.
By doing this we are decomposing the problem into smaller subtasks which are
easier to solve than the overall problem of “Is this barcode correct?”.
Each time we solve one of these subtasks we move on to the next and move
closer to a solution.

#### What to look for:

Are students able to independently break the calculation into the two halves,
and then perform the additions on each group of values, and combine them
to get the checksum?
Can they do this for a range of different codes with different errors in them?

{panel end}

{panel type="ct-pattern" title="Generalising and patterns"}

The same method can apply to shorter (e.g. 8-digit) and longer product codes.
If you look at some courier packages you might see much larger bar codes,
and these use similar error detection techniques.
To check each of these bar codes we follow the same algorithmic pattern of
using the numbers on the code (except for the last one) and applying a
mathematical formula to these to get the final digit (or what it should be
if there are no errors!).

#### What to look for:

Can students apply the algorithm (the version starting at the right hand end)
to different length product codes?
Do they appreciate how it still checks the digits in each case?
(You can find different codes by searching for images of barcodes online).

{panel end}

{panel type="ct-evaluation" title="Evaluation"}

This error detecting process isn't perfect.
To evaluate its effectiveness we need to thoroughly test it.
Ask students what the different ways we need to test the algorithm are.
Interestingly it is not enough to just test it with a bunch of different
barcodes with one number in them changed, we need to test a range of
different types of errors as well!
For example what if instead of one number changing two of the numbers are
switched around?
What if two numbers are changed?
Are there any situations where we couldn’t figure out if something had changed?

This is an example of an important technique used when evaluating algorithms
and programs, called edge case testing.

#### What to look for:

Can students demonstrate what kind of errors the checksum is guaranteed
to detect?
Can they give examples of errors that a human might make when typing in a
number that wouldn't be detected?
Can they work out how likely it is that an error will go undetected in each
of these cases?
They can do this by trial and error or by logical reasoning.

{panel end}

{panel type="ct-logic" title="Logic"}

The algorithm is designed to be sensitive to the type of errors that are
most likely to happen.

We can also evaluate the algorithm using logical thinking.

#### What to look for:

Can students explain the logic that was applied in the process of
designing a barcode checksum, and especially the choice to multiply some
of the numbers by 3?

In cases where the checksum is unable to detect and error can students
explain logically why the error cannot be detected?

{panel end}
