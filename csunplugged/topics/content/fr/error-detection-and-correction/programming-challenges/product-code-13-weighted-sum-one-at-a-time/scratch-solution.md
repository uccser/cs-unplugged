```scratch
when green flag clicked
set [total 1 v] to [0]
set [total 2 v] to [0]
set [index v] to [1]
repeat (6)
  ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
  change [index v] by (1)
  change [total 1 v] by (answer)
  ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
  change [index v] by (1)
  change [total 2 v] by (answer)
end
ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
change [total 1 v] by (answer)
set [total v] to ((total 1) + ((total 2) * (3)))
say (join [Total: ] (total))
```