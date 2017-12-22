Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429011/?autostart=false"}

{panel type="help" title="Recommended blocks for solution 1"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
ask [What's the number you want to find factors of?] and wait
```

```scratch:split:random
set [factors v] to []

set [number v] to (answer)

set [divisor v] to [1]

set [factors v] to (join (factors) (join (divisor) [, ]))

change [divisor v] by (1)
```

```scratch:split:random
say (factors)
```

```scratch:split:random
repeat until <(divisor) > (number)>
end

if <((number) mod (divisor)) = [0]> then
end
```

{panel end}

{panel type="help" title="Recommended blocks for solution 2"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
ask [What's the number you want to find factors of?] and wait
```

```scratch:split:random
set [factors v] to []

set [number v] to (answer)

set [divisor v] to (number)

set [factors v] to (join (divisor) (join [, ] (factors)))

change [divisor v] by (-1)
```

```scratch:split:random
say (factors)
```

```scratch:split:random
repeat until <(divisor) = [0]>
end

if <((number) mod (divisor)) = [0]> then
end
```

{panel end}
