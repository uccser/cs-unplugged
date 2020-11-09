Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149429841/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [prime factors v] to []

set [number v] to (answer)

set [divisor v] to (number)

set [index v] to [2]

set [is prime v] to [true]

set [is prime v] to [false]

set [prime factors v] to (join (number) (join [, ] (prime factors)))

change [divisor v] by (-1)

change [index v] by (1)
</code></pre>

<pre><code class="scratch:split:random">ask [What's the number you want to find prime factors of?] and wait
</code></pre>

<pre><code class="scratch:split:random">say (prime factors)
</code></pre>

<pre><code class="scratch:split:random">if &lt;((number) mod (divisor)) = [0]&gt; then
end

if &lt;(number) &gt; [1]&gt; then
end

if &lt;((number) mod (index)) = [0]&gt; then
end

if &lt;(is prime) = [true]&gt; then
end

repeat until &lt;(divisor) = [0]&gt;
end

repeat until &lt;&lt;(is prime) = [false]&gt; or &lt;(index) = (number)&gt;&gt;
end
</code></pre>

<pre><code class="scratch:split:random">define check_prime (number)

check_prime (divisor) :: custom
</code></pre>

{panel end}