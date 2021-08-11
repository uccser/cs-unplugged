Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148477141/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Enter first 11 digits of the product code:] and wait
```

```scratch
say (join [The last digit of the product code is: ] (last digit))

say [You must enter a 11 digit number!]
```

```scratch
repeat (5)
end

if <(length of (first 11 digits)) = [11]> then
else
end
```

```scratch
set [index v] to [1]

set [first 11 digits v] to [0]

set [total 1 v] to [0]

set [total 2 v] to [0]

set [last digit v] to [0]

set [total 1 v] to ((total 1) + (letter (index) of (first 11 digits)))

change [index v] by (1)

set [last digit v] to (((0) - (((total 1) * (3)) + (total 2))) mod (10))

set [total 1 v] to ((total 1) + (letter (index) of (first 11 digits)))

change [index v] by (1)

set [total 2 v] to ((total 2) + (letter (index) of (first 11 digits)))

change [index v] by (1)

set [first 11 digits v] to (answer)
```

{panel end}
