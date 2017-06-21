Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149428305/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [result v] to [1]

set [base v] to (answer)

set [power v] to (answer)

set [result v] to ((result) * (base))
```

```scratch:split:random
ask [Enter an integer for the base:] and wait

ask [Enter a positve integer for the power:] and wait
```

```scratch:split:random
say (join (join (join (join (base) [^]) (power)) [ = ]) (result))
```

```scratch:split:random
repeat (power)
end
```

{panel end}
