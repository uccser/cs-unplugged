{panel type="general" subtitle="true"}

# Solution 1

## (check digits of the binary number)

**Blocks for cat sprite (labelled binary number)**

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

```scratch
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (5) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

**Blocks for 2 dots card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (4) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

**Blocks for 4 dots card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (3) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

**Blocks for 8 dots card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (2) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

**Blocks for 16 dots card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [turn over card v]
if <(letter (1) of (binary number)) = [1]> then
  switch costume to [white v]
end
```

{panel end}

{panel type="general" subtitle="true"}

# Solution 2

## (broadcast the bit value)

**Blocks for cat sprite (labelled binary number)**

```scratch
when green flag clicked
ask [Please enter a decimal number between 0 and 31] and wait
set [decimal number v] to (answer)
set [bit value v] to [32]
repeat until <(bit value) = [1]>
  set [bit value v] to ((bit value) / (2))
  if <<(decimal number) > (bit value)> or <(decimal number) = (bit value)>> then
    set [decimal number v] to ((decimal number) - (bit value))
    broadcast (bit value)
  end
end
```

**Blocks for 1 dot card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [1 v]
switch costume to [white v]
```

**Blocks for 2 dots card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [2 v]
switch costume to [white v]
```

**Blocks for 4 dots card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [4 v]
switch costume to [white v]
```

**Blocks for 8 dots card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [8 v]
switch costume to [white v]
```

**Blocks for 16 dots card sprite**

```scratch
when green flag clicked
switch costume to [black v]

when I receive [16 v]
switch costume to [white v]
```

{panel end}

{panel type="general" subtitle="true"}

# Solution 3

## (using a variable to broadcast the bit value)

**Blocks for cat sprite (labelled binary number)**

```scratch
when green flag clicked
ask [Please enter a decimal number between 0 and 31] and wait
set [decimal number v] to (answer)
set [bit value v] to [32]
repeat until <(bit value) = [1]>
  set [bit value v] to ((bit value) / (2))
  if <<(decimal number) > (bit value)> or <(decimal number) = (bit value)>> then
    set [decimal number v] to ((decimal number) - (bit value))
    set [number of dots v] to (bit value)
  end
end
```

**Blocks for 1 dot card sprite**

```scratch
when green flag clicked
set [number of dots v] to [0]
switch costume to [black v]
wait until <(number of dots) = [1]>
switch costume to [white v]
```

**Blocks for 2 dots card sprite**

```scratch
when green flag clicked
set [number of dots v] to [0]
switch costume to [black v]
wait until <(number of dots) = [2]>
switch costume to [white v]
```

**Blocks for 4 dots card sprite**

```scratch
when green flag clicked
set [number of dots v] to [0]
switch costume to [black v]
wait until <(number of dots) = [4]>
switch costume to [white v]
```

**Blocks for 8 dots card sprite**

```scratch
when green flag clicked
set [number of dots v] to [0]
switch costume to [black v]
wait until <(number of dots) = [8]>
switch costume to [white v]
```

**Blocks for 16 dots card sprite**

```scratch
when green flag clicked
set [number of dots v] to [0]
switch costume to [black v]
wait until <(number of dots) = [16]>
switch costume to [white v]
```

{panel end}

{panel type="general" subtitle="true"}

# Solution 4

## (cloning the black card)

**Blocks for black card sprite**

```scratch
when green flag clicked
hide
set [x v] to [-190]
ask [Please enter a decimal number between 0 and 31] and wait
set [decimal number v] to (answer)
set [bit value v] to [32]
repeat until <(bit value) = [1]>
  set [bit value v] to ((bit value) / (2))
  if <<(decimal number) > (bit value)> or <(decimal number) = (bit value)>> then
    set [decimal number v] to ((decimal number) - (bit value))
  else
    go to x: (x) y: (0)
    show
    create clone of [myself v]
  end
  change [x v] by (94)
end
```

{panel end}
