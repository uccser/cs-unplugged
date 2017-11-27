```scratch
when green flag clicked
set [prime numbers v] to [ ]
set [number v] to [2]
ask [I'll generate the prime numbers up to this number:] and wait
set [upper range v] to (answer)
repeat ((upper range) - (1))
  set [is prime v] to [true]
  set [index v] to [2]
  repeat until <<(index) = (number)> or <(is prime) = [false]>>
    if <((number) mod (index)) = [0]> then
      set [is prime v] to [false]
    end
    change [index v] by (1)
  end
  if <(is prime) = [true]> then
    set [prime numbers v] to (join (prime numbers) (join (number) [, ]))
  end
  change [number v] by (1)
end
say (prime numbers)
```