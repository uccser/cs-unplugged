```scratch
when green flag clicked
set [total 1 v] to [0]
set [total 2 v] to [0]
set [index v] to [1]
set [last digit v] to [0]
repeat (5)
  ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
  change [index v] by (1)
  change [total 1 v] by (answer)
  ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
  change [index v] by (1)
  change [total 2 v] by (answer)
end
ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
change [index v] by (1)
change [total 1 v] by (answer)
set [last digit v] to (((0) - (((total 1) * (3)) + (total 2))) mod (10))
say (join [The last digit of the product code is ] (last digit))
```