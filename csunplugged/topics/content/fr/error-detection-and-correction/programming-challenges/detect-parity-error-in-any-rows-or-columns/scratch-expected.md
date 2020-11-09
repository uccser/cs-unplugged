Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426200/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

delete (all v) of [cards v]

add (row) to [cards v]

say (join (join (join [There is a parity error in row ] (error in row)) [ and column ]) (error in column))
</code></pre>

<pre><code class="scratch:split:random">change [black cards total v] by (1)

change [row index v] by (1)

set [error in column v] to (index)

change [index v] by (1)

set [black cards total v] to [0]

set [row index v] to [1]

set [index v] to [1]

change [row number v] by (1)

set [error in row v] to (row number)

change [index v] by (1)

set [black cards total v] to [0]

set [index v] to [1]

set [row number v] to [1]

set [error in row v] to [0]

set [error in column v] to [0]

set [number of rows v] to (answer)

set [row v] to (answer)

change [black cards total v] by (1)
</code></pre>

<pre><code class="scratch:split:random">ask (join (join (join [Enter ] (number of rows)) [ cards for row ]) (row number)) and wait

ask [How many rows would you like to enter?] and wait
</code></pre>

<pre><code class="scratch:split:random">repeat (number of rows)
end

repeat (length of (row))
end

if &lt;(letter (index) of (row)) = [B]&gt; then
end

if &lt;((black cards total) mod (2)) = [1]&gt; then
end

repeat (number of rows)
end

repeat (number of rows)
end

if &lt;(letter (index) of (item (row index) of [cards v] :: list)) = [B]&gt; then
end

if &lt;((black cards total) mod (2)) = [1]&gt; then
end

</code></pre>

{panel end}