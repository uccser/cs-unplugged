```scratch
when green flag clicked
set [coin v] to [0]
set [number of heads v] to [0]
set [number of tails v] to [0]
ask [How many times would you like to flip a coin?] and wait
set [number of flips v] to (answer)
repeat (number of flips)
  set [coin v] to (pick random (1) to (2))
  if <(coin) = [1]> then
    change [number of heads v] by (1)
  else
    change [number of tails v] by (1)
  end
end
say (join (round (((number of heads) * (100)) / (number of flips))) [% heads]) for (3) secs
say (join (round (((number of tails) * (100)) / (number of flips))) [% tail]) for (3) secs
```