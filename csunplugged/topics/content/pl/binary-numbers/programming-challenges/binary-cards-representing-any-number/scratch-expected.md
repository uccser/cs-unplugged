Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424247/?autostart=false"}

{panel type="help" title="Recommended blocks"}

<pre><code class="scratch:split:random">when green flag clicked

ask [Please enter a decimal number:] and wait

say (join (join (join [The binary representation for the number ] (answer)) [ is ]) (cards))
</code></pre>

<pre><code class="scratch:split:random">repeat until &lt;(number) &lt; (bit value)&gt;
end

if &lt;&lt;(number) &gt; (bit value)&gt; or &lt;(number) = (bit value)&gt;&gt; then
else
end

repeat until &lt;(bit value) = [1]&gt;
end
</code></pre>

<pre><code class="scratch:split:random">set [number v] to (answer)

set [bit value v] to [1]

set [cards v] to []

set [bit value v] to ((bit value) * (2))

set [bit value v] to ((bit value) / (2))

set [cards v] to (join (cards) [W])

set [number v] to ((number) - (bit value))

set [cards v] to (join (cards) [B])
</code></pre>

{panel end}