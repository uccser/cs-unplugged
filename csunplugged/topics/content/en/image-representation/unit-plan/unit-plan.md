# Image Representation

{panel type="text"}

# Preparatory knowledge

Students should have completed lesson 1 (for the relevant age group) of the [Binary Numbers unit]('topics:unit_plan' 'binary-numbers' 'unit-plan') before beginning this unit.

{panel end}

Images are everywhere on computers and digital devices.
If you think of all the different devices you use and what you do with them, it is likely that almost all of these will involve a screen of some kind!
Everything you see on computer screens, whether it is photographs, videos, websites, even text, is an image that a digital device has been programmed to display.
Because modern computers store data as digits, computer images are stored inside a computer using just 0's and 1's, and these are used to represent images.


{comment Add teaching this in action video here}

{comment Old version of text: All information that modern computers store and process is stored using just two states, represented by binary digits. This means that everything you see in computer images is stored inside a computer using just 0's and 1's, and these are used to *represent* images.}

{panel type="text"}

# Terminology note

In this unit and its lesson plans the word **image** is used to refer to what is displayed on a computer screen at any time.
It includes everything seen on a screen, such as videos, websites, apps, text, rather than just referring to static pictures or photos.

{panel end}


Computer screens are divided into a grid of tiny squares called {glossary-link term="pixel"}pixels{glossary-link end}.
These pixels can each show a different colour, and because they are so small when we look at a screen we don't see the individual pixels, instead we see them blend together into an image.
If you look very very closely at a computer or TV screen (especially older ones) then you might be able to see these individual pixels. Be careful not to hurt your eyes though!

The digits stored in the computer tell each of these pixels what colour they should be and when they should change colour, which means computers can turn a bunch of random looking binary digits into all the beautiful images we see on our screens!




## Digital Technologies | Data Representation

All data on computers is represented with digits, and using these digits to represent other types of data is a core concept of Computer Science.
At this point you have probably noticed the words **represent** and **representation** are being used a lot, so let's look at exactly what we mean by this.


{comment This image is currently too big for the page}

{image file-path="img/topics/binary-picture-showing-bits.png" alt="If we look closely at an image on a computer screen we can see it is made up of a grid of tiny dots called pixels. The colour of each of these is stored inside a computer using binary."}

The type of information a set of digits **represents** changes the way we interpret it.
For example, if a set of digits represents an image then we interpret those digits as the colours of different pixels.
If it is meant to be text on the other hand, we interpret it as letters.
The ability for computers to represent multiple types of information using just two states (represented with binary digits) is one of the things that makes them so powerful.

Just like learning about the binary number system, exploring image representation introduces students to the Computational Thinking concepts of Abstraction and Decomposition.
Students learn to break down images into pixels and then to digits, and how too move back up from digits, to pixels, to images.


## Digital Technologies | Algorithms

{comment Could include Algorithms as well because of RLE/encoding Algorithms}

When pixels are used to represent images, the process we go through to convert digits into these pixels is an Algorithm.
There are many different algorithms computers use to do this, and the one they use depends on things like the file type of the images being displayed, for example if it is a picture like a .png or .jpeg, or a video file like an .mp4 or .avi; or what resolution the image is.
We also use Algorithms to compress images to smaller file sizes, which means they use less memory, can be processed more quickly, and are faster to download.

{comment Through lerning about image representation students practice algorithmic thinking and pattern matching...}

## Vocabulary Explained

### Pixel

The word pixel is an abbreviation of *picture element*. On computer screens (and printers) an image is almost always displayed using a grid of tiny coloured squares, called pixels.

{comment Older version, which matches the pixels.md file in the glossary: This term is an abbreviation of picture element, the name given to the tiny squares that make up a grid that is used to represent images on a computer.}


### Display Resolution

The resolution of a screen refers to the number or density of pixels on the screen.
It is usually defined as either the number of pixels per inch on the screen, or the width x height of the screen measured in pixels (e.g. 1920x1080 pixels).


## Real world implications

{comment Check conventions around using numerals vs words}

The more bits we use to store the colour of a pixel, the more different colours we can make.
If we use one bit to store the colour of a pixel then we only have two options for what that colour can be (remember, with one bit we can represent two different values only, because we can only use 0 or 1).
If we use 8 bits (or 1 byte) then we can represent 256 different colours instead, which



- Screen resolutions


- File sizes and image quality


- Image processing time. Need better hardware to run newer games, streaming quality, matters a lot for creators and artists.




## Reflection questions

- What was most surprising about the learning that happened from the teaching of this unit?
- Who were the students who were very systematic in their activities?
- Who were the students who were very detailed in their activities?
- What would I change in my delivery of this unit?
