Click on the green flag, and use the buttons to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/158364683/?autostart=false"}

{panel type="help"}

# Recommended blocks

Events
```scratch
when green flag clicked

when this sprite clicked

when I receive [home v]

broadcast [go v]

broadcast [home v]
```

Control
```scratch
repeat (length of [source code v] :: list)
end

if <(statement) = [forward]> then
else
end

if <(statement) = [backward]> then
else
end

if <(statement) = [turn left]> then
else
end

if <(statement) = [turn right]> then
else
end

if <touching [border v] ?> then
else
end

if <touching [Mouse v] ?> then
else
end

stop [all v]

wait (0.5) secs
```

Data - Variable
```scratch
set [statement v] to [0]

set [source line v] to [1]

set [statement v] to (item (source line) of [source code v] :: list)

change [source line v] by (1)
```

Data - List
```scratch
insert [forward] at (last v) of [source code v]

insert [backward] at (last v) of [source code v]

insert [turn left] at (last v) of [source code v]

insert [turn right] at (last v) of [source code v]

insert [pause] at (last v) of [source code v]

delete (last v) of [source code v]

delete (all v) of [source code v]
```

Looks
```scratch
set size to (30) %

set size to (50) %

say [Oh no! Missed it! Press "home" and then "clear" to try again.] for (2) secs

say [Gotcha!] for (2) secs

say [Oh no! Missed it! Press "home" and then "clear" to try again.]
```

Sensing
```scratch
go to x: (50) y: (0)

go to x: ((pick random (-1) to (4)) * (50)) y: ((pick random (-3) to (3)) * (50))

move (50) steps

move (-50) steps

turn cw (90) degrees

turn ccw (90) degrees

point in direction (90 v)

```

Sound
```scratch
play sound [meow v]
```

{panel end}
