{panel type="ct-algorithm"}

# Algorithmisches Denken

In dieser Lektion haben wir einen Algorithmus angewendet, um eine Dezimalzahl in eine Binärzahl umzuwandeln. Es ist ein Algorithmus, da es sich um ein schrittweises Verfahren handelt, das für jede Eingabe stets die richtige Lösung liefert, solange das Verfahren genau eingehalten wird.

Hier ist ein Algorithmus in Textform, mit dem ausgerechnet werden kann, welche Punktekarten zu sehen sein sollten:

- Zunächst müssen wir die Anzahl der zu zeigenden Punkte herausfinden. (Wir bezeichnen dies als die „Anzahl der verbleibenden Punkte“, was anfangs die insgesamt zu zeigende Anzahl ist.)
- Für jede Karte, von links nach rechts (d. h. 16, 8, 4, 2 und dann 1), gilt: 
    - Wenn die Anzahl der Punkte auf der Karte höher ist als die Anzahl der verbleibenden Punkte: 
        - Karte verdecken
    - Anderenfalls: 
        - Karte zeigen
        - und die Anzahl der Punkte auf der Karte von der Anzahl der verbleibenden Punkte abziehen

Hinweis: Dieser Algorithmus (von rechts nach links vorgehen) funktioniert mit den Karten sehr gut, wenn wir hierfür jedoch Computerprogramme nachschlagen, finden wir unter Umständen einen anderen Algorithmus, bei dem von rechts nach links vorgegangen wird. Es ist nicht ungewöhnlich, dass es mehrere Algorithmen gibt, die dasselbe Ergebnis erzielen.

#### Worauf Sie beispielsweise achten können:

Welche Schüler gehen beim Umwandeln von dezimal zu binär methodisch vor? Welche Schüler beginnen mit der Karte ganz links und arbeiten sich dann Karte für Karte nach rechts vor, anstatt Karten zufällig auszuwählen und hin und her umzudrehen, bis sie zur richtigen Zahl gelangen?

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

Die binäre Darstellung von Zahlen (nur mittels 0 und 1) ist eine Abstraktion, hinter der sich die Komplexität der innerhalb eines Computers befindlichen Elektronik und Hardware verbirgt, mittels derer Daten gespeichert werden. Abstraktion hilft uns, Dinge zu vereinfachen, da wir Einzelheiten ignorieren können, die wir gegenwärtig nicht wissen müssen.

In diesem Fall können wir beispielsweise folgende Einzelheiten ignorieren: Computer nutzen physische Elemente wie elektronische Schaltkreise und Spannungen in Stromkreisen, um Daten zu speichern und weiterzuleiten, was durch zahlreiche komplexe physikalische und mathematische Theorien ermöglicht wird.

Es ist für uns völlig unerheblich, wie diese Schaltsysteme funktionieren, um Daten zu nutzen und Dinge binär darzustellen. Die Verwendung binärer Ziffernfolgen ist eine Abstraktion dieser Schaltsysteme und ermöglicht es uns, Zahlen aus Bits (Nullen und Einsen) bestehend darzustellen, Daten zu verstehen und Probleme zu lösen, ohne darüber nachdenken zu müssen, was „unter der Haube“ eines Computers vor sich geht.

Außerdem lässt sich anhand von Abstraktion überlegen, wie jede beliebige Zahl binär dargestellt werden kann. Dazu werden lediglich zwei unterschiedliche Dinge benötigt. Und es kann sich dabei um alles Mögliche handeln! Zwei verschiedene Farben, zwei verschiedene Tiere, zwei verschiedene Symbole usw. Solange es zwei davon gibt und die beiden verschieden sind, kann damit jede beliebige Zahl binär dargestellt werden, genauso wie ein Computer mithilfe von elektronischen Impulsen Daten darstellt.

Mittels binärer Ziffern kann jede Art von Daten, die auf einem Computer gespeichert ist, dargestellt werden. Bei der Darstellung anderer Formen von Daten (wie Buchstaben, Bilder und Ton) setzen wir ebenfalls Abstraktion ein, da wir die Details aller Binärzahlen darunter verbergen und lediglich dem Gesamtbild der Daten Beachtung schenken. Letztendlich werden alle Formen von Daten als Zahlen dargestellt (die wiederum eigentlich nur eine Kombination aus Bits sind) – bei Texten haben wir eine Zahl für jeden Buchstaben, bei Bildern verwenden wir eine Zahl für jede Farbe usw. Wir wenden vielerlei Abstraktionsebenen an! Eine geläufige Form von Abstraktion ist beispielsweise, dass der Monat „Oktober“ durch die Zahl zehn dargestellt werden kann, die wiederum durch die Bits 01010 dargestellt wird, und wenn diese nun im Computer als Spannungen gespeichert werden, ergibt sich für die Spannungen letztendlich die Darstellung „niedrig, hoch, niedrig, hoch, niedrig“.

#### Worauf Sie beispielsweise achten können:

Welche der Schüler können demonstrieren, wie Binärzahlen mit anderen Mitteln als „Einsen und Nullen“, „Schwarz und Weiß“ oder „Ein und Aus“ umgewandelt und dargestellt werden können (beispielsweise mittels :) und :( oder anhand von stehenden oder sitzenden Personen)? Wenn es Ihnen möglich ist, Begriffe wie „Schwarz“ und „Weiß“ mit 0 und 1 zu vertauschen, ohne dass sich die Schüler Gedanken über den Unterschied machen, wenden sie Abstraktion an.

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

Bei der Dekomposition wird beispielsweise die Umwandlung einer Zahl zur Binärzahl in die einzelnen Bits zerlegt. Die Frage „Sollte dies 1 oder 0 sein“ für jede Punktekarte zerlegt das Problem in eine Reihe von Fragestellungen.

#### Worauf Sie beispielsweise achten können:

Welche Schüler erkennen, dass es wichtig ist, mit der Karte ganz links zu beginnen und stets ein Bit nach dem anderen ins Auge zu fassen? Welche Schüler konzentrieren sich jeweils auf ein einzelnes Bit, anstatt sich selbst mit dem Versuch zu überwältigen, alle auf einen Schlag auszurechnen?

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

Das Erkennen von Mustern in der Funktionsweise des binären Zahlensystems hilft uns dabei, die damit einhergehenden Konzepte besser zu verstehen und diese Konzepte und Muster zu verallgemeinern, um sie dann auf andere Probleme anzuwenden.

Auf einem einfachen Niveau haben wir mit den Zahlen 1, 2 und 4 angefangen, die dann von den Schülern auf sich verdoppelnde Werte generalisiert wurden. Bei dieser Übung wurden 5-Bit-Zahlen verwendet, die Schüler sollten jedoch in der Lage sein, dies auf 8-Bit-Zahlen oder größer zu generalisieren.

Der Algorithmus zur Umwandlung einer Dezimalzahl in eine Binärzahl folgt einem Muster, das verallgemeinert werden kann, um die Frage des Wechselgelds bei einer Barzahlung zu lösen. Für Binärzahlen beginnen wir mit dem größten Bit und schalten es jeweils „ein“, wenn es benötigt wird, oder schalten es „aus“, wenn es nicht benötigt wird. Genauso ist es auch, wenn wir Wechselgeld geben: wir beginnen mit der größten Stückelung und fügen dann sooft wie nötig eine Münze (oder einen Geldschein) hinzu. Jargon-Hinweis: Das nennt sich gieriger Algorithmus – er versucht bei jedem Teilschritt, so viel wie möglich zu erreichen!

{panel type="math"}

# Mathematische Zusammenhänge

Fragen Sie die Schüler, was im Gegensatz zum allgemeinen Algorithmus des Wechselgeldgebens das Besondere an der Umwandlung von dezimalen zu binären Zahlen ist, und machen Sie sie darauf aufmerksam, dass im allgemeinen Fall unter Umständen mehr als eine Münze derselben Stückelung herausgegeben werden muss, während bei der binären Umwandlung immer nur ein (oder kein) Element einer jeden Einheit gegeben ist.

{panel end}

Beim binären Aufwärtszählen liegt ein Muster vor, wie oft bestimmte Karten umgedreht sind. Das erste Bit (mit 1 Punkt) wird jedes Mal umgedreht, das zweite (mit 2 Punkten) wird bei jeder zweiten Zahl umgedreht, das dritte (mit 4 Punkten) bei jeder vierten ... Gibt es ein ähnliches Muster, wenn wir in Dezimalzahlen zählen?

{image file-path="img/topics/col_binary_counting_pattern.png" alt="Binäres Zählmuster"}

Wenn wir fünf der Karten haben und alle sichtbar sind, haben wir die Zahl 31, die um eins kleiner ist als der Wert der nächsten Karte, 32. Trifft dieses Muster immer zu?

Die Anzahl der Zahlen, die mit einer bestimmten Anzahl von Bits dargestellt werden kann, entspricht dem Wert des nächsten Bit, das hinzugefügt werden kann. Beispiel: Anhand von vier Karten (1, 2, 4, 8) können 16 unterschiedliche Zahlen (0-15) dargestellt werden und die nächste Karte in der Folge ist die Zahl 16. Jedes Mal, wenn wir die nächste Karte hinzufügen, verdoppeln wir auch die Anzahl der verschiedenen Zahlen, die wir darstellen können.

Wenn wir mithilfe dieser Muster vorgehen, können wir die Beziehung zwischen der Anzahl der verwendeten Bits und ihrer Darstellungsfähigkeit besser nachvollziehen.

Erläutern Sie eines oder mehrere der folgenden Muster:

- Dass mit einer bestimmten Anzahl an Karten dieselbe Anzahl an verschiedenen Zahlen gebildet werden kann, wie die Anzahl der Punkte, die sich auf der nächsten links hinzuzufügenden Karte befinden würde (dabei stets daran denken, dass auch 0 eine Zahl ist).
- Beim Aufwärtszählen: die erste Karte (1 Punkt) wird jedes Mal umgedreht, die zweite Karte (2 Punkte) alle zwei Zahlen, die dritte (4 Punkte) alle vier Zahlen und die vierte (8 Punkte) alle acht Zahlen ...
- Dass sich, wenn alle vorhanden Karten sichtbar sind, die nächste Binärkartenzahl minus 1 ergibt.

#### Worauf Sie beispielsweise achten können:

Welche Schüler haben schnell verstanden, dass jede Karte die Zahl der Punkte verdoppelt hat? Können die Schüler die Ähnlichkeiten zwischen diesem System und dem Multiplizieren von Stellenwerten mit 10 beim Verwenden des Dezimalsystems erkennen?

Welche Schüler haben keine Mühe, die Muster umdrehender Karten beim Zählen mit Binärzahlen nachzuvollziehen?

{panel end}

{panel type="ct-logic"}

# Logik

Logisches Denken bedeutet, von bereits bekannten Regeln Gebrauch zu machen und von diesen Regeln unter Einsatz von Logik weitere Regeln und Informationen abzuleiten. Sobald wir wissen, welche Zahlen die einzelnen Binärkarten darstellen, können wir mithilfe dieses Wissens herausfinden, wie weitere Zahlen mit den Karten dargestellt werden können. Wenn wir uns nun einprägen, wie wir die mit fünf Karten möglichen Zahlen darstellen können – bedeutet dies, dass wir dann wissen, wir wir jede beliebige Zahl mit einer bestimmten Anzahl von Bits darstellen können? Das bedeutet es zwar nicht, aber wir können nachvollziehen, wie es funktioniert, wenn wir die Logik verstehen, auf deren Basis diese Zahlen mit den fünf Karten dargestellt werden.

Ein gutes Beispiel für logisches Denken in Binärzahlen ist die Argumentation dafür, warum jedes Bit einen bestimmten Wert haben „muss“ (z. B. es muss „1“ oder „0“ sein), um eine bestimmte Zahl darzustellen. Dadurch kann dann wiederum nachvollzogen werden, dass es für jede Zahl nur eine Darstellung gibt.

#### Worauf Sie beispielsweise achten können:

Erklären die Schüler ausdrücklich, dass das ganz rechts stehende Bit eine Eins sein muss, da dies die einzige ungerade Zahl und daher notwendig ist, um sämtliche ungeraden Zahlen bilden zu können? Ohne sie könnten wir nur gerade Zahlen bilden.

Können die Schüler erklären, dass jede Karte für eine bestimmte Zahl genau so gezeigt werden „muss“, wie sie es ist, z. B. dass die 16-Punkt-Karte für die Zahl 19 benötigt wird, da ohne sie nur 15 Punkte verblieben (nicht genügend), nicht jedoch für die Zahl 9, da dies zu viele Punkte ergeben würde?

{panel end}

{panel type="ct-evaluation"}

# Auswertung

Im Zuge einer Auswertung kann zum Beispiel ermittelt werden, wie viele verschiedene Werte mit einer bestimmten Anzahl von Bits dargestellt werden können (z. B. 5 Bits können 32 verschiedene Werte darstellen) und umgekehrt (um 1 000 verschiedene Werte darzustellen, werden mindestens 10 Bits benötigt).

#### Worauf Sie beispielsweise achten können:

Können Schüler den mit 4 Bits möglichen Wertebereich bestimmen? (16)

6 Bits? (64)

8 Bits? (256)

Wenn wir einer Darstellung ein weiteres Bit hinzufügen – um wie viel wird der Wertebereich dadurch erhöht? (er verdoppelt sich)

Wenn wir einer Darstellung zwei weitere Bits hinzufügen – um wie viel wird der Wertebereich dadurch erhöht? (er vervierfacht sich)

Wie viele Bits benötigen wir, um 1 000 verschiedene Werte darzustellen? (10 reichen aus)

{panel end}