```scratch
when green flag clicked
set [odd total v] to [0]
set [even total v] to [0]
set [index v] to [1]
set [last digit v] to [0]
repeat (6)
  ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
  change [index v] by (1)
  change [odd total v] by (answer)
  ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
  change [index v] by (1)
  change [even total v] by (answer)
end
set [last digit v] to (((0) - ((odd total) + ((even total) * (3)))) mod (10))
say (join [The last digit of the product code is ] (last digit))
```