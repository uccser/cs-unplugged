```scratch
when green flag clicked
set [black cards total v] to [0]
set [row number v] to [1]
ask [How many rows would you like to enter?] and wait
set [number of rows v] to (answer)
repeat (number of rows)
  set [index v] to [1]
  ask (join (join (join [Please enter ] (number of rows)) [ cards for row ]) (row number)) and wait
  set [row v] to (answer)
  repeat (length of (row))
    if <(letter (index) of (row)) = [B]> then
      change [black cards total v] by (1)
    end
    change [index v] by (1)
  end
  if <((black cards total) mod (2)) = [0]> then
    say (join (join [Row ] (row number)) [ is OK!]) for (2) secs
  else
    say (join [There is a parity error is row ] (row number)) for (2) secs
  end
  change [row number v] by (1)
  set [black cards total v] to [0]
end
```