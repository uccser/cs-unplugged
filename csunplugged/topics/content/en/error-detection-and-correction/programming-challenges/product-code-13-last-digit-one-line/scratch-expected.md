Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476672/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Enter first 12 digits of the barcode:] and wait
```

```scratch
repeat (6)
end

if <(length of (first 12 digits)) = [12]> then
else
end
```

```scratch
say [You must enter a 12 digit number!]

say (join [The last digit of the product code is: ] (last digit))
```

```scratch
set [index v] to [1]

set [first 12 digits v] to [0]

set [total 1 v] to [0]

set [total 2 v] to [0]

set [last digit v] to [0]

set [last digit v] to (((0) - ((total 1) + ((total 2) * (3)))) mod (10))

set [first 12 digits v] to (answer)

set [total 1 v] to ((total 1) + (letter (index) of (first 12 digits)))

change [index v] by (1)

set [total 2 v] to ((total 2) + (letter (index) of (first 12 digits)))

change [index v] by (1)
```

{panel end}
