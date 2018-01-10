Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165945729/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [original time v] to (answer)

set [hours to add v] to (answer)

set [new time v] to ((original time) + (hours to add))

change [new time v] by (-12)
```

```scratch:split:random
ask [Enter a time:] and wait

ask [Enter the number of hours to add:] and wait
```

```scratch:split:random
say (join [The new time is ] (join (new time) [ o'clock.]))
```

```scratch:split:random
repeat until <<(new time) < [12]> or <(new time) = [12]>>
end
```

{panel end}
