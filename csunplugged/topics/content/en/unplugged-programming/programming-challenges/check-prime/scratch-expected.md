Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429557/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [is prime v] to [false]

set [is prime v] to [true]

set [divisor v] to [2]

set [number v] to (answer)

change [divisor v] by (1)
```

```scratch:split:random
ask [Enter a number to check if it's a prime number:] and wait
```

```scratch:split:random
say (join (number) [ is not a prime number.])

say (join (number) [ is a prime number.])
```

```scratch:split:random
stop [this script v]

if <<(number) = [1]> or <(number) < [1]>> then
else
end

if <<(number) = [1]> or <(number) < [1]>> then
end

if <((number) mod (divisor)) = [0]> then
end

repeat until <<(is prime) = [false]> or <(divisor) = (number)>>
end

repeat until <(divisor) = (number)>
end
```

{panel end}
