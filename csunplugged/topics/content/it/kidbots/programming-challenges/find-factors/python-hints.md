We have provided 2 different algorithms to code this program;

Algorithms to find the factors of `number`:

Solution 1:

1. Create a variable called `divisor` and set its value to 1.
2. If `number` mod `divisor` is 0, `divisor` is one of the factors.
3. Increase the value of `divisor` by 1.
4. Repeat steps 2 and 3 while `divisor` <= `number`.

Solution 2:

1. Create a variable called `divisor` and set its value to the `number`.
2. If `number` mod `divisor` is 0, `divisor` is one of the factors.
3. Decrease the value of `divisor` by 1.
4. Repeat steps 2 and 3 while `divisor` > 0.