**Solution #1:**

```scratch
when green flag clicked
clear
set pen size to (3)
go to x: (0) y: (0)
point in direction (90 v)
ask [Enter an angle between 0 and 360 (not including 0 and 360):] and wait
set [angle v] to (answer)
if <<(angle) > [0]> and <(angle) < [90]>> then
  say [The angle you entered is an acute angle.] for (3) secs
end
if <(angle) = [90]> then
  say [The angle you entered is a right angle.] for (3) secs
end
if <<(angle) > [90]> and <(angle) < [180]>> then
  say [The angle you entered is an obtuse angle.] for (3) secs
end
if <(angle) = [180]> then
  say [The angle you entered is a straight angle.] for (3) secs
end
if <(angle) > [180]> then
  say [The angle you entered is a reflex angle.] for (3) secs
end
pen down
move (100) steps
turn ccw ((180) - (angle)) degrees
move (100) steps
pen up
```

**Solution #2:**

```scratch
when green flag clicked
clear
set pen size to (3)
go to x: (0) y: (0)
point in direction (90 v)
ask [Enter an angle between 0 and 360 (not including 0 and 360):] and wait
set [angle v] to (answer)
if <(angle) < [180]> then
  if <(angle) < [90]> then
    say [The angle you entered is an acute angle.] for (3) secs
  else
    if <(angle) = [90]> then
      say [The angle you entered is a right angle.] for (3) secs
    else
      say [The angle you entered is an obtuse angle.] for (3) secs
    end
  end
else
  if <(angle) = [180]> then
    say [The angle you entered is a straight angle.] for (3) secs
  else
    say [The angle you entered is a reflex angle.] for (3) secs
  end
end
pen down
move (100) steps
turn ccw ((180) - (angle)) degrees
move (100) steps
pen up
```