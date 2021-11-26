```scratch
when green flag clicked
ask [Please enter the number of dots:] and wait
set [total number of dots v] to (answer)
set [bits v] to [0]
set [bit value v] to [1]
repeat until <(total number of dots) < (bit value)>
  set [bit value v] to ((bit value) * (2))
  change [bits v] by (1)
end
say (join (join (join [You will need ] (bits)) [ bits to store number ]) (total number of dots))
```
