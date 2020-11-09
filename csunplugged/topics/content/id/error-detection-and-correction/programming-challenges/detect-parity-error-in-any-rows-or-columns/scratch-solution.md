```scratch
when green flag clicked
set [row number v] to [1]
set [error in row v] to [0]
set [error in column v] to [0]
delete (all v) of [cards v]
ask [How many rows would you like to enter?] and wait
set [number of rows v] to (answer)
repeat (number of rows)
  ask (join (join (join [Enter ] (number of rows)) [ cards for row ]) (row number)) and wait
  set [row v] to (answer)
  add (row) to [cards v]
  set [black cards total v] to [0]
  set [index v] to [1]
  repeat (length of (row))
    if <(letter (index) of (row)) = [B]> then
      change [black cards total v] by (1)
    end
    change [index v] by (1)
  end
  if <((black cards total) mod (2)) = [1]> then
    set [error in row v] to (row number)
  end
  change [row number v] by (1)
end
set [index v] to [1]
repeat (number of rows)
  set [black cards total v] to [0]
  set [row index v] to [1]
  repeat (number of rows)
    if <(letter (index) of (item (row index) of [cards v] :: list)) = [B]> then
      change [black cards total v] by (1)
    end
    change [row index v] by (1)
  end
  if <((black cards total) mod (2)) = [1]> then
    set [error in column v] to (index)
  end
  change [index v] by (1)
end
say (join (join (join [There is a parity error in row ] (error in row)) [ and column ]) (error in column))
```