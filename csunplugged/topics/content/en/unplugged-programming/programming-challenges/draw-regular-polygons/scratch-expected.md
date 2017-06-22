Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/152496450/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
clear

pen down

pen up
```

```scratch:split:random
set [sides v] to (answer)
```

```scratch:split:random
go to x: (0) y: (0)

move (50) steps

turn cw ((360) / (sides)) degrees
```

```scratch:split:random
say [I'll draw a polygon with the number of sides you give me.] for (3) secs
```

```scratch:split:random
ask [Enter the number of sides:] and wait
```

```scratch:split:random
wait (1) secs

repeat (sides)
end
```

{panel end}
