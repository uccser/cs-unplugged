```scratch
when green flag clicked
clear
go to x: (0) y: (0)
say [I'll draw a polygon with the number of sides you give me.] for (3) secs
ask [Enter the number of sides:] and wait
set [sides v] to (answer)
pen down
repeat (sides)
  move (50) steps
  turn cw ((360) / (sides)) degrees
end
pen up
```