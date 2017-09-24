```scratch
when green flag clicked
ask [What's the secret code?] and wait
set [secret code v] to (answer)
if <(secret code) = [planets]> then
  say [You entered the correct secret code!]
else
  say [The secret code you entered is incorrect!]
end
```
