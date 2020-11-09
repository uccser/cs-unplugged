```python
original = int(input('Please enter a decimal number: '))
decimal_number = original
remainder = 0
binary_number = ''
while decimal_number > 1:
  remainder = decimal_number % 2
  decimal_number = decimal_number // 2
  binary_number = str(remainder) + binary_number
binary_number = str(decimal_number) + binary_number
print('The binary representation for the number ' + str(original) + ' is ' + str(binary_number))
```