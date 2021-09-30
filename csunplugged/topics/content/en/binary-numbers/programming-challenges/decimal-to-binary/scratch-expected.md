Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424317/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter a decimal number:] and wait

say (join (join (join [The binary representation for the number ] (answer)) [ is ]) (binary number))
```

```scratch
if <<(decimal number) > (bit value)> or <(decimal number) = (bit value)>> then
else
end

repeat until <(decimal number) < (bit value)>
end

repeat until <(bit value) = [1]>
end
```

```scratch
set [decimal number v] to (answer)

set [bit value v] to [1]

set [binary number v] to []

set [bit value v] to ((bit value) * (2))

set [bit value v] to ((bit value) / (2))

set [binary number v] to (join (binary number) [1])

set [decimal number v] to ((decimal number) - (bit value))

set [binary number v] to (join (binary number) [0])
```

{panel end}
