Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165593878/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [original time v] to (answer)

set [hours to add v] to (answer)

set [new time v] to (((original time) + (hours to add)) mod (12))
</code></pre>

<pre><code class="scratch:split:random">ask [Enter a time:] and wait

ask [Enter the number of hours to add:] and wait
</code></pre>

<pre><code class="scratch:split:random">say [The new time is 12 o'clock.]

say (join [The new time is ] (join (new time) [ o'clock.]))
</code></pre>

<pre><code class="scratch:split:random">if &lt;(new time) = [0]&gt; then
else
end
</code></pre>

{panel end}