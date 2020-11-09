Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148426073/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Enter a number:] and wait

change [number v] by (-2)
</code></pre>

<pre><code class="scratch:split:random">if &lt;(number) &lt; [0]&gt; then
end

repeat until &lt;&lt;(number) = [0]&gt; or &lt;(number) = [1]&gt;&gt;
end

if &lt;(number) = [0]&gt; then
end

if &lt;(number) = [1]&gt; then
end
</code></pre>

<pre><code class="scratch:split:random">say [You entered an odd number!]

say [You entered an even number!]
</code></pre>

<pre><code class="scratch:split:random">set [number v] to [0]

set [number v] to (answer)

set [number v] to ((-1) * (number))
</code></pre>

{panel end}