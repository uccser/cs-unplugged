# Programming Reminders

## Print statements

```python3
# Print a string directly
print("Hello World!")

# Print a variable
print(my_var)
```

## Variables

```Python3
# Set a variable as a string
fruit_name = "Apple"

# Set a variable as an integer 
pieces_of_fruit = 7

# Set a variable from a calculation
cost_of_fruit = pieces_of_fruit * cost_per_item

# Add one to a value
pieces_of_fruit += 1
```

## Conditionals

```Python3
# Find out the discount on fruit
if pieces_of_fruit > 100:
   print(“Bulk discount applies”)
elif pieces_of_fruit > 5:
   print(“Discount applies”)
else:
   print(“No discount”)
```

## For loops

```Python3
# Print numbers 0-9 - remember Python starts counting from 0 
for num in range(10):
    print(num)
```

## While loops

```Python3
# Print numbers 0-9 using a while loop and a variable
num = 0
while num < 10:
    print(num)

    # Increment the variable by one.
    # It will prevent an infinite loop!
    num += 1 
```

## Lists

```Python3
# Create a list of fruit 
fruit = ["Apple", "Banana", "Orange", "Pear"]
```

## Functions

```Python3
# Create a function which prints a greeting
def greeting(name):
    print("Hello " + name)

# Call the function
greeting("Spiderman")
```
