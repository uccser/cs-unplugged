```scratch
when green flag clicked
set [new month v] to [0]
ask [Type in a number between 1 and 12 for a month of the year:] and wait
set [original month v] to (answer)
ask [Enter the number of months to add to the month:] and wait
set [months to add v] to (answer)
set [new month v] to (((original month) + (months to add)) mod (12))
if <(new month) = [0]> then
  say (join (join (months to add) (join [ months after ] (item (original month) of [months v] :: list))) [ is December. ])
else
  say (join (join (join (join (months to add) (join [ months after ] (item (original month) of [months v] :: list))) [ is ]) (item (new month) of [months v] :: list)) [.])
end
```
