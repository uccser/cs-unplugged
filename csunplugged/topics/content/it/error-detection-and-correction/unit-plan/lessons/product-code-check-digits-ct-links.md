{panel type="ct-algorithm"}

# Pensiero algoritmico

The steps we follow to calculate the barcode checksum is an Algorithm. We follow this same Algorithm every time we want to create a checksum for a barcode, and every time we want to check if there is an error in a barcode. It specifies exactly how we should do this, and students practice algorithmic thinking as they follow and articulate this algorithm.

#### Examples of what you could look for:

Can your students write instructions that allow someone else to calculate the barcode checksum of different products with the same number of digits in their barcodes (e.g. 12)? What about instructions that can be used for any different product, regardless of the number of digits?

{panel end}

{panel type="ct-abstraction"}

# Astrazione

When a barcode goes through a scanner the scanner reads the black and white bars on the barcode, whereas when a human looks at a barcode they will read the digits. The numbers on the barcode and the black and white bars both represent the same thing though - a numeric code that identifies a product, and the bars are an abstracted representation of these numbers.

When we are calculating the checksum we also don’t need to think about what product it actually represents is, we just want to find out whether or not the barcode is correct and all we need to do that is the barcode itself.

#### Examples of what you could look for:

Can your students explain how both of these represent the product? Can they explain the reason for the different representations?

{panel end}

{panel type="ct-decomposition"}

# Scomposizione

To check the product code, the task of calculating the checksum is broken down into individual steps: adding one number at a time; doing that for each subset of digits. By doing this we are decomposing the problem into smaller subtasks which are easier to solve than the overall problem of “Is this barcode correct?”. Each time we solve one of these subtasks we move on to the next and move closer to a solution.

#### Examples of what you could look for:

Are students able to independently break the calculation into the two halves, and then perform the additions on each group of values, and combine them to get the checksum? Can they do this for a range of different codes with different errors in them?

{panel end}

{panel type="ct-pattern"}

# Generalizzazione e riconoscimento di schemi (pattern)

The same method can apply to shorter (e.g. 8-digit) and longer product codes. If you look at some courier packages you might see much larger bar codes, and these use similar error detection techniques. To check each of these bar codes we follow the same algorithmic pattern of using the numbers on the code (except for the last one) and applying a mathematical formula to these to get the final digit (or what it should be if there are no errors!).

#### Examples of what you could look for:

Can students apply the algorithm (the version starting at the right hand end) to different length product codes? Do they appreciate how it still checks the digits in each case? (You can find different codes by searching for images of barcodes online).

{panel end}

{panel type="ct-evaluation"}

# Valutazione

This error detecting process isn't perfect. To evaluate its effectiveness we need to thoroughly test it. Ask students what the different ways we need to test the algorithm are. Interestingly it is not enough to just test it with a bunch of different barcodes with one number in them changed, we need to test a range of different types of errors as well! For example what if instead of one number changing two of the numbers are switched around? What if two numbers are changed? Are there any situations where we couldn’t figure out if something had changed?

This is an example of an important technique used when evaluating algorithms and programs, called edge case testing.

#### Examples of what you could look for:

Can students demonstrate what kind of errors the checksum is guaranteed to detect? Can they give examples of errors that a human might make when typing in a number that wouldn't be detected? Can they work out how likely it is that an error will go undetected in each of these cases? They can do this by trial and error or by logical reasoning.

{panel end}

{panel type="ct-logic"}

# Logica

The algorithm is designed to be sensitive to the type of errors that are most likely to happen.

We can also evaluate the algorithm using logical thinking.

#### Examples of what you could look for:

Can students explain the logic that was applied in the process of designing a barcode checksum, and especially the choice to multiply some of the numbers by 3?

In cases where the checksum is unable to detect and error can students explain logically why the error cannot be detected?

{panel end}