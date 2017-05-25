```scratch
when green flag clicked
set [total number of dots v] to [0]
set [index v] to [1]
set [number of dots v] to [16]
ask [Please enter 5 cards (B for black and W for white):] and wait
set [cards v] to (answer)
repeat (5)
  if <(letter (index) of (cards)) = [W]> then
    set [total number of dots v] to ((total number of dots) + (number of dots))
  end
  set [number of dots v] to ((number of dots) / (2))
  change [index v] by (1)
end
say (total number of dots)
```
