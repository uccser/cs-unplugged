# Product code check digits

## Key questions

How many people do you know check their dockets at the supermarket or in a shop to be sure that what they purchased matches the docket?

## Mögliche Antworten wären beispielsweise:

- Typically it’s not many, and that is because the barcode system is so reliable that we trust that it works.

## Lesson starter

{panel type="video"}

# Unterrichtsbeispiel ansehen

A demonstration of lesson two ("Product Code Check Digits") being taught is available here:

{video url="https://vimeo.com/437724764"}

{panel end}

{panel type="general"}

# Erforderliche Vorkenntnisse

It is helpful, but not essential, for students to have done the [lesson on the Modulo operator]('topics:lesson' 'unplugged-programming' 'numeracy-unit-plan' 'modulo') before doing this lesson.

{panel end}

{image file-path="img/topics/error-correction-paint-tin.png" alt="A black paint tin with paint across the name and barcode." alignment="right"}

Explain to your class that you can calculate what the last digit will be on a 12 or 13 digit product code (the number on a bar code). Have someone find a barcode on a product for you (e.g. some stationery or food item) and tell you all the digits except the last one (sometimes the digits have gaps or are before and after the bar code, so they may need to read carefully to get all digits in the right order; also, some small items have 8-digit codes, and it's best to avoid these for now).

If 13-digit codes are common in your country, use the following guide, otherwise skip to the 12-digit guide below.

## Lektionsaktivitäten

### 13-digit instructions

Here’s an example of how to calculate the last digit on a 13-digit barcode. It's a somewhat odd process of adding and multiplying numbers, but the same formula will always give you the correct value for the 13th digit, as long as there isn't an error in the number!

{image file-path="img/topics/barcode-13.jpg" alt="A barcode with the digits 9 400547 009879."}

The above example barcode is from a product that a student might have selected, so they would give you these 12 digits (they should keep the 13th digit secret):

{image file-path="img/topics/barcode-13-step-1.png" alt="63050942483."}

However, instead of writing it out as above, write it on the board with every second digit on alternating lines:

{image file-path="img/topics/barcode-13-step-2.png" alt="Top line has the digits 600443 and the bottom line has 35928."}

What you are doing is writing the numbers in an odd position at the top and the even positions in the second row.

Now add up all the numbers in the first row (= 29) and take the number in the ones column only. (Later we will introduce a shortcut, where you only need to keep the last digit after each addition e.g. 9+5 gives 4; for older classes you could introduce this now through the lesson on modulo arithmetic. Using only the last digit can seem too easy to them, and can challenge their thinking!)

{image file-path="img/topics/barcode-13-step-3.png" alt="6+0+0+4+4+3=17."}

Next add up all the numbers in the second row (to get 24), and again take the number in the ones column only.

{image file-path="img/topics/barcode-13-step-4.png" alt="4+0+4+0+9+7=24."}

Multiply the digit from the second sum by three i.e. the 4 in the 24 is multiplied by 3, but take the ones column answer only (the 2). With 13-digit barcodes, the units digit from the second row sum is always multiplied by three.

{image file-path="img/topics/barcode-13-step-5.png" alt="3x4=12."}

Add the result from the first sum to the multiplied answer (in this case, the 9 from the 29 to the 2 from the 12):

{image file-path="img/topics/barcode-13-step-6.png" alt="9+2=11."}

Once again, we only need the last digit; in the example it's a 1. Now ask what you need to add to that digit to get a 0 in the ones column (i.e. it will add up to either 0 or 10). In this case, we ask what plus 1 = 10? The answer, 9, gives us the checksum, which is the 13th number in the product code. If the brown total above had ended with a 0, then the checksum would be 0 (since that adds to give a 0 in the ones digit).

{image file-path="img/topics/barcode-13-step-7.png" alt="The checksum is 9."}

This number should be the final digit on the product code. Ask the student if you got the right one. Of course, at this stage there's a small chance you guessed it, but now they can explore the codes themselves, and they'll soon find out that it always works if the number is copied correctly.

{panel type="teaching"}

# Teaching observations

Check that students notice to multiply the second line by 3 and take the last digit of that number. If the final number doesn't match the one that was expected, then the product code had an error in it (which is a nice illustration of error detection at work - either you wrote it wrong, or the student read it out incorrectly), or you had an error in the calculations (which wouldn't happen on a computer, but at least it provides a chance for the class to use their basic maths facts!).

{panel end}

### 12-digit instructions

Here’s an example of how to calculate the last digit on a 12-digit barcode. It's a somewhat odd process of adding and multiplying numbers, but the same formula will always give you the correct value for the 12th digit, as long as there isn't an error in the number!

{image file-path="img/topics/barcode-12.jpg" alt="A barcode with the digits 6 30509 42483 2."}

The above example barcode is from a product that a student might have selected, so they would give you these 11 digits:

{image file-path="img/topics/barcode-12-step-1.png" alt="940054700987."}

However, instead of writing as above, write it on the board with every second digit on alternating lines:

{image file-path="img/topics/barcode-12-step-2.png" alt="Top line has the digits 600443 and the bottom line has 35928."}

What you are doing is writing the numbers in an odd position at top and the even positions in the second row.

Now add up all the numbers in the first row by drawing plus signs between each digit (in the example this will give 17), and take the number in the ones column only. (Later we will introduce a shortcut, where you only need to keep the last digit after each addition e.g. 6+4 gives 0; for older classes you could introduce this now through the lesson on modulo arithmetic. Using only the last digit can seem too easy to them, and can challenge their thinking!)

{image file-path="img/topics/barcode-12-step-3.png" alt="6+0+0+4+4+3=17."}

Next add up all the numbers in the second row (to get 27), and again take the number in the ones column only.

{image file-path="img/topics/barcode-12-step-4.png" alt="3+5+9+2+8=27."}

Multiply the digit from the first sum by three i.e. the 7 in the 17 is multiplied by 3, but take the ones column answer only (the 1 from the 21). With 12-digit barcodes, the units digit from the first row sum is always multiplied by three.

{image file-path="img/topics/barcode-12-step-5.png" alt="3x7=21."}

Add the multiplied answer to the second sum (in this case, the 1 from the 21 to the 7 from the 27):

{image file-path="img/topics/barcode-12-step-6.png" alt="9+2=11."}

Once again, we only need the last digit; in the example it's a single digit already (8). Now ask what you need to add to that digit to get a 0 in the ones column (i.e. it will add up to either 0 or 10). In this case, we ask what plus 8 = 10? The answer, 2, gives us the checksum, which is the 12th number in the product code. If the brown total above had ended with a 0, then the check digit would be 0 (since that adds to give a 0 in the ones digit).

{image file-path="img/topics/barcode-12-step-7.png" alt="The checksum is 2."}

This number should be the final digit on the product code. Ask the student if you got the right one. Of course, at this stage there's a small chance you guessed it, but now they can explore the codes themselves, and they'll soon find out that it always works if the number is copied correctly.

{panel type="teaching"}

# Teaching observations

Check that students notice to multiply the first line by 3 and take the last digit of that number. If the final number doesn't match the one that was expected, then the product code had an error in it (which is a nice illustration of error detection at work - either you wrote it wrong, or the student read it out incorrectly), or you had an error in the calculations (which wouldn't happen on a computer, but at least it provides a chance for the class to use their basic maths facts!)

{panel end}

## Checking a barcode

In the activity above we worked out the value of the final digit. When a barcode is scanned, an easy way to check the digits is to add the check digit to the total, and make sure that the sum ends with a 0 (since that's how the check digit was calculated).

This time you can ask students to check some product codes - ask them to choose a product with a product code on it (typically a stationery item around the room will be suitable; many books have 13-digit product codes that are suitable too). To simplify how we think about this, we will now express it by adding the values up backwards. (This approach will work for both 12- and 13-digit barcodes).

Have students start at the end of the barcode, and write down every second digit (starting with the last one). That line is added up (you only need to keep the last digit, but out of interest, keep the whole sum).

Then write down every second digit starting at the second to last one. These digits are summed and multiplied by three, again keeping the whole sum.

Now add the two sums together. If the digits are correct then the total should sum to a number ending with 0.

Try out different product codes to check that they sum to a number ending in zero (or if you keep only the last digit from each calculation along the way, the final value will be zero.)

Now try changing one digit in a valid product code, and see if the total is non-zero i.e. you can detect the error. Is there any single digit that you can change in a product code that will still result in the zero as the total? (This won't be possible). Are there any two digits that you can change that will give a zero total? (If one digit change happens to counteract another one, then this can happen, but it's a rare situation). If two wrong digits do happen to counteract each other, the error will go undetected, although the product code will be so incorrect that when the computer goes to look it up, chances are it's not going to find a product with that number anyway.

Have students check more product codes. Do they all add up to a multiple of 10?

## Applying what we have just learnt

There needs to be a system around the checksum to make sure that the people using it know when the checksum worked and when it didn’t. How do checkout systems let the operator know if there was an error in the scanning? (Typically with an error sound).

If the packaging has been damaged or is bent, it may not be possible to read the bars accurately (it keeps giving errors), so the operator has to type in the numbers.

What kind of errors can be made if a person types in the numbers? The main type of answers to look for are:

- A digit has its value changed.
- Two adjacent digits are swapped with each other.
- A digit is inserted in the number.
- A digit is removed from the number.