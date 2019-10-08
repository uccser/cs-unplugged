# RLE

## Key questions

- How can computers store images efficiently so that they take up less space?
- Does the type of image change how it can be stored efficiently?

## Lesson starter

In this lesson we will again just be looking at black and white images (this makes learning the CS concepts much simpler, and following lessons move on to coloured images).

Remind students about what they learnt in the previous lesson, that digital images are made up of pixels and computers store these pixels using binary digits (bits).
Show the students the following image of the letter C.
This can be on a projector, printed out, or drawn, it just needs to be large enough for everyone to see.

{image file-path="img/topics/pixel-visible-grid-with-letter-no-numbers.png" alt="A six by five grid is shown.
Some of the squares are white and others are coloured black to create the shape of the letter 'C'."}

**To do: Add in link to download**

Previously we represented this image by writing down a 0 or 1 to tell us which pixels were white and black. This time we'll be representing them in a different way.
Demonstrate how to do this by writing down the number of consecutive white pixels in the first line of the image (in the case of this image it will be one).
Then write down the number of consecutive black pixels (three), and then the number of white (one).
The first line of the image is now repesented by 1, 3, 1.

Continue doing this for each line of the image, asking students to tell you what numbers to write down.
You always start each line by writing down the number of white pixels, so the second line of the image starts with a 0 since there are no white pixels at the start of the line.

The final number representation for this image is shown below.

{image file-path="img/topics/pixel-visible-grid-with-letter-and-RLE-numbers.png" alt="A six by five grid is shown.
Some of the squares are white and others are coloured black to create the shape of the letter 'C'. To the right of this grid are a set of numbers which repesent the pixels in the grid."}

Students might say you should start the second line with a 1, or ask why you always start with the number of white pixels.
The answer to this is you need to follow a specific rule or algorithm, like "always start with the number of white pixels", because otherwise a computer wont know what the first number represents.
A computer will follow an algorithm exactly as it is given. Similarly, if you were using these numbers to draw the image you wouldn't want to just guess what numbers meant what colour! You might end up with a completely different picture.



## Lesson activities

Now that students have seen


{panel type="general"}

# Notes on resources

- Print spare copies of each worksheet in case students make mistakes and need a new one.
- Use the **Black and White (2 possible binary values) in in Run Length Encoding** option.
- Students can use a black colouring pencil, crayon, or felt tip pen, but easily erasable pencils work much better for the first time students do this activity.

{panel end}
