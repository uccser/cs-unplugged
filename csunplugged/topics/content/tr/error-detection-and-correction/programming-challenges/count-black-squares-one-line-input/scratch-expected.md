Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426017/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

say (black cards total)

ask [Please enter a sequence of black and white squares (B for black and W for white):] and wait
</code></pre>

<pre><code class="scratch:split:random">change [index v] by (1)

change [black cards total v] by (1)
</code></pre>

<pre><code class="scratch:split:random">repeat (length of (cards))
end

if &lt;(letter (index) of (cards)) = [B]&gt; then
end
</code></pre>

<pre><code class="scratch:split:random">set [black cards total v] to [0]

set [index v] to [1]

set [cards v] to (answer)
</code></pre>

{panel end}