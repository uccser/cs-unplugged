-   This approach is based on observing that the right-hand bit value is
    easily identified (the remainder of the decimal number when divided by 2
    will be 1 i.e. it's an odd number).
    The number can then be divided by 2, which moves all the digits one place
    to the right, and so the next bit becomes the right-hand bit.
-   Make variables called `original`, which is number that user enters as the input,
    `decimal_number`, which is set to original (so we can use original later),
    `binary_number`, which is type string and it will be used to store 0’s and 1’s
    that represent the binary number as the output, and `remainder`, which stores
    the remainders of values for `decimal_number` divided by 2.
-   Divide `decimal_number` by 2 and round down the result to the nearest integer
    by using the "//" operator
    For example `11 // 2` will give you 5
-   Store the remainder in variable `remainder` (use the modulo '%' operator to
    calculate the remainder. For example, `5 % 2` is 1.)
    Add `remainder` values using the addition operator to the front of the
    `binary_number` variable. Remember that when combining strings and integers,
    you need to cast the integers to strings. For example, `'hello' + 5`
    is not valid but `'hello' + str(5)` will become 'hello5'.
-   Repeat these blocks while `decimal_number` is greater than 1 (use a while loop)
-   Add `decimal_number` (which is now 1) to `binary_number` and display it
    as the output.
