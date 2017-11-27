```scratch
when green flag clicked
set [black cards total v] to [0]
set [index v] to [1]
ask [Please enter a row of black and white cards (B for black and W for white):] and wait
set [cards v] to (answer)
repeat (length of (cards))
  if <(letter (index) of (cards)) = [B]> then
    change [black cards total v] by (1)
  end
  change [index v] by (1)
end
if <((black cards total) mod (2)) = [0]> then
  say [There is no parity error in this row!]
else
  say [There is a parity error in this row!]
end
```