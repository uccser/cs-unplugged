```python
divisor = 2
number = int(input("Enter a number to check if it's a prime number: "))
if number <= 1:
  print(str(number) + ' is not a prime number.')
else:
  is_prime = True
  while is_prime and divisor < number:
    if number % divisor == 0:
      print(str(number) + ' is not a prime number.')
      is_prime = False
    divisor = divisor + 1
  if is_prime:
    print(str(number) + ' is a prime number.')
```