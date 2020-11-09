- Make a variable called `number_of_dots` and set its value to the input entered by the end user.
- Make another variable called `cards`. Below is the algorithm to help you program this:
    
        If `number_of_dots` less than or equal to 31
        If `number_of_dots` greater than or equal to 16
          Subtract 16 from `number_of_dots` and add `16, ` to cards
        If `number_of_dots` greater than or equal to 8
          Subtract 8 from `number_of_dots` and add `8, ` to cards
        If `number_of_dots` greater than or equal to 4
          Subtract 4 from `number_of_dots` and add `4, ` to cards
        If `number_of_dots` greater than or equal to 2
          Subtract 2 from `number_of_dots` and add `2, ` to cards
        If `number_of_dots` greater than or equal to 1
          Subtract 1 from `number_of_dots` and add `1, ` to cards
        else
        Ask the end user to enter a number less than or equal to `31`
        

- The if statement checks if the condition is true and then runs the lines inside of the if statement. In this challenge you need to use if statements to check if the `number_of_dots` is greater than or equal to 16 (use '>=') If it is, add '16, ' to the variable cards using an addition operator and subtract 16 from your number and do the same with the rest of the cards.

- You can also use an else statement to do something if the if statement is false

- In the extra challenge you need to ask the user to enter a number less than or equal to 31 if the input which was entered was greater than 31.

- Test your program with some values on the boundaries (i.e. 32, 31, 16, 8, 4, 2, 1)