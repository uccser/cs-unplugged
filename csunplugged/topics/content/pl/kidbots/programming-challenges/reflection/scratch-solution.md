**Solution #1:**

Sprite:

```scratch
when green flag clicked
clear
set pen size to (3)
set pen color to [#2ca5e2]
go to x: (0) y: (100)
pen down
wait (1) secs
go to x: (-100) y: (100)
wait (1) secs
go to x: (-100) y: (0)
wait (1) secs
go to x: (-100) y: (0)
wait (1) secs
go to x: (-200) y: (0)
wait (1) secs
go to x: (-200) y: (-100)
wait (1) secs
go to x: (0) y: (-100)
wait (1) secs
go to x: (0) y: (100)
pen up
```

Mirror Sprite:

```scratch
when green flag clicked
clear
set pen size to (3)
set pen color to [#db0705]
go to x: (0) y: (100)
pen down
wait (1) secs
go to x: (100) y: (100)
wait (1) secs
go to x: (100) y: (0)
wait (1) secs
go to x: (100) y: (0)
wait (1) secs
go to x: (200) y: (0)
wait (1) secs
go to x: (200) y: (-100)
wait (1) secs
go to x: (0) y: (-100)
wait (1) secs
go to x: (0) y: (100)
pen up
```

**Solution #2:**

Sprite:

```scratch
when green flag clicked
set [angle v] to [90]
clear
set pen size to (3)
set pen color to [#05d382]
go to x: (0) y: (0)
point in direction (0 v)
pen down
move (100) steps
turn ccw (angle) degrees
wait (1) secs
move (100) steps
turn ccw (angle) degrees
wait (1) secs
move (100) steps
turn cw (angle) degrees
wait (1) secs
move (100) steps
turn ccw (angle) degrees
wait (1) secs
move (100) steps
turn ccw (angle) degrees
wait (1) secs
move (200) steps
turn ccw (angle) degrees
wait (1) secs
move (100) steps
wait (1) secs
pen up
```

Mirror Sprite:

```scratch
when green flag clicked
set [mirror angle v] to ((360) - (angle))
clear
set pen size to (3)
set pen color to [#e81818]
go to x: (0) y: (0)
point in direction (0 v)
pen down
move (100) steps
turn ccw (mirror angle) degrees
wait (1) secs
move (100) steps
turn ccw (mirror angle) degrees
wait (1) secs
move (100) steps
turn cw (mirror angle) degrees
wait (1) secs
move (100) steps
turn ccw (mirror angle) degrees
wait (1) secs
move (100) steps
turn ccw (mirror angle) degrees
wait (1) secs
move (200) steps
turn ccw (mirror angle) degrees
wait (1) secs
move (100) steps
wait (1) secs
pen up
```