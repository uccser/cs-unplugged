# 12 and 13 digit product codes: Check for a valid product code (any length)

## Requirement:

Write a program that asks the user to enter a product code of any length in
one line of input and adds up all the digits (every second one multiplied
by 3).
To add up the digits you need to start from the last digit, multiply the last
digit by 1, second to last by 3 and so on.
It then checks if the product code is valid (total number is a multiple of 10).
Starting at the right-hand digit will make the formula work for a wide
variety of product codes.

(Note that this rule will work for most of the common product codes on shop
products, which use the alternating multipliers of 3 and 1.
The check digit is always multiplied by 1, so starting at the right is an
easy way to get the sequence correct.
Common codes that you may come across are GTIN-13, GTIN-12, GTIN-8, EAN-13,
EAN-8 and UPC-A, and these all use the alternating 1/3 formula.
An exception is UPC-E, which is very complex.
UPC-E is most common in America; it as an 8-digit code used on smaller items
such as soda cans.
Because the structure of UPC-E is so complex, it's best to not use them
unless you have advanced students wanting a difficult challenge.
UPC-E product codes can be recognised because they do not have a double line
from the bars extending down between the two sets of four digits i.e.
the 8 digits are all written without any gaps.)
