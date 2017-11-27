```scratch
when green flag clicked
set [result v] to [1]
ask [Enter an integer for the base:] and wait
set [base v] to (answer)
ask [Enter a positve integer for the power:] and wait
set [power v] to (answer)
repeat (power)
  set [result v] to ((result) * (base))
end
say (join (join (join (join (base) [^]) (power)) [ = ]) (result))
```