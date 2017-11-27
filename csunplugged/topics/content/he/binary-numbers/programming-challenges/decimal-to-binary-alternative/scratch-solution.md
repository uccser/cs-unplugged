```scratch
when green flag clicked
ask [Please enter a decimal number:] and wait
set [decimal number v] to (answer)
set [remainder v] to [0]
set [binary number v] to []
repeat until <(decimal number) = [1]>
  set [remainder v] to ((decimal number) mod (2))
  set [decimal number v] to ([floor v] of ((decimal number) / (2)))
  set [binary number v] to (join (remainder) (binary number))
end
set [binary number v] to (join (decimal number) (binary number))
say (join (join (join [The binary representation for the number ] (answer)) [ is ]) (binary number))
```