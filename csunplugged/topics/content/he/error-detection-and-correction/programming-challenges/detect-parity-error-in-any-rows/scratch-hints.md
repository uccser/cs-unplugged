- Make a variable called “number of rows” and set its value to the input entered by the end user. Make a variable called “black cards total” and set its value to 0. Also make a string variable called “row” and set its value to the input entered by the end user. Check each letter of the string and if it’s ‘B’ add 1 to the “black cards total”. If the value of the “black cards total” is even (after checking every card in the row), display a message that the parity row is ok. If the value of the “black cards total” is odd, display a message that the row has a parity error. Repeat this “number of rows” times (for each row).

- You can access a letter at the specified position in a string by using the `scratch:letter (1) of [world]` block under “Operators”. For example: `scratch:letter (1) of [world] //w`

- In this challenge you need to access all the letters in user’s input (each row of the parity trick) and check to see how many of them are equal to B (black). Store the total number of black squares in a variable called “black cards total”.

- You can find how many letters a string has by using the `scratch:length of [world]` block unders “Operators”.

- To find out if a number is even or odd, use the `scratch:() mod ()` block (under "Operators") to find the remainder after dividing that number by two. If the remainder is zero the number is even. For example: `scratch:(37) mod (10) //7`