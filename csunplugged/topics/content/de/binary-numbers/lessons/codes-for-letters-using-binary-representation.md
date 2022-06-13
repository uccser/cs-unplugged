# Buchstabencodierung mittels binärer Darstellung

## Schlüsselfragen

- Wie viele verschiedene Zeichen lassen sich auf einem Computer eintippen? (Als Vorschläge könnten zunächst die 26 Buchstaben des Standardalphabets der englischen Sprache angesprochen werden, und im weiteren Verlauf die anderen Zeichen auf der Tastatur, einschließlich Großbuchstaben, Zahlen und Satzzeichen. Manchen Schülern mag bewusst sein, dass andere Sprachen Tausende von Zeichen haben können und sich mit neuen Emoticons auch die Spanne verfügbarer Zeichen vergrößert!)

## Lektionseinstieg

{panel type="general"}

# Hinweise zu Ressourcen

[Hier](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8) ist auch eine interaktive Online-Version der Binärkarten aus dem [Computer Science Field Guide](http://www.csfieldguide.org.nz/) verfügbar, es empfiehlt sich jedoch, mit physischen Karten zu arbeiten.

{panel end}

{image file-path="img/topics/col_binary_robot_boy_convo.png" alt="Ein Junge, der mit einem Roboter spricht" alignment="left"}

Überlegt euch, wie ihr einer anderen Person einen Buchstaben des Alphabets mitteilen würdet, wenn die Mitteilung auf eine Zahl zwischen 0 und 26 beschränkt werden müsste. *(Schüler schlagen meistens vor, den Code 1 für a, 2 für b usw. zu verwenden.)*

Erarbeitet und notiert euch mithilfe von 5 Bits die Binärzahlen für 0 bis 26 auf der Ressource Binär zu Alphabet und fügt dann die Buchstaben des Alphabets hinzu.

{panel type="teaching"}

# Unterrichtsbeobachtungen

- Vergewissern Sie sich, dass die Schüler als Binärcode für die Zahl Drei 00011 verwenden, da Schüler häufig 00100 schreiben, wenn sie ein Muster vorwegnehmen, ohne zu prüfen, ob es richtig ist.
- Überprüfen Sie, ob die Schüler den Binärcode in der richtigen Reihenfolge, also mit dem geringfügigsten Wert rechts, aufschreiben. Manche Schüler beginnen beispielsweise mit der Eins als 10000 anstelle von 00001.
- Identifzieren Sie die Schüler, die eines oder alle dieser Merkmale des informatischen Denkens aufzeigen: systematisches Vorgehen, alles folgerichtig angeordnet, erkennen als erste das Muster und benötigen die Karten nicht mehr.
- Überprüfen Sie, ob Ihnen alle Schüler schildern können, wie sie die von ihnen genannte Zahl ermittelt haben. Dadurch zeigt sich, welche Schüler das Muster raten.
- Hinweis: Sofern das lokale Alphabet etwas abweicht (z. B. diakritische Zeichen, Überstriche usw. enthält) sollten Sie den Code ggf. anpassen, um ihn auf die üblichen Zeichen abzustimmen. Dies ist ebenfalls nachstehend berücksichtigt.

{panel end}

## Lektionsaktivitäten

Geben Sie den Schülern unter Verwendung der von den Schülern zuvor erstellten Tabelle eine Nachricht zu entschlüsseln, wie beispielsweise Ihren Namen oder den Namen eines Schriftstellers (z. B. 00001 00010 00010 11001 für ABBY).

Lassen Sie die Schüler anschließend ihre eigenen Nachrichten aufschreiben und kommunizieren. Erinnern Sie sie daran, dass sie Nullen und Einsen mit beliebigen Symbolen, wie beispielsweise Häkchen und Kreuzchen, schreiben können.

Geben Sie auch ungewöhnliche Darstellungen zu erwägen: Beispielsweise könnten die einzelnen Bits anhand von Tönen kommuniziert werden, die entweder hoch oder tief sind. Oder die 5-Bit-Zahl könnte durch Hochhalten von fünf Finger an einer Hand dargestellt werden, wobei jeder Finger einem Bit entspricht.

## Weitere Zeichen hinzufügen

Manche Sprachen verfügen über etwas mehr oder weniger Zeichen, wozu auch Buchstaben mit diakritischen Zeichen gehören. Wenn Schüler ein Alphabet mit mehr als 32 Zeichen in Erwägung ziehen, reichen 5 Bits nicht aus. Manche Schüler mögen erkannt haben, dass ein Code für ein Leerzeichen benötigt wird (0 ist eine gute Wahl dafür) und 5 Bits daher nur 31 alphabetische Zeichen abdecken.

Lassen Sie die Schüler ein System entwerfen, in dem ein paar zusätzliche Zeichen, wie beispielsweise diakritische Zeichen, untergebracht werden können. (Dies lässt sich in der Regel dadurch bewerkstelligen, dass den zusätzlichen Zeichen größere Zahlen wie 27 bis 31 zugeordnet werden.)

Eine typische Computertastatur der englischen Sprache verfügt über circa 100 Zeichen (dies umfasst Groß- und Kleinbuchstaben, Satzzeichen, Zahlen und Sonderzeichen). Wie viele Bits werden benötigt, um jedem Zeichen auf der Tastatur eine eindeutige Zahl zuzuordnen? (Normalerweise reichen 7 Bits aus, da damit 128 verschiedene Codes möglich sind.)

Lassen Sie nun die Schüler umfangreichere Alphabete erwägen. Wie viele Bits werden benötigt, wenn wir jedes der 50 000 chinesischen Schriftzeichen durch eine Zahl darstellen wollen? (16 Bits ermöglichen bis zu 65 536 unterschiedliche Darstellungen.)

{panel type="teaching"}

# Unterrichtsbeobachtungen

Es mag überraschen, dass für Zehntausende von Zeichen nur 16 Bits benötigt werden. Das liegt daran, dass jedes Bit den Bereich verdoppelt, und daher nur wenige Bits benötigt werden, um ein umfangreiches Alphabet abzudecken. Dies ist ein wichtiges Merkmal der binären Darstellung, mit dem sich Schüler vertraut machen sollten.

{panel end}

{panel type="math"}

# Mathematische Zusammenhänge

Die rasche Zunahme der Anzahl der verschiedenen Werte, die durch Hinzufügen von Bits dargestellt werden können, wird *exponentielles* Wachstum genannt, d. h. mit jedem zusätzlichen Bit verdoppelt sich der Wert. Nach 16 Verdoppelungen können 65 536 verschiedene Werte dargestellt werden und 20 Bits können über eine Million verschiedene Werte darstellen. Exponentielles Wachstum wird bisweilen anhand von hälftigem Falten von Papier illustriert. Nach zwei Faltungen ist es vier Blätter dick und nach einer weiteren Faltung bereits 8 Blätter dick. Nach 16 Faltungen ist es 65 536 Blätter dick! Tatsächlich sind um die 6 oder 7 Faltungen bereits unglaublich dick, selbst bei einem großen Blatt Papier.

{panel end}

{panel type="teaching"}

# Unterrichtsbeobachtungen

Die Verwendung eines 5-Bit-Codes für ein Alphabet kann bis mindestens 1870 (den „Baudot“-Code) zurückverfolgt werden. Über die Jahre hinweg wurden viele verschiedene Zahlen-zu-Buchstaben-Kodierungen verwendet, um Alphabete darzustellen. Eine davon, die eine Zeit lang verbreitet war, ist der„ASCII“-Code, der 7 Bits verwendete und somit über 100 verschiedene Zeichen darstellen konnte. Heute ist „Unicode“ gebräuchlich, mit dem über 100 000 verschiedene Zeichen dargestellt werden können. Dennoch umfassen all diese Codes, einschließlich Unicode, nach wie vor Elemente des in dieser Lektion behandelten einfachen Codes (A ist 1, B ist 2, ...). Zum Beispiel: Der ASCII-Code für „A“ ist 65 und „B“ ist 66 usw. Beim Ausarbeiten der entsprechenden binären Darstellung müssen einfach nur die ganz rechts stehenden 5 Bits beibehalten werden und wir sind bei dem Code, den wir oben verwendet haben.

{panel end}

## Lektionsbetrachtung

- Was sind Gründe dafür, warum wir das binäre Zahlensystem nicht als Kommunikationsmittel für unsere Schriftsprache verwenden?
- Wie hätten wohl die alten Ägypter ihre Hieroglyphen in eine binäre Darstellung umgewandelt?
- Was fandet ihr bei dieser Lektion schwierig?
- Wie habt ihr diese Schwierigkeiten gemeistert?