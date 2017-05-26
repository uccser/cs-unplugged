Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148423886/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
set [number of dots v] to [1]

set [binary cards v] to []

set [binary cards v] to ((join (binary cards) (join (number of dots) [, ])))

set [number of dots v] to ((number of dots) * (2))
```

```scratch:split:random
when green flag clicked

say (binary cards)

repeat (5)
end
```

{panel end}
