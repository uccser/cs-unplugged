Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424005/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked

ask [Enter the largest number of dots on a card:] and wait

repeat until <(number of dots) = [1]>
end
```

```scratch:split:random
set [number of dots v] to (answer)

set [number of dots v] to ((number of dots) / (2))
```

```scratch:split
say (number of dots) for (1) secs

say (number of dots) for (1) secs
```

{panel end}
