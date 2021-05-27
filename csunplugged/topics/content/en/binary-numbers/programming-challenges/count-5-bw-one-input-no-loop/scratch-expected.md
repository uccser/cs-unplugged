Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424155/?autostart=false"}


{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter 5 cards ('B' for black and 'W' for white):] and wait

say (total number of dots)
```

```scratch
if <(letter (1) of (cards)) = [W]> then
end

if <(letter (2) of (cards)) = [W]> then
end

if <(letter (3) of (cards)) = [W]> then
end

if <(letter (4) of (cards)) = [W]> then
end

if <(letter (5) of (cards)) = [W]> then
end
```

```scratch
set [total number of dots v] to [0]

set [cards v] to (answer)

set [total number of dots v] to ((total number of dots) + (16))

set [total number of dots v] to ((total number of dots) + (8))

set [total number of dots v] to ((total number of dots) + (4))

set [total number of dots v] to ((total number of dots) + (2))

set [total number of dots v] to ((total number of dots) + (1))
```

{panel end}
