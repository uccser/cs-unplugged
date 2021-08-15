Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424235/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Please enter the number of dots:] and wait

change [bits v] by (1)

repeat until <(total number of dots) < (bit value)>
end

say (join (join (join [You will need ] (bits)) [ bits to store number ]) (total number of dots))
```

```scratch
set [total number of dots v] to (answer)

set [bits v] to [0]

set [bit value v] to [1]

set [bit value v] to ((bit value) * (2))
```

{panel end}
