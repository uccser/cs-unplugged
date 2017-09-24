Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148478123/?autostart=false"}

{panel type="help" title="Recommended blocks" subtitle="Solution 1"}

```scratch:split:random
when green flag clicked

ask [Name a planet:] and wait

set [planet v] to (answer)
```

```scratch:split:random
if <(planet) = [mercury]> then
else
end

if <(planet) = [venus]> then
else
end

if <(planet) = [earth]> then
else
end

if <(planet) = [mars]> then
else
end

if <(planet) = [jupiter]> then
else
end

if <(planet) = [saturn]> then
else
end

if <(planet) = [uranus]> then
else
end

if <(planet) = [neptune]> then
else
end
```

```scratch:split:random
say [There are 8 planets in the Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.] for (5) secs

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (planet) [ is not a planet!])
```

{panel end}

{panel type="help" title="Recommended blocks" subtitle="Solution 2"}

```scratch:split:random
when green flag clicked

ask [Name a planet:] and wait
```

```scratch:split:random
if <(planet) = [mercury]> then
end

if <(planet) = [venus]> then
end

if <(planet) = [earth]> then
end

if <(planet) = [mars]> then
end

if <(planet) = [jupiter]> then
end

if <(planet) = [saturn]> then
end

if <(planet) = [uranus]> then
end

if <(planet) = [neptune]> then
end

if <(is found) = [false]> then
end
```

```scratch:split:random
set [is found v] to [false]

set [planet v] to (answer)

set [is found v] to [true]

set [is found v] to [true]

set [is found v] to [true]

set [is found v] to [true]

set [is found v] to [true]

set [is found v] to [true]

set [is found v] to [true]

set [is found v] to [true]
```

```scratch:split:random
say [There are 8 planets in the Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.] for (5) secs

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (planet) [ is not a planet!])
```

{panel end}
