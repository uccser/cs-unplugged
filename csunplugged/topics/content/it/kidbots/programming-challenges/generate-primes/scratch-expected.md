Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429772/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [prime numbers v] to [ ]

set [number v] to [2]

set [is prime v] to [true]

set [index v] to [2]

change [index v] by (1)

set [upper range v] to (answer)

set [prime numbers v] to (join (prime numbers) (join (number) [, ]))

change [number v] by (1)

set [is prime v] to [false]
</code></pre>

<pre><code class="scratch:split:random">ask [I'll generate the prime numbers up to this number:] and wait
</code></pre>

<pre><code class="scratch:split:random">say (prime numbers)
</code></pre>

<pre><code class="scratch:split:random">if &lt;((number) mod (index)) = [0]&gt; then
end

if &lt;(is prime) = [true]&gt; then
end

repeat ((upper range) - (1))
end

repeat until &lt;&lt;(index) = (number)&gt; or &lt;(is prime) = [false]&gt;&gt;
end
</code></pre>

{panel end}