Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/152883486/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">clear

set pen size to (3)

pen down

pen up
</code></pre>

<pre><code class="scratch:split:random">set [angle v] to (answer)

ask [Enter an angle between 0 and 180 (not including 0 and 180):] and wait
</code></pre>

<pre><code class="scratch:split:random">go to x: (0) y: (0)

go to x: (0) y: (0)

point in direction (90 v)

move (100) steps

move (100) steps

turn ccw ((180) - (angle)) degrees
</code></pre>

<pre><code class="scratch:split:random">say [This is an acute triangle.] for (2) secs

say [This is a right triangle.] for (2) secs

say [This is an obtuse triangle.] for (2) secs
</code></pre>

<pre><code class="scratch:split:random">if &lt;(angle) &lt; [90]&gt; then
end

if &lt;(angle) = [90]&gt; then
end

if &lt;(angle) &gt; [90]&gt; then
end
</code></pre>

{panel end}