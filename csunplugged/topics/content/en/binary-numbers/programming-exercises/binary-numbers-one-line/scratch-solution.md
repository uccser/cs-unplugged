```scratch
when flag clicked
set [dots v] to [1]
set [cards v] to [ ]
repeat (5)
set [cards v] to (join (cards) (join (dots) [,]))
set [dots v] to ((dots) * (2))
end
say (cards)
```
