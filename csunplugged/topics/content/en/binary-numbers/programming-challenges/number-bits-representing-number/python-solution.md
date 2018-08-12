```python
total_number_of_dots = input('Please enter the number of dots: ')
bits = 0
bit_value = 1
while total_number_of_dots >= bit_value:
  bit_value = bit_value * 2
  bits = bits + 1
print('You will need ' + str(bits) + ' bits to store number ' + str(total_number_of_dots))
```
