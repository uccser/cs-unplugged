Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149428874/?autostart=false"}

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
ask [Enter a number:] and wait

ask (join [Enter a number to check if it's a divisor of the number ] (number1)) and wait
```

```scratch
say (join (join (number2) [ is a divisor of the number ]) (number1)) for (3) secs

say (join (join (number2) [ is not a divisor of the number ]) (number1)) for (3) secs
```

```scratch
forever
end

if <((number1) mod (number2)) = [0]> then
else
end
```

{panel end}
