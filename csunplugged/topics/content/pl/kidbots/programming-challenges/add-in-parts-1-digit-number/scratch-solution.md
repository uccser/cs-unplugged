```scratch
when green flag clicked
say [Enter two numbers less than 10. Enter the larger number first.] for (3) secs
ask [Enter the 1st number:] and wait
set [num1 v] to (answer)
ask [Enter the 2nd number:] and wait
set [num2 v] to (answer)
if <((num1) + (num2)) > [10]> then
  set [ten minus num1 v] to ((10) - (num1))
  set [left from num2 v] to ((num2) - (ten minus num1))
  say (join (join (join (num1) [+]) (num2)) [=?]) for (3) secs
  say (join (join (join (join (join (join (join [To make ] (num1)) [ a tidy number I am splitting ]) (num2)) [ into a ]) (ten minus num1)) [ and a ]) (left from num2)) for (5) secs
  say (join (join [(] (join (join (num1) [+]) (join (join (join (ten minus num1) [)]) [+]) (left from num2)))) [=]) for (5) secs
  say (join [] ((num1) + (num2)))
else
  say (join (join (join (num1) [+]) (num2)) [=?]) for (5) secs
  say ((num1) + (num2))
end
```