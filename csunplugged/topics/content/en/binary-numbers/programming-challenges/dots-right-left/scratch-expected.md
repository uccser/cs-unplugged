Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148423954/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
set [binary cards v] to []

set [number of dots v] to [1]

set [number of cards v] to (answer)

set [binary cards v] to (join (binary cards) (join (number of dots) [, ]))

set [number of dots v] to ((number of dots) * (2))
```

```scratch
when green flag clicked

ask [How many cards would you like to display?] and wait

repeat (number of cards)
end

say (binary cards)
```

{panel end}
