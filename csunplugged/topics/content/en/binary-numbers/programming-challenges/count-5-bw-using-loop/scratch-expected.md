Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424135/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked

repeat (5)
end

say (total number of dots)

ask [Please enter a black or white card ('B' for black or 'W' for white):] and wait

if <(answer) = [W]> then
end
```

```scratch:split:random
set [number of dots v] to ((number of dots) / (2))

set [total number of dots v] to ((total number of dots) + (number of dots))

set [number of dots v] to [16]

set [total number of dots v] to [0]
```

{panel end}
