Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165605502/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [secs1 v] to [0]

set [mins1 v] to [0]

set [hours1 v] to [0]

set [secs2 v] to [0]

set [mins2 v] to [0]

set [hours2 v] to [0]

set [total secs v] to [0]

set [total mins v] to [0]

set [total hours v] to [0]

set [hours1 v] to (answer)

set [mins1 v] to (answer)

set [secs1 v] to (answer)

set [hours2 v] to (answer)

set [mins2 v] to (answer)

set [secs2 v] to (answer)

set [total secs v] to ((secs1) + (secs2))

set [total mins v] to ((mins1) + (mins2))

set [total hours v] to ((hours1) + (hours2))

set [total secs v] to ((total secs) mod (60))

change [total mins v] by (1)

set [total mins v] to ((total mins) mod (60))

change [total hours v] by (1)
```

```scratch
ask [Enter the number of hours for the first clip: ] and wait

ask [Enter the number of minutes for the first clip: ] and wait

ask [Enter the number of seconds for the first clip: ] and wait

ask [Enter the number of hours for the second clip: ] and wait

ask [Enter the number of minutes for the second clip: ] and wait

ask [Enter the number of seconds for the second clip: ] and wait
```

```scratch
if <(total secs) > [59]> then
end

if <(total mins) > [59]> then
end
```

{panel end}
