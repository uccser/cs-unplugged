```scratch
when green flag clicked
clear
go to x: (0) y: (0)
pen down
ask [Enter an odd number of points to draw a star:] and wait
set [points v] to (answer)
repeat (points)
  move (200) steps
  turn cw ((180) - ((180) / (points))) degrees
end
pen up
```