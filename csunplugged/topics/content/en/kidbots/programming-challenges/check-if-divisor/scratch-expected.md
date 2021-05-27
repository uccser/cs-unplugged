Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149428777/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [number1 v] to (answer)

set [number2 v] to (answer)
```

```scratch
ask [Enter the 1st number:] and wait

ask [Enter the 2nd number:] and wait
```

```scratch
say [Enter 2 numbers and I'll tell you if the second number is a divisor of the first number.] for (5) secs

say (join (join (number2) [ is a divisor of the number ]) (number1))

say (join (join (number2) [ is not a divisor of the number ]) (number1))
```

```scratch
if <((number1) mod (number2)) = [0]> then
else
end
```

{panel end}
