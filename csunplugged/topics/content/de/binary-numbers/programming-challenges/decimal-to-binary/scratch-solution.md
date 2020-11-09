```scratch
when green flag clicked
ask [Please enter a decimal number:] and wait
set [decimal number v] to (answer)
set [bit value v] to [1]
set [binary number v] to []
repeat until <(decimal number) < (bit value)>
  set [bit value v] to ((bit value) * (2))
end
repeat until <(bit value) = [1]>
  set [bit value v] to ((bit value) / (2))
  if <<(decimal number) > (bit value)> or <(decimal number) = (bit value)>> then
    set [binary number v] to (join (binary number) [1])
    set [decimal number v] to ((decimal number) - (bit value))
  else
    set [binary number v] to (join (binary number) [0])
  end
end
say (join (join (join [The binary representation for the number ] (answer)) [ is ]) (binary number))
```