```scratch
when green flag clicked
ask [Please enter a number of dots less than or equal to 31:] and wait
set [number of dots v] to (answer)
if <<(number of dots) < [31]> or <(number of dots) = [31]>> then
  if <<(number of dots) > [16]> or <(number of dots) = [16]>> then
    set [number of dots v] to ((number of dots) - (16))
    say [16] for (1) secs
  end
  if <<(number of dots) > [8]> or <(number of dots) = [8]>> then
    set [number of dots v] to ((number of dots) - (8))
    say [8] for (1) secs
  end
  if <<(number of dots) > [4]> or <(number of dots) = [4]>> then
    set [number of dots v] to ((number of dots) - (4))
    say [4] for (1) secs
  end
  if <<(number of dots) > [2]> or <(number of dots) = [2]>> then
    set [number of dots v] to ((number of dots) - (2))
    say [2] for (1) secs
  end
  if <<(number of dots) > [1]> or <(number of dots) = [1]>> then
    set [number of dots v] to ((number of dots) - (1))
    say [1] for (1) secs
  end
else
  say [Please choose a number less than or equal to 31.]
end
```