Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429925/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [coin v] to [0]

set [number of heads v] to [0]

set [number of tails v] to [0]

set [coin v] to (pick random (1) to (2))

change [number of heads v] by (1)

change [number of tails v] by (1)

set [number of flips v] to (answer)
</code></pre>

<pre><code class="scratch:split:random">ask [How many times would you like to flip a coin?] and wait
</code></pre>

<pre><code class="scratch:split:random">say (join (round (((number of heads) * (100)) / (number of flips))) [% heads]) for (3) secs

say (join (round (((number of tails) * (100)) / (number of flips))) [% tail]) for (3) secs
</code></pre>

<pre><code class="scratch:split:random">if &lt;(coin) = [1]&gt; then
else
end

repeat (number of flips)
end
</code></pre>

{panel end}