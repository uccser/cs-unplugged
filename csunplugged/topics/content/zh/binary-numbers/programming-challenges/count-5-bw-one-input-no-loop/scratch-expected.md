Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424155/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Please enter 5 cards ('B' for black and 'W' for white):] and wait

say (total number of dots)
</code></pre>

<pre><code class="scratch:split:random">if &lt;(letter (1) of (cards)) = [W]&gt; then
end

if &lt;(letter (2) of (cards)) = [W]&gt; then
end

if &lt;(letter (3) of (cards)) = [W]&gt; then
end

if &lt;(letter (4) of (cards)) = [W]&gt; then
end

if &lt;(letter (5) of (cards)) = [W]&gt; then
end
</code></pre>

<pre><code class="scratch:split:random">set [total number of dots v] to [0]

set [cards v] to (answer)

set [total number of dots v] to ((total number of dots) + (16))

set [total number of dots v] to ((total number of dots) + (8))

set [total number of dots v] to ((total number of dots) + (4))

set [total number of dots v] to ((total number of dots) + (2))

set [total number of dots v] to ((total number of dots) + (1))
</code></pre>

{panel end}