{panel type="video"}

# Unterrichtsbeispiel ansehen

Hier finden Sie ein Unterrichtsbeispiel zu Sortiernetzwerken:

{video url="https://vimeo.com/437722996"}

Die folgenden Videos zeigen weitere Beispiele zu Sortiernetzwerken:

- [Video 1](https://vimeo.com/437726931)
- [Video 2](https://vimeo.com/437726955)

{panel end}

Nachdem Computer immer mehr zu unserem Alltag gehören und die von uns genutzte Datenmenge beständig ansteigt, möchten wir natürlich, dass Computer all diese Daten so schnell wie möglich verarbeiten. Die Geschwindigkeit eines Computers kann zum einen mithilfe von Programmen beschleunigt werden, die weniger rechnerische Schritte anwenden (wie in den Lektionen zu Sortier- und Suchalgorithmen aufgezeigt). Zum anderen können Probleme schneller gelöst werden, wenn mehrere Computer gleichzeitig an verschiedenen Teilen derselben Aufgabe arbeiten, was in dieser Unterrichtseinheit behandelt wird. Leider ist es nicht immer ganz so einfach, Arbeitsgänge zwischen verschiedenen Prozessoren aufzuteilen!

{image file-path="img/topics/sorting-network-many-computers-vs-one.png" alt="Bild mehrerer Menschen, die an ihren Computern arbeiten, im Vergleich zu einer Einzelperson an einem Computer."}

Sortiernetzwerke werden dazu eingesetzt, Werte durch Vergleichen von Wertepaaren in aufsteigender Reihenfolge zu ordnen. Beispielsweise wendet das von uns in dieser Unterrichtseinheit herangezogene Sortiernetzwerk mit sechs Zahlen insgesamt 12 Vergleiche an, um die Zahlen zu ordnen, es können jedoch bis zu drei Vergleiche gleichzeitig ausgeführt werden. Das bedeutet, dass der Zeitaufwand derselbe ist, wie wenn ein Computer allein nur fünf Vergleichsschritte ausführen würde. Das ist so ähnlich, wie wenn wir vier Seiten an Text abtippen müssten: Wenn vier Personen gleichzeitig an vier Computern tippen, kann die Aufgabe wahrscheinlich viermal so schnell erledigt werden, als wenn nur eine Person daran arbeitet.

Mithilfe eines parallelen Sortiernetzwerks lässt sich ermitteln, wie viel schneller wir Werte in eine Reihenfolge ordnen können, wenn Vergleiche simultan angestellt werden können. Das in diesen Lektionen hauptsächlich verwendete sechswegige Parallelnetzwerk ordnet eine Liste an Werten zweimal so schnell wie ein System, das nur jeweils einen Vergleich ausführen kann.

{image file-path="img/topics/sorting-network-digging-hole-text-en.png" alt="Eine Person gräbt ein Loch und die zweite Person erklärt, nicht mit dem Graben beginnen zu können, bevor die andere Person fertig ist."}

Es können jedoch nicht alle Aufgabenstellungen durch parallele Verarbeitung schneller abgeschlossen werden. Stellen wir uns als Analogie eine Person vor, die einen zehn Meter langen Graben gräbt. Wenn zehn Personen gleichzeitig jeweils einen Meter des Grabens graben würden, würde die Aufgabe sehr viel schneller abgeschlossen werden. Allerdings könnte dieselbe Strategie nicht auf einen zehn Meter tiefen Graben angewendet werden, da der zweite Meter nicht zugänglich ist, bevor der erste Meter gegraben wurde.

{image file-path="img/topics/sorting-network-confused-people.png" alt="Eine verwirrte Gruppe von Personen vor einem Computer, die versuchen, eine einfache Aufgabe zwischen mehreren Personen zu koordinieren."}

Und was das Abtippen unseres vierseitigen Dokuments anbelangt – wenn uns 400 Personen dabei helfen, verbringen wir vermutlich so viel Zeit damit, die ganze Arbeit zu koordinieren, dass die Aufgabe nicht besonders schnell abgeschlossen würde! Informatiker suchen nach wie vor aktiv nach den besten Möglichkeiten, Aufgabenstellungen so zu zerlegen, dass sie von Computern parallel verarbeitet werden können. Dabei ermitteln sie, welche Teile der Verarbeitung gleichzeitig vorgenommen werden können und welche Teile nacheinander verarbeitet werden müssen.

In diesen Lektionen demonstrieren wir anhand einer unterhaltsamen Teamaktivität eine Methode zum parallelen Sortieren. Die Aktivität kann auf Papier ausgeführt werden, wir möchten sie Schülern jedoch gerne in großem Maßstab näherbringen, indem sie im Netzwerk von Knotenpunkt zu Knotenpunkt rennen.

Hier soll noch angemerkt werden, dass dies zwar als „Netzwerk“ bezeichnet wird, es jedoch nur eines von vielen verschiedenen Netzwerktypen ist, denen wir in der Informatik begegnen. Eine verbreitete Art eines „Netzwerks“ ist ein Kommunikationsnetzwerk, wie beispielsweise die von mobilen Telefonen genutzten Telekommunikationsnetze, und natürlich das Internet! Zudem gibt es Netzwerke zur Darstellung von Dingen wir Straßenkarten und Flugrouten. Es ist wichtig, zu verstehen, dass das Sortiernetzwerk in dieser Aktivität **nicht** eines dieser Netzwerktypen ist. Es wird Komparatornetzwerk genannt, da es sich um ein Netzwerk handelt, bei dem jeder Knotenpunkt zwei Werte vergleicht und nicht verschiedene Geräte (wie Telefone und Computer) miteinander verbindet.

## Digitaltechnik | Algorithmen

{image file-path="img/topics/sorting-network-too-far-kid.png" alt="Eines der Kinder läuft bei der Sortiernetzwerkaktivität zu weit, wodurch die Aktivität für alle misslingt."}

Um das Sortiernetzwerk einzusetzen, müssen die Schüler einem einfachen Algorithmus folgen und sollten erkennen, dass sie diesen Algorithmus präzise befolgen müssen, genau wie es ein Computer tun würde, damit sie kein falsches Ergebnis oder vielleicht sogar gar kein Ergebnis zu erhalten! Dabei müssen die Schüler gemeinschaftlich arbeiten, um sicherzustellen, dass jeder Teil des Algorithmus koordiniert wird. Wenn sich nämlich nur eine Person zu weit vorbewegt, ohne an den vorgesehenen Knotenpunkten anzuhalten, schlägt der Prozess für alle fehl. Es gibt auch viele Algorithmen, die dazu eingesetzt werden, überaus effiziente Sortiernetzwerke verschiedener Größen zu konstruieren, und Informatiker sind eingehend mit diesen Algorithmen befasst, um zu versuchen, sogar noch bessere zu erstellen. Derartige Netzwerke können jedoch äußerst komplex sein. Wenn Schüler ihre eigenen Netzwerke konstruieren, geschieht dies daher auf vereinfachte Weise.

## Begriffserläuterung

- **Prozessor/CPU:** Ein Bauteil, das Computerprogramme ausführen kann.
- **Parallele Verarbeitung:** Die Verwendung mehrerer Prozessoren, um an verschiedenen Teilen einer Aufgabenstellung gleichzeitig zu arbeiten.
- **Serielle Verarbeitung:** Das Ausführen eines Programms auf einem einzigen Prozessor, wobei alle Befehle nacheinander ausgeführt werden.
- **Netzwerk:** Eine Reihe miteinander verknüpfter Knotenpunkte, wie beispielsweise Computernetzwerke, Straßenkarten oder Komparatornetzwerke.
- **Rechnerischer Schritt:** Ein Grundarbeitsvorgang, der Teil eines Algorithmus ist.
- **GPU/Grafikprozessor:** Ein spezialisierter Prozessor in einem Computer, der einfache Operationen für die zahlreichen Pixel in einem Bild parallelisiert ausführen kann. Diese werden aufgrund ihrer Fähigkeit, Daten parallel zu verarbeiten, oft auch für andere Berechnungen verwendet.

{panel type="math"}

# Mathematische Zusammenhänge

Diese Aktivität unterstützt in hohem Maße das Erlernen des Vorher-Nachher-Konzepts (Ordnen) für Zahlen, einschließlich der Bestimmung der Beziehung zwischen zwei Zahlen (größer als, kleiner als).

{panel end}

## Praktische Auswirkungen

{image file-path="img/topics/sorting-network-tortoises-vs-rabbit.png" alt="Mehrere Schildkröten, die eine Mauer schneller bauen als ein Hase."}

Es ist oftmals kostengünstiger und zeitlich vorteilhafter, etliche langsame Prozessoren an einer rechnerischen Problemstellung arbeiten zu lassen, als einen sehr schnellen. Für Unternehmen mit massiven Cloud-Servern ist es oft wirtschaftlicher, viele langsamere aber günstigere Geräte zu haben, als wenige teure. Dazu ist es allerdings erforderlich, eine rechnerische Aufgabenstellung über mehrere Prozessoren verteilen zu können. Bei manchen rechnerischen Problemen ist dies ein Leichtes, bei anderen wiederum unmöglich. Die von uns hier betrachtete Aufgabenstellung ist zwischen diesen beiden Extremen angesiedelt.

Eine solch kleine Operation (zwei Werte vergleichen) über mehrere Geräte zu verteilen bedeutet, dass diese Art von Algorithmus auf spezialisierter Hardware ausgeführt werden muss. Derartige Algorithmen werden gegenwärtig nur für spezialisierte Programme verwendet, werden jedoch beispielsweise mitunter auf dem Grafikprozesser (GPU) eines Computers ausgeführt, da diese Prozessoren gut für die parallele Verarbeitung einfacher Aufgaben geeignet sind.

{image file-path="img/topics/sorting-network-ancient-sorting-network-text-en.png" alt="Ein GPU entdeckt eine Höhlenmalerei eines antiken Sortiernetzwerks."}

Sortiernetzwerke wurden lange vor der Entwicklung leistungsfähiger GPUs erfunden. Dies ist eine interessante Sache an der Informatik – einige unserer Entdeckungen sind der verfügbaren Hardware weit voraus. Wir sind also für die Hardware gerüstet, wenn sie denn allseits zur Verfügung stehen sollte! Hinweis: Die in diesen Lektionen behandelte Methode ist **kein** konventioneller Sortieralgorithmus, da das in einem konventionellen System ausgeführte Sortieren nur jeweils einen Vergleich anstellen kann. Konventionelle Sortieralgorithmen werden in einer anderen Lektion behandelt. Diese Lektionen sollen Schülern hauptsächlich dabei helfen, die Vor- und Nachteile zu erkunden, die zwischen der Verteilung von Arbeitsgängen über mehrere Computer und der Verwendung nur eines Prozessors bestehen.

Eine zurzeit populäres Modell der parallelen Verarbeitung ist „MapReduce“, das in vielen Cloud-Computing-Systemen Anwendung findet, wo Unmengen an Berechnungen über eine große Anzahl von Prozessoren verteilt werden.

## Überlegungen

- Was war hinsichtlich der durch das Unterrichten dieser Einheit erzielten Lernerfolge am überraschendsten?
- Welche Schüler sind beim Durcharbeiten der Aktivitäten sehr systematisch vorgegangen?
- Welche Schüler sind bei den Aktivitäten sehr detailliert vorgegangen?
- Wie würde ich das Unterrichten dieser Einheit anders gestalten?
