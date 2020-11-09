Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149512041/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [num1 v] to (answer)

set [num2 v] to (answer)

set [add to tidy num1 v] to ((10) - ((num1) mod (10)))

set [left from num2 v] to ((num2) - (add to tidy num1))
</code></pre>

<pre><code class="scratch:split:random">ask [Enter a number less than 100:] and wait

ask [Enter a number less than 10:] and wait
</code></pre>

<pre><code class="scratch:split:random">say [Enter two numbers. Enter the larger number first.] for (3) secs

say (join (join (join (num1) [+]) (num2)) [=?]) for (3) secs

say (join (join (join (join (join (join (join [To make ] (num1)) [ a tidy number I am splitting ]) (num2)) [ into a ]) (add to tidy num1)) [ and a ]) (left from num2)) for (5) secs

say (join (join [(] (join (join (num1) [+]) (join (join (join (add to tidy num1) [)]) [+]) (left from num2)))) [=]) for (5) secs

say (join [] ((num1) + (num2)))

say (join (join (join (num1) [+]) (num2)) [=?]) for (5) secs

say ((num1) + (num2))
</code></pre>

<pre><code class="scratch:split:random">if &lt;(((num1) mod (10)) + (num2)) &gt; [10]&gt; then 
else
end
</code></pre>

{panel end}