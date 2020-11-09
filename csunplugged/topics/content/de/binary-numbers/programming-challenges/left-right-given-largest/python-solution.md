```python
number_of_dots = int(input('Enter the largest card number: '))
binary_cards = ''
while number_of_dots >= 1:
  binary_cards = binary_cards + str(number_of_dots) + ', '
  number_of_dots = number_of_dots / 2
print(binary_cards)
```