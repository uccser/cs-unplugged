```scratch
when green flag clicked
ask [Enter the largest number of dots on a card:] and wait
set [number of dots v] to (answer)
say (number of dots) for (1) secs
repeat until <(number of dots) = [1]>
  set [number of dots v] to ((number of dots) / (2))
  say (number of dots) for (1) secs
end
```
