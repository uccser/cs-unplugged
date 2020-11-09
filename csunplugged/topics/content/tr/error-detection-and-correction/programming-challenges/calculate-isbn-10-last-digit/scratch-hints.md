- Calculate the sum of all the 9 digits each multiplied by its (integer) weight, descending from 10 to 2. The last digit (check digit) is calculated by subtracting the final total from 0 mod 11.

- If the last digit is the number 10, replace it with the letter ‘X’.
    
    For example the last digit of the ISBN-10 “020153082” is calculated by:
    
    \[ total=(100)+(92)+(80)+(71)+(65)+(53)+(40)+(38)+(22) \]
    
    \[ total=0+18+0+7+30+15+0+24+4=98 \]
    
    So the last digit is 1 (i.e. (0-98) mod 11 which is equal to 1).
    
    Another example: The last digit of the ISBN-10 “043942089” is calculated by:
    
    \[ total=(100)+(94)+(83)+(79)+(64)+(52)+(40)+(38)+(29) \]
    
    \[ total=0+36+24+63+24+10+0+24+18=199 \]
    
    So the last digit is ‘X’ (i.e. (0-199) mod 11 which is equal to 10).