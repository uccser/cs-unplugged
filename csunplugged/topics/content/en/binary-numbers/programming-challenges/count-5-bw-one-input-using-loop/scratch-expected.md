Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424160/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter 5 cards (B for black and W for white):] and wait

repeat (5)
end

if <(letter (index) of (cards)) = [W]> then
end

change [index v] by (1)

say (total number of dots)
```

```scratch
set [total number of dots v] to [0]

set [index v] to [1]

set [number of dots v] to [16]

set [cards v] to (answer)

set [total number of dots v] to ((total number of dots) + (number of dots))

set [number of dots v] to ((number of dots) / (2))
```

{panel end}
