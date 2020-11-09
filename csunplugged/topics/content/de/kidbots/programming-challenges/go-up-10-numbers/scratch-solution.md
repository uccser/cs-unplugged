```scratch
when green flag clicked
set [number v] to (pick random (1) to (100))
ask (join (join [What's 10 numbers after ] (number)) [?]) and wait
if <(answer) = ((number) + (10))> then
  say [Well done!]
else
  say (join (join (join (join (join (answer) [ is a good try! But 10 numbers after ]) (number)) [ is ]) ((number) + (10))) [.])
end
```