```python
original_time = int(input('Enter a time: '))
hours_to_add = int(input('Enter the number of hours to add: '))
new_time = original_time + hours_to_add
while new_time > 12:
  new_time = new_time - 12
print('The new time is ' + str(new_time) + " o'clock.")
```