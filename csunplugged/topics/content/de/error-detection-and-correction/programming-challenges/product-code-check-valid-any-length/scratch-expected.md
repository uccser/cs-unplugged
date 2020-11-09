Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476969/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Enter a product code:] and wait
</code></pre>

<pre><code class="scratch:split:random">set [total v] to ((total 1) + ((total 2) * (3)))

set [product code v] to [0]

set [total 1 v] to [0]

set [total 2 v] to [0]

set [total v] to [0]

change [product code v] by (answer)

set [index v] to (length of (product code))

set [total 1 v] to ((total 1) + (letter (index) of (product code)))

change [index v] by (-1)

set [total 2 v] to ((total 2) + (letter (index) of (product code)))

change [index v] by (-1)
</code></pre>

<pre><code class="scratch:split:random">repeat until &lt;(index) &lt; [1]&gt;
end

if &lt;((total) mod (10)) = [0]&gt; then
else
end
</code></pre>

<pre><code class="scratch:split:random">say [This is a valid product code]

say [This is an invalid product code]
</code></pre>

{panel end}