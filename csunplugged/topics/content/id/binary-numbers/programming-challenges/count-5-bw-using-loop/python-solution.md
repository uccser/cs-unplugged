```python
number_of_dots = 16
total_number_of_dots = 0
for i in range(0, 5):
  card = input('What is your card (B for black, W for white)? ')
  if card == 'W':
    total_number_of_dots = total_number_of_dots + number_of_dots
  number_of_dots = int(number_of_dots / 2)
print(total_number_of_dots)
```