```scratch
when green flag clicked
ask [Enter the largest card number:] and wait
set [number of dots v] to (answer)
set [binary cards v] to (join (answer) [, ])
repeat until <(number of dots) = [1]>
  set [number of dots v] to ((number of dots) / (2))
  set [binary cards v] to (join (binary cards) (join (number of dots) [, ]))
end
say (binary cards)
```