Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/158861213/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked

ask [Please enter a decimal number:] and wait
```

```scratch:split:random
play note (72 v) for (0.5) beats

play note (48 v) for (0.5) beats
```

```scratch:split:random
repeat until <(decimal number) < (bit value)>
end

repeat until <(bit value) = [1]>
end

if <<(decimal number) > (bit value)> or <(decimal number) = (bit value)>> then
else
end
```

```scratch:split:random
set [decimal number v] to (answer)

set [bit value v] to [1]

set [bit value v] to ((bit value) * (2))

set [bit value v] to ((bit value) / (2))

set [decimal number v] to ((decimal number) - (bit value))
```

{panel end}
