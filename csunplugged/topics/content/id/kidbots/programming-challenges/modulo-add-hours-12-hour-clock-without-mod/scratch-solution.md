```scratch
when green flag clicked
ask [Enter a time:] and wait
set [original time v] to (answer)
ask [Enter the number of hours to add:] and wait
set [hours to add v] to (answer)
set [new time v] to ((original time) + (hours to add))
repeat until <<(new time) < [12]> or <(new time) = [12]>>
  change [new time v] by (-12)
end
say (join [The new time is ] (join (new time) [ o'clock.]))
```