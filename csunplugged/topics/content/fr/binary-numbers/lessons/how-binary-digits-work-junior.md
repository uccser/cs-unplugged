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

Nous avons remarqué que lorsque nous enseignons le système de numération binaire aux élèves de 5 à 7 ans, nous nous concentrons sur la connaissance des nombres et leur identification plutôt que sur la façon dont le système binaire fonctionne. Nous aidons également les élèves à apprendre à compter de un en un, car ils comptent les points. Les élèves sont motivés pour apprendre parce qu'ils apprennent comment les ordinateurs stockent des informations. Les élèves pourraient vous poser des questions et être enthousiastes à l'idée d'explorer davantage les concepts décrits dans cette leçon. Nous avons ajouté beaucoup d’information à ce cours, cependant, il n’est pas dans notre intention que vous enseigniez et traitiez tous les concepts, mais plutôt que vous ayez toutes les informations nécessaires à portée de main si vos élèves demandent à en apprendre plus.

{panel end}

{panel type="general"}

# Notes sur les ressources

Il existe aussi une version interactive en ligne des cartes binaires (une version à quatre cartes, qui correspond à cette activité, ou une version à cinq cartes si les élèves sont à l'aise avec les nombres jusqu'à 31), ici : [Computer Science Field Guide](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8). Cependant, nous recommandons fortement d'utiliser des cartes physiques pour commencer.

{panel end}

Saviez-vous qu'à l'intérieur de n'importe quel ordinateur il y avait des milliards (c'est vraiment un très très grand nombre) de toutes petites choses qui peuvent être allumées ou éteintes, comme un interrupteur, et que, quand vous avez beaucoup de ces choses ensemble, ils peuvent afficher un nombre, une lettre, un film ou faire fonctionner votre jeu préféré sur votre appareil ? Voyons donc comment elles fonctionnent. Maintenant imaginons que nous sommes tellement petits que nous sommes à l'intérieur d'un ordinateur et que nous faisons en sorte que l'ordinateur affiche un nombre. Êtes-vous prêts ?

Tout d'abord, voici une carte qui est la petite chose qui peut être activée ou désactivée. Le mot technique pour cela est un "bit".

1. Tenez les 4 cartes (1, 2, 4 et 8 points), mais cachez le nombre de points aux élèves. Demandez à 4 élèves d'être volontaires pour être des “chiffres binaires”, et de se mettre en ligne devant la classe.

2. Donnez la carte avec un point à la personne à droite. Expliquez que la personne est un "bit" (chiffre binaire), et qu'elle peut être allumée ou éteinte, noire ou blanche, 0 ou 1 point. La seule règle est que leur carte est soit complètement visible, soit retournée. Donnez la deuxième carte, de sorte que la première carte reste toute à droite. Faites remarquer que cette carte comporte soit deux points, soit aucun.
    
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
    
    Informations supplémentaires pour ceux qui sont curieux ! Si nous avions continué à distribuer les cartes jusqu'à en avoir 8 nous aurions 256 points au total, si l'on additionne toutes les cartes. C'est 8 bits, ce qui est communément appelé un octet. Il peut être gênant d'aborder cette question à ce stade, mais certains élèves seront peut-être déjà familier avec l'idée que 8 bits forment un octet, et feront cette observation. Toutefois, pour le moment, nous allons travailler avec une représentation à 4 bits, qui n'est pas aussi utile qu'un octet, mais une bonne taille pour enseigner à des élèves plus jeunes. 4 bits est en fait un nibble (parfois écrit nybble) ! C'est une information amusante pour les élèves intéressés.
    
    Une erreur courante consiste à distribuer les cartes de gauche à droite, mais c'est la convention dans la représentation des nombres que la valeur la moins significative soit à droite, et c'est une idée importante que les élèves doivent retenir de cette activité.
    
    {panel end}

## Activités du cours

1. Dites aux élèves que la règle est qu'une carte a soit les points qui sont affichés, soit cachés. Si nous pouvons "allumer" une carte (afficher les points) ou l'"éteindre" (les cacher), comment pouvons-nous afficher 3 points ? Commencez par demander : combien de points sont sur la carte la plus à gauche ? Comptez ensemble qu'il y a 8 points. Regardons la lignes des nombres. Est-ce que 8 est plus grand que 3 ? Cachons le car c'est trop grand. Maintenant, regardons la carte suivante, combien de points peut-on voir? Comptons les. Il y en a 4, est-ce que 4 est plus grand que 3 ? Oui, nous devons donc cacher cette carte. Si nous n'avions pas masqué la carte 4 qu'arriverait-il ? (Il y aurait trop de points). Combien de points y a-t-il sur la carte suivante ? Comptons les. Il y a deux points. Regardons le nombre 3, (montrez avec le matériel que 2 est plus petit que 3, avec combien de point restant ?) Nous avons besoin d'un autre point pour faire le nombre 3. Donc on laisse cette carte visible.
    
    Sans avoir eu d'autres règles que chaque carte soit visible ou pas, les élèves arrivent généralement à la représentation suivante.
    
    {image file-path="img/topics/binary_cards_equals_three.png" alt="Diagramme montrant que les 2 cartes binaires font le nombre 3"}
    
    {panel type="math"}
    
    # Liens mathématiques
    
    À un autre niveau, nous nous concentrons sur l'utilisation de ce système de comptage pour représenter des nombres et faire l'association qu'avec ces “bits” nous pouvons faire n'importe quel nombre. Nous n'allons pas aller plus profondément dans la connaissance sur les systèmes de base des nombres. Les informations ci-dessous sont des informations supplémentaires pour vous.
    
    Pour les enseignants: la base 10 (notre système de comptage) a 10 chiffres, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Lorsque nous comptons en base 10, nous comptons de 0 à 9, puis manquons de chiffres. Nous devons donc ajouter une autre colonne; nous mettons un 1 dans cette colonne et recommençons à compter à partir de 0. Cela donne le nombre 10, nous répétons ensuite ce processus jusqu'à ce que la colonne des dizaines soit 9 et celle des unités soit 9 (soit 99) ; à partir de là, nous ajoutons une autre colonne. Par conséquent, le système de notation positionnelle ressemble à quelque chose comme :
    
    100 000 | 10 000 | 1 000 | 100 | 10 | 1 **Note: Utilisez l'exemple de notation positionnelle appropriée basée sur ce que vous avez déjà enseigné dans votre classe ; Celui-ci est un exemple détaillé.**
    
    La base 2 (binaire) suit la même logique, sauf qu'elle va beaucoup plus vite à la "prochaine" colonne, parce qu'il y a seulement deux chiffres, 0 et 1. La notation positionnelle binaire ressemble à ceci :
    
    32 | 16 | 8 | 4 | 2 | 1 |
    
    Parfois, les élèves confondent l'ordre des chiffres dans une représentation binaire. Pour aider les élèves à comprendre l'ordre correct des chiffres binaires, posez la question suivante : si j'allais vous donner 435,00 €, quel est le chiffre qui vous intéresse le plus ? Est-ce le 4 ou le 5? Pourquoi cela? C'est la même chose pour le binaire, la valeur la plus basse (le chiffre le moins significatif) est tout à droite, alors que le chiffre le plus significatif est tout à gauche.
    
    La base 16 est aussi couramment utilisée dans les ordinateurs - elle est appelée hexadécimal, et dispose de 16 chiffres. Tout cela est bien au-delà de la portée de cette leçon, nous avons voulu souligner qu'un chiffre hexadécimal est l'équivalent de 4 chiffres binaires (bits), car les deux peuvent représenter 16 valeurs différentes (de 0 à 15). Cet exercice que les élèves sont en train de faire fournit une excellente base pour la compréhension plus tard d'autres représentations communes qu'ils vont rencontrer dans les appareils numériques.
    
    {panel end}

2. Maintenant, demandez "Comment feriez-vous le nombre 6 ?" (Encore une fois, commencez par leur demander si ils veulent la carte 8, et ainsi de suite, de gauche à droite).

3. Le processus que nous avons suivi pour faire ces nombres est un algorithme qui convertit notre façon normale de compter les nombres pour la représentation binaire. Ensemble, nous allons réfléchir à travers les étapes que nous avons suivies pour ce faire. Nous allons le faire en utilisant de nouveau l'exemple de la représentation du nombre 3.
    
    a. Commencez avec tous les nombres activés (tous les points visibles). Vous pourriez commencer à introduire des représentations abstraites, comme varier la description des cartes (affichée/cachée ; avec les points/sans les points ; blanc/noir si le dos des cartes est noir ; oui/non ; ou allumé/éteint)
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_4.png" alt="4 ampoules allumées"}
    
    b. Est-ce que 8 tient dans 3 ? Non - donc retournez la
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_3.png" alt="3 ampoules allumées"}
    
    c. Est-ce que 4 tient dans 3 ? Non - donc retournez la
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_2.png" alt="2 ampoules allumées"}
    
    d. Est-ce que 2 tient dans 3 ? Oui : donc gardez la carte activée. Combien en reste-t-il ? (1)
    
    e. Est-ce que 1 tient dans 1 ? Oui : donc gardez la. Combien reste-t-il ? (plus rien)
    
    {image file-path="img/topics/lightbulb_series_4_bulbs_2.png" alt="2 ampoules allumées"}

## Appliquer ce que nous venons d'apprendre

- Groupez les élèves en binômes
- Donnez à chaque binôme un ensemble des plus petites cartes binaires
- Faites-les pratiquer l'algorithme avec des nombres inférieurs à 10.

1. Expliquez aux élèves que nous travaillons avec seulement deux chiffres, et que nous les appelons donc chiffres binaires. (Vous pouvez explorer le sens du préfixe "bi" des mots comme bicyclette, biennale, bilingue et biculturel.) Les chiffres binaires ("binary digit" en anglais) sont si communs que nous avons un diminutif pour eux : écrivez "binary digit" sur un morceau de papier, puis extrayez le "bi" du début et le "t" à la fin, mettez-les ensembles et demandez quel est le mot formé ("bit"). C'est le diminutif pour un nombre binaire, c'est pourquoi nous avons appelé les cartes des "bits" ; les 4 cartes qu'ils ont sont en fait 4 "bits".

2. Maintenant, comptons du plus petit nombre que l'on peut faire jusqu'au plus grand
    
    a. Quel est le plus petit nombre? (ils peuvent suggérer 1, puis réaliser qu'en fait c'est 0).

3. Montrez le nombre zéro avec les cartes (c'est à dire aucun point visible)

4. Maintenant comptez dans l'ordre croissant 1, 2, 3, 4 ... (chaque binôme devrait trouver les nombres entre eux)

5. Une fois qu'ils commencent à entrer dans une routine, demandez : combien de fois voyons-nous la carte à 1 point ? (une fois sur deux, pour chaque nombre impair)
    
    a. Quels autres motifs voyons nous? (la carte à 2 points se retourne une fois sur deux, celle à 4 points une fois sur 4, et ainsi de suite ; la carte à 8 points n'est pas très utile ; cela peut être difficile à reconnaitre pour certains élèves, mais l'objectif principal est qu'ils soient conscients que la carte à 1 point se retourne à chaque fois, et qu'un nombre sur deux est un nombre impair).

6. Continuez jusqu'à ce que toutes les cartes soient "allumées" et qu'elles comptent 15 points. Que se passe-t-il ensuite? (Nous devons ajouter une nouvelle carte.) Combien de points a-t-elle ? (16) Que devons-nous faire aux 4 autres cartes quand nous arrivons à 16? (nous devons toutes les retourner)

7. Idées d'extension...
    
    a. Donc quand j'ai 2 bits, je peux faire un maximum de ? (3)
    
    b. J'ajoute un nouveau bit, combien a-t-il de points ? (4)
    
    c. Je désactive les deux premiers bits pour donner 4 n'est-ce pas ?
    
    d. Maintenant activons les 3 bits, cela donne combien ? (7)
    
    e. J'ajoute un nouveau bit, combien de points a-t-il ? (8)
    
    f. Répétez jusqu'à ce qu'un motif soit reconnu : le nombre de points sur la prochaine carte est un de plus que le nombre total de points sur toutes les cartes à droite (par exemple il y a 7 points sur les cartes 4, 2 et 1, donc la prochaine carte à gauche aura 8 points). Il est donc facile de déterminer le nombre si tous les bits sont activés : on double la carte de gauche et on soustrait 1.
    
    g. Combien de nombres différents puis-je faire avec 2 bits ? (4; souvent les élèves disent 3 car ils ne comptent pas le 0).
    
    h. Ajoutons le bit suivant; combien de nombre différents peut on faire maintenant ? (8, encore une fois 7 sera surement proposé).
    
    i. Répétez jusqu'à ce que les élèves reconnaissent qu'à chaque fois que l'on ajoute un nouveau bit, on peut représenter deux fois plus de nombres.

{panel type="teaching"}

# Observations pour l'enseignant

Un concept qui pose des difficultés aux élèves ici est que le nombre de valeurs est une de plus que la valeur maximale (par exemple, de 0 à 7 il y a 8 nombres différents). La même observation peut se faire avec le nombre de chiffres dans les nombres décimaux classiques ; le plus grand chiffre est de 9, mais il y a 10 nombres possibles (en comptant 0). Cela est parfois appelé le problème des poteaux électriques (le nombre de poteaux est un de plus que le nombre d'écarts entre 2 poteaux), et il revient beaucoup en informatique et en mathématiques.

{panel end}

## Réflexion sur la leçon

- Est-ce que cette activité marcherait si nous utilisions des cartes blanches et couleur crème ? Pourquoi ? Pourquoi pas ?
    
    - En principe vous pourriez les utiliser, mais ce ne serait pas une bonne idée. Nous cherchons une réponse disant que ce ne sont pas des couleurs contrastées, par conséquent il serait difficile de voir si une carte est effectivement activée ou non. Les ordinateurs sont plus faciles à construire et cassent moins souvent lorsque nous utilisons deux valeurs contrastées.

- Quelles sont d'autres façons pour que nous puissions physiquement montrer que chacun des bits est activé ou non ?
    
    - Des idées pourraient inclure la tenue des cartes très hautes ou très basses ; ou simplement lever une main en l'air ; s'asseoir ou se mettre debout ; ou utiliser une représentation différence comme des lumières allumées ou éteintes.

- Quoi d'autre pourrions-nous utiliser pour représenter deux opposés, comme activé et désactivé, à l'écrit ?
    
    - Peut-être une croix ou un rond, un visage heureux ou triste, ou n'importe quelle autre paire de symboles.