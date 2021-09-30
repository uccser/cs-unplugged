Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476604/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Enter a 13-digit product code:] and wait
```

```scratch
say [Please enter a 13 digit number!]

say [Invalid product code!]

say [Valid product code!]
```

```scratch
repeat (6)
end

if <((total) mod (10)) = [0]> then
else
end

if <(length of (product code)) = [13]> then
else

end
```

```scratch
set [index v] to [1]

set [product code v] to []

set [total 1 v] to [0]

set [total 2 v] to [0]

set [total v] to [0]

set [total 1 v] to ((total 1) + (letter (index) of (product code)))

set [total v] to ((total 1) + ((total 2) * (3)))

set [total 1 v] to ((total 1) + (letter (index) of (product code)))

change [index v] by (1)

set [total 2 v] to ((total 2) + (letter (index) of (product code)))

change [index v] by (1)

change [product code v] by (answer)
```

{panel end}
