```python
def check_prime(number):
  index = 2
  is_prime = True
  if number > 1:
    while is_prime and index < number:
      if number % index == 0:
        is_prime = False
      index = index + 1
    if is_prime:
      return True
  return False

prime_factors = []
number = int(input("What's the number you want to find prime factors of? "))
divisor = number
while divisor > 0:
  if number % divisor == 0:
    if check_prime(divisor):
      prime_factors = [divisor] + prime_factors
  divisor = divisor - 1
print(prime_factors)
```