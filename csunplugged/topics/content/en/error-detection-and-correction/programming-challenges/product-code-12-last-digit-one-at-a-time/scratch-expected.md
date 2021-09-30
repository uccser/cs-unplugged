Click on the green flag, enter the inputs provided in the “testing examples” to
see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148477095/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

say (join [The last digit of the product code is ] (last digit))

repeat (5)
end
```


```scratch
ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait

ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait

ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
```

```scratch
set [total 1 v] to [0]

set [total 2 v] to [0]

set [index v] to [1]

set [last digit v] to [0]

change [index v] by (1)

change [total 1 v] by (answer)

change [index v] by (1)

change [total 2 v] by (answer)

change [index v] by (1)

change [total 1 v] by (answer)

set [last digit v] to (((0) - (((total 1) * (3)) + (total 2))) mod (10))
```

{panel end}
