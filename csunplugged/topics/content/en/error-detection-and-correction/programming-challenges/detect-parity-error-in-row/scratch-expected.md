Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426097/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter a row of black and white cards (B for black and W for white):] and wait
```


```scratch
if <(letter (index) of (cards)) = [B]> then
end

repeat (length of (cards))
end

if <((black cards total) mod (2)) = [0]> then
else
end
```

```scratch
say [There is no parity error in this row!]

say [There is a parity error in this row!]
```

```scratch
change [black cards total v] by (1)

change [index v] by (1)
```

```scratch
set [black cards total v] to [0]

set [index v] to [1]

set [cards v] to (answer)
```

{panel end}
