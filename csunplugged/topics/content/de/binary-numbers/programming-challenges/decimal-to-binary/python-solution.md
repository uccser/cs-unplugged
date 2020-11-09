```python
original = int(input('Please enter a decimal number: '))
decimal_number = original
bit_value = 1
binary_number = ''
while decimal_number >= bit_value:
  bit_value = bit_value * 2
while bit_value > 1:
  bit_value = bit_value / 2
  if decimal_number >= bit_value:
    binary_number = binary_number + '1'
    decimal_number = decimal_number - bit_value
  else:
    binary_number = binary_number + '0'
print('The binary representation for the number ' + str(original) + ' is ' + str(binary_number))
```