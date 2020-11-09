```scratch
when green flag clicked
ask [Enter a time:] and wait
set [original time v] to (answer)
ask [Enter the number of hours to add:] and wait
set [hours to add v] to (answer)
set [new time v] to (((original time) + (hours to add)) mod (24))
if <(new time) = [0]> then
  say [The new time is 00:00]
else
  say (join [The new time is ] (join (new time) [:00.]))
end
```