```python
original_month = int(input('Type in a number between 1 and 12 for a month of the year: '))
months_to_add = int(input('Enter the number of months to add to the month: '))
new_month = (original_month + months_to_add) % 12
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(str(months_to_add) + ' months after ' + months[original_month - 1] + ' is ' + months[new_month - 1] + '.')
```
