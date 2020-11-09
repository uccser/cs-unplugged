```scratch
when green flag clicked
set [total number of dots v] to [0]
set [number of dots v] to [1]
ask [Please enter a sequence of cards ('B' for black and 'W' for white):] and wait
set [cards v] to (answer)
set [index v] to (length of (cards))
repeat (length of (cards))
  if <(letter (index) of (cards)) = [W]> then
    set [total number of dots v] to ((total number of dots) + (number of dots))
  end
  set [number of dots v] to ((number of dots) * (2))
  set [index v] to ((index) - (1))
end
say (total number of dots)
```