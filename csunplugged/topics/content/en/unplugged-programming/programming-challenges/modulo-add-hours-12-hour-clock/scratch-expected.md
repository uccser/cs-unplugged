Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165593878/?autostart=false"}

{panel type="help" title="Recommended blocks for solution 1"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [original time v] to (answer)

set [hours to add v] to (answer)

set [new time v] to (((original time) + (hours to add)) mod (12))
```

```scratch:split:random
ask [Enter a time:] and wait

ask [Enter the number of hours to add:] and wait
```

```scratch:split:random
say [The new time is 12 o'clock.]

say (join [The new time is ] (join (new time) [ o'clock.]))
```

```scratch:split:random
if <(new time) = [0]> then
else
end
```

{panel end}
