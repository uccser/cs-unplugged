- You can find `make a new variable` under the `data` script to create a new variable.
  Make sure your variable names are meaningful for someone else to read.
  In the above example, the variables are called `total number of dots`, the number that user enters as the input, `bit value` which is bit values 1,2,4,8,... and `bits` which is the number of bits needed to store the number. 
- Use the `SET` block to set the value of your new variables.
  Set the variable `bit value` to ‘1’ and double it (Use the multiply operation under `Operators` script to multiply the `bit value` by 2) until it is bigger than the `total number of dots`.
  Every time that you double the `bit value` you need to add a new bit for storing the number.
  You can do this by using the `CHANGE` block to increase the value of variable `bits` value by 1.
  Use `REPEAT/UNTIL` block to repeat these steps until condition is true.
  In this challenge you need to repeat the blocks until “total number of dots” is greater than the `bit value`.
  Stop the loop when you find the `bit value` is larger than the `total number of dots`.
- Display the value of your variable `bits` on the screen by replacing `Hello` in your `SAY` block with variable `bits`.
  Use the `JOIN` blocks under `Operators` script to combine two or more strings.
  You can replace `hello` or `world` in your `JOIN` block with your variable which you want to display it’s value combined with some strings inside the `SAY` block.
  You will need to use more than one `JOIN` block inside each other if you need to display the value of your variable in the middle of a set of strings. 
- Test your program with some values on the boundaries (for example number 31 would need 5 bits and 32 needs 6 bits). 
