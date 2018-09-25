# Mögliche Abwandlungen eines Sortiernetzwerks

## Erforderliche Vorkenntnisse

Schüler sollten über das Grundwissen zu Sortiernetzwerken aus Lektion 1 verfügen.

## Schlüsselfragen

- Könnte man mit einem Sortiernetzwerk eventuell auch andere Dinge als Zahlen sortieren? Was könnten wir beispielsweise noch sortieren? (Mögliche Antworten wären beispielsweise: Dinge nach Farbe, Format, Alter oder Größe zu sortieren).

## Lektionseinstieg

Zeigen Sie den Schülern das Sortiernetzwerk erneut (Schüler finden oft Gefallen daran, das Netzwerk bei Bedarf nochmals neu zu zeichnen, und es vom Strukturdiagramm abzuzeichnen, ist eine nützliche Übung). Deuten Sie an, dass dieses Mal ein paar Abwandlungen ins Spiel kommen.

{panel type="math"}

# Mathematische Zusammenhänge

Ergebnisse voraussehen: Durch Nachvollziehen der Funktionsweise von Sortiernetzwerken untersuchen Schüler verschiedene Möglichkeiten der Verwendung des Sortiernetzwerks und erkunden, warum die niedrigste und die höchste Zahl stets an der richtigen Ausgabeposition ankommen.

{panel end}

## Abwandlungen

Dieser Teil der Lektion behandelt weitere Möglichkeiten, mit den Zahlen zu arbeiten.

### Abwandlung 1: Identischer Wert

{image file-path="img/topics/sorting-network-equal-3.png" alt="Zwei Personen, die jeweils eine Karte mit der Zahl 3 darauf hochhalten."}

Bei dieser Abwandlung testen die Schüler das Sortiernetzwerk mit einem Satz Karten, bei dem einige Karten identische Werte haben, wie beispielsweise 1, 2, 3, 3, 4, 5. Vermutlich werden die Schüler fragen, was zu tun ist, wenn sie zwei identische Karten vergleichen – fragen Sie zurück, was sie denken, und sie werden wahrscheinlich erkennen, dass es keinen Unterschied macht (wenn sich 3 und 3 treffen spielt es keine Rolle, welche Zahl nach links und welche nach rechts geht!). Stellen Sie den Schülern die Aufgabe vorauszusehen, was am Ende des Netzwerks passieren wird (eventuell erkennen sie, dass identische Werte nebeneinander landen werden).

Lassen Sie nun die Zahlen zur Überprüfung das Netzwerk durchlaufen. Hier ist eine kurze Zusammenfassung der Anweisungen für das Sortiernetzwerk; ausführliche Details sind in Lektion 1 zu finden.

1. Sechs Schüler starten in den Eingabekreisen, wobei jeder eine Karte mit einer der Zahlen darauf hält.

2. Alle gehen gleichzeitig los und wenn sie in einem Quadrat auf jemanden treffen, vergleichen sie ihre Karten.

3. Die Person mit der niedrigeren Karte folgt der Linie nach links und die Person mit der höheren Karte der Linie nach rechts (in der zweiten Abwandlung dieser Lektion ist dies genau umgekehrt).

4. Dies wird fortgesetzt, bis alle Schüler die Ausgabekreise erreichen, wo sie sich dann in geordneter Reihenfolge befinden sollten.

### Abwandlung 2: Größere nach links

Dieses Mal geht die Person mit der größeren Zahl nach links anstatt nach rechts und folgt der Linie zum nächsten Quadrat, während die Person mit der niedrigeren Zahl nach rechts anstatt nach links geht und so der Linie zum nächsten Quadrat folgt.

Bitten Sie die Schüler vorauszusehen, was passieren wird (sie sollten sich ausrechnen können, dass die Werte in umgekehrter Reihenfolge, d. h. von der größten zur kleinsten anstatt von der kleinsten zur größten, herauskommen werden).

Lassen Sie es die Schüler mit ein paar Zahlen ausprobieren, um es zu überprüfen.

{panel type="teaching"}

# Unterrichtsbeobachtungen

Wenn wir die Links/Rechts-Entscheidung umkehren, erhalten wir eine umgekehrte Reihenfolge des in Lektion 1 erzielten Ergebnisses.

{panel end}

### Abwandlung 3: Buchstaben des Alphabets

{image file-path="img/topics/sorting-network-variation-alphabet.png" alt="Karten mit Buchstaben darauf."}

Geben Sie den Schülern Karten mit Buchstaben darauf. Fragen Sie, wie die Karten verglichen werden könnten (Schüler sollten erkennen, dass eine alphabetische Reihenfolge möglich wäre). Lassen sie es die Schüler durch Ordnen der Karten ausprobieren.

## Umgekehrte Anwendung des Netzwerks

Dieses Experiment geht auf eine möglicherweise von Schülern gestellte Frage ein: Werden die Werte durch das Sortiernetzwerk richtig geordnet, wenn wir am anderen Ende beginnen?

Lassen Sie es die Schüler mit ein paar einfachen Werten (wie beispielsweise die Zahlen 1 bis 6) ausprobieren. Aller Wahrscheinlichkeit nach wird dies für etliche Ausgangsreihenfolgen der Werte funktionieren. Regen Sie die Schüler jedoch dazu an, es weiter zu versuchen, bis sie eine Ausgangsreihenfolge finden, für die es nicht funktioniert. Um dies zu erreichen, muss in hohem Maße logisch gedacht werden.

Wenn es den Schülern schwer fällt, ein Beispiel zu finden, können Sie ihnen das unten genannte Beispiel geben und sie dann auffordern, ein weiteres zu finden, das zu keinem geordneten Ergebnis führt.

{panel type="teaching"}

# Unterrichtsbeobachtungen

Das Sortiernetzwerk ist dazu ausgelegt, konsistent in eine Richtung und nicht in zwei Richtungen zu funktionieren. Zum Beispiel zeigt die erste Abbildung unten eine Eingabe, die zufällig geordnet herauskommt, wenn das Netzwerk rückwärts durchlaufen wird, während dies bei der zweiten Eingabe nicht der Fall ist. Wenn es bei nur einer Eingabe (der zweiten) scheitert, können wir uns nicht darauf verlassen, auch wenn es manchmal funktioniert. In die andere Richtung wird es die Zahlen stets richtig ordnen.

{image file-path="img/topics/sorting-network-backwards-1.png" alt="Diese Darstellung zeigt, dass uns das Sortiernetzwerk die Eingabe 654321 bei umgekehrter Ausführung in geordneter Reihenfolge zurückgibt."}

{image file-path="img/topics/sorting-network-backwards-2.png" alt="Diese Darstellung zeigt, dass uns das Sortiernetzwerk die Eingabe 512364 bei umgekehrter Ausführung nicht in geordneter Reihenfolge zurückgibt."}

{panel end}

## Das Gelernte anwenden

Diese Art von Algorithmus muss auf spezialisierter Hardware ausgeführt werden, um mehrere Vergleichsvorgänge gleichzeitig vornehmen zu können. Derartige Algorithmen werden gegenwärtig nur für spezialisierte Programme verwendet, beispielsweise werden sie mitunter auf dem Grafikprozesser (GPU) eines Computers ausgeführt, da diese Prozessoren gut für die parallele Verarbeitung geeignet sind. Sortiernetzwerke wurden lange vor der Entwicklung leistungsfähiger GPUs erfunden. Dies ist eine interessante Sache an der Informatik – einige unserer Entdeckungen sind der verfügbaren Hardware weit voraus. Wir sind also für die Nutzung der Hardware gerüstet, wenn sie allseits zur Verfügung stehen wird! Hinweis: Dies ist *kein* konventioneller Sortieralgorithmus, da das in einem konventionellen System ausgeführte Sortieren nur jeweils einen Vergleich anstellen kann. Konventionelle Sortieralgorithmen werden in einer anderen Lektion behandelt.

## Lektionsbetrachtung

Was ist euch bei jeder Abwandlung der Verwendung des Sortiernetzwerks aufgefallen?

Hattet ihr damit gerechnet?