```scratch
when green flag clicked
ask [Please enter a number between 0 and 31:] and wait
set [number v] to (answer)
set [bit value v] to [32]
set [cards v] to []
repeat until <(bit value) = [1]>
  set [bit value v] to ((bit value) / (2))
  if <<(number) > (bit value)> or <(number) = (bit value)>> then
    set [cards v] to (join (cards) [W])
    set [number v] to ((number) - (bit value))
  else
    set [cards v] to (join (cards) [B])
  end
end
say (join (join (join [The binary representation for the number ] (answer)) [ is ]) (cards))
```