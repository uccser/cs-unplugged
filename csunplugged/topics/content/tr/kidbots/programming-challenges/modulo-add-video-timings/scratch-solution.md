```scratch
when green flag clicked
set [secs1 v] to [0]
set [mins1 v] to [0]
set [hours1 v] to [0]
set [secs2 v] to [0]
set [mins2 v] to [0]
set [hours2 v] to [0]
set [total secs v] to [0]
set [total mins v] to [0]
set [total hours v] to [0]
ask [Enter the number of hours for the first clip: ] and wait
set [hours1 v] to (answer)
ask [Enter the number of minutes for the first clip: ] and wait
set [mins1 v] to (answer)
ask [Enter the number of seconds for the first clip: ] and wait
set [secs1 v] to (answer)
ask [Enter the number of hours for the second clip: ] and wait
set [hours2 v] to (answer)
ask [Enter the number of minutes for the second clip: ] and wait
set [mins2 v] to (answer)
ask [Enter the number of seconds for the second clip: ] and wait
set [secs2 v] to (answer)
set [total secs v] to ((secs1) + (secs2))
set [total mins v] to ((mins1) + (mins2))
set [total hours v] to ((hours1) + (hours2))
if <(total secs) > [59]> then
  set [total secs v] to ((total secs) mod (60))
  change [total mins v] by (1)
end
if <(total mins) > [59]> then
  set [total mins v] to ((total mins) mod (60))
  change [total hours v] by (1)
end
```