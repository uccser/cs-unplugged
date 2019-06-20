# Colour by numbers

{comment Do learning outcomes at some point. They go in the yaml file}

## Key questions

- How do you think computers display images on a screen?
- How do computers represent images when they can only store numbers?


## Lesson starter



Children will need:

  - A normal writing pencil.
  - Erasers.


This lesson includes two activities, one which students complete individually and one group activity.
In each activity you will need enough coloring pages for one per student.
These each require different versions of the Pixel Painter worksheets.
Use the Black and White colouring type (the first option on the list), and:

  - for the first activity choose from the 1 page images (the star, teacup, or the cat). You can use a combination of these images, students do not all need to complete the same one,
  - for the second activity choose from the 6, 8, and 9 page images. Print enough for one set of image worksheets per group of students.


{panel type="general"}

# Notes on resources

  - Print spare copies of each worksheet in case students make mistakes and need a new one.
  - Use the *Black and White (2 possible binary values)* colouring option, **not** the option which says "in Run Length Encoding"
  - Students can instead use a black pencil or felt tip pen, but easily erasable pencils work much better the first time students do this activity.

{panel end}


Teacher to class: Computer screens are divided up into a grid of small squares, each of which can display a colour.
We call these squares picture elements, or pixels.

Write the words "picture elements" on the board.
To show how we get the word pixels, circle the "pi" of picture and the "el" of elements, and write "pixel" underneath.

Teacher to class: Each of these pixels can be a different colour, and when we have a lot of them on a screen they form an image.
Has anyone heard of pixels before? What about megapixels?

{panel type="general"}

# Teaching observations

Megapixel means one million pixels.
Students may have heard the term "megapixels" used before because cameras are often described as being a certain number of megapixels, for example a phone with a 12-megapixel camera.
This describes the resolution of the photos a camera can take. A 12-mega pixel camera can produce an image with 12 million pixels in it.

Television screens are also made up of pixels.

{panel end}


Teacher to class: Every image we see on a screen, whether it is a picture, a video, or text, is shown using pixels, and all a computer needs to store is what colour each of the pixels on the screen should be.


Show the following images to students on a screen or on the board.

Teacher to class: In a black and white image, each pixel can be either black or white, so all the computer would need to store is which dots are black and which are white.
For example, if we wanted to display the letter *a* we need to divide it into squares.
If we zoom in further and further on the letter we can see a grid of pixels similar to these:

{image file-path="img/topics/letter-zooming-to-pixels.png" alt="Three images of the lower case letter 'a' are shown. These progressively zoom in to show the individual black and white squares which make up the letter on the screen."}

We can represent this image using binary digits.
If a 0 indicates a white square and a 1 indicates a black square then we can represent our letter *a*, on a 5x6 pixel grid, like this:

{image file-path="img/topics/a_in_binary_code.png" alt="A string of binary numbers is shown. They are divided in six lots of five numbers."}

If we take these numbers and draw the image they represent we get the letter a:

{image file-path="img/topics/pixel-visible-grid-with-letter-and-numbers.png" alt="A six by five grid is shown. Some of the squares are white and others are coloured black to create the shape of the letter 'a'. To the right of each row of squares there are five binary digits which describe the image."}


*Anything else to write here?*


## Lesson activities

Hand out the 1 page image worksheets to students and ask them to look at the grid of squares.
What do they notice about the numbers in the squares? They are all 1's or 0's.

Teacher to class: The grid on these sheets represents the pixels on a computer screen. Now you're going to be the computer and use the digits in the squares to make an image.


On the worksheets, have students colour in each square with a 1 in it, and leave each square with a 0 blank.
Advise them to colour them in lightly at first, and then when they are sure they haven't made any mistakes they can colour them in fully.
As they work through the worksheet they should see an image emerging.


Teacher to class: Now that we've made some simple images with our numbers and pixels, we can try making some more detailed ones. How do you think we could make more detailed or higher quality images?

{panel type="general"}

# Teaching observations

Possible answers might include adding more colours. This is a good answer and colours are part of more advanced lessons in this unit, but this lesson only focusses on black and white pixels, so bring students back to this and ask them how they can make a black and white image more detailed.

{panel end}

The answer you are looking for is to use more pixels for the image, which is what students will do in this next activity.

Put students into groups and give each group a set of the multipage image worksheets, so that each student has a page to work on.
If this isn't possible with the number of students you have just make sure groups are small enough for each students to have at least one page, or preferably for each student to have the same number of pages.
For example have groups of 3 each work on one of the 6 page images.


Teacher to class: These sets of grids can all be put together to create one larger image, which has much more pixels than the last ones. You're each going to colour in the pixels on your own sheet, in the same way as before, and then put the whole image together.

Once students have coloured in their sheets they can arrange them together to create the whole image.
There are diagrams on the worksheet printables which teachers can use to help students put their images together if they get stuck.



## Applying what we have just learnt

- Now that students have tried creating the larger images they could take it a step further and make an image as a whole class.
The Pixel Painter Parrots option is made up of 32 pages, and is a great challenge for a class.

- Students can also try creating their own pixel art, convert this into a grid of digits, and then have their friends try to re-create their image.

- Instead of writing the 1's and 0's into each of the boxes on the grid, have students write out the binary digits that represent their image (in the same way as the 'a' in the lesson starter section) and give this to other students and see if they can re-create the same picture.


{panel type="general"}

# Notes on resources

Students could use grid or graph paper to create their pictures, or a printed grid.
There is a printable 8 by 8 grid in the printables section.

There are a number of websites students can also use to easily create pixel art.
After creating their images they can try converting these to grid paper as well.

{panel end}


## Lesson reflection


This is just for black and white images, why can't we do more than two colours with this activity?

  - If we can only use one binary digit for each we can only represent two different colours.
  This means each pixel can only be one of two different colours.

What could we do to represent more colours?

  - If we want each pixel to be able to show more colours other than black and white then we need to use more numbers (or binary digits) to represent the colour of each pixel. This will be explored in future lessons.

{comment Come back and split lessons later once all the other content is done}

(We will explore this at older ages.)
