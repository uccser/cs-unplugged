```scratch
when green flag clicked
set [prime factors v] to []
ask [What's the number you want to find prime factors of?] and wait
set [number v] to (answer)
set [divisor v] to (number)
repeat until <(divisor) = [0]>
  if <((number) mod (divisor)) = [0]> then
    check_prime (divisor) :: custom
  end
  change [divisor v] by (-1)
end
say (prime factors)

define check_prime (number)
set [index v] to [2]
set [is prime v] to [true]
if <(number) > [1]> then
  repeat until <<(is prime) = [false]> or <(index) = (number)>>
    if <((number) mod (index)) = [0]> then
      set [is prime v] to [false]
    end
    change [index v] by (1)
  end
  if <(is prime) = [true]> then
    set [prime factors v] to (join (number) (join [, ] (prime factors)))
  end
end
```