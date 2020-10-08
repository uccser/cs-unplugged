```python
original_time = int(input('Enter a time: '))
hours_to_add = int(input('Enter the number of hours to add: '))
new_time = (original_time + hours_to_add) % 24
if new_time == 0:
  print('The new time is 00:00.')
else:
  print('The new time is ' + str(new_time) + ':00.')
```
