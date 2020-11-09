```scratch
when green flag clicked
set [index v] to [1]
set [first 11 digits v] to [0]
set [total 1 v] to [0]
set [total 2 v] to [0]
set [last digit v] to [0]
ask [Enter first 11 digits of the product code:] and wait
set [first 11 digits v] to (answer)
if <(length of (first 11 digits)) = [11]> then
  repeat (5)
    set [total 1 v] to ((total 1) + (letter (index) of (first 11 digits)))
    change [index v] by (1)
    set [total 2 v] to ((total 2) + (letter (index) of (first 11 digits)))
    change [index v] by (1)
  end
  set [total 1 v] to ((total 1) + (letter (index) of (first 11 digits)))
  change [index v] by (1)
  set [last digit v] to (((0) - (((total 1) * (3)) + (total 2))) mod (10))
  say (join [The last digit of the product code is: ] (last digit))
else
  say [You must enter a 11 digit number!]
end
```