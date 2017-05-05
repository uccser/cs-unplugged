# Counting black and white cards as one input (using a loop)

## Objective

- Explain what you need to consider if you are asking for input from the end user.
- Describe how variables store values and how they are used in this program.
- Identify when to use an if statement to check a set of conditions.
- Identify when to use a loop to repeat a set of instructions.
- Prove how indexing to access a letter at the specified position in a string works.

## Requirement

Write a program which asks the user to enter any number of black and white cards representing bits, all as one input ('B' for black and 'W' for white), and displays the total number of dots as the output. 

Make variables:

- `total number of dots` and set its value to 0. 
- `number of dots` and set its value to 1. 
- `cards` and set its value to the string entered as the input.
  Check each letter of the input string `cards` (use a loop to iterate the number of letters in the input) starting from the last letter.
  If it’s ‘W’ add the corresponding number of dots (1 for the last letter, 2 for the second to last letter and so on) to the `total number of dots`.
  Display the “total number of dots” as the output.
- `index` and set its value to the number of letters in the input.
  Use this variable to access a letter at the `index` position in the string. 

## Input

WBB

## Output

4
When the check mark button is clicked or Enter key is pressed you should see the following output:
