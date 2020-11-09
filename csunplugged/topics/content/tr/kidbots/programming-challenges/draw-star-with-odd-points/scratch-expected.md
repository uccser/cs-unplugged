Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/153925156/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">clear

pen down

pen up
</code></pre>

<pre><code class="scratch:split:random">ask [Enter an odd number of points to draw a star:] and wait

repeat (points)
end

set [points v] to (answer)
</code></pre>

<pre><code class="scratch:split:random">go to x: (0) y: (0)

move (200) steps

turn cw ((180) - ((180) / (points))) degrees
</code></pre>

{panel end}