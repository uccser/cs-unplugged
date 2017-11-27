Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/158861343/?autostart=false"}

{panel type="help" title="Recommended blocks"}

<pre><code class="scratch:split:random">when green flag clicked

ask [Please enter a decimal number between 0 and 31:] and wait
</code></pre>

<pre><code class="scratch:split:random">repeat until &lt;(bit value) = [1]&gt;
end

if &lt;&lt;(decimal number) &gt; (bit value)&gt; or &lt;(decimal number) = (bit value)&gt;&gt; then
else
end
</code></pre>

<pre><code class="scratch:split:random">play note (72 v) for (0.5) beats

play note (48 v) for (0.5) beats
</code></pre>

<pre><code class="scratch:split:random">set [decimal number v] to (answer)

set [bit value v] to [32]

set [bit value v] to ((bit value) / (2))

set [decimal number v] to ((decimal number) - (bit value))
</code></pre>

{panel end}