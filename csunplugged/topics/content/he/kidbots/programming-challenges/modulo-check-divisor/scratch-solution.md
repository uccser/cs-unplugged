```scratch
when green flag clicked
say [Enter 2 numbers and I'll tell you if the second number is a divisor of the first number.] for (5) secs
ask [Enter the 1st number:] and wait
set [number1 v] to (answer)
ask [Enter the 2nd number:] and wait
set [number2 v] to (answer)
if <((number1) mod (number2)) = [0]> then
  say (join (join (number2) [ is a divisor of the number ]) (number1))
else
  say (join (join (number2) [ is not a divisor of the number ]) (number1))
end
```