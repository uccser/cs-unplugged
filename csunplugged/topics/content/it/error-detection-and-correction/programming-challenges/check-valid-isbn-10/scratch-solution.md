```scratch
when green flag clicked
set [index v] to [1]
set [multiplier v] to [10]
set [total v] to [0]
ask [Enter an ISBN-10 number:] and wait
set [ISBN-10 number v] to (answer)
repeat (10)
  if <<(index) = [10]> and <(letter (index) of (ISBN-10 number)) = [X]>> then
    change [total v] by ((multiplier) * (10))
  else
    change [total v] by ((multiplier) * (letter (index) of (ISBN-10 number)))
    change [multiplier v] by (-1)
    change [index v] by (1)
  end
end
if <((total) mod (11)) = [0]> then
  say [This is a valid ISBN-10 number!]
else
  say [This is an invalid ISBN-10 number!]
end
```