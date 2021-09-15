-   Make variables called:

    -   “total number of dots” and set its value to 0.
    -   “number of dots” and set its value to 16.
    -   “cards” and set its value to the string entered as the input.
        Check each letter of the input string “cards” (use a loop to iterate
        5 times) starting from the first letter.
        If it’s ‘W’ add the corresponding number of dots (16 for the first
        letter, 8 for the second letter and so on) to the “total number
        of dots”.
        Display the “total number of dots” as the output.
    -   “index” and set its value to 1.
        Use this variable to access a letter at the “index” position in the
        string.

-   You can access a letter at the specified position in a string by using
    the `scratch:letter (1) of [world]` block under “Operators”.
    For example: `scratch:letter (1) of [world] //w`

-   In this challenge you need to access all the 5 letters in user’s input and
    check to see if each of them is equal to B (black) or W (white).
