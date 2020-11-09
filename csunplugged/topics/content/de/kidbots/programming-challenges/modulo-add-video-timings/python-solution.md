```python
hours1 = int(input('Enter the number of hours for the first clip: '))
mins1 = int(input('Enter the number of minutes for the first clip: '))
secs1 = int(input('Enter the number of seconds for the first clip: '))
hours2 = int(input('Enter the number of hours for the second clip: '))
mins2 = int(input('Enter the number of minutes for the second clip: '))
secs2 = int(input('Enter the number of seconds for the second clip: '))
total_secs = secs1 + secs2
total_mins = mins1 + mins2
total_hours = hours1 + hours2
if total_secs > 59:
  total_secs = total_secs % 60
  total_mins = total_mins + 1
if total_mins > 59:
  total_mins = total_mins % 60
  total_hours = total_hours + 1
print('Total time: ' + str(total_hours) + ' hours, ' + str(total_mins) + ' minutes, and ' + str(total_secs) + ' seconds')
```