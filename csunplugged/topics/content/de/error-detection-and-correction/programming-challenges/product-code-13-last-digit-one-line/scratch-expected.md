Click on the green flag, enter the inputs provided in the “testing examples” to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/148476672/?autostart=false"}

{panel type="help"}

# Recommended blocks

<pre><code class="scratch:split:random">when green flag clicked

ask [Enter first 12 digits of the barcode:] and wait
</code></pre>

<pre><code class="scratch:split:random">repeat (6)
end

if &lt;(length of (first 12 digits)) = [12]&gt; then
else
end
</code></pre>

<pre><code class="scratch:split:random">say [You must enter a 12 digit number!]

say (join [The last digit of the product code is: ] (last digit))
</code></pre>

<pre><code class="scratch:split:random">set [index v] to [1]

set [first 12 digits v] to [0]

set [total 1 v] to [0]

set [total 2 v] to [0]

set [last digit v] to [0]

set [last digit v] to (((0) - ((total 1) + ((total 2) * (3)))) mod (10))

set [first 12 digits v] to (answer)

set [total 1 v] to ((total 1) + (letter (index) of (first 12 digits)))

change [index v] by (1)

set [total 2 v] to ((total 2) + (letter (index) of (first 12 digits)))

change [index v] by (1)
</code></pre>

{panel end}