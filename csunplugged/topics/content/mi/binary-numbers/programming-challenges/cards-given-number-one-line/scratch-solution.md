```scratch
when green flag clicked
ask [Please enter a number of dots less than or equal to 31:] and wait
set [number of dots v] to (answer)
set [cards v] to []
if <<(number of dots) < [31]> or <(number of dots) = [31]>> then
  if <<(number of dots) > [16]> or <(number of dots) = [16]>> then
    set [cards v] to (join (cards) [16, ])
    set [number of dots v] to ((number of dots) - (16))
  end
  if <<(number of dots) > [8]> or <(number of dots) = [8]>> then
    set [cards v] to (join (cards) [8, ])
    set [number of dots v] to ((number of dots) - (8))
  end
  if <<(number of dots) > [4]> or <(number of dots) = [4]>> then
    set [cards v] to (join (cards) [4, ])
    set [number of dots v] to ((number of dots) - (4))
  end
  if <<(number of dots) > [2]> or <(number of dots) = [2]>> then
    set [cards v] to (join (cards) [2, ])
    set [number of dots v] to ((number of dots) - (2))
  end
  if <<(number of dots) > [1]> or <(number of dots) = [1]>> then
    set [cards v] to (join (cards) [1, ])
    set [number of dots v] to ((number of dots) - (1))
  end
  say (cards)
else
  say [Please choose a number less than or equal to 31.]
end
```