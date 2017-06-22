Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429772/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [prime numbers v] to [ ]

set [index v] to [2]

set [number v] to [2]

set [upper range v] to (answer)

set [is prime v] to [true]

set [is prime v] to [false]

set [prime numbers v] to (join (prime numbers) (join (number) [, ]))

change [number v] by (1)
```

```scratch:split:random
ask [I'll generate the prime numbers up to this number:] and wait
```

```scratch:split:random
say (prime numbers)
```

```scratch:split:random
if <((number) mod (index)) = [0]> then
end

if <(is prime) = [true]> then
end

repeat ((upper range) - (1))
end

repeat until <<(index) = (number)> or <(is prime) = [false]>>
end
```

{panel end}
