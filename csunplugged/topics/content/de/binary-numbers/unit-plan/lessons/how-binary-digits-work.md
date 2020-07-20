# Wie binäre Einheiten funktionieren

## Schlüsselfragen

- Welche verschiedenen Zahlensysteme kennen wir? (Mögliche Antworten wären beispielsweise: Römische Ziffern, Strichlisten, Zahlenbasen wie binäre, oktale und hexadezimale Systeme, sprachbasierte Systeme wie Chinesisch oder Altägyptisch.)
- Warum verwenden wir normalerweise zehn Ziffern? (Vermutlich weil wir zehn Finger haben und weil es, beispielsweise im Vergleich zu Strichlisten, eine ziemlich effiziente Methode ist, Dinge zu erfassen.)
- Warum haben wir verschiedene Zahlensysteme? (Sie sind für unterschiedliche Dinge geeignet. Beispielsweise sind Strichlisten beim Zählen praktisch und römische Ziffern können dazu dienen, eine Zahl mysteriöser aussehen zu lassen oder schwerer lesbar zu machen.)

## Lektionseinstieg

{panel type="video"}

# Unterrichtsbeispiel ansehen

{video url="https://vimeo.com/437725275"}

{panel end}

{panel type="general"}

# Hinweis der Autoren

Sobald Schüler verstehen, wie das binäre Zahlensystem funktioniert, haben sie unserer Erfahrung nach viele Fragen und möchten begeistert die in dieser Lektion behandelten Konzepte näher erkunden. Wir haben jede Menge Informationen in diese Lektion gepackt, damit jedoch nicht beabsichtigt, dass sämtliche Konzepte unterrichtet und abgedeckt werden. Wir wollten Ihnen lediglich hilfreiche Informationen für den Fall an die Hand geben, dass Ihre Schüler Interesse bekunden, mehr zu lernen.

{panel end}

{panel type="general"}

# Hinweise zu Ressourcen

[Hier](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8) ist auch eine interaktive Online-Version der Binärkarten aus dem [Computer Science Field Guide](http://www.csfieldguide.org.nz/) verfügbar, es empfiehlt sich jedoch, mit physischen Karten zu arbeiten.

{panel end}

1. Halten Sie die ersten fünf Karten (1, 2, 4, 8 und 16 Punkte), jedoch ohne dass die Punkte für die Schüler sichtbar sind. Bitten Sie fünf Schüler darum, sich freiwillig zu melden, um als „Bits“ zu fungieren, und sich in einer Reihe vor der Klasse aufzustellen.

2. Händigen Sie der rechts stehenden Person die 1-Punkt-Karte aus. Erläutern Sie, dass er oder sie nun ein „Bit“ (also eine binäre Einheit) ist und ein oder aus, schwarz oder weiß, oder 0 oder 1 Punkt sein kann. Die einzige Regel ist, dass die Karte dieser Person entweder vollständig sichtbar oder nicht sichtbar (d. h. umgedreht) ist. Händigen Sie der zweiten Person von rechts die zweite Karte aus. Weisen Sie darauf hin, dass diese Karte entweder 2 Punkte hat (sichtbar ist) oder keine (umgedreht ist).
    
    {image file-path="img/topics/col_binary_2cards.png" alt="2 Kinder, die Binärkarten halten"}

3. Fragen Sie die Klasse, wie viele Punkte auf der nächste Karte sein werden. Lassen Sie die Schüler erklären, warum sie dieser Auffassung sind.
    
    {panel type="teaching"}
    
    # Unterrichtsbeobachtungen
    
    Schüler behaupten in der Regel, dass es drei sein sollten. Wenn sie vier angeben, haben sie diese Übung möglicherweise bereits schon einmal gemacht (oder haben die Karten gesehen, die Sie halten!). Wird die falsche Zahl angegeben, berichtigen Sie dies nicht, sondern fahren Sie kommentarlos fort, damit die Schüler die Regel selbst erarbeiten können.
    
    {panel end}

4. Geben Sie wortlos die 4-Punkt-Karte aus und lassen Sie die Schüler versuchen, ein Muster zu erkennen.
    
    {image file-path="img/topics/col_binary_3cards.png" alt="3 Kinder, die Binärkarten halten"}
    
    {panel type="teaching"}
    
    # Unterrichtsbeobachtungen
    
    In den meisten Fällen weisen einige Schüler darauf hin, dass die Drei ausgelassen wurde. Merken Sie einfach an, dass Ihnen kein Fehler unterlaufen ist. So können die Schüler versuchen, das Muster selbst zu erarbeiten.
    
    {panel end}

5. Fragen Sie, was die nächste Karte ist und warum.
    
    {panel type="teaching"}
    
    # Unterrichtsbeobachtungen
    
    An dieser Stelle nehmen Schüler für gewöhnlich an, dass die nächste Karte die 6 ist (nachdem sie auf die Zahlen 2 und 4 folgt). Wenn Sie ihnen jedoch etwas mehr Zeit zum Nachdenken lassen, kommen normalerweise einige auf die 8, und diese Schüler sollten in der Lage sein, die anderen zu überzeugen, dass sie richtig liegen. (Schüler können dies auf verschiedene Weise erklären. Beispielsweise, dass jede Karte den doppelten Wert der vorherigen hat, oder dass, wenn man zwei einer Karte nimmt, sich daraus die nächste Karte ergibt.)
    
    {panel end}

6. Schüler sollten in der Lage sein, die fünfte Karte (16 Punkte) ohne Hilfe zu ermitteln:
    
    {image file-path="img/topics/col_binary_5cards.png" alt="5 Kinder, die Binärkarten halten"}

7. Wie viele Punkte hätte die nächste Karte, wenn wir nach links fortfahren würden? (32) Die nächste ...? (Es ist nicht nötig, dass Schüler diese Karten halten, da sie im nächsten Teil der Aktivität nicht verwendet werden. Sie können sie ihnen jedoch zeigen, um zu bestätigen, dass sie richtig liegen.)

8. Fahren Sie mit 64 und 128 Punkten fort.
    
    {panel type="teaching"}
    
    # Unterrichtsbeobachtungen
    
    Bei 128 Punkten hätten wir 8 Karten. Das sind 8 Bits, was allgemein als ein Byte bezeichnet wird. Dies hier zu erwähnen, kann unter Umständen ablenkend sein, manche Schüler mögen jedoch bereits mit dem Konzept vertraut sein, dass 8 Bits ein Byte sind, und werden dies anmerken. Einstweilen arbeiten wir jedoch mit einer 5-Bit-Darstellung, was nicht ganz so praktisch ist wie ein ganzes Byte, zum Unterrichten aber eine gute Größe ist. (Ein Byte ist eine praktische Zusammenfassung von Bits und ein Computerspeicher basiert normalerweise auf Bytes und nicht auf einzelnen Bits. Es ist ungefähr so wie im Dutzend verkaufte Eier. Natürlich könnten sie auch einzeln verkauft werden, sie im Dutzend zusammenzufassen ist jedoch für gewöhnlich praktischer für alle Beteiligten.)
    
    Oftmals werden die Karten fälschlicherweise von links nach rechts ausgehändigt. Bei der Zahlendarstellung gilt jedoch der Grundsatz, dass sich der geringste Wert rechts befindet, was für Schüler eine wichtige Erkenntnis ist, die sie aus dieser Übung gewinnen können.
    
    {panel end}

## Lektionsaktivitäten

1. Erinnern Sie die Schüler an die Regel, dass eine Karte die Punkte entweder vollständig anzeigt oder keine davon sichtbar sind. Wenn wir Karten durch Zeigen der Vorder- und Rückseiten ein- oder ausschalten können – wie würden wir genau 9 Punkte darstellen? Fragen Sie zunächst, ob sie die 16er-Karte haben möchten (sie sollten erkennen, dass diese zu viele Punkte hat), dann die 8er-Karte (sie werden vermutlich folgern, dass ohne diese Karte nicht genügend Punkte übrig sind), dann 4, 2 und 1. Mit nur der Regel ausgestattet, dass jede Karte entweder sichtbar ist oder nicht, kommen Schüler für gewöhnlich auf die folgende Darstellung.
    
    {image file-path="img/topics/binary-cards-total-9.png" alt="Darstellung, wonach 2 Binärkarten die Zahl 9 bilden"}
    
    {panel type="math"}
    
    # Mathematische Zusammenhänge
    
    Basis 10 bzw. das Dezimalsystem (unser Zahlensystem) enthält 10 Ziffern: 0, 1, 2, 3, 4, 5, 6, 7, 8 und 9. Wenn wir im Dezimalsystem zählen, zählen wir von 0 bis 9 und haben dann keine Ziffern mehr. Also müssen wir eine weitere Spalte hinzufügen, eine 1 in diese Spalte eintragen und erneut von 0 anfangen zu zählen. So erhalten wir die Zahl 10. Dann wiederholen wir diesen Vorgang, bis die Zehnerspalte 9 und die Einserspalte 9 ausweisen (und somit 99 ergeben) und fügen dann eine weitere Spalte hinzu. Damit haben wir das bekannte Stellenwertsystem, das etwa folgendermaßen angezeigt werden kann:
    
    100 000er | 10 000er | 1 000er | 100er |10er | 1
    
    *Hinweis: Dies ist ein erweitertes Beispiel. Verwenden Sie das Stellenwertbeispiel, das für den in Ihrer Klasse bereits unterrichteten Stoff geeignet ist.*
    
    Basis 2 bzw. das Dualsystem (Binärsystem) folgt derselben Logik, gelangt jedoch viel schneller zum „nächsten“ Stellenwert, da es nur zwei Ziffern gibt, nämlich 0 und 1. Die binären Stellenwerte sehen folgendermaßen aus:
    
    32 | 16 | 8 | 4 | 2 | 1 |
    
    Gelegentlich bringen Schüler die Reihenfolge der Einheiten in einer binären Darstellung durcheinander. Um Schülern dabei zu helfen, die richtige Anordnung von binären Einheiten zu verstehen, können Sie beispielsweise fragen: Wenn ich euch 435,00 Euro geben würde – welche Zahl wäre für euch von größter Bedeutung? Die 4 oder die 5? Aus welchem Grund? Das Gleiche gilt für die binäre Darstellung: der niedrigste Wert (geringwertigste Einheit) steht ganz rechts, während die höchstwertigste Einheit ganz links steht.
    
    {panel end}

2. Fragen Sie nun: „Wie würdet ihr die Zahl 21 bilden?“ (Fragen Sie auch hier zunächst, ob sie die 16er-Karte haben möchten usw., von links nach rechts).

3. Dies ist ein Algorithmus zur Umwandlung von Zahlen in eine binäre Darstellung. Gehen wir die dafür erforderlichen Schritte einmal gemeinsam durch.
    
    a. Fangen Sie mit allen Zahlen eingeschaltet an (alle Punkte sind sichtbar).
    
    {image file-path="img/topics/lightbulb_series_1.png" alt="5 Glühbirnen eingeschaltet"}
    
    b. Überlegen wir uns die die Darstellung der Zahl 10
    
    c. Geht 16 in 10? Nein – also schalten wir sie aus.
    
    {image file-path="img/topics/lightbulb_series_2.png" alt="4 Glühbirnen eingeschaltet"}
    
    d. Geht 8 in 10? Ja – also lassen wir sie an. Wie viele verbleiben? (2)
    
    e. Geht 4 in 2? Nein – also schalten wir sie aus.
    
    {image file-path="img/topics/lightbulb_series_3.png" alt="3 Glühbirnen eingeschaltet"}
    
    f. Geht 2 in 2? Ja – also lassen wir sie an. Wie viele verbleiben? (keine)
    
    g. Schalten wir also die 1 aus.
    
    {image file-path="img/topics/lightbulb_series_4.png" alt="2 Glühbirnen eingeschaltet"}

## Das Gelernte anwenden

- Teilen Sie die Schüler paarweise ein.
- Geben Sie jedem Paar einen Satz der kleineren Binärkarten (entweder fünf oder sechs Karten, je nach dem, mit welchem Zahlenbereich sie vertraut sind).
- Lassen Sie sie nun mit nur fünf Karten den Algorithmus für Zahlen wie 20, 15 und 8 üben (und dabei von links nach rechts über die einzelnen Karten entscheiden).

1. Erläutern Sie den Schülern, dass wir mit nur zwei Einheiten arbeiten und diese darum binäre Einheiten genannt werden. Diese Einheiten sind so verbreitet, dass wir eine Kurzbezeichnung dafür haben: Schreiben Sie „Binäre Einheit“ auf ein Blatt Papier und reißen Sie dann das „Bi“ am Anfang und das „t“ am Ende ab, setzen die beiden zusammen und fragen, welche Wortkombination („Bit“) dabei herauskommt. Das ist die Kurzbezeichnung für eine binäre Einheit und die fünf Karten, die sie haben, sind daher im Grunde fünf Bits.

2. Zählen wir jetzt von der kleinsten Zahl, die wir bilden können, bis zur höchsten Zahl:
    
    a. Was ist die kleinste Zahl? (eventuell geben Schüler die 1 an und erkennen dann, dass es tatsächlich die 0 ist).

3. Lassen Sie die Zahl Null mit den Karten anzeigen (d. h. keine Punkte sichtbar).

4. Zählen wir jetzt einmal vorwärts 1, 2, 3, 4 … (jedes Paar sollte diese Zahlen untereinander ausarbeiten).

5. Sobald sich dabei eine Routine entwickelt, fragen Sie: Wie oft sehen wir die 1-Punkt-Karte? (jedes zweite Mal, also jede ungerade Zahl)
    
    a. Welche anderen Muster können wir erkennen? (manche mögen feststellen, dass die 2-Punkt-Karte alle zwei Zahlen umgedreht wird, die 4-Punkt-Karte alle vier Zahlen usw.; mit der 16-Punkt-Karte passiert also nicht viel!)

6. Fahren Sie fort, bis alle Karten auf „ein“ geschaltet sind und bis 31 gezählt wurde. Was passiert als nächstes? (Wir müssen eine neue Karte hinzufügen.) Wie viele Punkte sind darauf? (32) Was müssen wir mit den anderen fünf Karten machen, wenn wir bei 32 ankommen? (wir müssen sie alle ausschalten)

7. Sehen wir uns dies etwas näher an ...
    
    a. Wenn ich nun zwei Bits habe, was kann ich höchstens bilden? (3)
    
    b. Ich füge ein weiteres Bit hinzu. Wie viele Punkte hat es? (4)
    
    c. Um 4 zu bilden, schalte ich die ersten beiden Bits aus, richtig?
    
    d. Wenn wir jetzt alle drei Bits einschalten, haben wir wie viel? (7)
    
    e. Ich füge ein weiteres Bit hinzu und das hat wie viele Punkte? (8)
    
    f. Wiederholen Sie dies, bis ein Muster erkannt wird, dass die Zahl auf der nächsten Karte zur Linken um eins größer ist als die Gesamtzahl der Punkte auf allen Karten zur Rechten (beispielsweise ergeben die 8er, 4er, 2er und 1er Karte 15 Punkte, die nächste Karte zur Linken ist also 16). Dies erleichtert das Berechnen der Zahl, wenn alle Bits eingeschaltet sind – die Karte zur Linken verdoppeln und 1 subtrahieren.
    
    g. Wie viele verschiedene Zahlen kann ich mit zwei Bits bilden? (4; Schüler geben oftmals 3 als Antwort, da sie die 0 nicht mitgezählt haben)
    
    h. Fügen wir nun das nächste Bit hinzu. Wie viele verschiedene Zahlen können wir jetzt bilden? (8; auch hier wird oft zunächst 7 als Antwort gegeben)
    
    i. Wiederholen Sie dies, bis ein Muster erkannt wird, dass mit jedem Hinzufügen eines weiteren Bits doppelt so viele Zahlen dargestellt werden können.

{panel type="teaching"}

# Unterrichtsbeobachtungen

Manche Schüler mögen sich hier mit dem Konzept schwer tun, dass die Anzahl der Werte um eins größer ist als der Höchstwert (z. B. von 0 bis 7, hier haben wir 8 verschiedene Zahlen). Dieses Muster kann auch bei der Anzahl normaler Dezimalzahlen beobachtet werden: Die größte Zahl ist 9, es gibt jedoch 10 mögliche Zahlen (einschließlich 0). Dies wird gelegentlich auch als Zaunpfahlproblem bezeichnet (die Anzahl der Zaunpfähle ist um eins größer als die Anzahl der Zwischenräume), was bei der elektronischen Datenverarbeitung häufig vorkommt.

{panel end}

## Lektionsbetrachtung

- Würde diese Aktivität auch mit weißen und cremefarbenen Karten funktionieren? Warum? Warum nicht? (Generell könnten diese verwendet werden, es wäre jedoch keine gute Idee. Hier sind wir auf die Antwort aus, dass es sich nicht um Kontrastfarben handelt und daher schwer zu erkennen wäre, ob sie ein- oder ausgeschaltet sind. Dies zeigt auf, warum Computer einfach zu unterscheidende physische Darstellungen verwenden.)
- Welche gegensätzlichen Symbole oder Möglichkeiten gibt es, die wir binär als ein und aus darstellen können?
    
    - (Hier sind Ideen gefragt wie beispielsweise die Karten nach oben oder nach unten zu halten, einfach den Arm hochzustrecken, sitzen oder stehen oder sich anderer Darstellungen wie ein- oder aus- geschalteter Glühbirnen zu bedienen.)

- Computer sind billiger und einfacher zu bauen, wenn sie Daten anhand von nur zwei gegensätzlichen Werten darstellen, die von uns als die Zahlen 0 und 1 dargestellt werden. Was könnten wir noch verwenden, um zwei Gegensätze in Schriftform darzustellen? (Etwa ein Kreuz oder Häkchen, ein glückliches oder trauriges Gesicht, oder eine sonstige Symbolpaarung.)

- Führt man diesen Ansatz weiter, könnten die Zahlen auch durch eine elektrische Spannung dargestellt werden, die entweder nahe bei 5 Volt oder nahe bei 0 Volt liegt. Der Schaltkreis wäre so konstruiert, dass alles kleiner als ca. 2,5 Volt als 0 und alles größer als 2,5 Volt als 1 zählt. Genau wie die gegensätzlichen Farben der Karten, kann auch dies leicht verstanden werden. Wir hätten die Zahlen von 0 bis 10 anhand von zehn Kartenfarben darstellen können und wir könnten mit zehn Spannungsbereichen (0 bis 0,5; 0,5 bis 1,0 usw.) arbeiten, es ist jedoch um einiges komplizierter, dafür schnelle und akkurate Schaltkreise zu konstruieren.