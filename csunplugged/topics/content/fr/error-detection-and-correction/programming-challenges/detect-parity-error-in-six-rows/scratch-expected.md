Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426115/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask (join [Please enter 6 black or white cards for row ] (row number)) and wait
</code></pre>

<pre><code class="scratch:split:random">repeat (6)
end

repeat (6)
end

if &lt;(letter (index) of (row)) = [B]&gt; then
end

if &lt;((black cards total) mod (2)) = [0]&gt; then
else
end
</code></pre>

<pre><code class="scratch:split:random">say (join (join [Row ] (row number)) [ is OK!]) for (2) secs

say (join [There is a parity error in row ] (row number)) for (2) secs
</code></pre>

<pre><code class="scratch:split:random">set [row v] to []

set [black cards total v] to [0]

set [row number v] to [1]

change [row number v] by (1)

set [black cards total v] to [0]

change [index v] by (1)

change [black cards total v] by (1)

set [row v] to (answer)

set [index v] to [1]
</code></pre>

{panel end}