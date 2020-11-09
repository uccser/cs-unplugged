Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148477751/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Enter a credit card number:] and wait
</code></pre>

<pre><code class="scratch:split:random">repeat (8)
end

if &lt;((letter (index) of (credit card number)) * (2)) &lt; [10]&gt; then
else
end

if &lt;(((even total) + (odd total)) mod (10)) = [0]&gt; then
else
end
</code></pre>

<pre><code class="scratch:split:random">say [Invalid credit card number!]

say [Valid credit card number!]
</code></pre>

<pre><code class="scratch:split:random">set [index v] to [1]

set [credit card number v] to [0]

set [even total v] to [0]

set [odd total v] to [0]

change [credit card number v] by (answer)

change [odd total v] by ((letter (index) of (credit card number)) * (2))

change [index v] by (1)

change [odd total v] by (((letter (index) of (credit card number)) * (2)) - (9))

change [index v] by (1)

change [even total v] by (letter (index) of (credit card number))

change [index v] by (1)
</code></pre>

{panel end}