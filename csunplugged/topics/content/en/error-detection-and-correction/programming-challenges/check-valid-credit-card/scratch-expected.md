Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148477751/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Enter a credit card number:] and wait
```


```scratch
repeat (8)
end

if <((letter (index) of (credit card number)) * (2)) < [10]> then
else
end

if <(((even total) + (odd total)) mod (10)) = [0]> then
else
end
```

```scratch
say [Invalid credit card number!]

say [Valid credit card number!]
```

```scratch
set [index v] to [1]

set [credit card number v] to [0]

set [even total v] to [0]

set [odd total v] to [0]

change [credit card number v] by (answer)

change [odd total v] by ((letter (index) of (credit card number)) * (2))

change [index v] by (1)

change [odd total v] by (((letter (index) of (credit card number)) * (2)) - (9))

change [index v] by (1)

change [even total v] by (letter (index) of (credit card number))

change [index v] by (1)
```

{panel end}
