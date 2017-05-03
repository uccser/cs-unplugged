# Cards to display for a given number (all in one line)

## Objective

- Explain what you need to consider if you are asking for input from the end user.
- Describe how variables store values and how they are used in this program.
- Identify when to use an if statement to check a set of conditions.

## Requirement

Write a program which asks the user to enter a number of dots less than or equal to 31 as the input and displays which of the 5 cards should be showing as the output all in one line.

Make a variable called `number of dots` and set its value to the input entered by the end user.
Make another variable called `cards`.
Below is the algorithm to help you program this;

If “number of dots” less than or equal to 31
	If “number of dots” greater than or equal to 16
		Subtract 16 from “number of dots” and add “16, ” to string variable “cards”
	If “number of dots” greater than or equal to 8
		Subtract 8 from “number of dots” and add “8, ” to string variable “cards”
	If “number of dots” greater than or equal to 4
		Subtract 4 from “number of dots” and add “4, ” to string variable “cards”
	If “number of dots” greater than or equal to 2
		Subtract 2 from “number of dots” and add “2, ” to string variable “cards”
	If “number of dots” greater than or equal to 1
		Subtract 1 from “number of dots” and add “1, ” to string variable “cards”
	Display the value of “cards”
else
	Ask the end user to enter a number less than or equal to “31”

## Input
 15 

## Output

When the check mark button is clicked or Enter key is pressed you should see the following output:

## Extra challenge

Now try removing the last ‘,’ from the end of your output.

## Output
