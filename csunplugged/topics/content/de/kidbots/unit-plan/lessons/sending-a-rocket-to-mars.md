# Sending a rocket to Mars

{image file-path="img/topics/unplugged-programming-icon.png" alt="Schüler, die um ein großes Schachbrettfeld herumstehen." caption="true"}

This example is a starter lesson with an object in the middle. The girl on the white square is 'The Bot', the girl at the back is 'The Programmer' and the boy in the green and gold is 'the Tester'.

{image end}

## Key questions

Why is it important to give very clear instructions? Have you ever been given unclear instructions and ended up doing the wrong thing? Why do you think computers need clear instructions?

## Lesson starter

Für diese Lektion wird ein großes Gitterfeld genötigt, wie beispielsweise:

- ein auf den Boden gemaltes Schachbrett im Freien,
- ein Gittermuster auf dem Klassenzimmerteppich,
- ein mit Abdeckband auf den Klassenzimmerboden geklebtes Gitterfeld,
- ein mit Kreide im Klassenzimmer oder im Freien gezeichnetes Gitterfeld.

Bitten Sie die Schüler um zwei Freiwillige und teilen Sie ihnen und sich selbst folgende Rollen zu:

**Role 1:** The Developer (who writes the program) - The teacher will model this initially

**Role 2:** The Tester (who instructs the Bot and looks for bugs)

**Role 3:** The Bot (who runs the program)

## Lektionsaktivitäten

{image file-path="img/topics/kidbots-rocket-1.png" alt="8 x 8 grid with a rocket ship at position (1,5) and Mars at position (4,3). Positions are counted from the top left corner."}

Lehrer: „Ich werde der Programmierer sein, werde aber eure Hilfe benötigen. Wir werden den Bot programmieren und nicht nur fernsteuern, da ALLE Anweisungen geschrieben werden, bevor der Bot diesen Anweisungen folgen kann.“

„Es ist unsere Aufgabe, klare Anweisungen für den Bot niederzuschreiben, der (nennen Sie den Namen des Schülers) sein wird. (Name des Schülers) wird der Tester sein und die Anweisungen an den Bot weitergeben. Der Tester wird nach Fehlern Ausschau halten.“

„Zuallererst müssen wir festlegen, welche Programmiersprache wir dafür verwenden werden. Ich habe Pfeile gewählt, um Vorwärts bewegen, Nach links drehen und Nach rechts drehen darzustellen.“

„Debugging macht Spaß, da man Gelegenheit erhält, sein Programm nach erfolgter Fertigstellung zu ändern, wenn man feststellt, dass es nicht wie vorgesehen funktioniert.“

"First of all I need to decide, what programming language are we are going to use for this? I’ve chosen arrows to represent move forward, turn left and turn right."

{panel type="teaching"}

# Teaching observations

Es gibt verschiedene Möglichkeiten, dieselbe Anweisung zum Ausdruck zu bringen (z. B. einen Pfeil zeichnen, „Vorwärts“ schreiben oder den obigen Ausdruck mit Pfeilen verwenden), es ist jedoch wichtig, dabei einheitlich vorzugehen. Die Entscheidungen über das genaue Format der Anweisungen haben unterschiedliche Programmiersprachen zur Folge und es ist völlig in Ordnung, wenn dies passiert, solange wir die begrifflichen Inhalte der jeweils verwendeten Sprache kennen.

{panel end}

Wenn sich Schüler über die Richtungen links und rechts nicht ganz sicher sind, können Sie die Links- und Rechts-Karten ausdrucken und an ihren Schuhen befestigen oder sie die Karten in der Hand halten lassen.

Lassen Sie den Bot die einzelnen Anweisungen ausführen: Vorwärts bedeutet, sich um ein Quadrat vorwärts zu bewegen, und Links bzw. Rechts bedeutet, sich an Ort und Stelle um 90 Grad zu drehen (und dabei nicht zu einem anderen Quadrat weiterzugehen).

Teacher: "We’re going to write our own program that gets the rocket to fly to Mars. The goal is to get the rocket to the square that Mars is in. Schreiben wir gemeinsam die ersten beiden Schritte auf das Whiteboard.“ (Zeichnen Sie zwei Vorwärtspfeile.)

{panel type="teaching"}

# Teaching observations

To work it out students may initially need to see the program in action, so place the arrows within the grid to demonstrate what the rocket will do. Es können auch zunächst die ersten paar Anweisungen des Codes aufgeschrieben, getestet und dann um weitere Anweisungen ergänzt werden, was ebenfalls eine ausgezeichnete Methode ist. Wenn Sie Pfeile auf dem Gitterefeld platzieren, ist in Quadraten mit Richtungsänderungspfeilen auch ein Vorwärtspfeil erforderlich. Alternativ dazu können die Vorwärtspfeile auch auf der Linie zwischen den Quadraten platziert werden, was deren Funktion deutlicher macht.

{panel end}

„Versuchen wir es also einmal und schauen, was passiert.“

"Tester - could you please take these instructions and pass them onto the Bot. Unterstreiche alles, was nicht funktioniert, wenn du siehst, dass der Bot etwas macht, das nicht richtig aussieht, und gib mir dann das Whiteboard zurück, um herauszufinden, wie der Fehler behoben werden kann.“

{panel type="teaching"}

# Teaching observations

A key point in this activity is that the instructions are all written before they are tested. Es ist nicht gestattet, dem Bot zusätzliche Anweisungen zu geben. Der Bot muss die niedergeschriebenen Anweisungen genau befolgen (was amüsant sein kann, wenn er in die falsche Richtung geht). Genau das geschieht beim Programmieren: Es werden Anweisungen, also Befehle, für ein Programm geschrieben, die dann während des Programmablaufs ausgeführt werden, ohne dass der Programmierer eingreift. Programmierer müssen sich beim Schreiben der Anweisungen die zu erwartenden Vorgänge vor ihrem geistigen Auge vorstellen. Während des Testens zeigt sich dann, ob ihre Planung richtig war!

{panel end}

Teacher: "Bot - please pick up the rocket ready to receive the instructions for the tester." (The bot can carry a toy or token representing the rocket; or they can imagine that they are guiding it).

Der Tester liest dann vom Whiteboard ab: „Vorwärts bewegen, vorwärts bewegen.“

**Rocket to Mars program:**

{image file-path="img/topics/kidbots-rocket-2.gif" alt="This animation builds upon the previous grid image. The cell with the rocket ship contains an up arrow, and the cell above the rocket contains an up arrow."}

{panel type="teaching"}

# Teaching observations

An dieser Stelle könnten Sie die Frage aufwerfen, ob eventuell eine „Stopp“-Anweisung benötigt wird. Die Schüler sollten in der Lage sein, die Schlussfolgerung zu ziehen, dass das Programm automatisch stoppt, nachdem es keine weiteren Anweisungen gibt.

{panel end}

"Tester, did the program run as you expected it to?" Depending on the tester's response, if it did then carry on programming, otherwise fix what didn’t work and run that again. In this example the rocket should be in the square three to the left of Mars.

Now let’s add to it. What would we program next?

Point to where the next piece of code needs to be added and add turn right, turn right. (This is deliberately incorrect.)

**Rocket to Mars program:**

{image file-path="img/topics/kidbots-rocket-3.gif" alt="This animation builds upon the previous grid image. The cell two above the rocket ship contains two turn right arrows."}

Ich glaube, wir können es jetzt testen. Tester, please test my program (the programmer hands the program on the whiteboard to the tester and the bot should return to the starting square ready to rerun the program).

Teacher: Remember Tester, it’s your job to find any "bugs" in my program. Fehler sind alle nicht erwartungsgemäß ablaufenden Vorgänge. Deine Aufgabe ist es, den Teil des Codes zu unterstreichen, an der du bemerkst, dass eine Anweisung nicht den gewünschten Verlauf zu nehmen scheint. You can stop the Bot at the point that you think there is a bug.

Der **Tester** liest dann die Programmanweisungen vom Whiteboard ab und der Bot führt diese aus während sie vorgelesen werden.

1. Move forward
2. Move forward
3. Turn right
4. Turn right

{panel type="teaching"}

# Teaching observations

The tester should underline under the second turn right because the rocket will have turned around twice on the spot rather than turning once and going forward again. (Which is what is needed to get to Mars.)

{panel end}

Lehrer: „Ausgezeichnet. Du hast einen Fehler entdeckt! Ich freue mich, wenn Fehler entdeckt werden und ich mich an die Lösung des Problems machen kann. Lasst uns jetzt zusammen daran arbeiten, meinen Fehler ausfindig zu machen. Tester, you’ve done a great job finding it, but it’s the programmer’s job to find and fix the bug."

{panel type="teaching"}

# Teaching observations

If the class can’t identify how the program needs debugging then talk through each step and model it with the rocket. War die Vorwärtsbewegung zweckmäßig? War die zweite Vorwärtsbewegung zweckmäßig? Did turn right make sense? What about turn right again? Nein? Okay, ich glaube, wir haben den Fehler gefunden. Unterstreichen wir diesen also und überlegen uns, was wir hier ändern müssen. Vorwärts bewegen? Testen wir es.

{panel end}

Once the bug has been identified then ask the Tester to test again. Ask the Bot to pick up the rocket and go back to the start position, then the Tester reads them the instructions.

{image file-path="img/topics/kidbots-rocket-4.gif" alt="This animation builds upon the previous grid image. The cell two above the rocket ship now contains one turn right arrow and one forward arrow. The cell to the right of this cell contains one forward arrow. The cell to the right of this cell (one left of Mars) contains one forward arrow."}

Did we successfully program the rocket to land on Mars? How do we know?

{panel type="teaching"}

# Teaching observations

We successfully programmed the rocket to land on Mars when the rocket and Mars are in the same square.

{panel end}

Are there other ways we could have programmed the rocket to get to Mars? (There will be lots of ways; for example, Right, Forward, Forward, Forward, Left, Forward, Forward will work.) Discuss the programming options and test each one. What if we want the rocket to get to Mars, and then come back safely?

{panel type="teaching"}

# Teaching observations

Beim Programmieren gibt es zahlreiche Möglichkeiten, denselben Vorgang zu programmieren. Manche mögen effizienter sein als andere, sie sind jedoch alle richtig, sofern sie das gewünschte Ergebnis erzielen. For example a student might program the rocket to go around the outside of the grid and then go and get to Mars. Dies wäre eine richtige Lösung, erfordert jedoch eine Menge zusätzlichen Code, der nicht notwendig ist. More commonly, two programmers might come up with programs that take a similar amount of time to achieve the same result, in this case (for example, "Forward, Left, Forward, Right" and "Left, Forward, Right, Forward" get the Bot to the same place and orientation; both are equivalent programs; there is rarely a single solution that is the best one, and this means that if a student’s work looks different to a model answer that might be available, it isn’t necessarily wrong. Sofern das beabsichtigte Ergebnis erzielt wird, wenn auch auf eine andere Weise, ist die Lösung dennoch richtig.

{panel end}

{panel type="teaching"}

# Teaching observations

Either set up your students to be working around the outside of your large grid, or you can use a smaller grid like a chessboard or the back of a 100s board (or print the grid provided with this lesson), in which case the bot moves a counter on the board instead of walking around the grid.

If you have multiple small grids, students can work independently in groups of three (programmer, tester, bot). Wenn Sie ein großes Gitterfeld verwenden, kann eine Schülergruppe an ihrem Programm arbeiten, während eine andere Gruppe ihr Programm testet. Jede Gruppe darf ihr Programm einmal testen und dann ist die nächste Gruppe dran, während die vorherige Gruppe mit der Programmfehlersuche beginnt.

{panel end}

Have the students choose their own two toys (one to be a space travelling object, the other to be the destination) and have them practise this task, as follows.

1. Place the traveller on a square on the edge of the grid, facing inwards.
2. Place the destination toy inside the grid.
3. The programmer writes down the program on a whiteboard.
4. The tester then takes the whiteboard and a different coloured whiteboard pen. The tester tells the Bot each instruction in the program. The tester puts a tick next to the code that is correct and underlines when the code is different to what the Bot should be doing. If this happens the Tester says "Stop" and the Bot stops and goes back to the start. The Tester gives the whiteboard to the Developer, who then debugs the code, and gives the Tester a revised version.
5. Wiederholt Schritt 4, bis das Programm fehlerfrei ist und wie vorgesehen funktioniert.
6. Change roles and move the Bot (space travelling object) starting point and the toy that represents the destination until everyone has had a turn.

{panel type="teaching"}

# Teaching observations

Wenn Sie bemerken, dass Ihre Schüler Unterstützung benötigen, um die benötigten Anweisungen zu visualisieren, können Sie die zur Verfügung gestellten Pfeile (Karten) auf dem Boden verwenden oder, bei einem kleinen Tischgitterfeld, mit einem Whiteboardstift oder kleinen Pfeilen aushelfen. So können sich die Schüler leichter vorstellen, was sie programmieren möchten.

{panel end}

### Die nächste Aufgabe

Add barriers to the grid so that the path is more complex because the Bot needs to avoid the barriers. This could be space junk and comets, or you could invent a new scenario for the grid.

{image file-path="img/topics/kidbots-rocket-barriers.png" alt="A grid with various cells containing planets, comets, space junk, etc."}

### Weitere Aufgaben

Have groups program the trip without using the left hand turn (i.e. the only instructions are Forward and Right turn.) Scaffold the students to realise that a left hand turn can be achieved by doing three Right turn instructions. Then challenge them to program with a Left turn but no Right turn.

Ask if they can write programs with only the Right and Left turn instructions (i.e. no Forward instruction)? (This isn't possible, as you would only be able to turn around on one square.)

{panel type="teaching"}

# Teaching observations

Durch Eliminieren einer der Drehanweisungen wird deutlich, dass unterschiedliche Anweisungssätze dasselbe Ergebnis erzielen können, wobei jedoch manche praktischer sind als andere (zum Beispiel gibt es viele verschiedene Programmiersprachen, die im Prinzip dieselben Berechnungen anstellen, nur dass manche für einige Zwecke besser geeignet sind als andere).

Werden weniger Anweisungen eingesetzt, vereinfacht dies die Konstruktion eines Computers, was diesen wiederum schneller oder günstiger macht. Nehmen wir das Beispiel eines äußerst einfachen Computers, der über eine Additionsanweisung, jedoch nicht über eine Multiplikationsanweisung verfügt. Wenn nun Multiplikationen ausgeführt werden müssten, könnte dies durch Ausführen zahlreicher Additionen erreicht werden. Viele gebräuchliche Prozessoren sind heutzutage mit reduzierten Anweisungs- bzw. Befehlsssätzen ausgestattet (diese werden Reduced Instruction Set Computers bzw. RISC genannt), da hierdurch mehr Leistungsfähigkeit erzielt wird, als mit umfangreichen Befehlssätzen (Complex Instruction Set Computers bzw. CISC).

{panel end}

## Applying what we have just learnt

It’s quite common to think that programming is some kind of special talent that people either have or don’t have, but this couldn’t be further from the truth! Wie alle Fertigkeiten ist auch Programmieren etwas, das man sich durch Übung, Fehler machen und aus diesen Fehlern lernen aneignen kann. The most important skill that programmers need is to be able to communicate with others, especially when they are finding and describing bugs. Fehler sind beim Programmieren keine Seltenheit. Daher ist es ungemein wichtig, erkennen zu können, wo ein Fehler auftritt, und Problemlösungen zur Fehlerbeseitigung erarbeiten zu können. Es spielt keine Rolle, wieviel Programmiererfahrung jemand hat. Es wird immer Fehler geben, die es zu finden und zu beseitigen gilt. That’s why the word "debugging" is so important to programmers.

## Lesson reflection

Now that you are all programmers, what did you think was the most challenging part of being a programmer?