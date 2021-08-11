Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424247/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter a decimal number:] and wait

say (join (join (join [The binary representation for the number ] (answer)) [ is ]) (cards))
```

```scratch
repeat until <(number) < (bit value)>
end

if <<(number) > (bit value)> or <(number) = (bit value)>> then
else
end

repeat until <(bit value) = [1]>
end
```

```scratch
set [number v] to (answer)

set [bit value v] to [1]

set [cards v] to []

set [bit value v] to ((bit value) * (2))

set [bit value v] to ((bit value) / (2))

set [cards v] to (join (cards) [W])

set [number v] to ((number) - (bit value))

set [cards v] to (join (cards) [B])
```

{panel end}
