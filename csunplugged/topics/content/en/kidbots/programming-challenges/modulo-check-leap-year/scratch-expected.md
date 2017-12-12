Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165754830/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [year v] to (answer)
```

```scratch:split:random
ask [Enter the year and I will tell you if it's a leap year or not:] and wait
```

```scratch:split:random
say (join (year) [ is not a leap year!])

say (join (year) [ is a leap year!])

say (join (year) [ is not a leap year!])

say (join (year) [ is a leap year!])
```

```scratch:split:random
if <not <((year) mod (4)) = [0]>> then
else
end

if <not <((year) mod (100)) = [0]>> then
else
end

if <not <((year) mod (400)) = [0]>> then
else
end
```

{panel end}
