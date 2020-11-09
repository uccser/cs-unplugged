# Image Representation

{panel type="text"}

# Connaissances préalables

Students should have completed Lesson 1 (for the relevant age group) of the [Binary Numbers unit]('topics:unit_plan' 'binary-numbers' 'unit-plan') before beginning this unit.

{panel end}

Images are everywhere on computers and other digital devices. If you think of all the different devices you use, and what you do with them, it is likely that almost all of these will involve a screen or display of some kind! Everything you see on computer screens, whether it is photographs, videos, websites, even text, is an image that a digital device has been programmed to display. Because computers store data as digits, computer images are ultimately represented inside a computer using just 0's and 1's.

{comment Add teaching this in action video here}

{panel type="text"}

# Terminology note

In this unit and its lesson plans the word **image** is used to refer to what is displayed on a computer screen or display at any time. It includes everything seen on a screen, such as videos, websites, apps, text, rather than just referring to static pictures or photos.

{panel end}

Computer screens are divided into a grid of tiny squares called {glossary-link term="pixel"}pixels{glossary-link end}. These pixels can each show a different colour, and because they are so small we don't see the individual pixels on a screen – instead we see them blend together into an image. If you look very, very closely at a computer or TV screen (especially older ones) then you might be able to see these individual pixels.

The digits stored in the computer tell each of these pixels what colour they should be and when they should change colour, which means computers can turn a bunch of random looking binary digits (bits) into all the beautiful images we see on our screens.

There are many different methods we can use to convert images into digital data and back again. The method we choose depends on what type of images the data needs to be converted into. A black and white image, where each pixel can be only either black or white, is much simpler to represent using digits than a full length, colour, and high-definition film is! In this unit students are introduced to simple examples of how they can use digits to create images, how the number of colours an image can include is based on the number of bits used to store it, and how images can be compressed so they take up less memory space.

## Les Technologies Numériques | La Représentation des Données

All data on computers is represented with digits, and using these digits to represent other types of data and information is a core concept of Computer Science. At this point you have probably noticed the words **represent** and **representation** are being used a lot, so let's look at exactly what we mean by this.

{image file-path="img/topics/binary-picture-showing-bits.png" alt="If we look closely at an image on a computer screen we can see it is made up of a grid of tiny dots called pixels. The colour of each of these is stored inside a computer using binary."}

The way a set of digits **represents** information changes the way we interpret it. For example, if a set of digits represents an image then we interpret those digits as the colours of different pixels. If it is meant to be text on the other hand, we interpret it as characters. The ability for computers to represent multiple types of information using just binary digits is one of the things that makes them so powerful. Computers use extra information, such as file extensions like `.txt` or `.gif` to show how the data should be interpreted and processed.

Just like learning about the binary number system, exploring image representation exposes students to the Computational Thinking concepts of Abstraction and Decomposition. Students learn to break down images into pixels and then to digits, and how to move back up from digits, to pixels, to images.

## Technologies numériques | Algorithmes

When pixels are used to represent images, the process we go through to convert digits into these pixels is a type of algorithm. If an image has been compressed to save space, algorithms are needed to uncompress... There are many different algorithms computers use to do this, and the one they use depends on things like the file type of the images being displayed, for example if it is a picture like a `.png` or `.jpeg`, or a video file like an `.mp4` or `.avi`, or what resolution the image is. We also use algorithms to compress images to smaller file sizes, which means they use less memory and are faster to download and copy. Through learning about image representation students practice algorithmic thinking, pattern matching, and abstract thinking.

## Vocabulaire expliqué

### Pixel

Computer screens are divided into a grid of tiny coloured squares, which are called pixels. The colour of each pixel can be set by a computer and they are used to display images on a computer screen. The word pixel is an abbreviation of *picture element*.

### Display Resolution

The resolution of a screen refers to the number, or density, of pixels on the screen. It is usually defined as either the number of pixels per inch on the screen, or the width and height of the screen measured in pixels. For example, a common screen resolution is 1920 by 1080 pixels (refered to as 1080p), which means it has 2,073,600 pixels, just over 2 million!

## Implications dans le monde réel

The way images are digitally represented affects how they are displayed, created, stored, and manipulated. The more bits (binary digits) we use to store the colour of a pixel, the larger the variety of colours we can make. If we use one bit to store the colour of a pixel then we only have two options for what that colour can be (remember, with one bit we can represent two different values only, because we can only use 0 or 1). If we use 8 bits (1 byte) per pixel we can display 256 different colours instead, and if we use 24 bits (3 bytes) then we can display over 16 million different colours, which is more than the human eye can discern.

However, using more bits to represent a colour will increase the size of an image file. This means it will take up more space in memory, take longer for a computer to process and display, and take longer to be transmitted between computers and over the internet. Film makers have to use powerful computers and store large amounts of data when they are editing their videos, otherwise it would take them far too long to do this, or they would have to decrease the image quality of their films. This is also why old computers can't always run newer games; the older computers simply can't process the game graphics quickly enough to display them.

For some types of images we can use a {glossary-link term="compression"}compression{glossary-link end} algorithm to decrease their file size. Compression algorithms can do this without losing, or only losing a small amount of, the image quality. Image compression algorithms allow us to store, process, transmit, and create images more quickly.

## Questions de réflexion

- Qu'est-ce qui était le plus surprenant dans l'apprentissage de ce module ?
- Quels étaient les étudiants très méthodiques dans leurs activités ?
- Quels étaient les étudiants très minutieux dans leurs activités ?
- Que changerais-je dans ma façon d'enseigner ce module ?