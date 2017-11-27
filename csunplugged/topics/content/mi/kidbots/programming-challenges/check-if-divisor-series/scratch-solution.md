```scratch
when green flag clicked
ask [Enter a number:] and wait
set [number1 v] to (answer)
forever
  ask (join [Enter a number to check if it's a divisor of the number ] (number1)) and wait
  set [number2 v] to (answer)
  if <((number1) mod (number2)) = [0]> then
    say (join (join (number2) [ is a divisor of the number ]) (number1)) for (3) secs
  else
    say (join (join (number2) [ is not a divisor of the number ]) (number1)) for (3) secs
  end
end
```