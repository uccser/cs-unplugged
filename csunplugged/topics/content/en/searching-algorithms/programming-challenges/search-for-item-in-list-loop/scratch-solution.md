```scratch
when green flag clicked
delete (all v) of [planets v]
add [mercury] to [planets v]
add [venus] to [planets v]
add [earth] to [planets v]
add [mars] to [planets v]
add [jupiter] to [planets v]
add [saturn] to [planets v]
add [uranus] to [planets v]
add [neptune] to [planets v]
set [index v] to [1]
ask [Name a planet:] and wait
set [key v] to (answer)
repeat (8)
  if <(item (index) of [planets v] :: list) = (key)> then
    say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])
  end
  change [index v] by (1)
end
```
