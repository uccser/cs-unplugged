```scratch
when green flag clicked
say [There are 8 planets in the Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.] for (10) secs
ask [Name a planet:] and wait
set [planet v] to (answer)
if <(planet) = [mercury]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
end
if <(planet) = [venus]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
end
if <(planet) = [earth]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
end
if <(planet) = [mars]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
end
if <(planet) = [jupiter]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
end
if <(planet) = [saturn]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
end
if <(planet) = [uranus]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
end
if <(planet) = [neptune]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
end
if <(planet) = [pluto]> then
  say (join (planet) [ is no longer a planet!])
end
```
