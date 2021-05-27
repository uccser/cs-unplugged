Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148477813/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

say (join [The last digit of the credit card should be: ] (((0) - ((total 2) + (total 1))) mod (10)))

ask [Enter the first 15 digits of the credit card:] and wait
```

```scratch
if <((letter (index) of (first 15 digits)) * (2)) < [10]> then
else
end

repeat (7)
end

repeat (8)
end
```

```scratch
set [index v] to [1]

set [first 15 digits v] to [0]

set [total 2 v] to [0]

set [total 1 v] to [0]

set [first 15 digits v] to (answer)

change [total 1 v] by ((letter (index) of (first 15 digits)) * (2))

change [index v] by (2)

change [total 1 v] by (((letter (index) of (first 15 digits)) * (2)) - (9))

change [index v] by (2)

set [index v] to [2]

change [total 2 v] by (letter (index) of (first 15 digits))

change [index v] by (2)
```

{panel end}
