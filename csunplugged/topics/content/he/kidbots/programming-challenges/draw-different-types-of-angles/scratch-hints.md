Description of different angles:

- An acute angle is an angle between 0 and 90 degrees (not including 90).
- A right angle is a 90 degrees angle.
- Obtuse angle is an angle between 90 and 180 degree (not including 90 and 180).
- A straight angle is a 180 degrees angle.
- A reflex angle is an angle greater than 180 degrees.

There are different ways to program checking the range using the **if()/else** blocks. Below are hints for two different ways you may program this:

- Use a series of **if()** blocks sequentially checking for the ranges in each if() block. If you need to check a range between two values you can use the `scratch:<> and <>` operator in the condition for your if() block (the AND operator reports true if both conditions are true).

- Use nested **if()** or **if()/else** blocks, which are **if()/else** blocks inside another set of **if()/else** blocks (i.e. a nested conditional statement is a conditional statement where the **if()** and/or **else** contains another conditional statement). For example:
    
    <pre><code class="scratch:">if &lt;[angle] &lt; [180]&gt; then
  if &lt;[angle] &lt; [90]&gt; then
    acute angle :: custom
  else
    if &lt;[angle] = [90]&gt; then
      right angle :: custom
    else
      obtuse angle :: custom
    end
  end
else
  if &lt;[angle] = [180]&gt; then
    straight angle :: custom
  else
    reflex angle :: custom
  end
end
</code></pre>