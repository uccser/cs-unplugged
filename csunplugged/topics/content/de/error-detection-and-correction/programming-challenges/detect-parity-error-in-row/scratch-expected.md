Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426097/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Please enter a row of black and white cards (B for black and W for white):] and wait
</code></pre>

<pre><code class="scratch:split:random">if &lt;(letter (index) of (cards)) = [B]&gt; then
end

repeat (length of (cards))
end

if &lt;((black cards total) mod (2)) = [0]&gt; then
else
end
</code></pre>

<pre><code class="scratch:split:random">say [There is no parity error in this row!]

say [There is a parity error in this row!]
</code></pre>

<pre><code class="scratch:split:random">change [black cards total v] by (1)

change [index v] by (1)
</code></pre>

<pre><code class="scratch:split:random">set [black cards total v] to [0]

set [index v] to [1]

set [cards v] to (answer)
</code></pre>

{panel end}