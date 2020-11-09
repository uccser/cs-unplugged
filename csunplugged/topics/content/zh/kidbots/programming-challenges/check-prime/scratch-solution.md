**Solution #1:**

```scratch
when green flag clicked
set [divisor v] to [2]
ask [Enter a number to check if it's a prime number:] and wait
set [number v] to (answer)
if <<(number) = [1]> or <(number) < [1]>> then
  say (join (number) [ is not a prime number.])
else
  repeat until <(divisor) = (number)>
    if <((number) mod (divisor)) = [0]> then
      say (join (number) [ is not a prime number.])
      stop [this script v]
    end
    change [divisor v] by (1)
  end
  say (join (number) [ is a prime number.])
end
```

**Solution #2:**

```scratch
when green flag clicked
set [is prime v] to [true]
set [divisor v] to [2]
ask [Enter a number to check if it's a prime number:] and wait
set [number v] to (answer)
if <<(number) = [1]> or <(number) < [1]>> then
  say (join (number) [ is not a prime number.])
else
  repeat until <<(is prime) = [false]> or <(divisor) = (number)>>
    if <((number) mod (divisor)) = [0]> then
      set [is prime v] to [false]
      say (join (number) [ is not a prime number.])
    end
    change [divisor v] by (1)
  end
  if <(is prime) = [true]> then
    say (join (number) [ is a prime number.])
  end
end
```