```scratch
when green flag clicked
ask [Enter the year and I will tell you if it's a leap year or not:] and wait
set [year v] to (answer)
if <not <((year) mod (4)) = [0]>> then 
  say (join (year) [ is not a leap year!])
else 
  if <not <((year) mod (100)) = [0]>> then 
    say (join (year) [ is a leap year!])
  else 
    if <not <((year) mod (400)) = [0]>> then 
      say (join (year) [ is not a leap year!])
    else 
      say (join (year) [ is a leap year!])
    end
  end
end
```