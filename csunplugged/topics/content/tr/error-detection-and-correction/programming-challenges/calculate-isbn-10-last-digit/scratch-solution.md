```scratch
when green flag clicked
set [index v] to [1]
set [multiplier v] to [10]
set [first 9 digits v] to [0]
set [total v] to [0]
set [last digit v] to [0]
ask [Enter the first 9 digits of an ISBN-10 number:] and wait
set [first 9 digits v] to (answer)
repeat (9)
  change [total v] by ((multiplier) * (letter (index) of (first 9 digits)))
  change [index v] by (1)
  change [multiplier v] by (-1)
end
set [last digit v] to (((0) - (total)) mod (11))
if <(last digit) = [10]> then
  say [The last digit is: X]
else
  say (join [The last digit is: ] (last digit))
end
```