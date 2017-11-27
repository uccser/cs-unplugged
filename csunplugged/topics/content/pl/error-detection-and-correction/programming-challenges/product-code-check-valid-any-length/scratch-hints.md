- To add up the digits you need to start from the last digit, multiply the last digit by 1, second to last by 3 and so on. It then checks if the product code is valid (total number is a multiple of 10). Starting at the right-hand digit will make the formula work for a wide variety of product codes.

- You can find the number digits in a number by using the `scratch:length of ()` block unders “Operators”. For example: `scratch:length of (2938339392383) //13`

- You can access a letter (or a digit) at a specified position in a string (or number) by using the `scratch:letter () of []` block under “Operators”. For example: `scratch:letter (4) of [18392819202910] //9`

- To access the last digit of the product code, make a variable called “index” and set it to the length of the product code. Now the last digit of the product code can be accessed by using the `scratch:length of ()` block with the index variable and the product code.