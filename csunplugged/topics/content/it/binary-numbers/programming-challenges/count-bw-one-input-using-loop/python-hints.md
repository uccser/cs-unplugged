- Make variables called:
    
    - `total_number_of_dots` and set its value to 0.
    - `number_of_dots` and set its value to 1. You will need to multiply number_of_dots by 2 each time you go through the loop
    - `cards` and set its value to the string entered as the input. Check each letter of the input string `cards` (use a loop to iterate the number of letters in the input) starting from the last letter. If it’s ‘W’ add the corresponding number of dots (1 for the last letter, 2 for the second to last letter and so on) to the `total
number of dots`. Display the `total_number_of_dots` as the output.
    - `i` and set its value to the number of letters in the input minus 1. Use this variable to access a letter at the `i` position in the string.

- You can access a letter at the specified position in a string by using brackets, like cards[i]

- In this challenge you need to access all the letters in user’s input and check to see if each of them is equal to B (black) or W (white).

- You can find how many letters a string has by using `len(cards)`

- In this challenge you need to check if each letter of the input is equal to ‘W’ or `B’ using and if statement