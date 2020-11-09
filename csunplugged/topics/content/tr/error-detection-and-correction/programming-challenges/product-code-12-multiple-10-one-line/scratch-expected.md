Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476927/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Enter a 12 digit product code:] and wait
</code></pre>

<pre><code class="scratch:split:random">set [index v] to [1]

set [product code v] to []

set [total 1 v] to [0]

set [total 2 v] to [0]

set [total v] to [0]

set [total 1 v] to ((total 1) + (letter (index) of (product code)))

change [index v] by (1)

set [total 2 v] to ((total 2) + (letter (index) of (product code)))

change [index v] by (1)

set [total v] to (((total 1) * (3)) + (total 2))

change [product code v] by (answer)
</code></pre>

<pre><code class="scratch:split:random">say [Valid product code!]

say [Invalid product code!]

say [Please enter a 12 digit number!]
</code></pre>

<pre><code class="scratch:split:random">if &lt;(length of (product code)) = [12]&gt; then
else
end

repeat (6)
end

if &lt;((total) mod (10)) = [0]&gt; then
else
end
</code></pre>

{panel end}