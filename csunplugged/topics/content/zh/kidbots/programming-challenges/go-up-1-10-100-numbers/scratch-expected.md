Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/149428180/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">set [upper range v] to (answer)

set [number v] to (pick random (1) to (upper range))

set [numbers after v] to (item (random v) of [numbers after list v] :: list)
</code></pre>

<pre><code class="scratch:split:random">ask [Enter a number as the upper range:] and wait

ask (join (join [What is the number after ] (number)) [?]) and wait

ask (join (join (join (join [What's ] (numbers after)) [ numbers after ]) (number)) [?]) and wait
</code></pre>

<pre><code class="scratch:split:random">say [I'll generate a random number between 1 and a number you enter.] for (5) secs

say [Well done!] for (3) secs

say (join [Nice try! The right answer is: ] ((number) + (numbers after))) for (3) secs
</code></pre>

<pre><code class="scratch:split:random">forever
end

if &lt;(numbers after) = [1]&gt; then
else
end

if &lt;(answer) = ((number) + (numbers after))&gt; then
else
end
</code></pre>

{panel end}