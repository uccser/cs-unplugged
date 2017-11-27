```scratch
when green flag clicked
set [index v] to [1]
set [product code v] to []
set [total 1 v] to [0]
set [total 2 v] to [0]
set [total v] to [0]
ask [Enter a 13-digit product code:] and wait
change [product code v] by (answer)
if <(length of (product code)) = [13]> then
  repeat (6)
    set [total 1 v] to ((total 1) + (letter (index) of (product code)))
    change [index v] by (1)
    set [total 2 v] to ((total 2) + (letter (index) of (product code)))
    change [index v] by (1)
  end
  set [total 1 v] to ((total 1) + (letter (index) of (product code)))
  set [total v] to ((total 1) + ((total 2) * (3)))
  if <((total) mod (10)) = [0]> then
    say [Valid product code!]
  else
    say [Invalid product code!]
  end
else
  say [Please enter a 13 digit number!]
end
```