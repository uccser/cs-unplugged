```python
decimal_number = int(input('Please enter a decimal number between 0 and 31: '))
bit_value = 32
while bit_value > 1:
  bit_value = bit_value / 2
  if decimal_number >= bit_value:
    print('high')
    decimal_number = decimal_number - bit_value
  else:
    print('low')
```