```python
import random
print("I'll generate a random number between 1 and a number you enter. ")
upper_range = int(input('Enter a number as the upper range: '))
numbers_after_list = [1, 10, 100]
number = random.randint(1, upper_range)
numbers_after = numbers_after_list[random.randint(0, 2)]
answer = 0
if numbers_after == 1:
    answer = int(input('What is the number after ' + str(number) + '? '))
else:
    answer = int(input('What is ' + str(numbers_after) + ' numbers after ' + str(number) + '? '))
if answer == number + numbers_after:
    print('Well done!')
else:
    print('Nice try! The right answer is: ' + str(number + numbers_after))
```