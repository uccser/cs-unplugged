Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148477875/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Enter an ISBN-10 number:] and wait
```

```scratch
say [This is a valid ISBN-10 number!]

say [This is an invalid ISBN-10 number!]
```

```scratch
change [total v] by ((multiplier) * (letter (index) of (ISBN-10 number)))

change [multiplier v] by (-1)

change [index v] by (1)

set [index v] to [1]

set [multiplier v] to [10]

set [total v] to [0]

change [total v] by ((multiplier) * (10))

set [ISBN-10 number v] to (answer)
```

```scratch
if <((total) mod (11)) = [0]> then
else
end

repeat (10)
end

if <<(index) = [10]> and <(letter (index) of (ISBN-10 number)) = [X]>> then
else
end
```

{panel end}
