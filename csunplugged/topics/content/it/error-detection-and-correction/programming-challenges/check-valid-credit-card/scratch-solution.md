```scratch
when green flag clicked
set [index v] to [1]
set [credit card number v] to [0]
set [even total v] to [0]
set [odd total v] to [0]
ask [Enter a credit card number:] and wait
change [credit card number v] by (answer)
repeat (8)
  if <((letter (index) of (credit card number)) * (2)) < [10]> then
    change [odd total v] by ((letter (index) of (credit card number)) * (2))
    change [index v] by (1)
  else
    change [odd total v] by (((letter (index) of (credit card number)) * (2)) - (9))
    change [index v] by (1)
  end
  change [even total v] by (letter (index) of (credit card number))
  change [index v] by (1)
end
if <(((even total) + (odd total)) mod (10)) = [0]> then
  say [Valid credit card number!]
else
  say [Invalid credit card number!]
end
```