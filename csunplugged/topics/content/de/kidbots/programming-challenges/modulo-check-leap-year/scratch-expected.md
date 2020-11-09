Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165754830/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [year v] to (answer)
</code></pre>

<pre><code class="scratch:split:random">ask [Enter the year and I will tell you if it's a leap year or not:] and wait
</code></pre>

<pre><code class="scratch:split:random">say (join (year) [ is not a leap year!])

say (join (year) [ is a leap year!])

say (join (year) [ is not a leap year!])

say (join (year) [ is a leap year!])
</code></pre>

<pre><code class="scratch:split:random">if &lt;not &lt;((year) mod (4)) = [0]&gt;&gt; then
else
end

if &lt;not &lt;((year) mod (100)) = [0]&gt;&gt; then
else
end

if &lt;not &lt;((year) mod (400)) = [0]&gt;&gt; then
else
end
</code></pre>

{panel end}