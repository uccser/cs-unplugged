- Make variables called:
    
    - `original` and set its value to the input number given by the end user.
    - `decimal_value` and set its value to `original` (this is so we can still use the original number later)
    - `bit_value` and set its value to 1. Find the smallest bit value which is larger than the `decimal_number` by doubling value of `bit_value` while it is smaller or equal to `decimal_number`.
    - `binary_number` is a string variable and stores the binary cards needed (‘1’ for dots showing and ‘0’ for not showing).

- Set the variable `bit_value` to 1 and find the smallest `bit_value` which is larger than `decimal_number` by multiplying `bit_value` by 2 while it is smaller or equal to `decimal_number`. You can do this by using a while loop.

- Now divide the `bit_value` by 2 and check if `decimal_number` is greater than or equal to `bit_value`. If it is, add ‘1’ to the string `binary_number` and subtract `bit_value` from `decimal_number`. If not, add ‘0’ to the string `binary_number`. Repeat while `bit_value` is greater than 1. Display the value of `binary_number` as the output.