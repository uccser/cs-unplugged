Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424337/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter a decimal number:] and wait

repeat until <(decimal number) = [1]>
end

say (join (join (join [The binary representation for the number ] (answer)) [ is ]) (binary number))
```

```scratch
set [decimal number v] to (answer)

set [remainder v] to [0]

set [binary number v] to []

set [remainder v] to ((decimal number) mod (2))

set [decimal number v] to ([floor v] of ((decimal number) / (2)))

set [binary number v] to (join (remainder) (binary number))

set [binary number v] to (join (decimal number) (binary number))
```

{panel end}
