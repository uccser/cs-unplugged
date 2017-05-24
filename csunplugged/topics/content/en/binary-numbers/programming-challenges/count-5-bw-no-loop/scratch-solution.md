```scratch
when green flag clicked
set [total number of dots v] to [0]
ask [What's your first card (B for black, W for white)?] and wait
if <(answer) = [W]> then
  set [total number of dots v] to ((total number of dots) + (16))
end
ask [What's your second card (B for black, W for white)?] and wait
if <(answer) = [W]> then
  set [total number of dots v] to ((total number of dots) + (8))
end
ask [What's your third card (B for black, W for white)?] and wait
if <(answer) = [W]> then
  set [total number of dots v] to ((total number of dots) + (4))
end
ask [What's your fourth card (B for black, W for white)?] and wait
if <(answer) = [W]> then
  set [total number of dots v] to ((total number of dots) + (2))
end
ask [What's your fifth card (B for black, W for white)?] and wait
if <(answer) = [W]> then
  set [total number of dots v] to ((total number of dots) + (1))
end
say (total number of dots)
```
