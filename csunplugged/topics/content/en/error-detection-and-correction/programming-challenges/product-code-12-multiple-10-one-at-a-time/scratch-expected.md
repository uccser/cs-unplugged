Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476891/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

say (join [Total: ] (total))
```


```scratch
repeat (6)
end
```

```scratch
ask (join (join [Enter digit ] (counter)) [ of the product code:]) and wait

ask (join (join [Enter digit ] (counter)) [ of the product code:]) and wait
```

```scratch
set [total 1 v] to [0]

set [total 2 v] to [0]

set [counter v] to [1]

change [counter v] by (1)

change [total 1 v] by (answer)

change [counter v] by (1)

change [total 2 v] by (answer)

set [total v] to (((total 1) * (3)) + (total 2))
```

{panel end}
