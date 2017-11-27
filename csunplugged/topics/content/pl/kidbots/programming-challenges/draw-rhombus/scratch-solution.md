```scratch
when green flag clicked
clear
pen down
set pen size to (3)
ask [Enter one angle of a rhombus:] and wait
set [angle v] to (answer)
repeat (2)
  move (100) steps
  turn ccw (angle) degrees
  move (100) steps
  turn ccw ((180) - (angle)) degrees
end
pen up
```