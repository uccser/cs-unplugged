**The Button Sprites**

forward:

```scratch
when this sprite clicked
insert [forward] at (last v) of [source code v]
```

backward:

```scratch
when this sprite clicked
insert [backward] at (last v) of [source code v]
```

left:

```scratch
when this sprite clicked
insert [turn left] at (last v) of [source code v]
```

right:

```scratch
when this sprite clicked
insert [turn right] at (last v) of [source code v]
```

go:

```scratch
when this sprite clicked
broadcast [go v]
```

home:

```scratch
when this sprite clicked
broadcast [home v]
```

undo:

```scratch
when this sprite clicked
delete (last v) of [source code v]
```

pause:

```scratch
when this sprite clicked
insert [pause] at (last v) of [source code v]
```

clear:

```scratch
when this sprite clicked
delete (all v) of [source code v]
```

**The Sprites**

Mouse:

```scratch
when green flag clicked
set size to (30) %
go to x: ((pick random (-1) to (4)) * (50)) y: ((pick random (-3) to (3)) * (50))
```

Cat:

```scratch
when I receive [go v]
set [statement v] to [0]
set [source line v] to [1]
repeat (length of [source code v] :: list)
  set [statement v] to (item (source line) of [source code v] :: list)
  if <(statement) = [forward]> then
    if <touching [border v] ?> then
      say [Oh no! Missed it! Press "home" and then "clear" to try again.] for (2) secs
      stop [all v]
    else
      move (50) steps
      wait (0.5) secs
    end
  else
    if <(statement) = [backward]> then
      if <touching [border v] ?> then
        say [Oh no! Missed it! Press "home" and then "clear" to try again.] for (2) secs
        stop [all v]
      else
        move (-50) steps
        wait (0.5) secs
      end
    else
      if <(statement) = [turn left]> then
        turn ccw (90) degrees
        wait (0.5) secs
      else
        if <(statement) = [turn right]> then
          turn cw (90) degrees
          wait (0.5) secs
        else
          if <(statement) = [pause]> then
            wait (5) secs
          end
        end
      end
    end
  end
  change [source line v] by (1)
end
if <touching [Mouse v] ?> then
  play sound [meow v]
  say [Gotcha!] for (2) secs
else
  say [Oh no! Missed it! Press "home" and then "clear" to try again.]
end
```

```scratch
when green flag clicked
set size to (50) %
go to x: (50) y: (0)
point in direction (90 v)
delete (all v) of [source code v]
```

```scratch
when I receive [home v]
point in direction (90 v)
go to x: (50) y: (0)
```