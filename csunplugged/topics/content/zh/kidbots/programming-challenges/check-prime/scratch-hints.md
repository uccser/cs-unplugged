We have provided 2 different algorithms to check if “number” is a prime or not:

Solution 1:

1. Create a variable called “divisor” and set its value to 2.
2. If “number” < or = 1, “number” is not a prime.
3. Else, If “number” mod “divisor” is 0, “number” is not a prime. Stop the program.
4. Increase the value of “divisor” by 1.
5. Repeat steps 3 and 4 until “divisor” = “number”.
6. “number” is a prime.
7. Stop the program using `scratch:stop [all v]` block under “Control” scripts.

Solution 2:

1. Create a variable called “divisor” and set its value to 2. Create a boolean variable called “is prime” and set its value to “true”.
2. If “number” < or = 1, “number” is not a prime.
3. Else, If “number” mod “divisor” is 0, “number” is not a prime. Set “is prime” to “false”.
4. Increase “divisor” by 1.
5. Repeat steps 3 and 4 until “divisor” = “number” or “is prime” is “false”.
6. If “is prime” is “true”, “number” is a prime.