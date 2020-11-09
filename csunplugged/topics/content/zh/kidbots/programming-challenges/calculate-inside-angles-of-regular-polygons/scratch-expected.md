Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/152498752/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">clear

pen down

pen up
</code></pre>

<pre><code class="scratch:split:random">set [sides v] to (answer)

set [turning angle v] to ((360) / (sides))

set [inside angle v] to ((180) - (turning angle))
</code></pre>

<pre><code class="scratch:split:random">go to x: (0) y: (0)

point in direction (90 v)

move (50) steps

turn cw (turning angle) degrees
</code></pre>

<pre><code class="scratch:split:random">say (join (join [Each inside angle is ] (inside angle)) [ degrees.])
</code></pre>

<pre><code class="scratch:split:random">ask [Enter the number of sides of a regular polygon:] and wait
</code></pre>

<pre><code class="scratch:split:random">wait (1) secs

repeat (sides)
end
</code></pre>

{panel end}