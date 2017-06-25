Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149427673/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [num1 v] to (answer)

set [num2 v] to (answer)

set [add to tidy num1 v] to ((10) - ((num1) mod (10)))

set [left from num2 v] to ((num2) - (add to tidy num1))
```

```scratch:split:random
ask [Enter a number less than 100:] and wait

ask [Enter a number less than 10:] and wait

ask (join [Now can you work out the answer to ] (join [(] (join (join (join (num1) [+]) (join (join (join (add to tidy num1) [)]) [+]) (left from num2))) [=]))) and wait

ask (join (join (join (num1) [+]) (num2)) [=?]) and wait
```

```scratch:split:random
say [Enter two numbers less than 10. Enter the larger number first.] for (3) secs

say (join (join (join (num1) [+]) (num2)) [=?]) for (5) secs

say (join (join (join (join (join (join (join [To make ] (num1)) [ a tidy number I am splitting ]) (num2)) [ into a ]) (add to tidy num1)) [ and a ]) (left from num2)) for (5) secs

say (join [(] (join (join (num1) [+]) (join (join (join (add to tidy num1) [)]) [+]) (left from num2)))) for (5) secs

say [Well done!]

say (join [Nice try! The correct answer is ] ((num1) + (num2)))

say [Well done!]

say (join [Nice try! The correct answer is ] ((num1) + (num2)))
```

```scratch:split:random
if <((num1) + (num2)) > [10]> then
else
end

if <(answer) = ((num1) + (num2))> then
else
end

if <(answer) = ((num1) + (num2))> then
else
end
```

{panel end}
