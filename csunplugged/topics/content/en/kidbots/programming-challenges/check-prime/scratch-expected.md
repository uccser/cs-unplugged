Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429557/?autostart=false"}

{panel type="help" title="Recommended blocks for solution 1"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [divisor v] to [2]

set [number v] to (answer)

change [divisor v] by (1)
```

```scratch:split:random
ask [Enter a number to check if it's a prime number:] and wait
```

```scratch:split:random
say (join (number) [ is not a prime number.])

say (join (number) [ is not a prime number.])

say (join (number) [ is a prime number.])
```

```scratch:split:random
if <((number) mod (divisor)) = [0]> then
end

if <<(number) = [1]> or <(number) < [1]>> then
else
end

repeat until <(divisor) = (number)>
end

stop [this script v]
```

{panel end}

{panel type="help" title="Recommended blocks for solution 2"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [is prime v] to [true]

set [divisor v] to [2]

set [is prime v] to [false]

change [divisor v] by (1)

set [number v] to (answer)
```

```scratch:split:random
ask [Enter a number to check if it's a prime number:] and wait
```

```scratch:split:random
say (join (number) [ is not a prime number.])

say (join (number) [ is not a prime number.])

say (join (number) [ is a prime number.])
```

```scratch:split:random
if <(is prime) = [true]> then
end

if <((number) mod (divisor)) = [0]> then
end

repeat until <<(is prime) = [false]> or <(divisor) = (number)>>
end

if <<(number) = [1]> or <(number) < [1]>> then
else
end
```

{panel end}
