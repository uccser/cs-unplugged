Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429925/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [coin v] to [0]

set [number of heads v] to [0]

set [number of tails v] to [0]

set [coin v] to (pick random (1) to (2))

change [number of heads v] by (1)

change [number of tails v] by (1)

set [number of flips v] to (answer)
```

```scratch
ask [How many times would you like to flip a coin?] and wait
```

```scratch
say (join (round (((number of heads) * (100)) / (number of flips))) [% heads]) for (3) secs

say (join (round (((number of tails) * (100)) / (number of flips))) [% tail]) for (3) secs
```

```scratch
if <(coin) = [1]> then
else
end

repeat (number of flips)
end
```

{panel end}
