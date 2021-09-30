Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149427587/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [num1 v] to (answer)

set [num2 v] to (answer)

set [ten minus num1 v] to ((10) - (num1))

set [left from num2 v] to ((num2) - (ten minus num1))
```

```scratch
ask [Enter the 1st number:] and wait

ask [Enter the 2nd number:] and wait
```

```scratch
say [Enter two numbers less than 10. Enter the larger number first.] for (3) secs

say (join (join (join (num1) [+]) (num2)) [=?]) for (3) secs

say (join (join (join (join (join (join (join [To make ] (num1)) [ a tidy number I am splitting ]) (num2)) [ into a ]) (ten minus num1)) [ and a ]) (left from num2)) for (5) secs

say (join (join [(] (join (join (num1) [+]) (join (join (join (ten minus num1) [)]) [+]) (left from num2)))) [=]) for (5) secs

say (join [] ((num1) + (num2)))

say (join (join (join (num1) [+]) (num2)) [=?]) for (5) secs

say ((num1) + (num2))
```

```scratch
if <((num1) + (num2)) > [10]> then
else
end
```

{panel end}
