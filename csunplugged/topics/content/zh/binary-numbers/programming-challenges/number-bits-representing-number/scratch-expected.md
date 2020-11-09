Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424235/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Please enter the number of dots:] and wait

change [bits v] by (1)

repeat until &lt;(total number of dots) &lt; (bit value)&gt;
end

say (join (join (join [You will need ] (bits)) [ bits to store number ]) (total number of dots))
</code></pre>

<pre><code class="scratch:split:random">set [total number of dots v] to (answer)

set [bits v] to [0]

set [bit value v] to [1]

set [bit value v] to ((bit value) * (2))
</code></pre>

{panel end}