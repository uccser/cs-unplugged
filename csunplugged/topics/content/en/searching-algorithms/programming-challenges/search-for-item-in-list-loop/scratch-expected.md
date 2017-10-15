Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148478378/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked

delete (all v) of [planets v]

say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])

ask [Name a planet:] and wait

if <(item (index) of [planets v] :: list) = (key)> then
end

change [index v] by (1)

repeat (8)
end
```

```scratch:split:random
set [index v] to [1]

set [key v] to (answer)
```

{panel end}
