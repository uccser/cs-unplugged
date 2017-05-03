# Number of bits representing a number


## Objective

- Explain what you need to consider if you are asking for input from the end user.
- Describe how variables store values and how they are used in this program.
- Identify when to use a loop to repeat a set of instructions.

## Requirement

Write a program which asks the user to enter a number of dots (i.e. decimal value) as the input and displays how many bits will be needed to represent that number as the output.
For example, the number 15 can be represented in 4 bits, but 16 requires 5 bits.

Make variables:
- `total number of dots` and set its value to the number entered by the end user
- `bit value` and set its value to ‘1’.
  Double its value until it is bigger than the `total number of dots`. 
- `bits` and set its value to 0.
  Every time that you double the `bit value` you need to add a new bit for storing the number (increase the value of `bits` by 1). 

Use `REPEAT/UNTIL` block to repeat the blocks until `total number of dots` is greater than the `bit value`.
Stop the loop when you find the `bit value` which is larger than the `total number of dots`.
Display the value of `bits` as the output.


## Input

5 

## Output

3 bits
