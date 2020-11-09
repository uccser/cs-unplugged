{panel type="ct-algorithm"}

# Algorithmisches Denken

We used multiple algorithms in this lesson: one to convert a letter into a decimal number and then into a binary number, and vice versa. Es sind Algorithmen, da es sich dabei um schrittweise Verfahren handeln, die für jede Eingabe stets die richtige Lösung liefern, solange das Verfahren genau eingehalten wird.

Hier ist ein Algorithmus zur Umwandlung eines Buchstabens in eine Dezimalzahl:

Zunächst wählen wir einen Buchstaben, den wir in eine Dezimalzahl umwandeln möchten. Anschließend ermitteln wir die numerische Position dieses Buchstabens im Alphabet wie folgt:

- Say A (the first letter in the alphabet)
- Say 1 (the first number in our sequence of numbers) 
    - Dann wiederholen wir den folgenden Ablauf, bis wir den Buchstaben erreichen, den wir umwandeln möchten: 
        - Wir gehen zum nächsten Buchstaben im Alphabet weiter
        - und dann zur nächsten Zahl (um eins vorwärtszählend)
- Die Zahl, die wir bei Erreichen des ausgewählten Buchstabens erhalten, ist die Dezimalzahl, die unserem Buchstaben entspricht.

Beispielsweise würden wir bei diesem Algorithmus zur Umwandlung des Buchstabens E folgendermaßen zählen: A, 1; B, 2; C, 3; D, 4; E, 5.

{image file-path="img/topics/binary_count_girl.png" alt="girl thinking about alphabet and numbers" alignment="right"}

(Ein effizienterer Algorithmus hätte eine Tabelle zum Nachsehen, ähnlich wie die zu Beginn der Aktivität erstellte, und die meisten Programmiersprachen können Zeichen direkt in Zahlen umwandeln, allerdings mit Ausnahme von Scratch, die den obigen Algorithmus verwendet.)

The next algorithm takes the algorithm from lesson 1 which we use to represent a decimal number as a binary number:

- Zunächst müssen wir die Anzahl der zu zeigenden Punkte herausfinden. (Wir bezeichnen dies als die „Anzahl der verbleibenden Punkte“, was anfangs die insgesamt zu zeigende Anzahl ist.)
- Für jede Karte, von links nach rechts (d. h. 16, 8, 4, 2 und dann 1), gilt: 
    - Wenn die Anzahl der Punkte auf der Karte höher ist als die Anzahl der verbleibenden Punkte: 
        - Karte verdecken
    - Anderenfalls: 
        - Karte zeigen
        - und die Anzahl der Punkte auf der Karte von der Anzahl der verbleibenden Punkte abziehen

#### Worauf Sie beispielsweise achten können:

Can students create instructions for, or demonstrate, converting a letter into a decimal number, and then convert a decimal number into binary; are they able to show a systematic solution?

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

Diese Aktivität ist in Bezug auf Abstraktion besonders relevant, da wir geschriebenen Text anhand einer einfachen Zahl darstellen und die Zahl anhand von binären Einheiten dargestellt werden kann, die (wie wir aus Lektion 1 wissen) eine Abstraktion der physischen elektronischen Elemente und Stromkreise in einem Computer darstellen. We could also expand our abstraction because we don’t actually have to use 0s and 1s to represent our message. We could use any two values, for example you could represent your message by flashing a torch on and off, or drawing a line of squares and triangles on the whiteboard.

{image file-path="img/topics/binary_torch.png" alt="Taschenlampe" alignment="right"}

Abstraktion hilft uns, Dinge zu vereinfachen, da wir Einzelheiten ignorieren können, die wir gegenwärtig nicht wissen müssen. Die binäre Darstellung von Zahlen ist eine Abstraktion, hinter der sich die Komplexität der innerhalb eines Computers befindlichen Elektronik und Hardware verbirgt, mittels der Daten gespeichert werden. Buchstaben sind eine Abstraktion, die Menschen schnell verstehen können. Über den Buchstaben H zu sprechen ist im Allgemeinen sinnvoller, als sich auf „den 10. Buchstaben des Alphabets“ zu beziehen. Und wenn wir lesen oder sprechen, ist es ohnehin belanglos, dass es der 10. Buchstabe ist.

#### Worauf Sie beispielsweise achten können:

Have students create instructions for, or demonstrate how to represent new language elements, such as a comma.

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

Das Erkennen von Mustern in der Funktionsweise des binären Zahlensystems hilft uns dabei, die damit einhergehenden Konzepte besser zu verstehen und diese Konzepte und Muster zu verallgemeinern, um sie dann auf andere Probleme anzuwenden.

#### Worauf Sie beispielsweise achten können:

Have students decode a binary message from another student, by converting the binary numbers into text to view the message. Can they recognise patterns in the binary to anticipate what the word is? Can they work with a different set of letters using the same principles?

{panel end}

{panel type="ct-logic"}

# Logik

Logical thinking means recognising what logic you are using to work these things out. If you memorise how to represent that the letter H is represented as binary 01010 it's not as generally applicable as learning the logic that any character can be represented by the process described in this activity.

#### Worauf Sie beispielsweise achten können:

Observe the systems students have created to translate their letters into binary and vice versa. What logic has been applied to these? Are they efficient systems?

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

An example of decomposition is breaking a long message such as 00001000100001011001 into 5-bit components (00001 00010 00010 11001), each of which can now be converted to a letter. The 5-bit components are then decomposed into the value of individual bits.

#### Worauf Sie beispielsweise achten können:

Can students convert a coded message with no spacing in it?

{panel end}

{panel type="ct-evaluation"}

# Auswertung

An example of evaluation is working out how many different characters can be represented by a given number of bits (e.g. 5 bits can represent 26 characters comfortably, but 6 bits are needed if you have more than 32 characters, and 16 bits are needed for a language with 50,000 characters.

#### Worauf Sie beispielsweise achten können:

Can a student work out how many bits are needed to represent the characters in a language with 50 characters? (6 bits are needed) How about represent emojis, if you have about 10 emojis available (10 bits will be needed for each one).

{panel end}