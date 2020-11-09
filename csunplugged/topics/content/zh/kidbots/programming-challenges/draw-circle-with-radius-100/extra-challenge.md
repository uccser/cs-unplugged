**Extra challenge #1:** Write a program that works for any radius. That means that it takes a radius as the input then draws a circle with the given radius, and then displays the circumference as the output.

**Extra challenge #2:** Write a program that takes a circumference as the input then draws a circle with the given circumference and then displays the radius as the output.

**Extra challenge #3:** [This requires advanced maths, but is a good challenge for a student who is familiar with Pythagoras' theorem] Draw a Circle Using Pythagoras’ Theorem.

{image file-path="img/topics/programming-challenges/circle_red.png" alt="A red circle drawn using the Pythagoras' Theorem method."}

The diagram above shows a circle (radius 100) drawn using the Pythagoras’ Theorem method. (Note: The red triangle inside the circle is only to show the calculation and does not need to be drawn).

You can use Pythagoras’ Theorem (in any right-angle triangle, the square of the side opposite the right angle is equal to the sum of the squares of the other two sides so here \( x^{2}+y^{2}=radius^{2}\)) to draw a circle. We can do this by rearranging the formula to solve for \(y\) like this:

\[ y^{2} = radius ^{2} - x^{2} \\ y = sqrt{(radius^{2} - x^{2})}  
\]

We then calculate \(y\) using a range of values for \(x\) (i.e. from 0 to \(\pm radius\)). Your programming language will probably only give you the positive square root, so you will also need to plot the negative of \(y\).