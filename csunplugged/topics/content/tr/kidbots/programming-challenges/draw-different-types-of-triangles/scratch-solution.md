```scratch
when green flag clicked
clear
set pen size to (3)
go to x: (0) y: (0)
point in direction (90 v)
ask [Enter an angle between 0 and 180 (not including 0 and 180):] and wait
set [angle v] to (answer)
pen down
move (100) steps
turn ccw ((180) - (angle)) degrees
move (100) steps
go to x: (0) y: (0)
pen up
if <(angle) < [90]> then
  say [This is an acute triangle.] for (2) secs
end
if <(angle) = [90]> then
  say [This is a right triangle.] for (2) secs
end
if <(angle) > [90]> then
  say [This is an obtuse triangle.] for (2) secs
end
```