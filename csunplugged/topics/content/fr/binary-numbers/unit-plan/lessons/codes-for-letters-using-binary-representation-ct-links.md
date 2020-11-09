{panel type="ct-algorithm"}

# Pensée algorithmique

Nous avons utilisé deux algorithmes dans cette leçon : un pour convertir une lettre en un nombre décimal, puis en un nombre binaire, et vice versa. These are algorithms because they are a step-by-step process that will always give the right solution for any input you give it as long as the process is followed exactly.

Here’s an algorithm for converting a letter into a decimal number:

Choose a letter to convert into a decimal number. Find the letter’s numerical position in the alphabet as follows:

- Say “A” (the first letter in the alphabet)
- Say “1” (the first number in our sequence of numbers) 
    - Repeat the following instructions until you come to the letter you are looking to convert 
        - Say the next letter in the alphabet
        - Say the next number (counting up by 1)
- The number you just said is the decimal number that your letter converts too.

For example, to convert the letter E, the algorithm would have you counting A,1; B, 2; C, 3; D, 4; E, 5.

{image file-path="img/topics/binary_count_girl.png" alt="Fille réfléchissant à l'algorithme" alignment="right"}

(A more efficient algorithm would have a table to look up, like the one created at the start of the activity, and most programming languages can convert directly from characters to numbers, with the notable exception of Scratch, which needs to use the above algorithm.)

The next algorithm is the same algorithm we used in lesson 1, which we use to convert a decimal number to a binary number:

- Find out the number of dots that is to be displayed. (We'll refer to this as the "number of dots remaining", which initially is the total number to be displayed.)
- For each card, from the left to the right (i.e. 16, 8, 4, 2, then 1): 
    - If the number of dots on the card is more than the number of dots remaining: 
        - Hide the card
    - Otherwise: 
        - Show the card
        - Subtract the number of dots on the card from the number of dots remaining

#### Examples of what you could look for:

Have students create instructions for, or demonstrate, converting a letter into a decimal number (with or without the table), and then convert a decimal number into binary; are they able to show a systematic solution? Can they explain what they are doing at each step and why?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

This activity is particularly relevant to abstraction, since we are representing written text with a simple number, and the number can be represented using binary digits, which, as we know from lesson 1, are an abstraction of the physical electronics and circuits inside a computer. We could also expand our abstraction because we could use any two symbols other than 0s and 1s to represent our message (although while students are first learning this we recommend sticking with 1s and 0s). For example, you could represent your message by flashing a torch on and off (this gives an idea of how information might be sent over a fibre-optic cable!), or drawing a line of squares and triangles on the whiteboard.

{image file-path="img/topics/binary_torch.png" alt="Flashlight" alignment="right"}

Abstraction helps us simplify things because we can ignore the details we don’t currently need to know. Binary number representation is an abstraction that hides the complexity of the electronics and hardware inside a computer that stores data. Letters are an abstraction that a human can make sense of quickly; talking about the letter H is generally more meaningful than calling it "the 10th letter of the alphabet", and when we are reading or speaking we don’t need to know it is the 10th letter anyway.

#### Examples of what you could look for:

When you use a different representation for binary, such as turning the torch on and off, who are the students who quickly see that this is equivalent to when they previously used 0s and 1s? They will probably feel comfortable working with this new representation quickly, and other students may be very confused by this change. Look for students who then decide to create their own representations of binary numbers.

{panel end}

{panel type="ct-decomposition"}

# Décomposition

The core example of decomposition in this activity is understanding that in computing we have to break down all information into tiny chunks so that computers can store and send this data as bits and bytes. Everything we store inside a computer and see appear on the screen has to have been, in some way, broken down into binary digits.

In this lesson students have performed several steps of decomposition as they have taken the task of encoding a message and broken it down into simple steps. Pour écrire un message en binaire, nous devons d'abord regarder le message une lettre à la fois et les convertir une par une, en nombres décimaux, et ensuite convertir chacun de ces nombres, un par un, en nombres binaires. Students perform these same steps in reverse to convert the message back to text.

#### Examples of what you could look for:

Can students explain why it is important that we can use binary to represent letters? Ask them why it is useful to choose a number value (binary or decimal) representing each letter, rather than choosing a number value representing each word.

{panel end}

{panel type="ct-pattern"}

# Généralisation et motifs

Recognising patterns in the way the binary number system works helps give us a deeper understanding of the concepts involved, and assists us in generalising these concepts and patterns so that we can apply them to other problems.

#### Examples of what you could look for:

Have students decode a binary message from another student, by converting the binary numbers into decimal numbers, and then to text to view the message. Ask them what they would do if they wanted to include other characters in their message: what if we wanted upper and lower case letters? What if we want to use exclamation and question marks? Observe which students see that we can simply generalise the method they are already using and can match other characters to bigger decimal numbers, e.g a-z can be 1-26, and A-Z can be 27-52. If we can represent 32 different characters in binary when we use 5 bits for each character, then how many would we need for 64? Quels élèves peuvent voir le motif du binaire et du doublement dans cette situation, et voir que nous avons simplement besoin d'utiliser 1 bit de plus pour ce faire?

{panel end}

{panel type="ct-logic"}

# Logique

Logical thinking involves making decisions based on knowledge you have, and these decisions should be sensible and well thought out. If you memorise that the letter H is represented as binary 01010 it's not as useful as learning how to represent any character using the process described in this activity. Si vous pouvez comprendre la logique des étapes que vous suivez pour convertir une lettre en un nombre binaire, et comment vous pouvez convertir dans l'autre sens, alors vous serez en mesure de représenter n'importe quel caractère binaire, et plus important encore, vous comprendrez le processus, puisque que vous le ferez certainement faire à un ordinateur plutôt que de le faire vous-même à la main. This is especially relevant if we want to represent a large number of characters. What if we wanted to represent every Chinese character? There are over 50,000 of them so trying to memorise them all would take a long time! When we choose the decimal numbers to use for each of the letters we didn’t have to choose 1 to 26, we could have decided to start at 17 instead and go from 17 to 42, or we could have chosen completely random numbers! What if we decide that A = 82, B = 5, C = 42… Would this be a logical decision to make? 1 to 26 makes much more sense because it is much easier to describe and remember.

#### Examples of what you could look for:

Observe the systems students have created to translate their letters into binary and vice versa. What logic has been applied to these? Are they efficient systems? Can they explain what they are doing at each step? Ask students why we are using the numbers 1 to 26 to represent our letters, or if they think there could be a better choice. Ask them how they would choose numbers for other characters, such as choosing a number to represent a space. Lesquels donnent des réponses logiques et peuvent expliquer pourquoi leur solution est un bon choix ?

{panel end}

{panel type="ct-evaluation"}

# Évaluation

Un exemple d'évaluation est de travailler sur la façon dont beaucoup de caractères différents peuvent être représentés par un nombre donné de bits. Par exemple 5 bits peuvent représenter 26 caractères confortablement, mais 16 bits sont nécessaires pour une langue avec 50 000 caractères. Lorsque vous pensez à combien de bits doivent être utilisés pour représenter quelque chose, les chercheurs en informatique doivent aussi réfléchir à la quantité d'espace que cela prendra dans un ordinateur (les caractères de 16 bits prennent deux fois plus d'espace que les caractères 8 bits), et si nous devrions utiliser des bits supplémentaires au cas où nous voudrions ajouter plus de caractères dans le futur. Évaluer les bénéfices et les coûts de l'utilisation d'un certain nombre de bits est également une idée que les élèves peuvent explorer.

#### Exemples de ce que vous pourriez observer :

Un élève peut-il déterminer combien de bits sont nécessaires pour représenter les caractères dans une langue qui en compte 100 ? (7 bits sont nécessaires) Comment représenter les émoticônes, lorsque vous avez au bas mot 4 000 émoticônes disponibles (12 bits seront nécessaires pour chacun).

{panel end}