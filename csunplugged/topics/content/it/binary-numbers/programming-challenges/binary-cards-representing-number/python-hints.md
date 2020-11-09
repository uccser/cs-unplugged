- Make variables called:
    
    - `original` and set its value to the input number given by the end user.
    - `number` and set its value to original (this is so that you can display the original number later)
    - `bit_value` and set its value to 32.
    - `cards` is a variable and stores the binary cards needed (‘B’ for black cards and ‘W’ for white cards).

- Now divide `bit_value` by 2 and check if `number` is greater than or equal to `bit_value`. If it is, add ‘W’ to string `cards` and subtract `bit_value` from `number`. If not, add ‘B’ to string variable `cards`. Repeat until `bit_value` is equal to 1, using a while loop while `bit_value` > 1 Display the value of `cards` as the output.

- Test your program with some values on the boundaries (for example test it with numbers 0 and 31).