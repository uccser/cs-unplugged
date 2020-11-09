Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429011/?autostart=false"}

{panel type="help"}

# Recommended blocks for solution 1

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">ask [What's the number you want to find factors of?] and wait
</code></pre>

<pre><code class="scratch:split:random">set [factors v] to []

set [number v] to (answer)

set [divisor v] to [1]

set [factors v] to (join (factors) (join (divisor) [, ]))

change [divisor v] by (1)
</code></pre>

<pre><code class="scratch:split:random">say (factors)
</code></pre>

<pre><code class="scratch:split:random">repeat until &lt;(divisor) &gt; (number)&gt;
end

if &lt;((number) mod (divisor)) = [0]&gt; then
end
</code></pre>

{panel end}

{panel type="help"}

# Recommended blocks for solution 2

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">ask [What's the number you want to find factors of?] and wait
</code></pre>

<pre><code class="scratch:split:random">set [factors v] to []

set [number v] to (answer)

set [divisor v] to (number)

set [factors v] to (join (divisor) (join [, ] (factors)))

change [divisor v] by (-1)
</code></pre>

<pre><code class="scratch:split:random">say (factors)
</code></pre>

<pre><code class="scratch:split:random">repeat until &lt;(divisor) = [0]&gt;
end

if &lt;((number) mod (divisor)) = [0]&gt; then
end
</code></pre>

{panel end}