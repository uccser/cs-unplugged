Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148477907/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Enter the first 9 digits of an ISBN-10 number:] and wait
</code></pre>

<pre><code class="scratch:split:random">say [The last digit is: X]

say (join [The last digit is: ] (last digit))
</code></pre>

<pre><code class="scratch:split:random">set [index v] to [1]

set [multiplier v] to [10]

set [first 9 digits v] to [0]

set [total v] to [0]

set [last digit v] to [0]

set [first 9 digits v] to (answer)

change [total v] by ((multiplier) * (letter (index) of (first 9 digits)))

change [index v] by (1)

change [multiplier v] by (-1)

set [last digit v] to (((0) - (total)) mod (11))
</code></pre>

<pre><code class="scratch:split:random">if &lt;(last digit) = [10]&gt; then
else
end

repeat (9)
end
</code></pre>

{panel end}