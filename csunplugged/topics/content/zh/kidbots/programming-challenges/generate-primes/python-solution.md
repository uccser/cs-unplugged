```python
prime_numbers = []
number = 2
upper_range = int(input("I'll generate the prime numbers up to this number: "))
for i in range(1, upper_range):
  is_prime = True
  index = 2
  while index < number and is_prime:
    if number % index == 0:
      is_prime = False
    index = index + 1
  if is_prime:
    prime_numbers = prime_numbers + [number]
  number = number + 1
print(prime_numbers)
```