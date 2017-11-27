```scratch
when green flag clicked
set [number of dots v] to [1]
set [binary cards v] to []
repeat (5)
  set [binary cards v] to (join (binary cards) (join (number of dots) [, ]))
  set [number of dots v] to ((number of dots) * (2))
end
say (binary cards)
```