**Solution #1:**

```scratch
when green flag clicked
clear
go to x: (0) y: (0)
set pen size to (3)
point in direction (90 v)
pen down
repeat (4)
  move (100) steps
  turn cw (90) degrees
end
repeat (2)
  move (100) steps
  turn ccw ((180) - (45)) degrees
  move (50) steps
  turn ccw (45) degrees
end
point in direction (180 v)
repeat (2)
  move (100) steps
  turn cw ((180) - (45)) degrees
  move (50) steps
  turn cw (45) degrees
end
pen up
```

**Solution #2:**

```scratch
when green flag clicked
clear
go to x: (0) y: (-100)
set pen size to (3)
point in direction (0 v)
pen down
repeat (2)
  move (100) steps
  turn ccw (45) degrees
  move (100) steps
  turn ccw ((180) - (45)) degrees
end
repeat (2)
  move (100) steps
  turn cw (45) degrees
  move (100) steps
  turn cw ((180) - (45)) degrees
end
move (100) steps
turn cw (45) degrees
repeat (2)
  move (100) steps
  turn ccw (90) degrees
  move (100) steps
  turn ccw ((180) - (90)) degrees
end
pen up
```