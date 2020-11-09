```python
total_number_of_dots = 0
card = input('What is your first card (B for black, W for white)? ')
if card == 'W':
  total_number_of_dots = total_number_of_dots + 16
card = input('What is your second card (B for black, W for white)? ')
if card == 'W':
  total_number_of_dots = total_number_of_dots + 8
card = input('What is your third card (B for black, W for white)? ')
if card == 'W':
  total_number_of_dots = total_number_of_dots + 4
card = input('What is your fourth card (B for black, W for white)? ')
if card == 'W':
  total_number_of_dots = total_number_of_dots + 2
card = input('What is your fifth card (B for black, W for white)? ')
if card == 'W':
  total_number_of_dots = total_number_of_dots + 1
print(total_number_of_dots)
```