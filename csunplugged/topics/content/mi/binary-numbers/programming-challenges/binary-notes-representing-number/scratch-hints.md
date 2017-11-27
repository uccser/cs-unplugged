- Make variables called:
    
    - “decimal number” and set its value to the input number given by the end user.
    - “bit value” and set its value to ‘32’.

- Now divide the “bit value” by 2 and check if “decimal number” is greater than or equal to “bit value”. If it is, play a high note and subtract “bit value” from the “decimal number”. If not, play a low note. Repeat until “bit value” is equal to 1.

- To play a musical note use the block `scratch:play note (60 v) for (0.5) beats` beats under the “Sound”. Type in the number “72” for a high note and “48” for a low note.
- Test your program with some values on the boundaries (for example test it with numbers 0 and 31).