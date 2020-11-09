Click on the green flag, and use the buttons to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/158364683/?autostart=false"}

{panel type="help"}

# Recommended blocks

Events

<pre><code class="scratch:split:random">when green flag clicked

when this sprite clicked

when I receive [home v]

broadcast [go v]

broadcast [home v]
</code></pre>

Control

<pre><code class="scratch:split:random">repeat (length of [source code v] :: list)
end

if &lt;(statement) = [forward]&gt; then
else
end

if &lt;(statement) = [backward]&gt; then
else
end

if &lt;(statement) = [turn left]&gt; then
else
end

if &lt;(statement) = [turn right]&gt; then
else
end

if &lt;touching [border v] ?&gt; then
else
end

if &lt;touching [Mouse v] ?&gt; then
else
end

stop [all v]

wait (0.5) secs
</code></pre>

Data - Variable

<pre><code class="scratch:split:random">set [statement v] to [0]

set [source line v] to [1]

set [statement v] to (item (source line) of [source code v] :: list)

change [source line v] by (1)
</code></pre>

Data - List

<pre><code class="scratch:split:random">insert [forward] at (last v) of [source code v]

insert [backward] at (last v) of [source code v]

insert [turn left] at (last v) of [source code v]

insert [turn right] at (last v) of [source code v]

insert [pause] at (last v) of [source code v]

delete (last v) of [source code v]

delete (all v) of [source code v]
</code></pre>

Looks

<pre><code class="scratch:split:random">set size to (30) %

set size to (50) %

say [Oh no! Missed it! Press "home" and then "clear" to try again.] for (2) secs

say [Gotcha!] for (2) secs

say [Oh no! Missed it! Press "home" and then "clear" to try again.]
</code></pre>

Sensing

<pre><code class="scratch:split:random">go to x: (50) y: (0)

go to x: ((pick random (-1) to (4)) * (50)) y: ((pick random (-3) to (3)) * (50))

move (50) steps

move (-50) steps

turn cw (90) degrees

turn ccw (90) degrees

point in direction (90 v)

</code></pre>

Sound

<pre><code class="scratch:split:random">play sound [meow v]
</code></pre>

{panel end}