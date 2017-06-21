Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/152883319/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
clear

set pen size to (3)

pen down

pen up
```

```scratch:split:random
set [angle v] to (answer)
```

```scratch:split:random
go to x: (0) y: (0)

point in direction (90 v)

move (100) steps

turn ccw ((180) - (angle)) degrees
```

```scratch:split:random
say [The angle you entered is an acute angle.] for (3) secs

say [The angle you entered is a right angle.] for (3) secs

say [The angle you entered is an obtuse angle.] for (3) secs

say [The angle you entered is a straight angle.] for (3) secs

say [The angle you entered is a reflex angle.] for (3) secs
```

```scratch:split:random
ask [Enter an angle between 0 and 360 (not including 0 and 360):] and wait
```

```scratch:split:random
if <(angle) < [180]> then
else
end

if <(angle) < [90]> then
else
end

if <(angle) = [90]> then
else
end

if <(angle) = [180]> then
else
end
```

{panel end}
