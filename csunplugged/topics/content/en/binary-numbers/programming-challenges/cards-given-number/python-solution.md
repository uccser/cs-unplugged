```python
number_of_dots = int(input('Please enter a number of dots less than or equal to 31: '))
if number_of_dots <= 31:
  if number_of_dots >= 16:
    number_of_dots = number_of_dots - 16
    print('16')
  if number_of_dots >= 8:
    number_of_dots = number_of_dots - 8
    print('8')
  if number_of_dots >= 4:
    number_of_dots = number_of_dots - 4
    print('4')
  if number_of_dots >= 2:
    number_of_dots = number_of_dots - 2
    print('2')
  if number_of_dots >= 1:
    number_of_dots = number_of_dots - 1
    print('1')
else:
  print('Please choose a number less than or equal to 31.')
```
