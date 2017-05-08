# Converting decimal to binary

## Objective

- Explain what you need to consider if you are asking for input from the end user.
- Describe how variables store values and how they are used in this program.
- Identify when to use an if statement to check a set of conditions.
- Identify when to use a loop to repeat a set of instructions.

## Requirement

Write a program which asks the user to enter any decimal number as the input and displays the binary cards representing that number using '1' for dots showing and '0' for not showing as the output (this converts the decimal number to binary).

Make variables:

- `decimal number` and set its value to the input number given by the end user
- `bit value` and set its value to ‘1’.
  Find the smallest bit value which is larger than the `number` by doubling value of `bit value` until it is bigger than the `number`.
- `binary number` is a string variable and stores the binary cards needed (‘1’ for dots showing and ‘0’ for not showing).

Now divide the `bit value` by 2 and check if `number` is greater than or equal to `bit value`.
If it is, add ‘1’ to string variable `cards` and subtract `bit value` from the `number`.
If not, add ‘0’ to string variable `cards`.
Repeat until `bit value` is equal to 1.
Display the value of `cards` as the output.

## Input

31

## Output
