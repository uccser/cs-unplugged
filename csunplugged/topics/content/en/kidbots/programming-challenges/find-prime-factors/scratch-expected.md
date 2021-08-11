Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429841/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
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

```scratch
ask [What's the number you want to find prime factors of?] and wait
```

```scratch
say (prime factors)
```

```scratch
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

```scratch
define check_prime (number)

check_prime (divisor) :: custom
```

{panel end}
