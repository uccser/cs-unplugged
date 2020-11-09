- Make variables called:
    
    - `original` and set its value to the input number given by the end user.
    - `number` and set its value to `original` (so we can use `original` later)
    - `bit_value` and set its value to 1. Find the smallest bit value which is larger than the `number` by doubling value of `bit_value` while it is smaller than or equal to `number`.
    - `cards` is a string variable and stores the binary cards needed (‘B’ for black cards and ‘W’ for white cards).

- Set the variable `bit_value` to 1 and find the smallest `bit_value` which is larger than `number` by multiplying `bit_value` by 2 while it is smaller than or equal to `number`. You can do this by using a while loop.

- Now divide the `bit_value` by 2 and check if `number` is greater than or equal to `bit_value`. If it is, add ‘W’ to string variable `cards` and subtract `bit_value` from the `number`. If not, add ‘B’ to string variable `cards`. Repeat while `bit_value` is greater than 1. Display the value of `cards` as the output.

- Test your program with some values on the boundaries (for example test it with numbers 255 and 256).