```scratch
when green flag clicked
clear
go to x: (0) y: (0)
point in direction (90 v)
set [pi v] to [3.1415]
set [radius v] to [50]
move (radius) steps
point in direction (0 v)
pen down
forever
  repeat (360)
    move ((((radius) * (2)) * (pi)) / (360)) steps
    turn ccw (1) degrees
  end
  turn cw (15) degrees
  change pen color by (10)
end
```