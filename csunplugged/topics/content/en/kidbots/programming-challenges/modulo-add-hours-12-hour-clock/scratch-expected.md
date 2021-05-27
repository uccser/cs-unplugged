Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165593878/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [original time v] to (answer)

set [hours to add v] to (answer)

set [new time v] to (((original time) + (hours to add)) mod (12))
```

```scratch
ask [Enter a time:] and wait

ask [Enter the number of hours to add:] and wait
```

```scratch
say [The new time is 12 o'clock.]

say (join [The new time is ] (join (new time) [ o'clock.]))
```

```scratch
if <(new time) = [0]> then
else
end
```

{panel end}
