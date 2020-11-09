```python
print('Enter two numbers. Enter the larger number first.')
num1 = int(input('Enter a number less than 100: '))
num2 = int(input('Enter a number less than 10: '))
if (num1 % 10 + num2) > 10:
  add_to_tidy_num1 = 10 - (num1 % 10)
  left_from_num2 = num2 - add_to_tidy_num1
  print(str(num1) + ' + ' + str(num2) + ' = ?')
  print('To make ' + str(num1) + ' a tidy number I am splitting ' + str(num2) + ' into a ' + str(add_to_tidy_num1) + ' and a ' + str(left_from_num2))
  print('(' + str(num1) + ' + ' + str(add_to_tidy_num1) + ')' + ' + ' + str(left_from_num2) + ' = ')
  print(num1 + num2)
else:
  print(str(num1) + ' + ' + str(num2) + ' = ')
  print(num1 + num2)
```