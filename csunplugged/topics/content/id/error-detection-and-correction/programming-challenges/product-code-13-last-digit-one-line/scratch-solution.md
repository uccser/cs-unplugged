```scratch
when green flag clicked
set [index v] to [1]
set [first 12 digits v] to [0]
set [total 1 v] to [0]
set [total 2 v] to [0]
set [last digit v] to [0]
ask [Enter first 12 digits of the barcode:] and wait
set [first 12 digits v] to (answer)
if <(length of (first 12 digits)) = [12]> then
  repeat (6)
    set [total 1 v] to ((total 1) + (letter (index) of (first 12 digits)))
    change [index v] by (1)
    set [total 2 v] to ((total 2) + (letter (index) of (first 12 digits)))
    change [index v] by (1)
  end
  set [last digit v] to (((0) - ((total 1) + ((total 2) * (3)))) mod (10))
  say (join [The last digit of the product code is: ] (last digit))
else
  say [You must enter a 12 digit number!]
end
```