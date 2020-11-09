Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426139/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">ask [How many rows would you like to enter?] and wait

ask (join (join (join [Please enter ] (number of rows)) [ cards for row ]) (row number)) and wait
</code></pre>

<pre><code class="scratch:split:random">set [black cards total v] to [0]

set [row number v] to [1]

set [index v] to [1]

set [number of rows v] to (answer)

set [row v] to (answer)

change [black cards total v] by (1)

change [index v] by (1)

change [row number v] by (1)

set [black cards total v] to [0]
</code></pre>

<pre><code class="scratch:split:random">say (join [There is a parity error is row ] (row number)) for (2) secs

say (join (join [Row ] (row number)) [ is OK!]) for (2) secs
</code></pre>

<pre><code class="scratch:split:random">if &lt;(letter (index) of (row)) = [B]&gt; then
end

repeat (number of rows)
end

repeat (length of (row))
end

if &lt;((black cards total) mod (2)) = [0]&gt; then
else
end
</code></pre>

{panel end}