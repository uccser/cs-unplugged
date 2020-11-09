```python
sides = int(input('Enter the number of sides of a regular polygon: '))
turning_angle = 360 / sides
inside_angle = 180 - turning_angle
print('Each inside angle is ' + str(inside_angle) + ' degrees.')
```