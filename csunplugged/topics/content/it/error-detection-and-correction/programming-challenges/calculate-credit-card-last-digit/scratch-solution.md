```scratch
when green flag clicked
set [index v] to [1]
set [first 15 digits v] to [0]
set [total 2 v] to [0]
set [total 1 v] to [0]
ask [Enter the first 15 digits of the credit card:] and wait
set [first 15 digits v] to (answer)
repeat (8)
  if <((letter (index) of (first 15 digits)) * (2)) < [10]> then
    change [total 1 v] by ((letter (index) of (first 15 digits)) * (2))
    change [index v] by (2)
  else
    change [total 1 v] by (((letter (index) of (first 15 digits)) * (2)) - (9))
    change [index v] by (2)
  end
end
set [index v] to [2]
repeat (7)
  change [total 2 v] by (letter (index) of (first 15 digits))
  change [index v] by (2)
end
say (join [The last digit of the credit card should be: ] (((0) - ((total 2) + (total 1))) mod (10)))
```