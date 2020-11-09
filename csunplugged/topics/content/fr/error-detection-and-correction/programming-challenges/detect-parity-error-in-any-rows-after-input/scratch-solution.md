```scratch
when green flag clicked
delete (all v) of [rows v]
set [black cards total v] to [0]
set [row number v] to [1]
ask [How many rows would you like to enter?] and wait
set [number of rows v] to (answer)
repeat (number of rows)
  ask (join [Enter row ] (row number)) and wait
  add (answer) to [rows v]
  change [row number v] by (1)
end
set [index row v] to [1]
repeat (length of [rows v] :: list)
  set [index v] to [1]
  repeat (length of (item (index row) of [rows v] :: list))
    if <(letter (index) of (item (index row) of [rows v] :: list)) = [B]> then
      change [black cards total v] by (1)
    end
    change [index v] by (1)
  end
  if <((black cards total) mod (2)) = [1]> then
    say (join [There is a parity error in row ] (index row)) for (3) secs
  end
  set [black cards total v] to [0]
  change [index row v] by (1)
end
```