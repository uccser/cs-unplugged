Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165754830/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked
```

```scratch
set [year v] to (answer)
```

```scratch
ask [Enter the year and I will tell you if it's a leap year or not:] and wait
```

```scratch
say (join (year) [ is not a leap year!])

say (join (year) [ is a leap year!])

say (join (year) [ is not a leap year!])

say (join (year) [ is a leap year!])
```

```scratch
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
