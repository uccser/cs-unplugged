**Solution #1:**

```python
factors = []
number = int(input("What's the number you want to find factors of? "))
divisor = 1
while divisor <= number:
  if number % divisor == 0:
    factors = factors + [divisor]
  divisor = divisor + 1
print(factors)
```

**Solution #2:**

```python
factors = []
number = int(input("What's the number you want to find factors of? "))
divisor = number
while divisor > 0:
  if number % divisor == 0:
    factors = factors + [divisor]
  divisor = divisor - 1
print(factors)
```