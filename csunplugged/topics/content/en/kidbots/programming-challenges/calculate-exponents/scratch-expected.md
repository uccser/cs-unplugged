Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149428305/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [result v] to [1]

set [base v] to (answer)

set [power v] to (answer)

set [result v] to ((result) * (base))
```

```scratch
ask [Enter an integer for the base:] and wait

ask [Enter a positve integer for the power:] and wait
```

```scratch
say (join (join (join (join (base) [^]) (power)) [ = ]) (result))
```

```scratch
repeat (power)
end
```

{panel end}
