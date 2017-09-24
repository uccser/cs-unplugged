Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148478123/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked

ask [Name a planet:] and wait

set [planet v] to (answer)
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

if <(planet) = [pluto]> then
end
```

```scratch:split:random
say [There are 8 planets in the Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.] for (10) secs

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (join [You are correct! ] (planet)) [ is a planet.])

say (join (planet) [ is no longer a planet!])
```

{panel end}
