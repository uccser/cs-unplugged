```scratch
when green flag clicked
say [Enter two numbers less than 10. Enter the larger number first.] for (3) secs
ask [Enter a number less than 100:] and wait
set [num1 v] to (answer)
ask [Enter a number less than 10:] and wait
set [num2 v] to (answer)
if <((num1) + (num2)) > [10]> then
  set [add to tidy num1 v] to ((10) - ((num1) mod (10)))
  set [left from num2 v] to ((num2) - (add to tidy num1))
  say (join (join (join (num1) [+]) (num2)) [=?]) for (5) secs
  say (join (join (join (join (join (join (join [To make ] (num1)) [ a tidy number I am splitting ]) (num2)) [ into a ]) (add to tidy num1)) [ and a ]) (left from num2)) for (5) secs
  say (join [(] (join (join (num1) [+]) (join (join (join (add to tidy num1) [)]) [+]) (left from num2)))) for (5) secs
  ask (join [Now can you work out the answer to ] (join [(] (join (join (join (num1) [+]) (join (join (join (add to tidy num1) [)]) [+]) (left from num2))) [=]))) and wait
  if <(answer) = ((num1) + (num2))> then
    say [Well done!]
  else
    say (join [NIce try! The correct answer is ] ((num1) + (num2)))
  end
else
  ask (join (join (join (num1) [+]) (num2)) [=?]) and wait
  if <(answer) = ((num1) + (num2))> then
    say [Well done!]
  else
    say (join [Nice try! The correct answer is ] ((num1) + (num2)))
  end
end
```
