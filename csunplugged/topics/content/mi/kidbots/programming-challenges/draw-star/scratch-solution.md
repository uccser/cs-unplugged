**Solution #1:**

```scratch
when green flag clicked
clear
go to x: (50) y: (0)
set pen size to (3)
set pen color to (0)
pen down
repeat (6)
  move (50) steps
  turn cw (120) degrees
  move (50) steps
  turn ccw (60) degrees
end
change pen color by (50)
repeat (6)
  turn cw (60) degrees
  move (50) steps
end
pen up
```

**Solution #2:**

```scratch
when green flag clicked
clear
set pen size to (3)
go to x: (50) y: (0)
point in direction (0 v)
repeat (6)
  triangle :: custom
  move (50) steps
  turn ccw (60) degrees
  change pen color by (30)
end

define triangle
pen down
repeat (3)
  turn ccw ((360) / (3)) degrees
  move (50) steps
end
pen up
```

**Solution #3:**

```scratch
when green flag clicked
clear
go to x: (0) y: (0)
set pen size to (3)
set pen color to (0)
point in direction (90 v)
pen down
repeat (3)
  move (150) steps
  turn ccw (120) degrees
end
pen up
go to x: (75) y: (-45)
turn ccw (120) degrees
change pen color by (50)
pen down
repeat (3)
  move (150) steps
  turn cw (120) degrees
end
pen up
```