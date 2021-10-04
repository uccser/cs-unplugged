Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165945729/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [original time v] to (answer)

set [hours to add v] to (answer)

set [new time v] to ((original time) + (hours to add))

change [new time v] by (-12)
```

```scratch
ask [Enter a time:] and wait

ask [Enter the number of hours to add:] and wait
```

```scratch
say (join [The new time is ] (join (new time) [ o'clock.]))
```

```scratch
repeat until <<(new time) < [12]> or <(new time) = [12]>>
end
```

{panel end}
