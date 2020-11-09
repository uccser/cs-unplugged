{panel type="ct-algorithm"}

# Algorithmisches Denken

How to detect and correct errors in data is a very important problem in Computer Science, and to solve this problem we need algorithms. Asking “Has this barcode been scanned correctly?” has a yes or no answer, and means you can perform error control on that specific barcode, but it is not a solution to the bigger problem of “How do we perform error control for barcodes?”. The solution to that problem is an algorithm, and if we use that algorithm we can check any barcode we are given and find out if it is correct or not.

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

When we perform error control there are only some details we need to focus on to perform this task, and many others can be ignored by using abstraction when we look at the problem. With error control, we only care about what the bits or numbers we are looking at are, and we don’t need to know what those bits and numbers actually represent or mean - we don’t need to know if they are the numbers and check digit on the barcode for a loaf of bread, or if the bits we are checking for even parity represent a video stored on a laptop. This information can be discarded because it is irrelevant to the task of error control. Similarly, if we have performed error control on our piece of data and now we are using it for something, we no longer need to think about how that error detection and correction worked; it is usually hidden from the user, so all they see is data that seems to be stored and transmitted accurately. The designer of such a system needs to know error control is enabling the data to get through accurately, but once that is happening, they can put all the information about how it is happening to one side and focus on working with the data.

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

To solve our problem of performing error control we need to break this problem down into smaller components. The instruction “Detect the error in this data and correct it” involves many steps and can’t be solved all at once! First it needs to be broken down into smaller steps and then each of these can be solved.

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

Detecting and correcting errors is a very common problem in Computer Science, and it relates to data validation in general, which is important for security and encryption as well. Seeing the similarities between each of these problems allows us to generalise the algorithms we use to multiple situations where we need to find out if data has been changed or not. For example, the simple single-digit checksum used on product codes can be generalised to multiple-digit checksums used for some ID numbers, through to checksums that are dozens of digits long that are used to check the downloaded files have arrived reliably.

{panel end}

{panel type="ct-evaluation"}

# Auswertung

We can evaluate our solutions by testing them with a range of different inputs. Does our solution detect when data has an error in it or not? What happens if there is more than one error in our data? Students can test the algorithms with many different inputs to evaluate how good (or not good!) they are. We can also evaluate our algorithms like the ones in this unit, and show that they will always work by constructing a mathematical proof, or through logical reasoning, which ties in with the next Computational Thinking skill: logic.

{panel end}

{panel type="ct-logic"}

# Logik

If we have even parity in the magic trick, why will flipping a card always cause the number of white cards to become odd? There is a logical reason for this and getting students to articulate that this is because of the relationship between even and odd numbers is a way to exercise their logical reasoning and maths understanding. If we know that the data in our parity trick grid should have even parity, how do we determine which card has been flipped? We can follow an algorithm to do this, but we need to use our logic skills to construct this algorithm and understand why it works.

{panel end}