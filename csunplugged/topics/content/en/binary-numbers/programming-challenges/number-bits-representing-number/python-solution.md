```python
total_number_of_dots = int(input('Please enter the number of dots: '))
bits = 0
bit_value = 1
while total_number_of_dots >= bit_value:
  bit_value = bit_value * 2
  bits = bits + 1
print(str(bits) + ' bits')
```
