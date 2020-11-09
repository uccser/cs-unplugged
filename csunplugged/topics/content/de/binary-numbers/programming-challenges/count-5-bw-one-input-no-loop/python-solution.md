```python
total_number_of_dots = 0
cards = input('Please enter 5 cards (B for black and W for white) as one line, no spaces ')
if cards[0] == 'W':
  total_number_of_dots = total_number_of_dots + 16
if cards[1] == 'W':
  total_number_of_dots = total_number_of_dots + 8
if cards[2] == 'W':
  total_number_of_dots = total_number_of_dots + 4
if cards[3] == 'W':
  total_number_of_dots = total_number_of_dots + 2
if cards[4] == 'W':
  total_number_of_dots = total_number_of_dots + 1
print(total_number_of_dots)
```