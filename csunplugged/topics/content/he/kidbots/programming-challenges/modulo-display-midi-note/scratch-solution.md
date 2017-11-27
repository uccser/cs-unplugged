```scratch
when green flag clicked
forever
  ask [Type in a number between 0 and 127 (60 is middle C) and I display the corresponding MIDI note name as well as playing the note:] and wait
  set [note v] to (answer)
  play note (note) for (0.5) beats
  say (item (((note) mod (12)) + (1)) of [notes v] :: list) for (3) secs
end
```