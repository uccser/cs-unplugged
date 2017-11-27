```scratch
when green flag clicked
set [product code v] to [0]
set [total 1 v] to [0]
set [total 2 v] to [0]
set [total v] to [0]
ask [Enter a product code:] and wait
change [product code v] by (answer)
set [index v] to (length of (product code))
repeat until <(index) < [1]>
  set [total 1 v] to ((total 1) + (letter (index) of (product code)))
  change [index v] by (-1)
  set [total 2 v] to ((total 2) + (letter (index) of (product code)))
  change [index v] by (-1)
end
set [total v] to ((total 1) + ((total 2) * (3)))
if <((total) mod (10)) = [0]> then
  say [This is a valid product code]
else
  say [This is an invalid product code]
end
```