```scratch
when green flag clicked
set [number of dots v] to [1]
ask [How many cards would you like to display?] and wait
set [number of cards v] to (answer)
repeat (number of cards)
  say (number of dots) for (1) secs
  set [number of dots v] to ((number of dots) * (2))
end
```