```python
print("Enter 2 numbers and I'll tell you if the second number is a divisor of the first number.")
number1 = int(input('Enter the 1st number: '))
number2 = int(input('Enter the 2nd number: '))
if number1 % number2 == 0:
  print(str(number2) + ' is a divisor of the number ' + str(number1))
else:
  print(str(number2) + ' is not a divisor of the number ' + str(number1))
```