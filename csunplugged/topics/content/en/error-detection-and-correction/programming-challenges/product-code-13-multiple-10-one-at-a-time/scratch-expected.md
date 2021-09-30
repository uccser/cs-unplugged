Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476573/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
say [The sum is NOT a multiple of 10]

say [The sum is a multiple of 10]
```

```scratch
ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait

ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait

ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
```

```scratch
repeat (6)
end

if <((total) mod (10)) = [0]> then
else
end
```

```scratch
set [odd total v] to [0]

set [even total v] to [0]

set [index v] to [1]

change [odd total v] by (answer)

set [total v] to ((odd total) + ((even total) * (3)))

change [index v] by (1)

change [odd total v] by (answer)

change [index v] by (1)

change [even total v] by (answer)
```

{panel end}
