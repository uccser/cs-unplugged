- Make variables called:
    
    - “number” and set its value to the input number given by the end user.
    - “bit value” and set its value to ‘1’. Find the smallest bit value which is larger than the “number” by doubling value of “bit value” until it is bigger than the “number”.
    - “cards” is a string variable and stores the binary cards needed (‘B’ for black cards and ‘W’ for white cards).

- Set the variable “bit value” to 1 and find the smallest “bit value” which is larger than “number” by multiplying “bit value” by 2 (Use the `scratch:() * ()` block under “Operators” to multiply the “bit value” by 2) until it is larger than “number”. You can do this by using a `scratch:repeat until <>` loop.

- Now divide the “bit value” by 2 and check if “number” is greater than or equal to “bit value”. If it is, add ‘W’ to string variable “cards” and subtract “bit value” from the “number”. If not, add ‘B’ to string variable “cards”. Repeat until “bit value” is equal to 1. Display the value of “cards” as the output.

- Test your program with some values on the boundaries (for example test it with numbers 255 and 256).