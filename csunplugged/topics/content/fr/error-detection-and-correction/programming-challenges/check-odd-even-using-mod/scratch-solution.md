```scratch
when green flag clicked
ask [Enter a number:] and wait
set [number v] to (answer)
if <((number) mod (2)) = [0]> then
  say [You entered an even number!]
else
  say [You entered an odd number!]
end
```