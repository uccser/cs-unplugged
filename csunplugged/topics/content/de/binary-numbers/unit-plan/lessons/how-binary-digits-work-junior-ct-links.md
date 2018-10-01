{panel type="ct-algorithm"}

# Algorithmisches Denken

In dieser Lektion haben wir einen Algorithmus angewendet, um eine Dezimalzahl in eine Binärzahl umzuwandeln. Es ist ein Algorithmus, da es sich um ein schrittweises Verfahren handelt, das für jede Eingabe stets die richtige Lösung liefert, solange das Verfahren genau eingehalten wird.

Hier ist ein Algorithmus in Textform, mit dem ausgerechnet werden kann, welche Punktekarten zu sehen sein sollten:

- Zunächst müssen wir die Anzahl der zu zeigenden Punkte herausfinden. (Wir bezeichnen dies als die „Anzahl der verbleibenden Punkte“, was anfangs die insgesamt zu zeigende Anzahl ist.)

- Für jede Karte, von links nach rechts (d. h. 8, 4, 2 und dann 1), gilt:
    
    - Wenn die Anzahl der Punkte auf der Karte höher ist als die Anzahl der verbleibenden Punkte:
        
        - Karte verdecken
    
    - Anderenfalls:
        
        - Karte zeigen
        
        - und die Anzahl der Punkte auf der Karte von der Anzahl der verbleibenden Punkte abziehen

#### Worauf Sie beispielsweise achten können:

Welche Schüler gehen beim Umwandeln von dezimal zu binär methodisch vor? Welche Schüler beginnen mit der Karte ganz links und arbeiten sich dann Karte für Karte nach rechts vor, anstatt Karten zufällig auszuwählen und hin und her umzudrehen, bis sie zur richtigen Zahl gelangen?

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

Abstraktion und abstraktes Denken sind für jüngere Schüler in der Regel schwer nachvollziehbar. Für sie ist daher sicherlich nur ein geringer Teil dieser Lektion geeignet. Wir haben diese Ausführungen jedoch hier miteinbezogen, da sie nützliches Hintergrundwissen zum Unterrichten dieses Themas darstellen.

Abstraktion hilft uns, Dinge zu vereinfachen, da wir Einzelheiten ignorieren können, die wir gegenwärtig nicht wissen müssen. Die binäre Darstellung von Zahlen ist eine Abstraktion, hinter der sich die Komplexität der innerhalb eines Computers befindlichen Elektronik und Hardware verbirgt, mittels der Daten gespeichert werden.

In diesem Fall können wir beispielsweise folgende Einzelheiten ignorieren: Computer nutzen physische Elemente wie elektronische Schaltkreise und Spannungen in Stromkreisen, um Daten zu speichern und weiterzuleiten, was durch zahlreiche komplexe physikalische und mathematische Theorien ermöglicht wird.

Es ist für uns völlig unerheblich, wie diese Schaltsysteme funktionieren, da wir anhand der binären Abstraktion in Zahlen, die aus Bits (Nullen und Einsen) bestehen, Daten begreifen und Probleme lösen können, ohne darüber nachdenken zu müssen, was „unter der Haube“ des Computers vor sich geht.

Außerdem lässt sich anhand von Abstraktion überlegen, wie jede beliebige Zahl binär dargestellt werden kann. Dazu werden lediglich zwei unterschiedliche Dinge benötigt. Und es kann sich dabei um alles Mögliche handeln! Zwei unterschiedliche Farben, Tiere, Symbole usw. Solange es zwei davon gibt und die beiden verschieden sind, kann damit jede beliebige Zahl binär dargestellt werden, genauso wie ein Computer mithilfe von elektronischen Impulsen Daten darstellt.

#### Worauf Sie beispielsweise achten können:

Welche der Schüler können demonstrieren, wie Binärzahlen mit anderen Mitteln als „Einsen und Nullen“, „Schwarz und Weiß“ oder „Ein und Aus“ umgewandelt und dargestellt werden können (beispielsweise mittels :] und :[ oder anhand von stehenden oder sitzenden Personen)? Wenn es Ihnen möglich ist, Begriffe wie „Schwarz“ und „Weiß“ mit 0 und 1 zu vertauschen, ohne dass sich die Schüler Gedanken über den Unterschied machen, wenden sie Abstraktion an.

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

Bei der Dekomposition wird beispielsweise die Umwandlung einer Zahl zur Binärzahl in die einzelnen Bits zerlegt. Die Frage „Sollte dies 1 oder 0 sein“ für jede Punktekarte zerlegt das Problem in eine Reihe von Fragestellungen.

#### Worauf Sie beispielsweise achten können:

Welche Schüler erkennen, dass es wichtig ist, mit der Karte ganz links zu beginnen und stets ein Bit nach dem anderen ins Auge zu fassen? Welche Schüler konzentrieren sich jeweils auf ein einzelnes Bit, anstatt sich selbst mit dem Versuch zu überwältigen, alle auf einen Schlag auszurechnen?

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

Das Erkennen von Mustern in der Funktionsweise des binären Zahlensystems hilft uns dabei, die damit einhergehenden Konzepte besser zu verstehen und diese Konzepte und Muster zu verallgemeinern, um sie dann auf andere Probleme anzuwenden. Jüngeren Schülern könnte es etwas schwerer fallen, diese Muster zu verallgemeinern, doch allein das Erkennen der Muster ist eine gute Übung.

Auf einem einfachen Niveau haben wir mit den Zahlen 1, 2 und 4 angefangen, die dann von den Schülern auf sich verdoppelnde Werte generalisiert wurden. Bei dieser Übung wurde zu 4-Bit-Zahlen umgewandelt, doch manche Schüler (die in der Lage sind, hoch genug zu zählen), können dies unter Umständen auf weitere 8-Bit-Zahlen oder größer generalisieren.

Der Algorithmus zur Umwandlung einer Dezimalzahl in eine Binärzahl folgt einem Muster, das verallgemeinert werden kann, um die Frage des Wechselgelds bei einer Barzahlung zu lösen. Für Binärzahlen beginnen wir mit dem größten Bit und schalten es „ein“, wenn es benötigt wird, oder schalten es „aus“, wenn es nicht benötigt wird. Genauso ist es auch, wenn wir Wechselgeld geben: wir beginnen mit der größten Stückelung und nehmen dann sooft wie nötig eine Münze (oder einen Geldschein). Jargon-Hinweis: Das nennt sich gieriger Algorithmus.

{panel type="math"}

# Mathematische Zusammenhänge

Fragen Sie die Schüler, was im Gegensatz zum allgemeinen Algorithmus des Wechselgeldgebens das Besondere an der Umwandlung von dezimalen zu binären Zahlen ist, und machen Sie sie darauf aufmerksam, dass im allgemeinen Fall unter Umständen mehr als eine Münze derselben Stückelung herausgegeben werden muss, während bei der binären Umwandlung immer nur ein (oder kein) Element einer jeden Einheit gegeben ist.

{panel end}

Beim binären Aufwärtszählen liegt ein Muster vor, wie oft bestimmte Karten umgedreht sind. Das erste Bit (mit 1 Punkt) wird jedes Mal umgedreht, wenn wir um eins vorwärts zählen, das zweite (mit 2 Punkten) wird bei jeder zweiten Zahl umgedreht, das dritte (mit 4 Punkten) bei jeder vierten … Gibt es ein ähnliches Muster, wenn wir in Dezimalzahlen zählen?

{image file-path="img/topics/col_binary_counting_pattern.png" alt="Binäres Zählmuster"}

Wenn wir vier der Karten haben und alle sichtbar sind, haben wir die Zahl 15, die um eins kleiner ist als der Wert der nächsten Karte, 16. Trifft dieses Muster immer zu?

Die Anzahl der Zahlen, die mit einer bestimmten Anzahl von Bits dargestellt werden kann, entspricht dem Wert des nächsten Bit, das hinzugefügt werden kann. Beispiel: Anhand von vier Karten (1, 2, 4, 8) können 16 unterschiedliche Zahlen (0-15) dargestellt werden und die nächste Karte in der Folge ist die Zahl 16. Jedes Mal, wenn wir die nächste Karte hinzufügen, verdoppeln wir auch die Anzahl der verschiedenen Zahlen, die wir darstellen können.

Wenn wir mithilfe dieser Muster vorgehen, können wir die Beziehung zwischen der Anzahl der verwendeten Bits und ihrer Darstellungsfähigkeit besser nachvollziehen.

#### Worauf Sie beispielsweise achten können:

Welche Schüler erkennen schnell, dass jede Karte die Anzahl der Punkte verdoppelt? Welche Schüler verstehen mühelos die Muster umgedrehter Karten beim Zählen mit Binärzahlen?

{panel end}

{panel type="ct-logic"}

# Logik

Logisches Denken bedeutet, von bereits bekannten Regeln Gebrauch zu machen und von diesen Regeln unter Einsatz von Logik weitere Regeln und Informationen abzuleiten. Sobald wir wissen, welche Zahlen die einzelnen Binärkarten darstellen, können wir mithilfe dieses Wissens herausfinden, wie weitere Zahlen mit den Karten dargestellt werden können. Wenn wir uns einprägen, wie wir die mit vier Karten möglichen Zahlen darstellen können – bedeutet dies, dass wir dann wissen, wir wir jede beliebige Zahl mit einer beliebigen Anzahl von Bits darstellen können? Das bedeutet es zwar nicht, aber wir können nachvollziehen, wie es funktioniert, wenn wir die Logik verstehen, auf deren Basis diese Zahlen mit den vier Karten dargestellt werden.

Ein gutes Beispiel für logisches Denken in Binärzahlen ist die Argumentation dafür, warum jedes Bit einen bestimmten Wert „haben muss“ (z. B. es muss „ein“ oder „aus“ sein), um eine bestimmte Zahl darzustellen. Dies wiederum führt zu dem Argument, dass es für jede Zahl nur eine Darstellung gibt.

#### Worauf Sie beispielsweise achten können:

Erklären die Schüler ausdrücklich, dass das erste Bit eine Eins sein muss, da dies die einzige ungerade Zahl und daher notwendig ist, um sämtliche ungeraden Zahlen bilden zu können? Ohne sie könnten wir nur gerade Zahlen bilden. Können die Schüler erklären, dass jede Karte für eine bestimmte Zahl genau so gelegt „sein muss“, wie sie es ist, z. B. wird die 8-Punkt-Karte für die Zahl 9 benötigt, da ohne sie nur 7 Punkte verblieben (nicht genügend), nicht jedoch für die Zahl 6, da dies zu viele Punkte ergeben würde?

{panel end}

{panel type="ct-evaluation"}

# Auswertung

Im Zuge einer Auswertung kann zum Beispiel ermittelt werden, wie viele verschiedene Werte mit einer bestimmten Anzahl von Bits dargestellt werden können (z. B. 4 Bits können 16 verschiedene Werte darstellen) und umgekehrt (um 1 000 verschiedene Werte darzustellen, werden mindestens 10 Bits benötigt).

#### Worauf Sie beispielsweise achten können:

Können Schüler den mit 2 Bits möglichen Wertebereich bestimmen? (4)

3 Bits? (8)

4 Bits? (16)

Wenn wir einer Darstellung ein weiteres Bit hinzufügen – um wie viel wird der Wertebereich dadurch erhöht? (er verdoppelt sich)

{panel end}