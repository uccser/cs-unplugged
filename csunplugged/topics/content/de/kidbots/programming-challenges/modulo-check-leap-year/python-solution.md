```python
year = int(input("Enter the year and I will tell you if it's a leap year or not: "))
if year % 4 != 0:
  print(str(year) + ' is not a leap year!')
else:
  if year % 100 != 0:
    print(str(year) + ' is a leap year!')
  else:
    if year % 400 != 0:
      print(str(year) + ' is not a leap year!')
    else:
      print(str(year) + ' is a leap year!')
```