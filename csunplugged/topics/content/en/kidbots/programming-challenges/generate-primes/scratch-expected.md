Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429772/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [prime numbers v] to [ ]

set [number v] to [2]

set [is prime v] to [true]

set [index v] to [2]

change [index v] by (1)

set [upper range v] to (answer)

set [prime numbers v] to (join (prime numbers) (join (number) [, ]))

change [number v] by (1)

set [is prime v] to [false]
```

```scratch
ask [I'll generate the prime numbers up to this number:] and wait
```

```scratch
say (prime numbers)
```

```scratch
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
