Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149428305/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [result v] to [1]

set [base v] to (answer)

set [power v] to (answer)

set [result v] to ((result) * (base))
</code></pre>

<pre><code class="scratch:split:random">ask [Enter an integer for the base:] and wait

ask [Enter a positve integer for the power:] and wait
</code></pre>

<pre><code class="scratch:split:random">say (join (join (join (join (base) [^]) (power)) [ = ]) (result))
</code></pre>

<pre><code class="scratch:split:random">repeat (power)
end
</code></pre>

{panel end}