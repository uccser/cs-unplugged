Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149428874/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [number1 v] to (answer)

set [number2 v] to (answer)
</code></pre>

<pre><code class="scratch:split:random">ask [Enter a number:] and wait

ask (join [Enter a number to check if it's a divisor of the number ] (number1)) and wait
</code></pre>

<pre><code class="scratch:split:random">say (join (join (number2) [ is a divisor of the number ]) (number1)) for (3) secs

say (join (join (number2) [ is not a divisor of the number ]) (number1)) for (3) secs
</code></pre>

<pre><code class="scratch:split:random">forever
end

if &lt;((number1) mod (number2)) = [0]&gt; then
else
end
</code></pre>

{panel end}