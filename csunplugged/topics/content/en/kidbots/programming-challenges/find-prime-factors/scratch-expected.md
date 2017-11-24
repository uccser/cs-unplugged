Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429841/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [prime factors v] to []

set [number v] to (answer)

set [divisor v] to (number)

set [index v] to [2]

set [is prime v] to [true]

set [is prime v] to [false]

set [prime factors v] to (join (number) (join [, ] (prime factors)))

change [divisor v] by (-1)

change [index v] by (1)
```

```scratch:split:random
ask [What's the number you want to find prime factors of?] and wait
```

```scratch:split:random
say (prime factors)
```

```scratch:split:random
if <((number) mod (divisor)) = [0]> then
end

if <(number) > [1]> then
end

if <((number) mod (index)) = [0]> then
end

if <(is prime) = [true]> then
end

repeat until <(divisor) = [0]>
end

repeat until <<(is prime) = [false]> or <(index) = (number)>>
end
```

```scratch:split:random
define check_prime (number)

check_prime (divisor) :: custom
```

{panel end}
