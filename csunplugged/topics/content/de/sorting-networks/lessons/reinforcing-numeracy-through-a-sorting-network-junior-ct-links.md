{panel type="ct-algorithm"}

# Algorithmisches Denken

In dieser Lektion haben wir einen Algorithmus verwendet, um die Zahlen mithilfe eines Parallelprozessors in eine Reihenfolge zu ordnen (normalerweise wäre dieser Prozessor in eine Hardware eingebaut, aber unser Kreidenetzwerk ist ja auch einer! Es wird nur von Menschen anstatt von Strom angetrieben).

#### Worauf Sie beispielsweise achten können:

Verstehen die Schüler, wie die einzelnen Knotenpunkte funktionieren (zwei Werte annehmen und diese zu tauschen, wenn sie in der falschen Reihenfolge sind)? Können sie anderen Schülern erklären, wie das Netzwerk richtig angewendet wird?

Erkennen die Schüler, dass wir unabhängig davon, welche Zahlen oder Daten wir in das Netzwerk eingeben, stets eine Lösung erhalten, wenn wir den Algorithmus genau befolgen?

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

Das bei diesen Aktivitäten verwendete Sortiernetzwerk ist an sich eine abstrakte Darstellung davon, wie Sortiernetzwerke in Hardware und Software ausgeführt werden. Es stellt die Kernfunktionalitäten eines Sortiernetzwerks dar, während alle wesentlichen Funktionsdetails der Hardware und der Schaltkreise verborgen bleiben.

#### Worauf Sie beispielsweise achten können:

Sind die Schüler in der Lage, zwischen den Linien und Knotenpunkten dieser grafischen Darstellung und der Art und Weise, wie Computer durch Vergleichsvorgänge Daten verarbeiten, eine Verbindung herzustellen? Verstehen die Schüler, dass anhand dieser Darstellung vorgeführt werden kann, wie ein echter Parallelcomputer arbeiten würde?

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

Der gesamte Prozess des Sortierens in dieser Aktivität ist in eine äußerst einfache Operation zerlegt: zwei Werte vergleichen. Die Operation an sich ist sehr simpel, wenn sie jedoch viele, viele Male ausgeführt wird, kann damit eine Lösung zu einer viel größeren Aufgabenstellung aufbaut werden.

#### Worauf Sie beispielsweise achten können:

Verstehen die Schüler, wie ein Sortiernetzwerk erstellt wird, um nur zwei Werte zu sortieren? (Es wäre nur ein einziger Komparatorknotenpunkt.)

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

In dieser Lektion haben die Schüler nur mit einer Art von Daten, nämlich Zahlen, gearbeitet, so dass Generalisierung wenig zum Tragen kam. Dies wird in der nächsten Lektion eingehender behandelt.

{panel end}

{panel type="ct-evaluation"}

# Auswertung

Bei diesem Sortiernetzwerk können bis zu drei Vergleiche gleichzeitig vorgenommen werden und die Länge des Netzwerks bestimmt, wie lange es dauern würde, all diese Vergleiche durchzuführen. Obgleich beim Durchlaufen des Netzwerks 12 Vergleiche vorgenommen werden müssen, kann das Netzwerk in der Zeit durchlaufen werden, die ein einzelner Knotenpunkt dazu benötigt, 5 Vergleich vorzunehmen.

#### Worauf Sie beispielsweise achten können:

Können die Schüler den längsten Pfad bestimmen, den eine beliebige Zahl durchlaufen müsste, um ans Ende zu gelangen? (Die zwei mittleren Zahlen müssen fünf Vergleiche vornehmen.) Können die Schüler erklären, dass der Sortiervorgang in 5 x 2 Sekunden und nicht 12 x 2 Sekunden abgeschlossen wäre, wenn jeder Vergleich circa zwei Sekunden dauern würde?

{panel end}

{panel type="ct-logic"}

# Logik

Der kleinste Wert nimmt bei jedem Vergleichsvorgang stets den linken Pfad und jeder Pfad, der von einem Startpunkt aus nach links abzweigt, führt zu diesem Knotenpunkt. Daher kommt der kleinste Wert am Ende stets an der ganz linken Position an.

#### Worauf Sie beispielsweise achten können:

Können die Schüler erklären, wo der kleinste Wert ankommen wird, unabhängig davon, was die anderen Werten sind? Verstehen die Schüler die Funktion der einzelnen Knotenpunkte? Vermeiden sie es, einfach zum letzten Knotenpunkt zu gehen, ohne die Vergleiche durchzuführen?

{panel end}