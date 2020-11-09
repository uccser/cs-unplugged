```scratch
when green flag clicked
set [number v] to [0]
ask [Enter a number:] and wait
set [number v] to (answer)
if <(number) < [0]> then
  set [number v] to ((-1) * (number))
end
repeat until <<(number) = [0]> or <(number) = [1]>>
  change [number v] by (-2)
end
if <(number) = [0]> then
  say [You entered an even number!]
end
if <(number) = [1]> then
  say [You entered an odd number!]
end
```