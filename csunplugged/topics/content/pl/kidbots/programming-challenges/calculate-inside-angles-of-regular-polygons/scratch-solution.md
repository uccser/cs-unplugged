```scratch
when green flag clicked
clear
go to x: (0) y: (0)
point in direction (90 v)
ask [Enter the number of sides of a regular polygon:] and wait
set [sides v] to (answer)
set [turning angle v] to ((360) / (sides))
set [inside angle v] to ((180) - (turning angle))
pen down
repeat (sides)
  move (50) steps
  turn cw (turning angle) degrees
  wait (1) secs
end
pen up
say (join (join [Each inside angle is ] (inside angle)) [ degrees.])
```