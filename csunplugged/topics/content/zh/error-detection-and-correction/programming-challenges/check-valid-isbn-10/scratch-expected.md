Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148477875/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Enter an ISBN-10 number:] and wait
</code></pre>

<pre><code class="scratch:split:random">say [This is a valid ISBN-10 number!]

say [This is an invalid ISBN-10 number!]
</code></pre>

<pre><code class="scratch:split:random">change [total v] by ((multiplier) * (letter (index) of (ISBN-10 number)))

change [multiplier v] by (-1)

change [index v] by (1)

set [index v] to [1]

set [multiplier v] to [10]

set [total v] to [0]

change [total v] by ((multiplier) * (10))

set [ISBN-10 number v] to (answer)
</code></pre>

<pre><code class="scratch:split:random">if &lt;((total) mod (11)) = [0]&gt; then
else
end

repeat (10)
end

if &lt;&lt;(index) = [10]&gt; and &lt;(letter (index) of (ISBN-10 number)) = [X]&gt;&gt; then
else
end
</code></pre>

{panel end}