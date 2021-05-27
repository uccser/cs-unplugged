Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426115/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask (join [Please enter 6 black or white cards for row ] (row number)) and wait
```


```scratch
repeat (6)
end

repeat (6)
end

if <(letter (index) of (row)) = [B]> then
end

if <((black cards total) mod (2)) = [0]> then
else
end
```

```scratch
say (join (join [Row ] (row number)) [ is OK!]) for (2) secs

say (join [There is a parity error in row ] (row number)) for (2) secs
```

```scratch
set [row v] to []

set [black cards total v] to [0]

set [row number v] to [1]

change [row number v] by (1)

set [black cards total v] to [0]

change [index v] by (1)

change [black cards total v] by (1)

set [row v] to (answer)

set [index v] to [1]
```

{panel end}
