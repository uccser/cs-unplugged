```python
result = 1
base = int(input('Enter an integer for the base: '))
power = int(input('Enter a positive integer for the power: '))
for i in range(0, power):
  result = result * base
print(str(base) + '^' + str(power) + ' = ' + str(result))
```