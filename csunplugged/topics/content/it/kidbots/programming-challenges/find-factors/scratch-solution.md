**Solution #1:**

```scratch
when green flag clicked
set [factors v] to []
ask [What's the number you want to find factors of?] and wait
set [number v] to (answer)
set [divisor v] to [1]
repeat until <(divisor) > (number)>
  if <((number) mod (divisor)) = [0]> then
    set [factors v] to (join (factors) (join (divisor) [, ]))
  end
  change [divisor v] by (1)
end
say (factors)
```

**Solution #2:**

```scratch
when green flag clicked
set [factors v] to []
ask [What's the number you want to find factors of?] and wait
set [number v] to (answer)
set [divisor v] to (number)
repeat until <(divisor) = [0]>
  if <((number) mod (divisor)) = [0]> then
    set [factors v] to (join (divisor) (join [, ] (factors)))
  end
  change [divisor v] by (-1)
end
say (factors)
```