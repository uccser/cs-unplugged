Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424217/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter a number of dots less than or equal to 31:] and wait
```

```scratch
if <<(number of dots) > [16]> or <(number of dots) = [16]>> then
end

if <<(number of dots) > [8]> or <(number of dots) = [8]>> then
end

if <<(number of dots) > [4]> or <(number of dots) = [4]>> then
end

if <<(number of dots) > [2]> or <(number of dots) = [2]>> then
end

if <<(number of dots) > [1]> or <(number of dots) = [1]>> then
end

if <<(number of dots) < [31]> or <(number of dots) = [31]>> then
else
end
```

```scratch
set [number of dots v] to (answer)

set [cards v] to []

set [cards v] to (join (cards) [16, ])

set [number of dots v] to ((number of dots) - (16))

set [cards v] to (join (cards) [8, ])

set [number of dots v] to ((number of dots) - (8))

set [cards v] to (join (cards) [4, ])

set [number of dots v] to ((number of dots) - (4))

set [cards v] to (join (cards) [2, ])

set [number of dots v] to ((number of dots) - (2))

set [cards v] to (join (cards) [1, ])

set [number of dots v] to ((number of dots) - (1))

```

```scratch
say (cards)

say [Please choose a number less than or equal to 31.]
```

{panel end}
