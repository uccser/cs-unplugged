Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149428180/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [upper range v] to (answer)

set [number v] to (pick random (1) to (upper range))

set [numbers after v] to (item (random v) of [numbers after list v] :: list)
```

```scratch:split:random
ask [Enter a number as the upper range:] and wait

ask (join (join [What is the number after ] (number)) [?]) and wait

ask (join (join (join (join [What's ] (numbers after)) [ numbers after ]) (number)) [?]) and wait
```

```scratch:split:random
say [Well done!] for (3) secs

say (join [Nice try! The right answer is: ] ((number) + (numbers after))) for (3) secs
```

```scratch:split:random
forever
end

if <(numbers after) = [1]> then
else
end

if <(answer) = ((number) + (numbers after))> then 
else
end
```

{panel end}
