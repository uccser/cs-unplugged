{panel type="general" title="Solution 1"}

```scratch
when green flag clicked
say [There are 8 planets in the Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.] for (5) secs
ask [Name a planet:] and wait
set [planet v] to (answer)
if <(planet) = [mercury]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
else
  if <(planet) = [venus]> then
    say (join (join [You are correct! ] (planet)) [ is a planet.])
  else
    if <(planet) = [earth]> then
      say (join (join [You are correct! ] (planet)) [ is a planet.])
    else
      if <(planet) = [mars]> then
        say (join (join [You are correct! ] (planet)) [ is a planet.])
      else
        if <(planet) = [jupiter]> then
          say (join (join [You are correct! ] (planet)) [ is a planet.])
        else
          if <(planet) = [saturn]> then
            say (join (join [You are correct! ] (planet)) [ is a planet.])
          else
            if <(planet) = [uranus]> then
              say (join (join [You are correct! ] (planet)) [ is a planet.])
            else
              if <(planet) = [neptune]> then
                say (join (join [You are correct! ] (planet)) [ is a planet.])
              else
                say (join (planet) [ is not a planet!])
              end
            end
          end
        end
      end
    end
  end
end
```

{panel end}

{panel type="general" title="Solution 2"}

```scratch
when green flag clicked
set [is found v] to [false]
say [There are 8 planets in the Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune.] for (5) secs
ask [Name a planet:] and wait
set [planet v] to (answer)
if <(planet) = [mercury]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
  set [is found v] to [true]
end
if <(planet) = [venus]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
  set [is found v] to [true]
end
if <(planet) = [earth]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
  set [is found v] to [true]
end
if <(planet) = [mars]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
  set [is found v] to [true]
end
if <(planet) = [jupiter]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
  set [is found v] to [true]
end
if <(planet) = [saturn]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
  set [is found v] to [true]
end
if <(planet) = [uranus]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
  set [is found v] to [true]
end
if <(planet) = [neptune]> then
  say (join (join [You are correct! ] (planet)) [ is a planet.])
  set [is found v] to [true]
end
if <(is found) = [false]> then
  say (join (planet) [ is not a planet!])
end
```

{panel end}
