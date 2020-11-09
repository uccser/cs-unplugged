```python
total_number_of_dots = 0
number_of_dots = 16
cards = input('Please enter 5 cards (B for black and W for white) as one line, no spaces ')
for i in range(0, 5):
  if cards[i] == 'W':
    total_number_of_dots = total_number_of_dots + number_of_dots
  number_of_dots = int(number_of_dots / 2)
print(total_number_of_dots)
```