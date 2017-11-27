```scratch
when green flag clicked
set [binary cards v] to []
set [number of dots v] to [1]
ask [How many cards would you like to display?] and wait
set [number of cards v] to (answer)
repeat (number of cards)
  set [binary cards v] to (join (binary cards) (join (number of dots) [, ]))
  set [number of dots v] to ((number of dots) * (2))
end
say (binary cards)
```