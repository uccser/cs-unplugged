```python
import random
coin = 0
number_of_heads = 0
number_of_tails = 0
number_of_flips = int(input('How many times would you like to flip a coin? '))
for i in range(0, number_of_flips):
  coin = random.randint(1, 2)
  if coin == 1:
    number_of_heads = number_of_heads + 1
  else:
    number_of_tails = number_of_tails + 1
print(str(int(number_of_heads * 100 / number_of_flips)) + '% heads')
print(str(int(number_of_tails * 100 / number_of_flips)) + '% tails')
```