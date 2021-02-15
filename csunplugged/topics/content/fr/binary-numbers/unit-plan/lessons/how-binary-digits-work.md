# Comment les chiffres binaires fonctionnent

## Questions clés

- Quels sont les différents systèmes de numération que nous connaissons ? (Les réponses peuvent inclure : Les chiffres romains; les traits; les bases numériques comme le binaire, l'octal et l'hexadécimal; les langages tels que le Chinois ou l'ancien Égyptien.)
- Pourquoi utilisons-nous habituellement 10 chiffres ? (Probablement parce que nous avons 10 doigts, et que c'est plus simple d'écrire avec qu'avec des batons par exemple)
- Pourquoi avons-nous différents systèmes de numération ? (Ils sont pratiques pour différentes choses, par exemple, les traits sont pratiques pour compter ; les chiffres Romains peuvent être utiles pour faire qu'un nombre semble plus mystérieux ou plus difficile à lire.)

## Lancement du cours

{panel type="video"}

# Voir l'activité en action

{video url="https://vimeo.com/437725275"}

{panel end}

{panel type="general"}

# Note des auteurs

Nous avons remarqué qu'une fois que les élèves avaient compris comment le système binaire fonctionnait, ils avaient beaucoup de questions et étaient ravis d'explorer encore plus loin les concepts présentés dans cette leçon. Nous avons ajouté beaucoup d'informations dans cette leçon, cependant, il n'est pas dans notre intention que vous enseigniez et couvriez tous les concepts, mais que vous ayez à portée de main les informations dont vous avez besoin lorsque vos élèves expriment un intérêt à en apprendre davantage.

{panel end}

{panel type="general"}

# Notes sur les ressources

Il existe également une version interactive en ligne des cartes binaires [ici](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), du [Computer Science Field Guide ](http://www.csfieldguide.org.nz/), mais il est préférable de travailler avec des cartes physiques.

{panel end}

1. Prenez les 5 premières cartes (1, 2, 4, 8 et 16 points), mais ne laissez pas les élèves voir les points. Demandez 5 volontaires pour être des chiffre binaires, et mettez les en ligne en face de la classe.

2. Donnez la carte avec un point à la personne à droite. Expliquez qu'il représente un "bit" (binary digit), et peut être activé ou non, blanc ou noir, 0 ou 1. La seule règle est que leur carte est soit complètement visible, soit retournée. Tendez la seconde carte à la deuxième personne sur la droite. Faites remarquer que cette carte possède soit deux points (face visible), soit aucun (face retournée).
    
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
    
    Au bout de 128 points il devrait y avoir 8 cartes. Cela représente 8 bits, ce qui correspond à un octet. Ça peut être déroutant de parler de cela à ce moment, mais certains élèves sont peut être déjà familier avec l'idée que 8 bits représentent un octet, et font l'observation. Cependant, nous travaillerons avec une représentation sur 5 bits, qui n'est pas aussi utile qu'un octet complet, mais une bonne taille pour enseigner. (Un octet est une façon pratique de regrouper des bits, et généralement la mémoire de stockage d'un ordinateur est basé sur des octets plutôt que des bits individuels ; c'est la même chose que des œufs vendus par 12 ; ils pourraient être vendus à l'unité, mais une douzaine est plus pratique pour tout le monde.)
    
    Une erreur courante consiste à distribuer les cartes de gauche à droite, mais c'est la convention dans la représentation des nombres que la valeur la moins significative soit à droite, et c'est une idée importante que les élèves doivent retenir de cette activité.
    
    {panel end}

## Activités de la leçon

1. Rappelez aux élèves que la règle est qu'une carte doit avoir soit tous ses points visibles, soit aucun (carte retournée). Si nous pouvons activer et désactiver les cartes en montrant la face avant ou en la retournant, comment montrerions-nous exactement 9 points ? Commencez par demander si ils veulent la carte 16 (ils devraient remarquer qu'elle possède trop de points), puis la carte 8 (ils devraient cette fois ci remarquer que sans elle, il n'y aura plus assez de points), puis 4, 2 et 1. Sans avoir d'autres instructions que le fait de pouvoir retourner ou non une carte, les élèves devraient normalement trouver la représentation suivante.
    
    {image file-path="img/topics/binary-cards-total-9.png" alt="Diagramme montrant que 2 cartes binaires permettent de former un 9"}
    
    {panel type="math"}
    
    # Liens mathématiques
    
    La base 10 (notre système de numération) possède 10 chiffres, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Lorsque nous comptons en base 10, nous comptons de 0 à 9, puis manquons de chiffres. Nous devons donc ajouter une autre colonne; nous mettons un 1 dans cette colonne et recommençons à compter à partir de 0. Cela donne le nombre 10, nous répétons ensuite ce processus jusqu'à ce que la colonne des dizaines soit 9 et celle des unités soit 9 (soit 99) ; à partir de là, nous ajoutons une autre colonne. Par conséquent, le système de notation positionnelle ressemble à quelque chose comme :
    
    100 000 | 10 000 | 1 000 | 100 | 10 | 1
    
    *Remarque : utilisez l'exemple de notation positionnelle appropriée basée sur ce que vous avez déjà enseigné dans votre classe ; celui-ci est un exemple détaillé.*
    
    La base 2 (binaire) suit la même logique, sauf qu'elle va beaucoup plus vite à la "prochaine" colonne, parce qu'il y a seulement deux chiffres, 0 et 1. La notation positionnelle binaire ressemble à ceci :
    
    32 | 16 | 8 | 4 | 2 | 1 |
    
    Parfois, les élèves confondent l'ordre des chiffres dans une représentation binaire. Afin d'aider les élèves à comprendre l'ordre correct des chiffres binaires, posez la question : si je vous donnais 435.00 €, quel chiffre vous intéresserait le plus ? Est-ce le 4 ou le 5? Pour quelle raison? C'est la même chose pour les chiffres binaires. La valeur la plus basse (le chiffre le moins significatif) est tout à droite, tandis que le chiffre le plus significatif est tout à gauche.
    
    {panel end}

2. Demandez maintenant "Comment formeriez vous le nombre 21 ?" (À nouveau, commencez par demander si ils veulent la carte 16, puis la carte 8, et ainsi de suite, de gauche à droite).

3. C'est un algorithme pour convertir les nombres dans une représentation binaire. Réfléchissons ensemble aux étapes pour le faire.
    
    a. Commencez avec tous les nombres activés (les points sont visibles).
    
    {image file-path="img/topics/lightbulb_series_1.png" alt="5 ampoules allumées"}
    
    b. Considérez la représentation du nombre 10
    
    c. Est-ce que 16 tient dans 10? Non - donc désactivez la carte (retournez la)
    
    {image file-path="img/topics/lightbulb_series_2.png" alt="4 ampoules allumées"}
    
    d. Est-ce que 8 tient dans 10 ? Oui - donc gardez la carte activée. Combien reste-t-il ? (2)
    
    e. Est-ce que 4 tient dans 2 ? Non - désactivez la carte
    
    {image file-path="img/topics/lightbulb_series_3.png" alt="3 ampoules allumées"}
    
    f. Est-ce que 2 tient dans 2 ? Oui - donc continuez. Combien reste-t-il ? (Rien)
    
    g. Donc désactivez 1.
    
    {image file-path="img/topics/lightbulb_series_4.png" alt="2 ampoules allumées"}

## Appliquer ce que nous venons d'apprendre

- Groupez les élèves en binômes.
- Donnez à chaque binôme un ensemble des plus petites cartes binaires (soit 5 cartes, soit 6, en fonction du confort des élèves).
- En commençant avec seulement 5 cartes, demandez-leur de pratiquer l'algorithme (décider pour chaque carte de gauche à droite) pour des nombres comme 20, 15 ou 8.

1. Expliquez aux élèves que nous ne travaillons qu'avec deux chiffres, et que nous les appelons donc chiffres binaires. Il sont si communs que nous utilisons un diminutif : écrivez "binary digit" sur une feuille de paper, puis déchirez le "bi" au début, et le "t" de la fin, assemblez-les et demandez comment on prononce le mot formé ("bit"). C'est le diminutif pour un nombre binaire, ainsi les 5 cartes que possèdent les élèves sont 5 bits.

2. Maintenant, comptons du plus petit nombre que l'on peut faire jusqu'au plus grand :
    
    a. Quel est le plus petit nombre? (il pourraient proposer 1, avant de réaliser que c'est 0).

3. Montrez le nombre zéro avec les cartes (c'est à dire aucun point visible).

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
    
    f. Répéter jusqu'à ce qu'un motif soit reconnu : le nombre de points sur la prochaine carte à gauche est un de plus que le nombre total de points sur toutes les cartes de droite (par exemple, il y a 15 points avec les cartes 8, 4, 2 et 1 de sorte que la prochaine carte à gauche est 16). Il est donc facile de déterminer le nombre si tous les bits sont activés - doublez la valeur de la carte la plus a gauche, et enlevez 1.
    
    g. Combien de nombres différents puis-je faire avec deux bits ? (4; souvent, les élèves disent 3 parce qu'ils n'ont pas compté le 0)
    
    h. Ajoutons le bit suivant; combien de nombres peut-on faire maintenant ? (8, 7 sera souvent proposé comme première réponse)
    
    i. Répéter jusqu'à ce qu'un motif soit reconnu : à chaque fois que nous ajoutons un bit, nous pouvons représenter deux fois plus de chiffres.

{panel type="teaching"}

# Observations pour l'enseignant

Un concept qui pose des difficultés aux élèves ici est que le nombre de valeurs est une de plus que la valeur maximale (par exemple, de 0 à 7 il y a 8 nombres différents). La même observation peut se faire avec le nombre de chiffres dans les nombres décimaux classiques; le plus grand chiffre est de 9, mais il y a 10 nombres possibles (en comptant 0). Cela est parfois appelé le problème des poteaux électriques (le nombre de poteaux est un de plus que le nombre d'écarts entre 2 poteaux), et il revient beaucoup en informatique.

{panel end}

## Réflexion sur la leçon

- Cette activité fonctionnerait-elle si nous utilisions des cartes de couleur blanche et crème? Pourquoi? Pourquoi pas? (En principe, vous pourriez les utiliser mais ce ne serait pas une bonne idée. Nous cherchons une réponse disant que ce ne sont pas des couleurs contrastées, par conséquent il serait difficile de voir si une carte est effectivement activée ou non. Cela explique pourquoi les ordinateurs utilisent des représentations physiques faciles à distinguer.)
- Quels sont d'autres façons ou symboles contrastés que nous pourrions activer ou désactiver, comme le binaire ?
    
    - (Des idées pourraient inclure la tenue des cartes très hautes ou très basses ; ou simplement lever une main en l'air ; s'asseoir ou se mettre debout ; ou utiliser une représentation différence comme des lumières allumées ou éteintes.)

- Les ordinateurs sont moins chers et plus faciles à construire si ils représentent des données avec juste deux valeurs contrastées, représentées par les nombres 0 et 1. Quoi d'autre pourrions-nous utiliser pour représenter deux opposés à l'écrit? (Peut-être une croix ou un rond, un visage heureux ou triste, ou n'importe quelle autre paire de symboles.)

- En étendant cette idée, les nombres pourraient être représentés par une tension qui est soit proche de 5 volts, soit proche de 0 volts. Le circuit est construit de telle sorte que tout ce qui est plus petit que 2,5 volts compte comme 0 et tout ce qui est plus grand que 2,5 volts compte comme 1. Comme le contraste de couleurs de cartes, c'est très facile à reconnaitre. Nous pourrions avoir 10 couleurs de cartes pour représenter les chiffres de 0 à 10, et nous pourrions avoir dix plages de tension (de 0 à 0,5, de 0,5 à 1,0 et ainsi de suite), mais il est beaucoup plus compliqué de construire des circuits rapides et précis pour cela.