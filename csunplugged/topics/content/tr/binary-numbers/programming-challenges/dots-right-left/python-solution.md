```python
number_of_cards = int(input('How many cards would you like to display? '))
number_of_dots = 1
binary_cards = ''
for i in range(0, number_of_cards):
  binary_cards = binary_cards + str(number_of_dots) + ', '
  number_of_dots = number_of_dots * 2
print(binary_cards)
```