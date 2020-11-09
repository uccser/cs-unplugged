# Comment les chiffres binaires fonctionnent

## Question clé

- Comment pensez-vous qu'un appareil numérique enregistre les informations ?

Acceptez et notez toutes les réponses, à revoir à la fin du cours.

## Lancement du cours

{panel type="video"}

# Voir ce cours en action

{video url="https://vimeo.com/437725275"}

{panel end}

{panel type="general"}

# Note des auteurs

Nous avons remarqué que lorsque nous enseignons le système de numération binaire aux élèves de 5 à 7 ans, nous nous concentrons sur la connaissance des nombres et leur identification plutôt que sur la façon dont le système binaire fonctionne. We also support students to learn to count by one to one matching, because they are counting the dots. Les élèves sont motivés pour apprendre parce qu'ils apprennent comment les ordinateurs stockent des informations. Les élèves pourraient vous poser des questions et être enthousiastes à l'idée d'explorer davantage les concepts décrits dans cette leçon. Nous avons ajouté beaucoup d’information à ce cours, cependant, il n’est pas dans notre intention que vous enseigniez et traitiez tous les concepts, mais plutôt que vous ayez toutes les informations nécessaires à portée de main si vos élèves demandent à en apprendre plus.

{panel end}

{panel type="general"}

# Notes sur les ressources

Il existe aussi une version interactive en ligne des cartes binaires (une version à quatre cartes, qui correspond à cette activité, ou une version à cinq cartes si les élèves sont à l'aise avec les nombres jusqu'à 31), ici : [Computer Science Field Guide](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8). Cependant, nous recommandons fortement d'utiliser des cartes physiques pour commencer.

{panel end}

Saviez-vous qu'à l'intérieur de n'importe quel ordinateur il y avait des milliards (c'est vraiment un très très grand nombre) de toutes petites choses qui peuvent être allumées ou éteintes, comme un interrupteur, et que, quand vous avez beaucoup de ces choses ensemble, ils peuvent afficher un nombre, une lettre, un film ou faire fonctionner votre jeu préféré sur votre appareil ? Voyons donc comment elles fonctionnent. Maintenant imaginons que nous sommes tellement petits que nous sommes à l'intérieur d'un ordinateur et que nous faisons en sorte que l'ordinateur affiche un nombre. Êtes-vous prêts ?

Tout d'abord, voici une carte qui est la petite chose qui peut être activée ou désactivée. Le mot technique pour cela est un "bit".

1. Tenez les 4 cartes (1, 2, 4 et 8 points), mais cachez le nombre de points aux élèves. Demandez à 4 élèves d'être volontaires pour être des “chiffres binaires”, et de se mettre en ligne devant la classe.

2. Donnez la carte avec un point à la personne à droite. Explain that they are one "bit" (binary digit), and can be on or off, black or white, 0 or 1 dots. La seule règle est que leur carte est soit complètement visible, soit retournée. Donnez la deuxième carte, de sorte que la première carte reste toute à droite. Faites remarquer que cette carte comporte soit deux points, soit aucun.
    
    {image file-path="img/topics/col_binary_4_kids_2_cards.png" alt="Deux enfants tenant des cartes binaires"}

3. Demandez à la classe quel sera le nombre de points sur la prochaine carte. Demandez-leur d'expliquer pourquoi ils pensent cela.
    
    {panel type="teaching"}
    
    # Observations pour l'enseignant
    
    Les élèves suggèrent généralement que le prochain nombre sera 3. S'ils suggèrent 4, il est possible qu'ils aient déjà fait l'activité auparavant (ou qu'ils ont vu les cartes que vous tenez !), ou qu'ils ont de très bonnes compétences en reconnaissance de suites ! S'ils suggèrent le mauvais nombre, ne les corrigez pas, mais continuez sans commentaire, de sorte qu'ils peuvent se construire la règle pour eux-mêmes.
    
    {panel end}

4. Sans rien dire, donnez la carte à quatre points, et laissez-les essayer de trouver le motif. Cela dépendra de leur niveau de connaissance des nombres. Mentionnez que chaque nombre est multiplié par deux (ou que si vous aviez deux exemplaires d'une carte cela vous donnerait la carte à côté), et passez à l'étape suivante.
    
    {image file-path="img/topics/col_binary_4_kids_3_cards.png" alt="Trois enfants tenant des cartes binaires"}
    
    {panel type="teaching"}
    
    # Observations pour l'enseignant
    
    Habituellement, certains élèves feront remarquer que vous avez oublié le 3, mais dites simplement que vous n'avez pas commis d'erreur, qu'il se passe quelque chose avec les nombres et que vous serez en mesure d'obtenir 3 en utilisant les cartes.
    
    {panel end}

5. Demandez quelle est la prochaine carte, et pourquoi.
    
    {panel type="teaching"}
    
    # Observations pour l'enseignant
    
    À ce stade, il est courant pour les élèves de répondre que c'est le nombre 6 (puisqu'il suit les nombres 2 et 4). Cependant, si vous les laissez réfléchir un peu plus, certains vont habituellement proposer 8, et ces élèves devraient pouvoir convaincre les autres qu'ils ont raison. Il y a plusieurs façons pour les élèves d'expliquer cela. Par exemple que chaque carte est le double de la précédente, ou que si vous prenez deux exemplaires d'une carte, vous obtenez la suivante. Certains peuvent réciter la suite : 1+1=2, 2+2=4, 4+4=8.
    
    Si votre classe apprend à compter, montrez toutes les cartes et comptez combien il y a de points sur chacune d'entre elles. Recherchez la succession de doublements et comptez les points pour le prouver.
    
    {panel end}

6. Montrez la 4e carte et donnez-la :
    
    {panel type="teaching"}
    
    # Observations pour l'enseignant
    
    Background information for those who are curious! If we kept handing out cards then once we got to 8 cards we would have 256 dots in total if we added up all the cards. C'est 8 bits, ce qui est communément appelé un octet. It may be distracting to bring this up at this point, but some students may already be familiar with the idea that 8 bits is a byte, and make that observation. However, in the meantime, we'll work with a 4-bit representation, which isn't as useful as a whole byte, but a good size for teaching younger students. 4 bits est en fait un nibble (parfois écrit nybble) ! C'est une information amusante pour les élèves intéressés.
    
    A common mistake is to hand out the cards from left to right, but it's convention in number representation that the least significant value is on the right, and this is an important idea for students to take away from this activity.
    
    {panel end}

## Activités de la leçon

1. Tell the students that the rule is that a card either has the dots showing, or hiding. If we can turn cards on (showing) and off (hiding) by showing the front and back of the card, how would we show 3 dots? Commencez par demander : combien de points sont sur la carte la plus à gauche ? Comptez ensemble qu'il y a 8 points. Let’s look at the number line. Est-ce que 8 est plus grand que 3? Cachons le car c'est trop grand. Maintenant, regardons la carte suivante, combien de points peut-on voir? Comptons les. Il y en a 4, est-ce que 4 est plus grand que 3? Oui, nous devons donc cacher cette carte. Si nous n'avions pas masqué la carte 4 qu'arriverait-il? (Il y aurait trop de points). Combien de points y a-t-il sur la carte suivante? Comptons les. Il y a deux points. Let’s look at the number 3, (show it with materials and show that 2 fits into 3, with how many left over?) We need one more dot to make the number 3. Donc on laisse cette carte visible.
    
    Sans avoir eu d'autres règles que chaque carte soit visible ou pas, les élèves arrivent généralement à la représentation suivante.
    
    {image file-path="img/topics/binary_cards_equals_three.png" alt="Diagramme montrant que les 2 cartes binaires font le nombre 3"}
    
    {panel type="math"}
    
    # Liens mathématiques
    
    At a junior level we are focusing on using this counting system to represent numbers and making the association that with these “bits” you can make any number. We’re not going to focus on further knowledge about number base systems. The information below is extra information for you.
    
    Pour les enseignants: la base 10 (notre système de comptage) a 10 chiffres, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. When we count in base 10, we count from 0 to 9 and then run out of digits. Nous devons donc ajouter une autre colonne; nous mettons un 1 dans cette colonne et recommençons à compter à partir de 0. This makes the number 10, we then repeat that process until the tens column is 9 and the ones column is 9 (making 99); from there we then add another column. Hence we have the familiar place value system that can be shown something like this:
    
    100,000s | 10,000s | 1,000s | 100s |10s | 1 **Note: Use the appropriate place value example based on what you have already taught in your class; this is an extended example.**
    
    Base 2 (binary) follows the same logic, except it moves a lot quicker to the “next” place value, because there are only two digits, 0 and 1. The binary place values look like this:
    
    32 | 16 | 8 | 4 | 2 | 1 |
    
    Parfois, les élèves confondent l'ordre des chiffres dans une représentation binaire. To support students to understand the correct ordering of binary digits, ask the question: If I was going to give you $435.00 which number are you most interested in? Est-ce le 4 ou le 5? Pourquoi cela? C'est la même chose pour le binaire, la valeur la plus basse (le chiffre le moins significatif) est tout à droite, alors que le chiffre le plus significatif est tout à gauche.
    
    La base 16 est aussi couramment utilisée dans les ordinateurs - elle est appelée hexadécimal, et dispose de 16 chiffres. Tout cela est bien au-delà de la portée de cette leçon, nous avons voulu souligner qu'un chiffre hexadécimal est l'équivalent de 4 chiffres binaires (bits), car les deux peuvent représenter 16 valeurs différentes (de 0 à 15). So this exercise that the students are doing provides a great basis for later understanding another common representation that they will encounter on digital devices.
    
    {panel end}

2. Now ask "How would you make the number 6?" (Again, start by asking if they want the 8 card, and so on from left to right).

3. The process we have been following to make these numbers is an algorithm, which converts our normal counting numbers to a binary representation. Together let’s think through the steps we followed to do this. We'll do this by using the earlier example of representing the number 3 again.
    
    a. Start with all the numbers switched to on (all the dots visible). You could start to introduce abstract representations, like varying the description of the cards (visible/hidden; dots/no-dots; white/black if the backing is black; yes/no; or on/off)
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_4.png" alt="4 ampoules allumées"}
    
    b. Est-ce que 8 tient dans 3 ? Non - donc retournez la
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_3.png" alt="3 ampoules allumées"}
    
    c. Est-ce que 4 tient dans 3 ? Non - donc retournez la
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_2.png" alt="2 ampoules allumées"}
    
    d. Does 2 fit into 3? Yes - so keep it on. How many are left over? (1)
    
    e. Does 1 fit into 1? Yes - so keep it on. How many are left over? (none)
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_2.png" alt="2 ampoules allumées"}

## Appliquer ce que nous venons d'apprendre

- Groupez les élèves en binômes
- Give each pair a set of the smaller binary cards
- Have them practise the algorithm for numbers below 10.

1. Expliquez aux élèves que nous travaillons avec seulement deux chiffres, et que nous les appelons donc chiffres binaires. (You could explore the meaning of the "bi" prefix with words like bicycle, biennial, bilingual and bicultural.) Binary digits are so common that we have a short name for them: write "binary digit" on a piece of paper, then rip off the "bi" at the start, and the "t" at the end, put it together and ask what the combined word ("bit") spells. This is the short name for a binary digit, which is why we've been referring to the cards as bits; the 4 cards that they have are actually 4 bits.

2. Now let’s count from the smallest number that we can make, up to the highest number
    
    a. Quel est le plus petit nombre? (ils peuvent suggérer 1, puis réaliser qu'en fait c'est 0).

3. Get the number 0 displayed on the cards (i.e. no dots showing)

4. Maintenant comptez dans l'ordre croissant 1, 2, 3, 4 ... (chaque binôme devrait trouver les nombres entre eux)

5. Une fois qu'ils commencent à entrer dans une routine, demandez : combien de fois voyons-nous la carte à 1 point ? (une fois sur deux, pour chaque nombre impair)
    
    a. Quels autres motifs voyons nous? (the 2-dot card flips on every second count, the 4-dot on every 4th and so on; the 8 dot card doesn't do much; this may be challenging for some students to recognise, and the main goal is that they are aware that the 1-dot card flips every time, and that every second number is an odd number).

6. Continue until all the cards are switched to “on” and have counted to 15. Que se passe-t-il ensuite? (Nous devons ajouter une nouvelle carte.) Combien de points a-t-elle ? (16) Que devons-nous faire aux 4 autres cartes quand nous arrivons à 16? (nous devons toutes les retourner)

7. Idées d'extension...
    
    a. Donc quand j'ai 2 bits, je peux faire un maximum de ? (3)
    
    b. J'ajoute un nouveau bit, combien a-t-il de points ? (4)
    
    c. Je désactive les deux premiers bits pour donner 4 n'est-ce pas ?
    
    d. Maintenant activons les 3 bits, cela donne combien ? (7)
    
    e. J'ajoute un nouveau bit, combien de points a-t-il ? (8)
    
    f. Repeat until a pattern is recognised that the number on the next card is one more than the total number of dots on all the cards to the right (e.g. there are 7 dots on the 4, 2 and 1 cards, so the next card to the left is 8). This makes it easy to work out the number if all the bits are switched on - double the left-hand card, and subtract 1.
    
    g. Combien de nombres différents puis-je faire avec 2 bits ? (4; souvent les élèves disent 3 car ils ne comptent pas le 0).
    
    h. Ajoutons le bit suivant; combien de nombre différents peut on faire maintenant ? (8, encore une fois 7 sera surement proposé).
    
    i. Répétez jusqu'à ce que les élèves reconnaissent qu'à chaque fois que l'on ajoute un nouveau bit, on peut représenter deux fois plus de nombres.

{panel type="teaching"}

# Observations pour l'enseignant

A concept that students may struggle with here is that the number of values is one more than the maximum value (e.g. from 0 to 7, there are 8 different numbers). The same observation occurs with the number of digits in conventional decimal numbers; the largest digit is 9, but there are 10 possible digits (counting 0). This is sometimes called the fencepost problem (the number of fence posts is one more than the number of gaps between them), and it comes up a lot in computing and in maths.

{panel end}

## Réflexion sur la leçon

- Est-ce que cette activité marcherait si nous utilisions des cartes blanches et couleur crème ? Pourquoi ? Pourquoi pas ?
    
    - En principe vous pourriez les utiliser, mais ce ne serait pas une bonne idée. We are looking for the answer that they are not contrasting colours, therefore it would be difficult to see if it is actually on or off. Les ordinateurs sont plus faciles à construire et cassent moins souvent lorsque nous utilisons deux valeurs contrastées.

- What are some other ways we could physically show that each of the bits are on or off?
    
    - Ideas could include holding the cards up high, or down low; simply holding up a hand; sitting down or standing up; or using a different representation such as lights that are on or off.

- What else could we use to represent two opposites, like on and off, in writing?
    
    - Perhaps a cross or tick; happy or sad face; or any other pair of symbols.