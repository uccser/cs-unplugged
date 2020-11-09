Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424337/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Please enter a decimal number:] and wait

repeat until &lt;(decimal number) = [1]&gt;
end

say (join (join (join [The binary representation for the number ] (answer)) [ is ]) (binary number))
</code></pre>

<pre><code class="scratch:split:random">set [decimal number v] to (answer)

set [remainder v] to [0]

set [binary number v] to []

set [remainder v] to ((decimal number) mod (2))

set [decimal number v] to ([floor v] of ((decimal number) / (2)))

set [binary number v] to (join (remainder) (binary number))

set [binary number v] to (join (decimal number) (binary number))
</code></pre>

{panel end}