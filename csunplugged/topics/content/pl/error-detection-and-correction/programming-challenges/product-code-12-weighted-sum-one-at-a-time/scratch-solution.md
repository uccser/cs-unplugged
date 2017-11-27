```scratch
when green flag clicked
set [total 1 v] to [0]
set [total 2 v] to [0]
set [counter v] to [1]
repeat (6)
  ask (join (join [Enter digit ] (counter)) [ of the product code:]) and wait
  change [counter v] by (1)
  change [total 1 v] by (answer)
  ask (join (join [Enter digit ] (counter)) [ of the product code:]) and wait
  change [counter v] by (1)
  change [total 2 v] by (answer)
end
set [total v] to (((total 1) * (3)) + (total 2))
if <((total) mod (10)) = [0]> then
  say [The sum is a multiple of 10]
else
  say [The sum is NOT a multiple of 10]
end
```