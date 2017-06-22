Description of different angles:

-   An acute angle is an angle between 0 and 90 degrees (not including 90).
-   A right angle is a 90 degrees angle.
-   Obtuse angle is an angle between 90 and 180 degree (not including 90 and 180).
-   A straight angle is a 180 degrees angle.
-   A reflex angle is an angle greater than 180 degrees.

There are different ways to program checking the range using the **if()/else** blocks. Below are hints for two different ways you may program this:

-   Use a series of **if()** blocks sequentially checking for the ranges in each if() block. If you need to check a range between two values you can use the `scratch:<> and <>` operator in the condition for your if() block (the AND operator reports true if both conditions are true).

-   Use nested **if()** or **if()/else** blocks, which are **if()/else** blocks inside another set of **if()/else** blocks (i.e. a nested conditional statement is a conditional statement where the **if()** and/or **else** contains another conditional statement). For example:

    ```scratch:
    if <[angle] < [180]> then
      if <[angle] < [90]> then
        acute angle
      else
        if <[angle] = [90]> then
          right angle
        else
          obtuse angle
        end
      end
    else
      if <[angle] = [180]> then
        straight angle
      else
        reflex angle
      end
    end
    ```
