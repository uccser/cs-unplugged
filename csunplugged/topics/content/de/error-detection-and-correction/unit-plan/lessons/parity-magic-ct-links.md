{panel type="ct-algorithm"}

# Algorithmisches Denken

Der schrittweise Vorgang zum Zählen der schwarzen Quadrate in jeder Reihe und zum Erkennen, ob die Parität gerade ist, und die Wiederholung dieses Prozesses für jede Spalte ist ein Beispiel für einen Algorithmus. Der vollständige Algorithmus zur Fehlererkennung beinhaltet auch eine Lösung für den Fall, dass ein Fehler gefunden wird.

#### Worauf man beispielsweise achten könnte:

Können die Schüler die umgedrehte Karte in einem Gitter sicher erkennen? Können sie anderen Schülern den Algorithmus erklären, damit auch diese die Aufgabe ausführen können?

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

Jede der Karten in dieser Aktivität steht für ein Bit in einem digitalen Gerät. Wenn wir all unsere ‚Bits‘ im Quadrat anordnen, ist das eine Darstellung von Daten (bei diesem Zaubertrick sind das natürlich zufällige Daten, man könnte aber auch echte Daten nehmen!). Das bedeutet, dass unser Gitter eine Abstraktion ist, denn es handelt sich um ein Modell, das beliebige Daten darstellen kann, die auf einem digitalen Gerät gespeichert werden können, beispielsweise eine Audiodatei, ein Video oder sogar ein Stück Code!

#### Worauf man beispielsweise achten könnte:

Können die Schüler erklären, dass jede Karte ein Bit ist und dass die Karten Daten repräsentieren? Können die Schüler die Verbindung zwischen dem Kartengitter und einem Datensatz aus Bytes sehen?

{panel end}

{panel type="ct-decomposition"}

# Zerlegung

Um diese Aufgabe zu erfüllen, müssen die Schüler den Prozess „Finde den Fehler“ in kleinere Schritte zerlegen. Der erste Schritt der Zerlegung könnte so aussehen: „Ich schaue eine Reihe nach der anderen an, bis ich einen Fehler finde“. Schüler können den Prozess weiter zerlegen, indem sie sich auf eine Reihe konzentrieren und sich fragen, ob es in dieser Reihe eine gerade oder eine ungerade Anzahl an schwarzen Karten gibt. Sie zerlegen das größere Problem in Teilaufgaben, die sie dann bearbeiten können, um so der Lösung für das ganze Problem näherzukommen. Wenn sie die Spalte mit dem Fehler finden müssen, können sie diese Aufgabe genauso zerlegen, indem sie sich auf eine Spalte konzentrieren und die gleiche Frage stellen wie zuvor: Ist die Anzahl der schwarzen Karten in dieser Spalte gerade oder ungerade? Diese Teilaufgaben sind viel einfacher zu lösen als das große Problem „Finde den Fehler“, doch wenn man sie alle sorgfältig bearbeitet, hat man das große Problem gelöst!

#### Worauf man beispielsweise achten könnte:

Können die Schüler die Aufgabe in einzelne Schritte unterteilen und diese Schritte beschreiben, ohne dass man ihnen zuerst den Algorithmus erklärt?

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

Haben die Schüler den Algorithmus verstanden, mit dem man die umgedrehte Karte finden kann, können sie eine (einzelne) umgedrehte Karte in einem beliebig großen Gitter finden. Ein Gitter mit 10x10 (100 Karten) kann man schnell legen, und sogar ein Gitter mit 20x20 Karten ist möglich, wenn man genug Zeit (und genug Karten!) hat. Die Schüler können das Problem „Finde den Fehler in einem **6x6-Gitter**“ verallgemeinern zu „Finde den Fehler in **einem Gitter**“.

#### Worauf man beispielsweise achten könnte:

Können die Schüler die umgedrehte Karte in größeren Gittern finden?

{panel end}

{panel type="ct-evaluation"}

# Auswertung

Mit dem Paritätstrick kann man immer Fehler erkennen und korrigieren, wenn ein Bit umgedreht wurde. Es ist jedoch wichtig, zu prüfen, ob dieser Algorithmus auch bei anderen Arten von Fehlern angewendet werden kann. Wenn nicht nur eine Karte umgedreht wurde (es also mehr als einen Fehler gibt), können wir zwar feststellen, dass mit den Daten etwas nicht stimmt, aber unser Algorithmus kann uns nicht sagen, wie wir das Problem beheben können! Was noch schlimmer ist: Wenn mehr als zwei Bits umgedreht wurden, können wir den Fehler manchmal gar nicht erkennen! Es ist wichtig, dass wir diesen Algorithmus beurteilen, denn wenn er nicht immer funktioniert, müssen wir das wissen. Informatiker evaluieren Algorithmen wie diesen und verbessern sie, wenn sie auf ein Problem stoßen.

#### Worauf man beispielsweise achten könnte:

Fragen Sie die Schüler: „Welche Arten von Fehlern können mit den Paritätskarten entdeckt und korrigiert werden? Wann kann man einen Fehler nur entdecken, aber nicht korrigieren? Warum ist das so?“

Können die Schüler erklären, was nicht funktioniert, wenn wir versuchen, den Fehler zu finden, wenn zwei Karten umgedreht wurden?

{panel end}

{panel type="ct-logic"}

# Logik

Beim Umdrehen einer Karte verändert sich die Anzahl in einer Reihe/Spalte immer von gerade zu ungerade, unabhängig davon, wie die Karte aussieht und wie die anderen Karten in der Reihe/Spalte aussehen.

Der Gedanke, dass die Eckkarte sowohl für die neue Reihe als auch für die Spalte richtig ist, ist ein fortschrittliches Konzept, doch manche Schüler erkennen dieses Muster möglicherweise.

#### Worauf man beispielsweise achten könnte:

Können die Schüler erklären, warum die Anzahl der schwarzen Karten durch das Umdrehen einer einzelnen Karte immer ungerade wird?

Können die Schüler erklären, warum die Eckkarte sowohl für die Reihe als auch für die Spalte richtig ist? (Diese Aufgabe erfordert tieferes logisches Denken).

{panel end}