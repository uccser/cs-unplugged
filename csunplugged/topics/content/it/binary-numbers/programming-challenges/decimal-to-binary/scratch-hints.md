- Make variables called:
    
    - “decimal number” and set its value to the input number given by the end user.
    - “bit value” and set its value to ‘1’. Find the smallest bit value which is larger than the “decimal number” by doubling value of “bit value” until it is bigger than the “decimal number”.
    - “binary number” is a string variable and stores the binary cards needed (‘1’ for dots showing and ‘0’ for not showing).

- Set the variable “bit value” to 1 and find the smallest “bit value” which is larger than “decimal number” by multiplying “bit value” by 2 (Use the `scratch:() * ()` block under “Operators” to multiply the “bit value” by 2) until it is larger than “decimal number”. You can do this by using a `scratch:repeat until <>` loop.

- Now divide the “bit value” by 2 and check if “decimal number” is greater than or equal to “bit value”. If it is, add ‘1’ to string variable “cards” and subtract “bit value” from the “ decimal number”. If not, add ‘0’ to string variable “cards”. Repeat until “bit value” is equal to 1. Display the value of “cards” as the output.