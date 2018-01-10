Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426073/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch:split:random
when green flag clicked

ask [Enter a number:] and wait

change [number v] by (-2)
```

```scratch:split:random
if <(number) < [0]> then
end

repeat until <<(number) = [0]> or <(number) = [1]>>
end

if <(number) = [0]> then
end

if <(number) = [1]> then
end
```

```scratch:split:random
say [You entered an odd number!]

say [You entered an even number!]
```

```scratch:split:random
set [number v] to [0]

set [number v] to (answer)

set [number v] to ((-1) * (number))
```

{panel end}
