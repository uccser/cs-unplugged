Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/152883486/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
clear

set pen size to (3)

pen down

pen up
```

```scratch
set [angle v] to (answer)

ask [Enter an angle between 0 and 180 (not including 0 and 180):] and wait
```

```scratch
go to x: (0) y: (0)

go to x: (0) y: (0)

point in direction (90 v)

move (100) steps

move (100) steps

turn ccw ((180) - (angle)) degrees
```

```scratch
say [This is an acute triangle.] for (2) secs

say [This is a right triangle.] for (2) secs

say [This is an obtuse triangle.] for (2) secs
```

```scratch
if <(angle) < [90]> then
end

if <(angle) = [90]> then
end

if <(angle) > [90]> then
end
```

{panel end}
