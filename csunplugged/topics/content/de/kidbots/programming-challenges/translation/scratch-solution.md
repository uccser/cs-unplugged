```scratch
when green flag clicked
set [sides v] to [50]
clear
go to x: (-180) y: (-50)
set pen size to (3)
repeat (6)
  pen down
  point in direction (0 v)
  repeat (2)
    move (sides) steps
    turn ccw (45) degrees
    move (sides) steps
    turn ccw ((180) - (45)) degrees
  end
  repeat (2)
    move (sides) steps
    turn cw (45) degrees
    move (sides) steps
    turn cw ((180) - (45)) degrees
  end
  move (sides) steps
  turn cw (45) degrees
  repeat (2)
    move (sides) steps
    turn ccw (90) degrees
    move (sides) steps
    turn ccw ((180) - (90)) degrees
  end
  pen up
  point in direction (90 v)
  move ([sqrt v] of (((sides) * (sides)) + ((sides) * (sides)))) steps
  point in direction (180 v)
  move (sides) steps
end
```