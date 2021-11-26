```scratch
when green flag clicked
set [number of dots v] to [16]
set [total number of dots v] to [0]
repeat (5)
  ask [Please enter a black or white card ('B' for black or 'W' for white):] and wait
  if <(answer) = [W]> then
    set [total number of dots v] to ((total number of dots) + (number of dots))
  end
  set [number of dots v] to ((number of dots) / (2))
end
say (total number of dots)
```
