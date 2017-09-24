{panel type="help" title="Solution 1"}

One of the possible ways is to use nested `scratch:if <> then` blocks (the block can be nested, when you have multiple conditions to meet.
The **false** value is being replaced by another `scratch:if <> then` block to make a further test).
In this challenge you check the following:

-   If the input is "Mercury" display a message that "Mercury is a planet".
-   If not, check if it’s "Venus" and display a message that "Venus is a planet".  
-   If not, check if it’s "Earth" and so on.
-   If the input is none of the 8 planets then display "that is not a planet".

{panel end}

{panel type="help" title="Solution 2"}

Another way is using a boolean variable (a variable which has two possible values: **true** or **false**).
This avoids using the **else** statements.
In this challenge call your boolean variable "is found" and set its value to **false**.
Use an **if** statement to check the input against the name of each of the eight planets, and if it matches one, change the value of "is found" to **true**.
At the end, check if the value of "is found" is still **false**.
If it is, then the input is not one of the 8 planets therefore it's not a planet.

{panel end}
