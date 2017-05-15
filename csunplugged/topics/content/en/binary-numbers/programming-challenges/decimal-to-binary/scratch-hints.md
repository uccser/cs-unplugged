- You can find `make a new variable` under the `data` script to create a new variable.
  Make sure your variable names are meaningful for someone else to read.
  In the above example, the variables are called "decimal number" which is the number that user enters as the input, `bit value` which is bit values 1,2,4,8,... and variable `binary number` which is a type string and it will be used to store the binary cards to represent the number. 
- Use the SET block to set the value of your new variables.
  Set the variable `bit value` to 1 and find the smallest `bit value` which is larger than `decimal number` by multiplying `bit value` by 2 (Use the `MULTIPLY` block under `Operators` script to multiply the `bit value` by 2) until it is larger than `decimal number`.
  You can do this by using a `REPEAT/UNTIL` loop.
- Now divide `bit value` by 2 (Use `DIVIDE` block under `Operators` script) and repeat until `bit value` is equal to 1.
  Every time you divide `bit value` by 2, check if the new `bit value` is greater than or equal to `decimal number` (use `GREATER THAN`, `EQUAL` and `OR` blocks under `Operators` script) and if so add ‘1’ to variable `binary numbers` and set `decimal number` to `decimal number` minus `bit value`. Otherwise add ‘0’ to variable `cards`.
- The `IF` block checks if the condition is true and then runs the blocks inside of the `IF` block.
  In this challenge use the `IF/ELSE` block as you also need to run a set of blocks if the condition is not true.
- Display the value of variable `binary number` on the screen by replacing `Hello` in your `SAY` block with variable `binary numbers`.
  Use the JOIN block under `Operators` script to combine two or more strings.
  If you want to display the value of your variable combined with a set of strings, replace `hello` or `world` in your `JOIN` block with your variable and type in the rest of your output inside the `SAY` block.
  You will need to use more than one `JOIN` block inside each other if you need to display the value of your variable in the middle of a set of strings. 
- Make sure all your blocks are `snapped` together in a line like a jigsaw puzzle.
- Whenever you click the green flag, your script will start. To stop, click the stop button.
- Test your program with some values on the boundaries (for example test it with numbers 7 and 8). 
