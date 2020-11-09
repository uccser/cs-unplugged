We have provided an algorithm to check if `number` is a prime or not:

1. Create a variable called `divisor` and set its value to 2. Create a boolean variable called `is_prime` and set its value to `True`.
2. If `number` <= 1, `number` is not a prime.
3. Else, if `number` mod `divisor` is 0, `number` is not a prime. Set is_prime to `False`.
4. Increase `divisor` by 1.
5. Repeat steps 3 and 4 while `divisor` < `number` and `is_prime` is `True`.
6. If `is_prime` is `True`, `number` is a prime.