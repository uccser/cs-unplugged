{panel type="ct-algorithm"}

# Algorithmisches Denken

In dieser Lektion haben wir zwei Algorithmen verwendet: Einen, um einen Buchstaben in eine Dezimalzahl und dann in eine Binärzahl umzuwandeln, und umgekehrt. Es sind Algorithmen, da es sich dabei um schrittweise Verfahren handeln, die für jede Eingabe stets die richtige Lösung liefern, solange das Verfahren genau eingehalten wird.

Hier ist ein Algorithmus zur Umwandlung eines Buchstabens in eine Dezimalzahl:

Zunächst wählen wir einen Buchstaben, den wir in eine Dezimalzahl umwandeln möchten. Anschließend ermitteln wir die numerische Position dieses Buchstabens im Alphabet wie folgt:

- Wir beginnen mit „A“ (dem ersten Buchstaben des Alphabets)
- Und kombinieren ihn mit „1“ (der ersten Zahl in unserer Zahlenfolge) 
    - Dann wiederholen wir den folgenden Ablauf, bis wir den Buchstaben erreichen, den wir umwandeln möchten: 
        - Wir gehen zum nächsten Buchstaben im Alphabet weiter
        - und dann zur nächsten Zahl (um eins vorwärtszählend)
- Die Zahl, die wir bei Erreichen des ausgewählten Buchstabens erhalten, ist die Dezimalzahl, die unserem Buchstaben entspricht.

Beispielsweise würden wir bei diesem Algorithmus zur Umwandlung des Buchstabens E folgendermaßen zählen: A, 1; B, 2; C, 3; D, 4; E, 5.

{image file-path="img/topics/binary_count_girl.png" alt="Ein Mädchen, das sich den Algorithmus überlegt" alignment="right"}

(Ein effizienterer Algorithmus hätte eine Tabelle zum Nachsehen, ähnlich wie die zu Beginn der Aktivität erstellte, und die meisten Programmiersprachen können Zeichen direkt in Zahlen umwandeln, allerdings mit Ausnahme von Scratch, die den obigen Algorithmus verwendet.)

Der nächste Algorithmus ist derselbe Algorithmus, den wir in Lektion 1 verwendet haben, und mit dem wir nun eine Dezimalzahl in eine Binärzahl umwandeln:

- Zunächst müssen wir die Anzahl der zu zeigenden Punkte herausfinden. (Wir bezeichnen dies als die „Anzahl der verbleibenden Punkte“, was anfangs die insgesamt zu zeigende Anzahl ist.)
- Für jede Karte, von links nach rechts (d. h. 16, 8, 4, 2 und dann 1), gilt: 
    - Wenn die Anzahl der Punkte auf der Karte höher ist als die Anzahl der verbleibenden Punkte: 
        - Karte verdecken
    - Anderenfalls: 
        - Karte zeigen
        - und die Anzahl der Punkte auf der Karte von der Anzahl der verbleibenden Punkte abziehen

#### Worauf Sie beispielsweise achten können:

Lassen Sie die Schüler Anweisungen dafür erstellen oder demonstrieren, wie (mit oder ohne die Tabelle) ein Buchstabe in eine Dezimalzahl und dann eine Dezimalzahl in eine Binärzahl umgewandelt wird. Sind sie in der Lage, eine systematische Lösung aufzuzeigen? Können sie erklären, wie sie bei den einzelnen Schritten vorgehen und warum?

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

Diese Aktivität ist in Bezug auf Abstraktion besonders relevant, da wir geschriebenen Text anhand einer einfachen Zahl darstellen und die Zahl anhand von binären Einheiten dargestellt werden kann, die (wie wir aus Lektion 1 wissen) eine Abstraktion der physischen elektronischen Elemente und Stromkreise in einem Computer darstellen. Wir könnten unsere Abstraktion auch erweitern, da wir anstelle von Nullen und Einsen ebenso gut zwei beliebige Symbole verwenden können, um unsere Nachricht darzustellen (wir empfehlen jedoch, zu Anfang des Lernprozesses bei Einsen und Nullen zu bleiben). Beispielsweise könnten wir unsere Nachricht durch Ein- und Ausschalten einer Taschenlampe (was uns eine Vorstellung davon gibt, wie Daten wohl über faseroptische Kabel gesendet werden!) oder Zeichnen einer Reihe von Quadraten und Dreiecken auf dem Whiteboard darstellen.

{image file-path="img/topics/binary_torch.png" alt="Taschenlampe" alignment="right"}

Abstraktion hilft uns, Dinge zu vereinfachen, da wir Einzelheiten ignorieren können, die wir gegenwärtig nicht wissen müssen. Die binäre Darstellung von Zahlen ist eine Abstraktion, hinter der sich die Komplexität der innerhalb eines Computers befindlichen Elektronik und Hardware verbirgt, mittels der Daten gespeichert werden. Buchstaben sind eine Abstraktion, die Menschen schnell verstehen können. Über den Buchstaben H zu sprechen ist im Allgemeinen sinnvoller, als sich auf „den 10. Buchstaben des Alphabets“ zu beziehen. Und wenn wir lesen oder sprechen, ist es ohnehin belanglos, dass es der 10. Buchstabe ist.

#### Worauf Sie beispielsweise achten können:

Wenn Sie eine andersartige Darstellung eines Binärcodes wählen, wie beispielsweise das Ein- und Ausschalten der Taschenlampe – welche Schüler erkennen schnell, dass dies den zuvor verwendeten Nullen und Einsen entspricht? Diese Schüler kommen vermutlich schnell mit dieser neuen Darstellungsart zurecht, während sie bei anderen Schülern unter Umständen Verwirrung stiftet. Achten Sie auf Schüler, die sich dann entschließen, ihre eigenen Darstellungen von Binärzahlen auszudenken.

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

Das Wichtigste in Bezug auf Dekomposition in dieser Aktivität ist die Folgerung, dass bei der elektronischen Datenverarbeitung alle Informationen in winzige Stückchen zerlegt werden müssen, damit sie von Computern gespeichert und als Bits und Bytes weitergeleitet werden können. Alles was in einem Computer gespeichert und auf dem Bildschirm angezeigt wird, muss in irgendeiner Form in binäre Einheiten zerlegt worden sein.

In dieser Lektion wurden von den Schülern mehrere Schritte der Dekomposition ausgeführt, während sie sich mit der Kodierung einer Nachricht beschäftigt und diese Aufgabe in einfache Schritte zerlegt haben. Um eine Nachricht in Binärcode zu schreiben, müssen wir uns zunächst die Nachricht Buchstabe für Buchstabe ansehen, dann die Buchstaben nacheinander in Dezimalzahlen umwandeln und anschließend jede dieser Zahlen, eine nach der anderen, in Binärzahlen umwandeln. Um die Nachricht in Text zurückzuverwandeln, führen die Schüler diesselben Schritte in umgekehrter Reihenfolge aus.

#### Worauf Sie beispielsweise achten können:

Können die Schüler erklären, warum es wichtig ist, Buchstaben binär darstellen zu können? Fragen Sie sie, warum es praktischer ist, einen (binären oder dezimalen) Zahlenwert zur Darstellung der einzelnen Buchstaben zu wählen, anstatt für jedes Wort eine Dezimal- und eine Binärzahl zu verwenden.

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

Das Erkennen von Mustern in der Funktionsweise des binären Zahlensystems hilft uns dabei, die damit einhergehenden Konzepte besser zu verstehen und diese Konzepte und Muster zu verallgemeinern, um sie dann auf andere Probleme anzuwenden.

#### Worauf Sie beispielsweise achten können:

Lassen Sie die Schüler eine binäre Nachricht eines Mitschülers durch Umwandeln der Binärzahlen in Dezimalzahlen und dann in Text entschlüsseln, um die Nachricht zu lesen. Fragen Sie die Schüler, was sie tun würden, wenn sie in ihrer Nachricht andere Zeichen einsetzen wollten: Was wäre, wenn wir Groß- und Kleinbuchstaben einbeziehen wollten? Was wäre, wenn wir Ausrufe- und Fragezeichen verwenden wollten? Beobachten Sie, welche Schüler erkennen, dass die bereits verwendete Methode schlichtweg verallgemeinert werden kann und wir den zusätzlichen Zeichen einfach größere Dezimalzahlen zuordnen können. Zum Beispiel: a-z kann 1-26 sein und A-Z kann 27-52 sein. Wenn wir unter Verwendung von 5 Bits für jedes Zeichen 32 verschiedene Zeichen binär darstellen können, wie viele würden wir dann für 64 benötigen? Welche Schüler bemerken das Muster des binären Systems und der Verdoppelung in dieser Situation und erkennen, dass wir dazu jeweils einfach nur ein weiteres Bit benötigen?

{panel end}

{panel type="ct-logic"}

# Logik

Zu logischem Denken gehört, basierend auf vorhandenem Wissen Entscheidungen zu treffen, wobei diese Entscheidungen sinnvoll und gut durchdacht sein sollten. Sich zu merken, dass der Buchstabe H binär als 01010 dargestellt wird, ist weniger nützlich als zu lernen, wie jedes beliebige Zeichen anhand der in dieser Aktivität beschriebenen Vorgehensweise dargestellt werden kann. Wenn wir die beim Umwandeln eines Buchstabens in eine Binärzahl befolgten logischen Schritte nachvollziehen können und verstehen, wie wir diese Zahl zurückverwandeln können, sind wir in der Lage, jedes beliebige Zeichen binär darzustellen und, was noch wichtiger ist, den zugrundeliegenden Prozess zu verstehen, da wir diesen normalerweise eher von einem Computer ausführen lassen anstatt ihn manuell durchzuführen. Dies ist insbesondere dann relevant, wenn wir eine große Anzahl an Zeichen darstellen wollen. Was wäre, wenn wir alle chinesischen Schriftzeichen darstellen wollten? Davon gibt es über 50 000 – zu versuchen, sich all diese Zeichen einzuprägen, würde sehr lange dauern! Beim Auswählen der Dezimalzahlen, die wir den einzelnen Buchstaben zuordnen möchten, hätten wir nicht unbedingt 1 bis 26 wählen müssen. Wir hätten stattdessen genauso gut bei 17 anfangen und von 17 bis 42 zählen oder ganz andere Zahlen völlig zufällig auswählen können! Was wäre, wenn wir sagen A = 82, B = 5, C = 42 … Wäre dies eine logische Entscheidung? 1 bis 26 ist viel sinnvoller, da diese Zahlenfolge viel einfacher zu beschreiben und einprägsamer ist.

#### Worauf Sie beispielsweise achten können:

Betrachten Sie die von den Schülern zur Umwandlung ihrer Buchstaben in Binärzahlen und zur Rückumwandlung erstellten Systeme. Welche Logik wurde dabei angewendet? Sind es effiziente Systeme? Können sie erklären, wie sie bei den einzelnen Schritten vorgehen? Fragen Sie die Schüler, warum wir die Zahlen 1 bis 26 verwenden, um unsere Buchstaben darzustellen, und ob sie glauben, dass es eine bessere Möglichkeit gäbe. Fragen Sie die Schüler, wie sie Zahlen für andere Zeichen wählen würden, wie beispielsweise eine Zahl zur Darstellung eines Leerzeichens. Welche Schüler geben logische Antworten und können erklären, warum ihre Lösung eine gute Wahl ist?

{panel end}

{panel type="ct-evaluation"}

# Auswertung

Im Zuge einer Auswertung kann zum Beispiel ermittelt werden, wie viele verschiedene Zeichen mit einer bestimmten Anzahl von Bits dargestellt werden können. Beispielsweise können mit 5 Bits mühelos 26 Zeichen dargestellt werden, wohingegen für eine Sprache mit 50 000 Zeichen 16 Bits benötigt werden. Wenn Informatiker sich überlegen, wie viele Bits zur Darstellung von etwas zu verwenden sind, müssen sie zudem darüber nachdenken, wie viel Platz dies auf dem Computer einnehmen wird (16-Bit-Zeichen benötigen zweimal so viel Platz wie 8-Bit-Zeichen) und ob ein paar zusätzliche Bits einzuplanen wären, falls später weitere Zeichen hinzugefügt werden sollen. Auch die Auswertung der Vorteile und Kosten der Verwendung einer bestimmten Anzahl von Bits ist ein Aspekt, der von den Schülern erkundet werden kann.

#### Worauf Sie beispielsweise achten können:

Können Schüler ausarbeiten, wie viele Bits benötigt werden, um die Zeichen einer 100 Zeichen umfassenden Sprache darzustellen? (es werden 7 Bits benötigt) Wie wäre es mit der Darstellung von Emojis, wenn wir circa 4 000 Emojis zur Verfügung haben (für jedes einzelne werden 12 Bits benötigt).

{panel end}