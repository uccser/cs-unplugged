Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148424217/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Please enter a number of dots less than or equal to 31:] and wait
</code></pre>

<pre><code class="scratch:split:random">if &lt;&lt;(number of dots) &gt; [16]&gt; or &lt;(number of dots) = [16]&gt;&gt; then
end

if &lt;&lt;(number of dots) &gt; [8]&gt; or &lt;(number of dots) = [8]&gt;&gt; then
end

if &lt;&lt;(number of dots) &gt; [4]&gt; or &lt;(number of dots) = [4]&gt;&gt; then
end

if &lt;&lt;(number of dots) &gt; [2]&gt; or &lt;(number of dots) = [2]&gt;&gt; then
end

if &lt;&lt;(number of dots) &gt; [1]&gt; or &lt;(number of dots) = [1]&gt;&gt; then
end

if &lt;&lt;(number of dots) &lt; [31]&gt; or &lt;(number of dots) = [31]&gt;&gt; then
else
end
</code></pre>

<pre><code class="scratch:split:random">set [number of dots v] to (answer)

set [cards v] to []

set [cards v] to (join (cards) [16, ])

set [number of dots v] to ((number of dots) - (16))

set [cards v] to (join (cards) [8, ])

set [number of dots v] to ((number of dots) - (8))

set [cards v] to (join (cards) [4, ])

set [number of dots v] to ((number of dots) - (4))

set [cards v] to (join (cards) [2, ])

set [number of dots v] to ((number of dots) - (2))

set [cards v] to (join (cards) [1, ])

set [number of dots v] to ((number of dots) - (1))

</code></pre>

<pre><code class="scratch:split:random">say (cards)

say [Please choose a number less than or equal to 31.]
</code></pre>

{panel end}