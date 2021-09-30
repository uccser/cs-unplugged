Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165595531/?autostart=false"}

{panel type="help"}

# Recommended blocks

```scratch
when green flag clicked

ask [Type in a number between 0 and 127 (60 is middle C) and I display the corresponding MIDI note name as well as playing the note:] and wait

set [note v] to (answer)

play note (note) for (0.5) beats

say (item (((note) mod (12)) + (1)) of [notes v] :: list) for (3) secs

forever
end
```

{panel end}
