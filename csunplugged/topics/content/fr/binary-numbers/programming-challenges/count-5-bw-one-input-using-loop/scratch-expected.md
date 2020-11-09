Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424160/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Please enter 5 cards (B for black and W for white):] and wait

repeat (5)
end

if &lt;(letter (index) of (cards)) = [W]&gt; then
end

change [index v] by (1)

say (total number of dots)
</code></pre>

<pre><code class="scratch:split:random">set [total number of dots v] to [0]

set [index v] to [1]

set [number of dots v] to [16]

set [cards v] to (answer)

set [total number of dots v] to ((total number of dots) + (number of dots))

set [number of dots v] to ((number of dots) / (2))
</code></pre>

{panel end}