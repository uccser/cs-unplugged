Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476646/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

say (join [The last digit of the product code is ] (last digit))

repeat (6)
end
</code></pre>

<pre><code class="scratch:split:random">ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait

ask (join (join [Enter digit ] (index)) [ of the product code:]) and wait
</code></pre>

<pre><code class="scratch:split:random">set [odd total v] to [0]

set [even total v] to [0]

set [index v] to [1]

set [last digit v] to [0]

change [index v] by (1)

change [odd total v] by (answer)

change [index v] by (1)

change [even total v] by (answer)

set [last digit v] to (((0) - ((odd total) + ((even total) * (3)))) mod (10))
</code></pre>

{panel end}