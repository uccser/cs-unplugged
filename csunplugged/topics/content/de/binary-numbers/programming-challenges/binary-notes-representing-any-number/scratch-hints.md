- Make variables called:
    
    - “decimal number” and set its value to the input number given by the end user.
    - “bit value” and set its value to ‘1’. Find the smallest bit value which is larger than the “decimal number” by doubling value of “bit value” until it is bigger than the “decimal number”.

- Set the variable “bit value” to 1 and find the smallest “bit value” which is larger than “decimal number” by multiplying “bit value” by 2 (Use the `scratch:() * ()` block under “Operators” to multiply the “bit value” by 2) until it is larger than “decimal number”. You can do this by using a `scratch:repeat until <>` loop.

- Now divide the “bit value” by 2 and check if “decimal number” is greater than or equal to “bit value”. If it is, play a high note and subtract “bit value” from the “decimal number”. If not, play a low note. Repeat until “bit value” is equal to 1.
- To play a musical note use the block `scratch:play note (60 v) for (0.5) beats` beats under the “Sound”. Type in the number “72” for a high note and “48” for a low note.