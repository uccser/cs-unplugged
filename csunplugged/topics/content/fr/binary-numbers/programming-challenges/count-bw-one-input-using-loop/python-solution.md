```python
total_number_of_dots = 0
cards = input('Please enter cards (B for black and W for white) as one line, no spaces ')
number_of_dots = 1
i = len(cards) - 1
while i >= 0:
  if cards[i] == 'W':
    total_number_of_dots = total_number_of_dots + number_of_dots
  number_of_dots = number_of_dots * 2
  i = i - 1
print(total_number_of_dots)
```