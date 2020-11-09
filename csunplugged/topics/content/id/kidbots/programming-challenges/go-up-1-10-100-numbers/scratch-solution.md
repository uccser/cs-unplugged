```scratch
when green flag clicked
say [I'll generate a random number between 1 and a number you enter.] for (5) secs
ask [Enter a number as the upper range:] and wait
set [upper range v] to (answer)
forever
  set [number v] to (pick random (1) to (upper range))
  set [numbers after v] to (item (random v) of [numbers after list v] :: list)
  if <(numbers after) = [1]> then
    ask (join (join [What is the number after ] (number)) [?]) and wait
  else
    ask (join (join (join (join [What's ] (numbers after)) [ numbers after ]) (number)) [?]) and wait
  end
  if <(answer) = ((number) + (numbers after))> then
    say [Well done!] for (3) secs
  else
    say (join [Nice try! The right answer is: ] ((number) + (numbers after))) for (3) secs
  end
end
```