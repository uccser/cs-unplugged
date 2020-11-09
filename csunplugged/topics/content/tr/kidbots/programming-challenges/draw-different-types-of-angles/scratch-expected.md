Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/152883319/?autostart=false"}

{panel type="help"}

# Recommended blocks for solution 1

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">clear

set pen size to (3)

pen down

pen up
</code></pre>

<pre><code class="scratch:split:random">go to x: (0) y: (0)

point in direction (90 v)

move (100) steps

turn ccw ((180) - (angle)) degrees

move (100) steps
</code></pre>

<pre><code class="scratch:split:random">say [The angle you entered is an acute angle.] for (3) secs

say [The angle you entered is a right angle.] for (3) secs

say [The angle you entered is an obtuse angle.] for (3) secs

say [The angle you entered is a straight angle.] for (3) secs

say [The angle you entered is a reflex angle.] for (3) secs
</code></pre>

<pre><code class="scratch:split:random">ask [Enter an angle between 0 and 360 (not including 0 and 360):] and wait

set [angle v] to (answer)
</code></pre>

<pre><code class="scratch:split:random">if &lt;&lt;(angle) &gt; [0]&gt; and &lt;(angle) &lt; [90]&gt;&gt; then
end

if &lt;(angle) = [90]&gt; then
end

if &lt;&lt;(angle) &gt; [90]&gt; and &lt;(angle) &lt; [180]&gt;&gt; then
end

if &lt;(angle) = [180]&gt; then
end

if &lt;(angle) &gt; [180]&gt; then
end
</code></pre>

{panel end}

{panel type="help"}

# Recommended blocks for solution 2

<pre><code class="scratch:split:random">when green flag clicked
</code></pre>

<pre><code class="scratch:split:random">clear

set pen size to (3)

pen down

pen up
</code></pre>

<pre><code class="scratch:split:random">go to x: (0) y: (0)

point in direction (90 v)

move (100) steps

turn ccw ((180) - (angle)) degrees

move (100) steps
</code></pre>

<pre><code class="scratch:split:random">ask [Enter an angle between 0 and 360 (not including 0 and 360):] and wait

set [angle v] to (answer)
</code></pre>

<pre><code class="scratch:split:random">say [The angle you entered is an acute angle.] for (3) secs

say [The angle you entered is a right angle.] for (3) secs

say [The angle you entered is an obtuse angle.] for (3) secs

say [The angle you entered is a straight angle.] for (3) secs

say [The angle you entered is a reflex angle.] for (3) secs
</code></pre>

<pre><code class="scratch:split:random">if &lt;(angle) &lt; [90]&gt; then
else
end

if &lt;(angle) &lt; [180]&gt; then
else
end

if &lt;(angle) = [90]&gt; then
else
end

if &lt;(angle) = [180]&gt; then 
else
end
</code></pre>

{panel end}