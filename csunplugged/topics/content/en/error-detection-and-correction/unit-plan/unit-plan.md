# Error detection and correction

{panel type="video"}

# See teaching this in action

{video url="https://vimeo.com/437726658"}

{video url="https://vimeo.com/437724764"}

{panel end}

The world is a complicated and imperfect place, and errors can occur whenever
information is stored or transmitted.
Data stored on hard disks, DVDs and flash memory can be changed if there is a
tiny fault in the device (and these occur regularly!).
Information received over networks can be corrupted if there's interference on
the line or a faulty component in the system.
Even scanning information from barcodes and QR codes is a form of information
transmission, and small errors such as dirt or scratches on the code can change
the information.
Yet we rely on data so much that there could be serious implications from even
a single digit error in a student's grade, or a small change to a payment, or
an incorrect reading in a medical scan.
Error detection techniques add extra information to data to determine when
errors have occurred.
The extra information might be an extra "check digit" such as the last digit of
a credit card number or barcode number on a product, or extra binary digits
(bits) in data stored on a computer.

{image file-path="img/topics/parity-trick-example.png" alt="A student is surprised another student can detect the changed card in the Parity Trick."}

Not only can most digital systems detect errors, but many can correct them as
well, back to what the data should have been.
Error correction can appear to be magic, since it involves being able to put
data back to how it was originally, even when you don’t know what the original
data was.
In fact, the first lesson plan presents a technique called "parity error
correction" as a magic trick that most audiences find intriguing.
In the trick the demonstrator is “magically” able to figure which one out of
dozens of cards has been turned over, using the same kind of method that
computers use to figure out when and where an error has occurred in a piece of
data.

{image file-path="img/topics/mug-with-barcode.png" alignment="right" alt="A mug with a barcode."}

A related technique is used on the barcodes printed on products to check that
they are scanned correctly at a checkout; the last digit in the product code is
based on a mathematical combination of all the other digits, and can easily be
calculated from them.
If the calculation comes up with a different value for the last digit, it's a
warning that one of the digits is wrong, in which case the scanner gives a
warning, and the operator might have to scan the item again, or type in the
number, or look it up some other way.

The lessons in this unit show how errors can be detected, and in same cases,
corrected to restore the original data.
It also enables students to explore how we use some relatively simple ideas to
make our digital systems so reliable that people using them don't realise that
this is all happening underneath the surface!

{panel type="video"}

# See teaching this in action

A demonstration of lesson one ("Parity magic") being taught is available here:

{video url="https://vimeo.com/437726658"}

{panel end}

## Digital Technologies | Data Representation

When data is stored on a disk or transmitted from one computer to another, we
usually assume that it doesn’t get changed in the process.
We are going to learn about some ways in which computers make sure that
information can be retrieved reliably even when errors have occurred.
The digital nature of the data (i.e. it is made up of digits) is what allows us
to detect and correct these errors.

## Vocabulary Explained

**Error detection** is a method that can look at some data and detect if it has
been corrupted while it was stored or transmitted.

**Error correction** is a step better than error detection; when it detects an
error it tries to put the data back to how it should have been.

**Error control** is the general term for error correction and error detection
systems.

“**Parity**” often comes up in error control as there is a well-known method
based on it.
The word "parity" has a general meaning of simply saying if a number is even or
odd.
It comes from the same root word as “pair” – **even parity** means that there is
an even number of objects (they can be put in pairs), and **odd parity** means
they can’t be put into pairs.
If you have 5 white socks, then they have odd parity, but you want them to have
even parity!
The system described in lesson plan one uses even parity, as it is slightly
easier to work with in this situation; so "even parity" is just a fancy way of
saying that there is an even number of something.

A "**check digit**" is an extra digit added to the end of an important number
such as a credit card number, product code (bar code), identity number, tax
number, or a passport number, that can be used to check if the number has been
typed in correctly.
In some situations more than one digit is used, in which case it is referred to
as a checksum.

{panel type="math"}

# Mathematical links

-   Even and odd numbers.
-   That even and odd numbers alternate (adding or subtracting one from a number
    changes it from even to odd, or from odd to even).
    Mathematically, if *N* is even, then *N + 1* and *N -1* are odd.
-   Basic facts knowledge (adding, multiplying).
-   Clock arithmetic (can also be presented as remainder from division, or the
    modulo operator).

{panel end}

## Real world implications

{image file-path="img/topics/arrest-mugshot-for-typo.png" alt="Mugshot for making a typo."}

Imagine that you send an email to an online trader saying that you will pay $20
for their product.
But suppose some interference occurs along the way, and the $20 is changed to
$80.
The trader will probably be very happy to accept your offer, and charge you 4
times as much for the product as you wanted to pay!
Or what if someone types in a credit card number to buy something, but gets one
digit wrong?
Someone else might get charged for the item and person who mis-typed the number
might be accused of fraud just because of a simple typing mistake.

{image file-path="img/topics/cd-with-marks.png" alignment="right" alt="CD with marks on it."}

Everything stored by computers and sent between them is represented as bits
(binary digits).
It is easy for these to be changed accidentally because of errors in the devices
that are storing or transmitting them.
A **CD** might get a scratch or a piece of dust on it that changes a zero into a
one or vice versa.
A hard **disk** might have the magnetism accidentally fade where a bit (binary
digit) is stored.
On the Internet, interference and bad connections can cause bits to be altered.
When scanning printed information such as barcodes and QR codes there might be
ice or dirt on the product that causes the wrong value to be scanned.
So how come we don’t have to worry about this?

And even worse, what if we detect that there's been an error in the data, but
can't get a new copy?
For example, if data is received from a deep space probe, it would be very
tedious to wait for retransmission if an error has occurred and we can’t fix it!
(It takes just over half an hour to get a radio signal from Jupiter when it is
at its closest to Earth!)
And when you read data from a computer's file system, if an error is detected
you can't go back in time and save a new copy (well, making a backup is like
anticipating that you'll need to go back in time one day, but it's not always
convenient or easy to remember to use a backup).
We need to be able to recognize when the data has been corrupted (error
detection) and ideally we also need to be able to reconstruct the original data (error correction).

This was a serious problem on early computers, so scientists soon invented
methods to allow computers to detect errors in data and correct those errors.
We will learn about one way to do this using a method that is called **parity**.
But instead of using zero and one bits inside a computer system, we’ll use
cards with two sides, and do it as a magic trick.
More sophisticated versions of this are widely used on modern storage and
transmission devices to make sure that typical minor hardware problems are
unlikely to result in a major loss of data.
The more complex error control systems used on modern digital devices are able
to detect and correct multiple errors.
The hard disk in a computer has a large amount of its space allocated to
correcting errors so that it will work reliably even if parts of the disk
surface fail.
The activities here will show how adding extra information (without going to the
trouble of making a whole backup, which would use twice the space) provides a
good level of resilience against errors.

## Reflection questions

- What was most surprising about the learning that happened from the teaching of this unit?
- Who were the students who were very systematic in their activities?
- Who were the students who were very detailed in their activities?
- What would I change in my delivery of this unit?
