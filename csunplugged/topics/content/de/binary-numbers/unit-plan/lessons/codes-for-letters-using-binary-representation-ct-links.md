{panel type="ct-algorithm" title="Algorithmisches Denken"}

Wir haben in dieser Lektion zwei Algorithmen verwendet: einen, um einen Buchstaben in eine Dezimalzahl und dann in eine Binärzahl umzuwandeln, und umgekehrt.
Dies sind Algorithmen, weil sie ein Schritt-für-Schritt-Prozess sind, der immer die richtige Lösung für jede Eingabe gibt, die Sie ihm geben, solange der Prozess genau befolgt wird.

Hier ist ein Algorithmus zum Konvertieren eines Buchstabens in eine Dezimalzahl:

Wählen Sie einen Buchstaben aus, der in eine Dezimalzahl konvertiert werden soll. Suchen Sie die numerische Position des Buchstabens im Alphabet wie folgt:

- Sagen Sie "A" (der erste Buchstabe im Alphabet)
- Sagen Sie "1" (der erste Buchstabe in unserer Zahlenfolge)
     - Wiederhole die folgenden Anweisungen, bis du zu dem Buchstaben kommst, den du suchen möchtest
         - Sag den nächsten Buchstaben im Alphabet
         - Sagen Sie die nächste Nummer (um 1 höher)
- Die gerade angegebene Zahl ist die Dezimalzahl, die auch Ihr Brief konvertiert.

Um zum Beispiel den Buchstaben E zu konvertieren, müsste der Algorithmus A, 1; B, 2; C, 3; D 4; E, 5.

{image file-path="img/topics/binary_count_girl.png" alt="Girl thinking about the algorithm"}

(Ein effizienterer Algorithmus würde eine Tabelle haben, die ähnlich wie die zu Beginn der Aktivität erstellte Tabelle ist, und die meisten Programmiersprachen können direkt von Zeichen in Zahlen umwandeln, mit der bemerkenswerten Ausnahme von Scratch, die den obigen Algorithmus verwenden muss .)

Der nächste Algorithmus ist derselbe Algorithmus, den wir in Lektion 1 verwendet haben, mit dem wir eine Dezimalzahl in eine Binärzahl umwandeln:

- Finden Sie heraus, wie viele Punkte angezeigt werden sollen. (Dies wird als die "Anzahl verbleibender Punkte" bezeichnet, die anfangs die Gesamtanzahl ist, die angezeigt werden soll.)
- Für jede Karte von links nach rechts (d. H. 16, 8, 4, 2 und dann 1):
  - Wenn die Anzahl der Punkte auf der Karte größer ist als die Anzahl der verbleibenden Punkte:
      - Verstecke die Karte
  - Andernfalls:
      - Zeige die Karte
      - Subtrahieren Sie die Anzahl der Punkte auf der Karte von der Anzahl der verbleibenden Punkte

#### Beispiele für das, wonach Sie suchen könnten:

Lassen Sie die Schüler Anweisungen für die Konvertierung eines Buchstabens in eine Dezimalzahl (mit oder ohne Tabelle) erstellen oder demonstrieren und konvertieren Sie dann eine Dezimalzahl in Binär; Können sie eine systematische Lösung zeigen?
Können sie erklären, was sie bei jedem Schritt tun und warum?

{panel end}
