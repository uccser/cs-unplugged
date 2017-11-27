```scratch
when green flag clicked
set [row v] to []
set [black cards total v] to [0]
set [row number v] to [1]
repeat (6)
  ask (join [Please enter 6 black or white cards for row ] (row number)) and wait
  set [row v] to (answer)
  set [index v] to [1]
  repeat (6)
    if <(letter (index) of (row)) = [B]> then
      change [black cards total v] by (1)
    end
    change [index v] by (1)
  end
  if <((black cards total) mod (2)) = [0]> then
    say (join (join [Row ] (row number)) [ is OK!]) for (2) secs
  else
    say (join [There is a parity error in row ] (row number)) for (2) secs
  end
  change [row number v] by (1)
  set [black cards total v] to [0]
end
```