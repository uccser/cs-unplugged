```scratch
when green flag clicked
set [total number of dots v] to [0]
ask [Please enter 5 cards ('B' for black and 'W' for white):] and wait
set [cards v] to (answer)
if <(letter (1) of (cards)) = [W]> then
  set [total number of dots v] to ((total number of dots) + (16))
end
if <(letter (2) of (cards)) = [W]> then
  set [total number of dots v] to ((total number of dots) + (8))
end
if <(letter (3) of (cards)) = [W]> then
  set [total number of dots v] to ((total number of dots) + (4))
end
if <(letter (4) of (cards)) = [W]> then
  set [total number of dots v] to ((total number of dots) + (2))
end
if <(letter (5) of (cards)) = [W]> then
  set [total number of dots v] to ((total number of dots) + (1))
end
say (total number of dots)
```