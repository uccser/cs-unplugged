Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/158861343/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter a decimal number between 0 and 31:] and wait
```

```scratch
repeat until <(bit value) = [1]>
end

if <<(decimal number) > (bit value)> or <(decimal number) = (bit value)>> then
else
end
```

```scratch
play note (72 v) for (0.5) beats

play note (48 v) for (0.5) beats
```

```scratch
set [decimal number v] to (answer)

set [bit value v] to [32]

set [bit value v] to ((bit value) / (2))

set [decimal number v] to ((decimal number) - (bit value))
```

{panel end}
