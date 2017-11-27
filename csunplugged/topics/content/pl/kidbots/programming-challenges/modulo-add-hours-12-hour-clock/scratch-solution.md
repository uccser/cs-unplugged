```scratch
when green flag clicked
ask [Enter a time:] and wait
set [original time v] to (answer)
ask [Enter the number of hours to add:] and wait
set [hours to add v] to (answer)
set [new time v] to (((original time) + (hours to add)) mod (12))
if <(new time) = [0]> then
  say [The new time is 12 o'clock.]
else
  say (join [The new time is ] (join (new time) [ o'clock.]))
end
```