```scratch
when green flag clicked
set [black cards total v] to [0]
repeat (5)
  ask [Please enter a black or white square (B for black or W for white):] and wait
  if <(answer) = [B]> then
    change [black cards total v] by (1)
  end
end
say (black cards total)
```