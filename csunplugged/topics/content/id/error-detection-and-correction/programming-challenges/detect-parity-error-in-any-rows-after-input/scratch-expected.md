Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426175/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

say (join [There is a parity error in row ] (index row)) for (3) secs

add (answer) to [rows v]

delete (all v) of [rows v]
</code></pre>

<pre><code class="scratch:split:random">set [black cards total v] to [0]

set [row number v] to [1]

set [number of rows v] to (answer)

change [row number v] by (1)

set [index row v] to [1]

set [index v] to [1]

change [black cards total v] by (1)

change [index v] by (1)

set [black cards total v] to [0]

change [index row v] by (1)

change [black cards total v] by (1)
</code></pre>

<pre><code class="scratch:split:random">ask [How many rows would you like to enter?] and wait

ask (join [Enter row ] (row number)) and wait
</code></pre>

<pre><code class="scratch:split:random">repeat (number of rows)
end

repeat (length of [rows v] :: list)
end

repeat (length of (item (index row) of [rows v] :: list))
end

if &lt;((black cards total) mod (2)) = [1]&gt; then
end

if &lt;(letter (index) of (item (index row) of [rows v] :: list)) = [B]&gt; then
end
</code></pre>

{panel end}