```scratch
when green flag clicked
set [odd total v] to [0]
set [even total v] to [0]
set [index v] to [1]
repeat (6)
  ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
  change [index v] by (1)
  change [odd total v] by (answer)
  ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
  change [index v] by (1)
  change [even total v] by (answer)
end
ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
change [odd total v] by (answer)
set [total v] to ((odd total) + ((even total) * (3)))
if <((total) mod (10)) = [0]> then
  say [The sum is a multiple of 10]
else
  say [The sum is NOT a multiple of 10]
end
```