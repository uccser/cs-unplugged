{panel type="ct-algorithm"}

# Algorithmisches Denken

In diesen Lektionen lernen Schüler, verschiedene Dinge in eine Reihenfolge zu ordnen, der zugrundeliegende Algorithmus zur Ausführung dieser Aufgaben bleibt jedoch gleich. Es ist ein Algorithmus, da es sich um ein schrittweises Verfahren handelt, das stets die richtige Lösung liefert, solange er genau eingehalten wird. In diesem Fall handelt es sich um eine besondere Algorithmuskategorie, die „paralleler Algorithmus“ genannt wird. Die Schüler müssen diesen Algorithmus präzise befolgen, um zur richtigen Lösung zu gelangen (was vor allem dann deutlich wird, wenn Schüler zu „mogeln“ versuchen, indem sie ans Ende des Netzwerks rasen und dann feststellen, dass dadurch andere Schüler in der Mitte feststecken bleiben! Es ergibt ein sehr anschauliches Lernbeispiel, wenn einer der Schüler so vorgeht).

{panel end}

{panel type="ct-abstraction"}

# Abstraktion

Das in diesen Aktivitäten von uns eingesetzte Sortiernetzwerk ist eine einfache Darstellung von etwas viel komplexerem: wie Sortiernetzwerke mittels spezialisierter Hardware und Software auf manchen Computern implementiert werden, um eine parallele Verarbeitung auszuführen. Die in unseren Sortiernetzwerken verwendeten Linien, Kreise und Quadrate verbergen die komplizierten Details der Hard- und Software.

Ein weiteres Detail, das wir bei der Verwendung eines Sortiernetzwerks ignorieren können: was die von uns sortierten Daten tatsächlich sind oder darstellen. Es spielt keine Rolle, ob wir Zahlen oder Wörter oder Musiknoten in eine Reihenfolge sortieren – wir folgen stets demselben Prozess. Was jedoch hinsichtlich der Daten eine Rolle spielt, ist dass wir die einzelnen Elemente vergleichen können und dass sie nach einer bestimmten Methode sortiert werden (z. B. in alphabethischer Reihenfolge). Dies wird im Abschnitt zu Logik näher geschildert.

Auch die generelle Idee eines Sortiernetzwerks stellt ein abstraktes Konzept dar. Dies wird im Abschnitt Generalisierung erläutert.

{panel end}

{panel type="ct-decomposition"}

# Dekomposition

{image file-path="img/topics/sorting-network-comparing-apples.png" alt="Eine Person vergleicht einen großen und einen kleinen Apfel." alignment="right"}

Um einen Algorithmus zu erstellen, der rechnerische Aufgabenstellungen mithilfe von Parallelprozessoren effektiv lösen kann, müssen wir die Aufgabe zunächst in äußerst kleine und einfache Operationen zerlegen, die bei vielfacher Wiederholung eine Lösung für das Problem aufbauen können. Diese Operationen sind das, was von jedem Prozessor im Netzwerk ausgeführt wird. Für das Sortiernetzwerk in diesen Lektionen ist die einfache Operation der Vergleich von zwei Werten, den wir an jedem Knotenpunkt durchführen. Diese Operationen müssen so einfach sein, dass sie von Knotenpunkten zeitgleich und unabhängig voneinander ausgeführt werden können. Parallele Algorithmen eigenen sich am besten für Aufgaben, bei denen mehrmalige und unabhängige Kalkulationen mit großen Datenmengen ausgeführt werden müssen.

Dekomposition ist einer der wichtigsten Schritte beim Erstellen von Algorithmen zur parallelen Verarbeitung!

{panel end}

{panel type="ct-pattern"}

# Generalisierung und Muster

Es gibt viele Zusammenhänge zwischen diesem Abschnitt und dem obigen Abschnitt Abstraktion – schaut genau hin!

Die Sortiernetzwerke, mit denen wir uns beschäftigen werden, sind alle darauf ausgelegt, eine bestimmte Anzahl an Eingaben aufzunehmen, und zwar genau diese Anzahl. Ein Sortiernetzwerk, das sechs Zahlen ordnet, kann nicht dazu verwendet werden, stattdessen zehn Zahlen zu ordnen. Die verallgemeinerte Idee eines Sortiernetzwerks kann jedoch auch auf andere Problemstellungen angewendet werden. Das verallgemeinerte Konzept eines Sortiernetzwerks ist lediglich ein Komparatornetzwerk (Komparator bedeutet einfach, dass es Vergleiche vornimmt, genau wie wir in jedem Kreis im Netzwerk Zahlen vergleichen), das eine Anzahl an Eingaben aufnimmt und diese in eine Reihenfolge sortiert. Diese allgemeine Idee eines Sortiernetzwerks kann dann zur Lösung vieler verschiedener Probleme herangezogen werden, indem ein Sortiernetzwerk für eine bestimmte Anzahl an Eingaben erstellt wird, die für das betreffende Problem benötigt werden, und die Vergleichsknotenpunkte in einem bestimmten Muster angeordnet werden.

Auch in der Gestaltung von Sortiernetzwerken sind Muster vorhanden. Diese zu erkennen hilft uns dabei, größere Netzwerke anzulegen. Beispielsweise folgen (optimale) zwei-, vier- und sechswegige Sortiernetzwerke in ihrer Ausführung ähnlichen Mustern. Ein einfaches Muster zur Erstellung von Sortiernetzwerken wird am Ende von Lektion 3 für die Altersgruppe 11–14 behandelt (dies kann jedoch für jede Altersgruppe verwendet werden, wenn die Schüler daran interessiert sind!).

Zudem können Schüler ein Muster beobachten, das all den verschiedenen Arten von Informationen, die wir mit dem Sortiernetzwerk ordnen, gemeinsam ist, und zwar, dass sie verglichen und auf präzise Weise geordnet werden können. Dies wird im Abschnitt Logik erläutert.

{panel end}

{panel type="ct-evaluation"}

# Auswertung

Parallele Systeme müssen auf ihre Genauigkeit hin ausgewertet werden: Werden Werte von ihnen stets richtig geordnet? Außerdem muss ihre Leistungsfähigkeit ausgewertet werden: Wie viel Zeit benötigt diese Netzwerkstruktur, um Werte zu ordnen, oder gibt es eine schnellere Struktur, die wir verwenden könnten? Könnte das Problem mit einem nicht-parallelen System einfacher gelöst werden?

{panel end}

{panel type="ct-logic"}

# Logik

Für Daten, die von Sortiernetzwerken verarbeitet werden können, gibt eine sehr wichtige Regel: Zwischen den Daten muss eine sogenannte transitive Relation bestehen. Transitive Relation bedeutet: wenn a kleiner ist als b, und b kleiner ist als c, dann ist a kleiner als c. Beispielsweise besteht zwischen Zahlen eine transitive Relation: die Zahl 5 ist kleiner als 10, und 10 ist kleiner als 15, was bedeutet, dass 5 ebenfalls kleiner als 15 sein muss. Daten müssen eine solche Beziehung haben, damit sie von einem Sortiernetzwerk geordnet werden können. Wenn Elemente nicht über diese Beziehung verfügen, gibt es keine logische Methode, sie zu ordnen!

Darüber hinaus wird deutlich, dass Sortiernetzwerke nicht dadurch ausgewertet werden können, dass jede nur mögliche Eingabe ausprobiert wird (naja, es wäre möglich, könnte jedoch Stunden, Tage oder sogar Hunderte von Jahren für große Netzwerke dauern!), es sei denn, es wird nur eine kleine Menge an Daten geordnet. Stattdessen müssen wir Logik und Rationalität anwenden, um nachzuweisen, dass sie die Daten stets richtig ordnen. Bei diesen Lektionen sind keine fortgeschrittenen Nachweise zu erbringen, dass das gesamte Netzwerk funktionieren wird. Die Schüler können jedoch ihr logisches Denkvermögen einsetzen, um nachzuweisen, dass der kleinste und der größte Wert stets an die richtige Stelle gelangen werden.

{panel end}