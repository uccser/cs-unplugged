- Make variables called:
    
    - `decimal_number` and set its value to the input number given by the end user.
    - `bit_value` and set its value to 1. Find the smallest bit value which is larger than `decimal_number` by doubling value of `bit_value` until it is bigger than the `decimal_number` (by using a while loop while `bit_value` is less than or equal to `decimal_number`).

- Set the variable `bit_value` to 1 and find the smallest `bit_value` which is larger than `decimal_number` by multiplying `bit_value` by 2 until it is larger than `decimal number`. You can do this by using a while loop.

- Now divide the `bit_value` by 2 and check if `decimal_number` is greater than or equal to `bit_value`. If it is, print "high" for a high note and subtract `bit_value` from `decimal_number`. If not, print "low" for a low note. Repeat until `bit_value` is equal to 1 (by using a while loop while `bit_value` is greater than 1)