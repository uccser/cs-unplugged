# Paritätsmagie

## Schlüsselfragen

- Warum ist es wichtig, dass Computer erkennen können, ob die über das Internet erhaltenen Daten dieselben sind wie die gesendeten Daten?
- Stellt euch vor, ich würde euch eine E-Mail schicken, in der steht, dass am Montag meine Klasse ausfällt, doch es gibt eine elektrische Interferenz und ein **Bit** verändert sich von "Aus" zu "An". Ihr erhaltet stattdessen eine E-Mail, in der das Wort „meine“ zu „keine“ geändert wurde. Was wäre eure Reaktion?
- Können Computer diese Art von Fehlern automatisch korrigieren? Wenn ja, wie funktioniert das?

### Mögliche Antworten wären beispielsweise:

Schüler schlagen vielleicht Situationen vor, in denen Computer eine Disk nicht lesen oder einen Code nicht scannen können, doch möglicherweise verwechseln sie diese Art von Problem auch mit anderen Störungen wie Fehlern in Programmen oder leeren Akkus.

{image file-path="img/topics/school-test-error.png" alt="Ein Schultest zeigt für jede Frage die richtige Antwort, doch die erreichte Gesamtpunktzahl beträgt 0."}

Erwachsene nutzen Computer für wichtige Dinge, beispielsweise zum Abwickeln von Bankgeschäften, zum Schreiben von Zeugnissen und zur Kommunikation mit anderen. Wenn die gespeicherten Informationen verändert werden, ohne dass es jemand bemerkt, hat man plötzlich einen falschen Kontostand (zu viel oder zu wenig), eine falsche Note im Zeugnis oder die falsche Nachricht in einer E-Mail. Oder noch schlimmer: Die Website, die man zum Lernen besuchen will oder die DVD, die man abspielen möchte, funktioniert nicht! In dieser Aktivität beschäftigen wir uns damit, wie Computer solche Fälle automatisch korrigieren.

## Lektionseinstieg

{panel type="video"}

# Unterrichtsbeispiel ansehen

{video url="https://vimeo.com/437726658"}

{panel end}

{panel type="general"}

# Hinweise zu Ressourcen

{image file-path="img/topics/parity-cards.png" alt="Ein Stapel quadratischer Karten, die auf einer Seite schwarz und auf der anderen weiß sind."}

Man braucht:

- Einen Satz von 36 Kühlschrankmagnet-Karten, die alle identisch sind und auf beiden Seiten verschiedene Farben haben (z. B. schwarz und weiß), oder nicht-magnetische Karten; in diesem Fall sollte die Demonstration auf einem Tisch oder auf dem Fußboden erfolgen. Die magnetischen Karten müssen auf beiden Seiten magnetisch sein. Dazu kann man doppelseitig magnetisches Material kaufen, denn gewöhnliche Kühlschrankmagneten bleiben meist nur auf einer Seite hängen. Man kann auch beidseitig magnetische Karten basteln, indem man einseitig magnetisches Material aufeinander klebt. Karten aus Papier (nicht magnetisch) können hergestellt werden, indem man ein Blatt festes Papier zerschneidet, das auf der Rückseite eine andere Farbe hat.
- Eine Metalltafel (im Idealfall ein Whiteboard), wenn Magnetkarten benutzt werden.
- Jedes Schülerpaar braucht einen Satz mit 36 (nicht magnetischen) Karten wie oben beschrieben.

[Hier gibt es eine interaktive Onlineversion der Paritätskarten](http://csfieldguide.org.nz/en/interactives/parity/index.html) von Computer Science Field Guide.

{panel end}

1. Lehrer/in zur Klasse: „Ich habe gerade einen Zaubertrick gelernt, den ich euch zeigen möchte.“

2. Lehrer/in zur Klasse: „Wer möchte mir assistieren?“

3. Lehrer/in gibt der Schülerin oder dem Schüler die Karten und bittet sie bzw. ihn darum, ein Gitter aus fünf mal fünf Karten zu legen (für jüngere Schüler ist es möglicherweise verständlicher, wenn man sie darum bittet, fünf Reihen mit je fünf Karten zu legen). „Leg keine Muster, versuche das Ganze so willkürlich wie möglich zu machen.“ Um den Aufbau zu beschleunigen, könnte man zwei Schüler darum bitten, diese Aufgabe zu erledigen. Sie sollten dazu ermutigt werden, kleine Lücken zwischen den Karten zu lassen und nicht zu kleinlich zu sein beim Ausrichten der Karten, sie müssen nicht ganz gerade liegen.

4. Weisen Sie darauf hin, dass die Karten Bits (binäre Einheiten) repräsentieren. Haben die Schüler Binärzahlen noch nicht durchgenommen, könnte man ihnen erklären, dass auf diese Art und Weise alles auf Computern dargestellt wird – die Karten hier könnten für eine Datei stehen, eine Nachricht, eine Webseite oder sogar ein Programm.

5. Lehrer/in zur Klasse: „Ich mache das Ganze ein bisschen schwieriger, indem ich noch eine Reihe und noch eine Spalte hinzufüge.“

{panel type="teaching"}

# Unterrichtsbeobachtungen

Natürlich machen wir das mit Absicht, denn wir wollen sicherstellen, dass die Anzahl an schwarzen Karten in jeder Reihe und in jeder Spalte eine gerade Zahl ist. Das ist immer möglich: Wenn die Schülerin oder der Schüler eine ungerade Anzahl an schwarzen Karten in eine Reihe gelegt hat, legen wir einfach eine weitere schwarze Karte in die Reihe. Hat sie bzw. er eine gerade Anzahl in die Reihe gelegt, legen wir eine weiße Karte hinzu, damit die Anzahl gerade bleibt. Wir müssen immer daran denken, dass Null eine gerade Zahl ist.

Diese zusätzlichen Karten nennen wir „Paritätsbits“ (oder Paritätskarten), aber die Terminologie muss jetzt noch nicht eingeführt werden, da sie die „Magie“ enthüllt. Fürs Erste soll die Klasse denken, dass Sie einfach nur mehr zufällige Karten hinzufügen, um die Aufgabe schwieriger zu gestalten.

Sie sollten diesen Vorgang einige Male üben, bevor Sie ihn vor der Klasse durchführen, denn durch die Routine können Sie es viel einfacher zwanglos und zufällig aussehen lassen; so wird der Trick noch mysteriöser.

{panel end}

{image file-path="img/topics/parity-cards-6x6-grid-step-1.png" alt="Fünf Reihen mit je fünf Paritätskarten in zufälliger Anordnung." caption="true"}

Schritt 1: Beispiellayout eines 5x5-Gitters, gelegt von einem Freiwilligen.

{image end}

### Schritt für Schritt wird ein Paritätsbit zu jeder Reihe und Spalte dazugelegt

{image file-path="img/topics/parity-cards.gif" alt="An animation of adding a parity bit to each row and column."}

Das letzte gelegte Paritätsbit ist sehr nützlich, denn es funktioniert immer für die Spalte und die Reihe. Wenn es nicht zur Spalte und zur Reihe passt, haben Sie bei einer der Karten einen Fehler gemacht und sollten zurückgehen und das überprüfen (versuchen Sie, das nicht zu offensichtlich zu zeigen).

{panel type="teaching"}

# Unterrichtsbeobachtungen

Nun haben Sie Paritätskarten hinzugefügt, damit die Anzahl an schwarzen Quadraten in jeder Reihe und in jeder Spalte gerade ist. Sagen Sie das den Schülern noch nicht.

{panel end}

## Lektionsaktivitäten

Lehrer/in zu Schülerin oder Schüler: „Ich möchte, dass du eine Karte umdrehst. Ich schließe dabei meine Augen.“

Lehrer/in zur Klasse: „Achtet gut darauf, welche Karte es ist, damit ihr überprüfen könnt, ob ich den Zaubertrick richtig gemacht habe!“

{panel type="teaching"}

# Unterrichtsbeobachtungen

Sie müssen betonen, dass nur eine Karte umgedreht werden soll. So stellen Sie sicher, dass nicht zu viele Karten (oder gar keine) umgedreht werden. In der Regel wird die Schülerin oder der Schüler diese Anweisung befolgen, und die anderen Schüler können Ihnen das bestätigen oder Ihnen mitteilen, dass noch keine Karte umgedreht wurde.

{panel end}

Nachdem die Klasse bestätigt hat, dass eine einzige Karte umgedreht wurde, öffnen Sie die Augen und schauen Sie sich die Karten an. Suchen Sie die Reihe mit einer ungeraden Anzahl an schwarzen Quadraten und die Spalte mit einer ungeraden Anzahl an schwarzen Quadraten. Die Karte, die umgedreht wurde, befindet sich am Schnittpunkt dieser beiden Linien. Drehen Sie die Karte lässig um, damit sie wieder die richtige Farbe hat, und sagen Sie dabei: „Es ist diese hier.“

Sie können so tun, als wäre es nur ein Glückstreffer, und den Trick wiederholen. (Nachdem Sie die Karte wieder so gedreht haben, wie sie ursprünglich lag, schauen Sie wieder weg und bitten Sie darum, dass eine andere Karte umgedreht wird.)

{image file-path="img/topics/parity-wizard.png" alt="Ein Zauberer, der einen Zauberstab mit Paritätskarten in der Hand hält." alignment="right"}

Ist es Magie? Oder ist es ein Trick?

Lehrer/in zur Klasse: „Schauen wir uns zuerst an, wie die Karten lagen, bevor eine umgedreht wurde.“ (Stellen Sie sicher, dass die Karte, die gerade umgedreht wurde, wieder richtig liegt). Folgende Schritte helfen den Schülern dabei, zu erkennen, was Sie gemacht haben:

- „Seht ihr irgendwelche Muster? Denkt nach, tut euch zusammen und teilt eure Ideen.“
- „Unterteilen wir das Ganze in Einzelschritte.“
- „Beginnen wir mit der ersten Reihe: Zählt die schwarzen Quadrate – wie viele sind es?“ 4 (im oben gezeigten Beispiel).
- „Nun die zweite Reihe: Zählt die schwarzen Quadrate – wie viele sind es?“ 2.
- Beachten Sie, dass es eine Reihe geben kann, die ausschließlich aus weißen Quadraten besteht – das wären also 0 schwarze Quadrate – oder eine Reihe mit nur schwarzen Quadraten, also 6.

Lehrer/in zur Klasse: „Was haben diese Zahlen gemeinsam?“ Die Schüler sollten bemerken, dass es alles gerade Zahlen sind. Wenn sie einen Tipp brauchen, können Sie sie fragen, ob ungerade Zahlen dabei sind.

Schauen wir uns nun die Spalten an:

- „Gilt für die erste Spalte dieselbe Regel wie bei den Reihen?“
- „Und was ist mit den anderen Spalten?“

Lehrer/in zur Klasse: „Wie ist es denn dazu gekommen, dass in jeder Reihe und in jeder Spalte eine gerade Anzahl liegt? Haben die Assistenten das so gelegt?“ (Nein, haben sie nicht!)

Nehmen Sie Ihre zusätzlich gelegte Reihe und Spalte weg und lassen Sie die Schüler erklären, welche Farbe ans Ende der ersten Reihe muss, um dafür zu sorgen, dass in dieser Reihe eine gerade Anzahl an schwarzen Karten liegt. Wenn es beispielsweise drei schwarze Karten gibt, welche Farbe muss man dann dazulegen, damit es eine gerade Zahl wird? (Schwarz). Wenn es vier schwarze Karten gibt, sollten die Schüler darauf kommen, dass man eine weiße Karte hinlegen muss, damit die Zahl gerade bleibt.

Führen Sie diesen Vorgang für alle Zeilen und dann für alle Spalten durch. Das ist eine gute Übung für Schüler, bei der sie über gerade und ungerade Zahlen nachdenken müssen. Fragen Sie die Schüler bei der letzten Karte (der Eckkarte), ob die Reihe oder die Spalte entscheidend ist. Diese sollten feststellen, dass es keinen Unterschied macht.

Wenn die zusätzliche Zeile und die zusätzliche Spalte hinzugefügt wurden, fragen Sie die Schüler: „Was passiert, wenn ich eine schwarze Karte umdrehe und sie weiß wird?“ (Die Anzahl der schwarzen Karten verringert sich um eins, es ist nun also eine ungerade Zahl). „Und wenn ich eine weiße Karte umdrehe und sie schwarz wird?“ (Die Anzahl der schwarzen Karten erhöht sich um eins, es ist also auch eine ungerade Zahl).

Die Schüler könnten so herausfinden, wie man die Karte finden kann, die umgedreht wurde. Lassen Sie aber auf jeden Fall eine Schülerin oder einen Schüler nach vorne kommen und bitten Sie sie bzw. ihn, wegzuschauen, während Sie eine Karte umdrehen. Wenn die Schülerin oder der Schüler wieder hinschaut, fragen Sie: „Ist die erste Reihe in Ordnung?“ (Sie bzw. er sollte feststellen, dass es noch eine gerade Zahl ist, also nichts verändert wurde). Machen Sie so weiter mit jeder Reihe, bis die Reihe gefunden wird, in der eine ungerade Anzahl an schwarzen Karten liegt. Kreisen Sie diese Reihe ein und sagen Sie: „Also wurde eine dieser Karten umgedreht?“ Gehen Sie nun mit den Spalten genauso vor – fragen Sie bei jeder, ob sie richtig ist, und kreisen Sie die Spalte ein, die die Schüler als nicht richtig erkennen.

Fragen Sie nun: „Welche Karte wurde also umgedreht?“ In der Regel entscheiden Schüler sich für die Karte am Schnittpunkt.

{panel type="teaching"}

# Unterrichtsbeobachtungen

Die Schüler haben nun selbst erarbeitet, wie es funktioniert. Die Schlüsselidee besteht darin, dass wir nur wenige Daten hinzugefügt haben, aber so das Original rekonstruieren können, wenn eine Karte verändert wurde.

{panel end}

{panel type="math"}

# Mathematische Zusammenhänge

Diese Lektion ist gut geeignet für Schüler, die gerade lernen, was gerade und ungerade Zahlen sind.

Außerdem wird das Konzept der Gitter geübt (Sie können Phrasen wie „5 mal 5“ nutzen) sowie die Verwendung der Ausdrücke "Spalten und Reihen".

{panel end}

## Das Gelernte anwenden

- Solche Methoden werden bei fast allen Daten angewendet, die auf Computern gespeichert oder über Computer übertragen werden (meist wird die Methode jedoch etwas abgewandelt und ist so komplexer und noch zuverlässiger). Ohne Fehlererkennung und Fehlerkorrektur gäbe es häufig unerwartete Fehler bei Daten, und man würde digitale Geräte nicht zum Speichern von wichtigen Dingen nutzen. Die Welt wäre ein einziges Chaos und Menschen würden Computern nicht vertrauen. Computer wären nicht zuverlässig und vertrauenswürdig.
- DVDs und CDs würden nicht funktionieren, wenn ein winziges bisschen Staub auf der Disk wäre.
- Sicherungskopien würden nicht viel helfen, da auch diese unzuverlässig wären.
- Datenübertragungen über große Entfernungen (z. B. von Raumsonden) wären besonders unzuverlässig, da es Minuten oder sogar Tage dauern kann, bis die Daten ankommen und sie nicht erneut angefordert werden können, wenn es eine Interferenz gab.

## Lektionsbetrachtung

Versuchen Sie es mit anderen Gegenständen. Es eignet sich alles, was zwei leicht zu unterscheidende „Zustände“ hat. Sie könnten beispielsweise Spielkarten nehmen, Münzen (Kopf oder Zahl) oder Karten, auf denen 0 und 1 steht (so kann die Verbindung zum binären Zahlensystem geschaffen werden).

Was passiert, wenn zwei oder mehr Karten umgedreht werden? (Es kann nicht herausgefunden werden, welche beiden Karten umgedreht wurden, es kann aber erkannt werden, dass sich etwas geändert hat. Die Suche nach den umgedrehten Karten lässt sich in der Regel auf ein oder zwei Kartenpaare eingrenzen. Bei vier umgedrehten Karten ist es möglich, dass alle Paritätsbits hinterher richtig sind; der Fehler könnte also unbemerkt bleiben.)

Eine weitere interessante Übung besteht darin, die Karte rechts unten anzuschauen. Wenn sie für die Spalte nach oben richtig ist, ist sie dann auch für die Reihe nach links richtig? (Die Antwort ist immer ja. Bei dieser Kartenübung haben wir eine gerade Parität genutzt – eine gerade Anzahl an schwarzen Karten. Geht es auch mit ungerader Parität? (Das ist möglich, aber die Karte unten rechts ist nur gleich für Reihe und Spalte, wenn sowohl die Anzahl der Reihen als auch die der Spalten gerade bzw. ungerade ist. Beispielsweise funktioniert ein Layout mit 5x9, eins mit 4x6 auch, aber eins mit 3x4 nicht.)