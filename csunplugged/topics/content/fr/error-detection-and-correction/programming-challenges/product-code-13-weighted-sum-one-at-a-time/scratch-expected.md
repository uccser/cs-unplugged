Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476545/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

say (join [Total: ] (total))
</code></pre>

<pre><code class="scratch:split:random">repeat (6)
end
</code></pre>

<pre><code class="scratch:split:random">ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait

ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait

ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
</code></pre>

<pre><code class="scratch:split:random">change [total 1 v] by (answer)

set [total v] to ((total 1) + ((total 2) * (3)))

change [index v] by (1)

change [total 1 v] by (answer)

change [index v] by (1)

change [total 2 v] by (answer)

set [total 1 v] to [0]

set [total 2 v] to [0]

set [index v] to [1]
</code></pre>

{panel end}