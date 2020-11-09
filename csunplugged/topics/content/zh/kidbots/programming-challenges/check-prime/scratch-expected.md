Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429557/?autostart=false"}

{panel type="help"}

# Recommended blocks for solution 1

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [divisor v] to [2]

set [number v] to (answer)

change [divisor v] by (1)
</code></pre>

<pre><code class="scratch:split:random">ask [Enter a number to check if it's a prime number:] and wait
</code></pre>

<pre><code class="scratch:split:random">say (join (number) [ is not a prime number.])

say (join (number) [ is not a prime number.])

say (join (number) [ is a prime number.])
</code></pre>

<pre><code class="scratch:split:random">if &lt;((number) mod (divisor)) = [0]&gt; then
end

if &lt;&lt;(number) = [1]&gt; or &lt;(number) &lt; [1]&gt;&gt; then
else
end

repeat until &lt;(divisor) = (number)&gt;
end

stop [this script v]
</code></pre>

{panel end}

{panel type="help"}

# Recommended blocks for solution 2

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [is prime v] to [true]

set [divisor v] to [2]

set [is prime v] to [false]

change [divisor v] by (1)

set [number v] to (answer)
</code></pre>

<pre><code class="scratch:split:random">ask [Enter a number to check if it's a prime number:] and wait
</code></pre>

<pre><code class="scratch:split:random">say (join (number) [ is not a prime number.])

say (join (number) [ is not a prime number.])

say (join (number) [ is a prime number.])
</code></pre>

<pre><code class="scratch:split:random">if &lt;(is prime) = [true]&gt; then
end

if &lt;((number) mod (divisor)) = [0]&gt; then
end

repeat until &lt;&lt;(is prime) = [false]&gt; or &lt;(divisor) = (number)&gt;&gt;
end

if &lt;&lt;(number) = [1]&gt; or &lt;(number) &lt; [1]&gt;&gt; then
else
end
</code></pre>

{panel end}