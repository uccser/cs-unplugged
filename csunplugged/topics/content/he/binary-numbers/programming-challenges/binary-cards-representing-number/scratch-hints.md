- Make variables called:
    
    - “number” and set its value to the input number given by the end user.
    - “bit value” and set its value to ‘32’.
    - “cards” is a string variable and stores the binary cards needed (‘B’ for black cards and ‘W’ for white cards).

- Now divide the “bit value” by 2 and check if “number” is greater than or equal to “bit value”. If it is, add ‘W’ to string variable “cards” and subtract “bit value” from the “number”. If not, add ‘B’ to string variable “cards”. Repeat until “bit value” is equal to 1. Display the value of “cards” as the output.

- Test your program with some values on the boundaries (for example test it with numbers 0 and 31).