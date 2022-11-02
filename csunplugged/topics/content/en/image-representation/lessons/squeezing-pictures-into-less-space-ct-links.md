{panel type="ct-algorithm"}

# Algorithmic thinking

#### Examples of what you could look for:

Students are able to articulate and follow the process (algorithm) for converting a sequence of pixels to numbers, and convert numbers to pixels.
Those who have learned programming could implement the algorithm that reads in the numbers, and displays lines of pixels (in a text-based language this could be done using the @ symbol for a black pixel and a space for a white pixel), and vice-versa.

{panel end}

{panel type="ct-abstraction"}

# Abstraction

#### Examples of what you could look for:

Students are able to see that the run-length encoding codes are equivalent to a representation of a picture.
They may make the connection that the numbers in the RLE code will actually be stored using a binary representation.

{panel end}

{panel type="ct-decomposition"}

# Decomposition

#### Examples of what you could look for:

Students can decompose an image into horizontal lines, and then decompose those lines into alternating run-length encodings of white and black pixels.

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

#### Examples of what you could look for:

They appreciate that run-length encoding works because images tend to have a pattern of clusters (runs) of black or white pixels.
They can generalise the concept to using more than two colours (this requires stating which colour each RLE is).
They could also apply run-length encoding to other types of data (such as minute-by-minute temperature readings, where the same temperature is read many times in a row).

{panel end}

{panel type="ct-evaluation"}

# Evaluation

#### Examples of what you could look for:

Are students able to see that reading out the run-length encoding is likely to be faster than reading out all the pixels?
Can they think of a kind of image where it wouldn’t be? (You could guide them towards images that have alternating black and white pixels).

If they are familiar with how numbers are represented on computers (binary), are they able to evaluate how much space this encoding saves in more detail?
For example, if run-length encodings are represented as a 3-bit binary value (000 to 111), then the maximum run length is 7 pixels (111 in binary equals 7 in decimal).
A RLE code of 6 identical pixels would be represented as 3 bits (110), half the size, compared to recording each individual pixel (111111 or 000000), but alternating single black and white pixels would actually use more space because they don’t fit the expected pattern of long run-length encodings of the same colour.

{panel end}

{panel type="ct-logic"}

# Logic

#### Examples of what you could look for:

They can reason that the assumption that each code line begins with white pixels does not prevent the first pixel from being black.
They can also see solutions to having a maximum length of a run-length encoding (inserting a zero-length RLE of the opposite colour).

{panel end}
