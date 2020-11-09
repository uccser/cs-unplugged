```python
number1 = int(input('Enter a number: '))
done = False
print("Enter 'done' at any time to stop")
while not done:
  number2 = int(input("Enter a number to check if it's a divisor of the number " + str(number1)))
  if number2 == 'done':
    done = True
  elif number1 % number2 == 0:
    print(str(number2) + ' is a divisor of the number ' + str(number1))
  else:
    print(str(number2) + ' is not a divisor of the number ' + str(number1))
```