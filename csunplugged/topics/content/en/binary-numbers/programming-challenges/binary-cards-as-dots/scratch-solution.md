{panel type="general" title="Solution 1" subtitle="(check digits of the binary number)"}

**Blocks for cat sprite**

```scratch
when green flag clicked
ask [Please enter a decimal number between 0 and 31] and wait
set [decimal number v] to (answer)
set [bit value v] to [32]
set [binary number v] to []
repeat until <(bit value) = [1]>
  set [bit value v] to ((bit value) / (2))
  if <<(decimal number) > (bit value)> or <(decimal number) = (bit value)>> then
    set [binary number v] to (join (binary number) [1])
    set [decimal number v] to ((decimal number) - (bit value))
  else
    set [binary number v] to (join (binary number) [0])
  end
end
broadcast [turn over card v]
```

**Blocks for 1 dot card sprite**

```scratch:inline
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (5) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

**Blocks for 2 dots card sprite**

```scratch:inline
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (4) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

**Blocks for 4 dots card sprite**

```scratch:inline
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (3) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

**Blocks for 8 dots card sprite**

```scratch:inline
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (2) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

**Blocks for 16 dots card sprite**

```scratch:inline
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (1) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

{panel end}
