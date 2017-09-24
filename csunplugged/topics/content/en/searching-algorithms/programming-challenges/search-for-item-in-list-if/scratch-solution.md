```scratch
when green flag clicked
delete (all v) of [planets v]
add [Mercury] to [planets v]
add [Venus] to [planets v]
add [Earth] to [planets v]
add [Mars] to [planets v]
add [Jupiter] to [planets v]
add [Saturn] to [planets v]
add [Uranus] to [planets v]
add [Neptune] to [planets v]
set [index v] to [1]
ask [Name a planet:] and wait
set [key v] to (answer)
if <(item (1 v) of [planets v] :: list) = (key)> then
  say (join (join (join (key) [ is a planet and it was found at the index  ]) (index)) [ of the "planets" list.])
end
change [index v] by (1)
if <(item (2 v) of [planets v] :: list) = (key)> then
  say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])
end
change [index v] by (1)
if <(item (3 v) of [planets v] :: list) = (key)> then
  say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])
end
change [index v] by (1)
if <(item (4 v) of [planets v] :: list) = (key)> then
  say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])
end
change [index v] by (1)
if <(item (5 v) of [planets v] :: list) = (key)> then
  say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])
end
change [index v] by (1)
if <(item (6 v) of [planets v] :: list) = (key)> then
  say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])
end
change [index v] by (1)
if <(item (7 v) of [planets v] :: list) = (key)> then
  say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])
end
change [index v] by (1)
if <(item (8 v) of [planets v] :: list) = (key)> then
  say (join (join (join (key) [ is a planet and it was found at the index ]) (index)) [ of the "planets" list.])
end
```
