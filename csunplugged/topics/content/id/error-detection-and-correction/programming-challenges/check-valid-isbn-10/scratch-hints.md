- To check if an ISBN-10 number is valid, the sum of all the ten digits each multiplied by its (integer) weight, descending from 10 to 1, needs to be a multiple of 11 (i.e. total mod 11 is equal to 0).

- If the last digit of an ISBN-10 is X, you need to multiply 10 by its integer weight 1 (as it’s the last digit) to calculate the total.
    
    For example for an ISBN-10 of 0201530821:
    
    \[ total=(100)+(92)+(80)+(71)+(65)+(53)+(40)+(38)+(22)+(11) \]
    
    \[ total=0+18+0+7+30+15+0+24+4+1=99 \]
    
    This is a valid ISBN-10 as 99 mod 11 is 0.