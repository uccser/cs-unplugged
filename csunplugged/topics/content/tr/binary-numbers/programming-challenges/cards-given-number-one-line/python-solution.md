```python
number_of_dots = int(input('Please enter a number of dots less than or equal to 31: '))
cards = ''
if number_of_dots <= 31:
  if number_of_dots >= 16:
    number_of_dots = number_of_dots - 16
    cards = cards + '16, '
  if number_of_dots >= 8:
    number_of_dots = number_of_dots - 8
    cards = cards + '8, '
  if number_of_dots >= 4:
    number_of_dots = number_of_dots - 4
    cards = cards + '4, '
  if number_of_dots >= 2:
    number_of_dots = number_of_dots - 2
    cards = cards + '2, '
  if number_of_dots >= 1:
    number_of_dots = number_of_dots - 1
    cards = cards + '1, '
  print(cards)
else:
  print('Please choose a number less than or equal to 31.')
```