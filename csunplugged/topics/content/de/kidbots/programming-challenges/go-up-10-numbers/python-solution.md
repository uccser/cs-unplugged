```python
import random
number = random.randint(0, 100)
answer = int(input("What's 10 numbers after " + str(number) + "? "))
if answer == number + 10:
  print('Well done!')
else:
  print(str(answer) + ' is a good try! But 10 numbers after ' + str(number) + ' is ' + str(number + 10) + '.')
```