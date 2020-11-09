- For this challenge you need to use a list to store all the rows (each item in the list is a row). You then need to go through each row (item of your list) and check if they have a parity error (i.e. the total number of black cards in each row is odd). If one or more rows have parity errors, you then need to find their positions in the list and report these positions as the output.

- To make a new list select “Make a list” under “Data” script.

- Add items to your list by using the `scratch:add () to [rows v]` block.

- You can access an item in a specific position in your list by using the `scratch:item () of [rows v] :: list` block.

- The `scratch:length of [rows v] :: list` block reports how many items are in the list.

- You need to delete all the previous items from your list at the start of your program. If you don’t do this, your new items get added to the list every time you run your program. To delete all the items from your list select “all” from the drop down list on the `scratch:delete (all v) of [rows v]` block.

- You can access a letter at the specified position in a string by using the `scratch:letter (1) of [world]` block under “Operators”. For example: `scratch:letter (1) of [world] //w`

- In this challenge you need to access all the letters in user’s input (each row of the parity trick) and check to see how many of them are equal to B (black). Store the total number of black squares in a variable called “black cards total”.

- You can find how many letters a string has by using the `scratch:length of [world]` block unders “Operators”.

- To find out if a number is even or odd, use the `scratch:() mod ()` block (under "Operators") to find the remainder after dividing that number by two. If the remainder is zero the number is even. For example: `scratch:(37) mod (10) //7`