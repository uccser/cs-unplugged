# Comment les chiffres binaires fonctionnent

## Questions clés

- Quels sont les différents systèmes de numération que nous connaissons ? (Les réponses peuvent inclure : Les chiffres romains; les traits; les bases numériques comme le binaire, l'octal et l'hexadécimal; les langages tels que le Chinois ou l'ancien Égyptien.)
- Pourquoi utilisons-nous habituellement 10 chiffres ? (Probablement parce que nous avons 10 doigts, et que c'est plus simple d'écrire avec qu'avec des batons par exemple)
- Pourquoi avons-nous différents systèmes de numération ? (They are convenient for different things e.g. tally marks are easy if you are counting; Roman numerals can be useful for making a number look more mysterious or harder to read.)

## Lancement du cours

{panel type="video"}

# Voir l'activité en action

{video url="https://vimeo.com/437725275"}

{panel end}

{panel type="general"}

# Note des auteurs

We’ve noticed that once students understand how the binary number system works, they have many questions and are excited to explore the concepts outlined in this lesson further. Nous avons ajouté beaucoup d’information à ce cours, cependant, il n’est pas dans notre intention que vous enseigniez et traitiez tous les concepts, mais plutôt que vous ayez toutes les informations nécessaires à portée de main si vos élèves demandent à en apprendre plus.

{panel end}

{panel type="general"}

# Notes sur les ressources

Il existe également une version interactive en ligne des cartes binaires [ici](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), du [Computer Science Field Guide ](http://www.csfieldguide.org.nz/), mais il est préférable de travailler avec des cartes physiques.

{panel end}

1. Prenez les 5 premières cartes (1, 2, 4, 8 et 16 points), mais ne laissez pas les élèves voir les points. Demandez 5 volontaires pour être des chiffre binaires, et mettez les en ligne en face de la classe.

2. Donnez la carte avec un point à la personne à droite. Expliquez qu'il représente un "bit" (binary digit), et peut être activé ou non, blanc ou noir, 0 ou 1. La seule règle est que leur carte est soit complètement visible, soit retournée. Tendez la seconde carte à la deuxième personne sur la droite. Point out that this card has either 2 dots (visible), or none (upside down).
    
    {image file-path="img/topics/col_binary_2cards.png" alt="2 enfants tenant des cartes binaires"}

3. Demandez à la classe quel sera le nombre de points sur la prochaine carte. Demandez-leur d'expliquer pourquoi ils pensent cela.
    
    {panel type="teaching"}
    
    # Observations pour l'enseignant
    
    Les élèves suggèrent généralement que le prochain nombre sera 3. S'ils suggèrent 4, ils ont probablement fait l'activité avant (ou ont vu les cartes que vous tenez !) S'ils suggèrent le mauvais nombre, ne les corrigez pas, mais continuez sans commentaire, de sorte qu'ils peuvent se construire la règle pour eux-mêmes.
    
    {panel end}

4. Sans rien dire, donnez la carte à quatre points, et laissez les essayer de trouver le motif.
    
    {image file-path="img/topics/col_binary_3cards.png" alt="3 enfants tenant des cartes binaires"}
    
    {panel type="teaching"}
    
    # Observations pour l'enseignant
    
    Habituellement, certains étudiants se plaignent que vous avez raté le trois, mais dites simplement que vous n'avez pas fait d'erreur. Cela leur donne l'opportunité d'essayer de construire le motif par eux mêmes.
    
    {panel end}

5. Demandez quelle est la prochaine carte, et pourquoi.
    
    {panel type="teaching"}
    
    # Observations pour l'enseignant
    
    À ce stade, il est courant que les élèves devinent que c'est 6 (étant donné que 6 suit les nombres 2 et 4). Cependant, si vous les laissez réfléchir un petit peu plus, certains vont surement proposer 8, et ces élèves devraient être capables de convaincre les autres qu'ils ont raison (il y a de nombreuses manières pour l'élève d'expliquer cela, par exemple, chaque carte est le double de la précédente, ou que si vous prenez deux fois une carte, vous obtenez la suivante)
    
    {panel end}

6. Les élèves devraient être capables de trouver la cinquième carte (16 points) sans aide :
    
    {image file-path="img/topics/col_binary_5cards.png" alt="5 enfants tenant des cartes binaires"}

7. Combien de points posséderait la carte suivante si nous continuions ? (32) La suivante...? (Il n'y a pas besoin que les élèves tiennent ces cartes, elles ne seront pas utilisées dans la prochaine partie de l'activité, mais vous pouvez les montrer pour confirmer qu'ils ont raison).

8. Continuez avec 64 et 128 points.
    
    {panel type="teaching"}
    
    # Observations pour l'enseignant
    
    Au bout de 128 points il devrait y avoir 8 cartes. Cela représente 8 bits, ce qui correspond à un octet. Ça peut être déroutant de parler de cela à ce moment, mais certains élèves sont peut être déjà familier avec l'idée que 8 bits représentent un octet, et font l'observation. Cependant, nous travaillerons avec une représentation sur 5 bits, qui n'est pas aussi utile qu'un octet complet, mais une bonne taille pour enseigner. (A byte is a convenient grouping of bits, and usually computer storage is based around bytes rather than individual bits; it's just the same as eggs being sold as a dozen; they could be sold individually, but groups of a dozen are usually more convenient for everyone concerned.)
    
    A common mistake is to hand out the cards from left to right, but it's convention in number representation that the least significant value is on the right, and this is an important idea for students to take away from this activity.
    
    {panel end}

## Activités de la leçon

1. Rappelez aux élèves que la règle est qu'une carte doit avoir soit tous ses points visibles, soit aucun (carte retournée). Si nous pouvons activer et désactiver les cartes en montrant la face avant ou en la retournant, comment montrerions-nous exactement 9 points ? Commencez par demander si ils veulent la carte 16 (ils devraient remarquer qu'elle possède trop de points), puis la carte 8 (ils devraient cette fois ci remarquer que sans elle, il n'y aura plus assez de points), puis 4, 2 et 1. Sans avoir d'autres instructions que le fait de pouvoir retourner ou non une carte, les élèves devraient normalement trouver la représentation suivante.
    
    {image file-path="img/topics/binary-cards-total-9.png" alt="Diagramme montrant que 2 cartes binaires permettent de former un 9"}
    
    {panel type="math"}
    
    # Liens mathématiques
    
    La base 10 (notre système de numération) possède 10 chiffres, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. When we count in base 10, we count from 0 to 9 and then run out of digits. Nous devons donc ajouter une autre colonne; nous mettons un 1 dans cette colonne et recommençons à compter à partir de 0. This makes the number 10, we then repeat that process until the tens column is 9 and the ones column is 9 (making 99); from there we then add another column. Hence we have the familiar place value system that can be shown something like this:
    
    100,000s | 10,000s | 1,000s | 100s |10s | 1
    
    *Note: Use the appropriate place value example based on what you have already taught in your class; this is an extended example.*
    
    Base 2 (binary) follows the same logic, except it moves a lot quicker to the “next” place value, because there are only two digits, 0 and 1. The binary place values look like this:
    
    32 | 16 | 8 | 4 | 2 | 1 |
    
    Parfois, les élèves confondent l'ordre des chiffres dans une représentation binaire. To support students to understand the correct ordering of binary digits, ask the question: If I was going to give you $435.00 which number are you most interested in? Est-ce le 4 ou le 5? Pour quelle raison? C'est la même chose pour les chiffres binaires. La valeur la plus basse (le chiffre le moins significatif) est tout à droite, tandis que le chiffre le plus significatif est tout à gauche.
    
    {panel end}

2. Demandez maintenant "Comment formeriez vous le nombre 21 ?" (À nouveau, commencez par demander si ils veulent la carte 16, puis la carte 8, et ainsi de suite, de gauche à droite).

3. C'est un algorithme pour convertir les nombres dans une représentation binaire. Réfléchissons ensemble aux étapes pour le faire.
    
    a. Commencez avec tous les nombres activés (les points sont visibles).
    
    {image file-path="img/topics/lightbulb_series_1.png" alt="5 ampoules allumées"}
    
    b. Considérez la représentation du nombre 10
    
    c. Est-ce que 16 tient dans 10? Non - donc désactivez la carte (retournez la)
    
    {image file-path="img/topics/lightbulb_series_2.png" alt="4 ampoules allumées}
    
    d. Est-ce que 8 tient dans 10 ? Oui - donc gardez la carte activée. Combien reste-t-il ? (2)
    
    e. Est-ce que 4 tient dans 2 ? Non - désactivez la carte
    
    {image file-path="img/topics/lightbulb_series_3.png" alt="3 ampoules allumées"}
    
    f. Est-ce que 2 tient dans 2 ? Oui - donc continuez. Combien reste-t-il ? (Rien)
    
    g. Donc désactivez 1.
    
    {image file-path="img/topics/lightbulb_series_4.png" alt="2 ampoules allumées"}

## Appliquer ce que nous venons d'apprendre

- Groupez les élèves en binômes.
- Give each pair a set of the smaller binary cards (either 5 or 6 cards, depending on the range of numbers they are comfortable with).
- Starting with just 5 cards, have them practise the algorithm (deciding about each card from left to right) for numbers such as 20, 15, and 8.

1. Expliquez aux élèves que nous ne travaillons qu'avec deux chiffres, et que nous les appelons donc chiffres binaires. They are so common that we have a short name for them: write "binary digit" on a piece of paper, then rip off the "bi" at the start, and the "t" at the end, put it together and ask what the combined word ("bit") spells. This is the short name for a binary digit, so the 5 cards that they have are actually 5 bits.

2. Now let’s count from the smallest number we can make up to the highest number:
    
    a. Quel est le plus petit nombre? (il pourraient proposer 1, avant de réaliser que c'est 0).

3. Get the number zero displayed on the cards (i.e. no dots showing).

4. Comptez alors dans l'ordre croissant: 1, 2, 3, 4 ... (chaque binôme devrait pouvoir trouver les nombres par eux-mêmes).

5. Une fois qu'ils commencent à s'habituer, demandez : à quelle fréquence observons nous la carte 1 ? (tous les deux nombres, pour chaque nombre impair)
    
    a. Quels autres motifs pouvons-nous voir ? (certains pourraient remarquer que la carte 2 est retournée tous les 2 nombres, la 4 tous les 4 nombres et ainsi de suite; la carte 16 n'est pas souvent retournée !)

6. Continuez jusqu'à ce que toutes les cartes soient activées et donnent le nombre 31. Que se passe-t-il ensuite ? (Nous devons ajouter une nouvelle carte.) Combien de points a-t-elle ? (32) Que devons nous faire avec les 5 autres cartes pour obtenir 32 ? (nous devons toutes les retourner)

7. Allons un peu plus loin...
    
    a. Donc quand j'ai deux bits, je peux faire un maximum de ? (3)
    
    b. Je rajoute un nouveau bit et combien a-t-il de points ? (4)
    
    c. Je "désactive" (retourne) les deux premiers bits pour faire 4 n'est-ce pas ?
    
    d. Maintenant allumons les 3 bits, nous obtenons combien ? (7)
    
    e. J'ajoute un nouveau bit, combien de points avons nous ? (8)
    
    f. Repeat until a pattern is recognised that the number on the next card to the left is one more than the total number of dots on all the cards to the right (e.g. there are 15 dots on the 8, 4, 2 and 1 cards, so the next card to the left is 16). Il est donc facile de déterminer le nombre si tous les bits sont activés - doublez la valeur de la carte la plus a gauche, et enlevez 1.
    
    g. Combien de nombres différents puis-je faire avec deux bits ? (4; souvent, les élèves disent 3 parce qu'ils n'ont pas compté le 0)
    
    h. Ajoutons le bit suivant; combien de nombres peut-on faire maintenant ? (8, 7 sera souvent proposé comme première réponse)
    
    i. Répéter jusqu'à ce qu'un motif soit reconnu : à chaque fois que nous ajoutons un bit, nous pouvons représenter deux fois plus de chiffres.

{panel type="teaching"}

# Observations sur l'enseignement

A concept that students may struggle with here is that the number of values is one more than the maximum value (e.g. from 0 to 7, there are 8 different numbers). The same observation occurs with the number of digits in conventional decimal numbers; the largest digit is 9, but there are 10 possible digits (counting 0). This is sometimes called the fencepost problem (the number of fence posts is one more than the number of gaps between them), and it comes up a lot in computing.

{panel end}

## Lesson Reflection

- Cette activité fonctionnerait-elle si nous utilisions des cartes de couleur blanche et crème? Pourquoi? Pourquoi pas? (En principe, vous pourriez les utiliser mais ce ne serait pas une bonne idée. We are looking for the answer that they are not contrasting colours, therefore it would be difficult to see if it is actually on or off. Cela explique pourquoi les ordinateurs utilisent des représentations physiques faciles à distinguer.)
- What are some contrasting symbols or ways that we can show on and off in binary?
    
    - (Ideas could include holding the cards up high, or down low; simply holding up a hand; sitting down or standing up; or using a different representation such as lights that are on or off.)

- Computers are cheaper and easier to build if they represent data with just two contrasting values, which we represent as the numbers 0 and 1. Quoi d'autre pourrions-nous utiliser pour représenter deux opposés à l'écrit? (Peut-être une croix ou un rond, un visage heureux ou triste, ou n'importe quelle autre paire de symboles.)

- Extending this idea, the numbers might be represented by a voltage that is either close to 5 volts, or close to 0 volts. The circuitry is built so that anything less than about 2.5 volts counts as 0 and anything over 2.5 volts counts as 1. Like the contrasting colours of the cards, this is very easy to recognise. We could have had 10 colours of cards to represent the digits from 0 to 10, and we could have ten voltage ranges (0 to 0.5, 0.5 to 1.0 and so on), but it's way more complicated to build fast and accurate circuitry for this.