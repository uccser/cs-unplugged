```python
print('Enter two numbers less than 10. Enter the larger number first.')
num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
if (num1 + num2) > 10:
  ten_minus_num1 = 10 - num1
  left_from_num2 = num2 - ten_minus_num1
  print(str(num1) + ' + ' + str(num2) + ' = ?')
  print('To make ' + str(num1) + ' a tidy number I am splitting ' + str(num2) + ' into a ' + str(ten_minus_num1) + ' and a ' + str(left_from_num2))
  print('(' + str(num1) + ' + ' + str(ten_minus_num1) + ')' + ' + ' + str(left_from_num2) + ' = ?')
  print(num1 + num2)
else:
  print(str(num1) + ' + ' + str(num2) + ' = ?')
  print(num1 + num2)
```