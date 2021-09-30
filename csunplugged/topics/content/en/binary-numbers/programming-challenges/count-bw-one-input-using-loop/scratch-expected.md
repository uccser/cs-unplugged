Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424178/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter a sequence of cards ('B' for black and 'W' for white):] and wait

if <(letter (index) of (cards)) = [W]> then
end

repeat (length of (cards))
end

say (total number of dots)
```


```scratch
set [total number of dots v] to [0]

set [number of dots v] to [1]

set [cards v] to (answer)

set [index v] to (length of (cards))

set [total number of dots v] to ((total number of dots) + (number of dots))

set [number of dots v] to ((number of dots) * (2))

set [index v] to ((index) - (1))
```

{panel end}
