# Check if a year is a leap year

## Requirement:

Write a program that takes a year as the input and displays a message saying if the year is a leap year or not.

Following is the algorithm to check if a year is a leap year or not:

1. if (year is not divisible by 4) then (it is a common year)
2. else if (year is not divisible by 100) then (it is a leap year)
3. else if (year is not divisible by 400) then (it is a common year)
4. else (it is a leap year)

## Testing examples:

Your program should display the outputs shown in this table for the given inputs provided;

| Input | Output                   |
| ----- | ------------------------ |
| 1600  | 1600 is a leap year!     |
| 2000  | 2000 is a leap year!     |
| 2400  | 2400 is a leap year!     |
| 1700  | 1700 is not a leap year! |
| 2100  | 2100 is not a leap year! |
| 2300  | 2300 is not a leap year! |