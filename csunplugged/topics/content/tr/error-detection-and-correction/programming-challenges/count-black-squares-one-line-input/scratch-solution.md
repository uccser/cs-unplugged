```scratch
when green flag clicked
set [black cards total v] to [0]
set [index v] to [1]
ask [Please enter a sequence of black and white squares (B for black and W for white):] and wait
set [cards v] to (answer)
repeat (length of (cards))
  if <(letter (index) of (cards)) = [B]> then
    change [black cards total v] by (1)
  end
  change [index v] by (1)
end
say (black cards total)
```