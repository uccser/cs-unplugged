```python
note = int(input('Type in a number between 0 and 127 (60 is middle C) and I display the corresponding MIDI note name: '))
notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
print(notes[note % 12])
```