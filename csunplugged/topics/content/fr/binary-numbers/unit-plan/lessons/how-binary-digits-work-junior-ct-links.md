{panel type="ct-algorithm"}

# Pensée algorithmique

Dans cette leçon, nous avons utilisé un algorithme pour convertir un nombre décimal en un nombre binaire. C'est un algorithme car il s'agit d'un processus étape par étape qui donnera toujours la bonne solution pour n'importe quelle entrée que vous lui donnez tant que le processus est suivi exactement.

Voici un algorithme pour déterminer quelles cartes à points doivent être affichées, écrit en texte :

- Trouvez le nombre de points à afficher. (Nous appellerons cela le "nombre de points restants", qui est initialement le nombre total à afficher.)

- Pour chaque carte, de gauche à droite (c'est-à-dire 8, 4, 2 puis 1) :
    
    - Si le nombre de points sur la carte est plus grand que le nombre de points restants :
        
        - Cachez la carte
    
    - Sinon :
        
        - Montrez la carte
        
        - Soustrayez le nombre de points sur la carte du nombre de points restants

#### Exemples de ce que vous pourriez observer :

Quels étudiants sont méthodiques lorsqu'ils convertissent entre décimal et binaire ? Quels élèves commencent avec la carte de gauche et retournent une carte à la fois vers la droite, plutôt que de choisir des cartes au hasard et de les retourner jusqu'à obtenir le bon nombre ?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

L'abstraction et la pensée abstraite sont généralement difficiles pour les jeunes élèves, de sorte que seule une petite quantité de cette partie est susceptible de leur être applicable. Nous avons toutefois inclus ces informations ici parce qu'elles constituent des connaissances de base utiles pour l'enseignement de ce sujet.

L’abstraction nous aide à simplifier les choses parce que nous pouvons ignorer les détails que nous n’avons pas besoin de connaitre. La représentation de nombre binaire est une abstraction qui cache la complexité de l'électronique et du matériel à l'intérieur d'un ordinateur qui stocke des données.

Dans ce cas, les détails que nous pouvons ignorer incluent : les ordinateurs utilisent des dispositifs physiques comme des circuits électroniques et des tensions dans ces circuits pour stocker et déplacer des données, et cela demande beaucoup de théories physico-mathématiques complexes pour faire ce travail correctement.

Nous n'avons pas besoin de comprendre comment fonctionnent ces circuits parce que nous pouvons utiliser l'abstraction du binaire, comme des nombres composés de bits (0 et 1), pour comprendre les données et résoudre les problèmes, sans avoir à penser à ce qui se passe ‘sous le capot’ l'ordinateur.

Une autre utilisation de l'abstraction est de considérer ce qui est nécessaire pour représenter un chiffre donné en binaire. La réponse est : tout ce dont vous avez besoin c'est deux choses différentes. Ces choses peuvent être n'importe quoi ! Deux couleurs différentes, deux animaux, deux symboles, etc. Tant qu'il y en a deux, et qu'ils sont différents, vous pouvez les utiliser pour représenter n'importe quel nombre, en utilisant le binaire, de la même façon qu'un ordinateur utilise l'électricité pour représenter les données.

#### Exemples de ce que vous pourriez observer :

Qui sont les élèves qui peuvent démontrer la conversion et la représentation de nombres binaires en utilisant des éléments autres que «1 et 0», «noir et blanc» et «off and on» (par exemple en utilisant:] et :[ou en utilisant des personnes debout ou assises). Si vous êtes en mesure d'échanger des termes comme "noir" et "blanc" avec des 0 et des 1 sans que les élèves ne se préoccupent de la différence, c'est qu'ils font de l'abstraction.

{panel end}

{panel type="ct-decomposition"}

# Décomposition

Un exemple de décomposition est de découper la conversion d'un nombre binaire un seul bit à la fois. Les questions "Devrait-il être 1 ou 0" pour chacune des cartes points décomposent le problème en une série de questions.

#### Exemples de ce que vous pourriez observer :

Quels élèves se rendent compte qu'il est important de commencer par la carte la plus à gauche et de ne considérer qu'un seul bit à la fois? Quels élèves se concentrent sur chaque bit individuellement, plutôt que d'être submergé en essayant de travailler avec tous d'un seul coup ?

{panel end}

{panel type="ct-pattern"}

# Généralisation et motifs

La reconnaissance de motifs dans la façon dont le système de numération binaire fonctionne nous aide à donner une compréhension approfondie des concepts en jeu, et nous aide dans la généralisation de ces concepts et modèles de sorte que nous pouvons les appliquer à d'autres problèmes. La généralisation de ces motifs peut être plus difficile pour les jeunes étudiants, mais la reconnaissance de motifs est un bon exercice.

À un niveau simple, nous avons commencé avec les numéros 1, 2, et 4, et les élèves ont généralisé cela par le doublement des valeurs. Dans ces exercices, nous avons converti des nombres à 4 bits, mais les étudiants (qui sont capables de compter assez haut) sont en mesure de généraliser à des nombres de 8 bits ou plus.

L'algorithme de conversion d'un nombre décimal en binaire suit un modèle qui peut être généralisé pour résoudre le problème du rendu de monnaie quand quelqu'un paie en espèces. Pour les nombres binaires, vous commencez avec le bit le plus grand, vous l'activez si vous en avez besoin, tout comme lorsque vous rendez la monnaie, vous commencez avec la valeur la plus grande, puis vous prenez toujours une pièce (ou un billet) quand vous en avez besoin. Remarque de jargon : C'est un algorithme glouton.

{panel type="math"}

# Liens mathématiques

Demandez aux élèves ce qui est spécial au sujet de la virgule dans la conversion en binaire, en opposition avec l'algorithme habituel de rendu de monnaie, et faites-leur observer que, dans le cas général, vous devrez peut-être donner plus d'une pièce de la même valeur, alors que dans la conversion en binaire il y a toujours une seule fois (ou non) chaque valeur.

{panel end}

Lorsque l'on compte de façon croissante en binaire, il existe un schéma pour la façon dont on tourne les cartes. Le 1er bit (1 point) se retourne à chaque fois, le 2e (avec 2 points) se retourne une fois sur 2, le 3e (4 points) se retourne une fois sur 4... Existe-t-il un schéma de ce genre quand on compte en nombres décimaux ?

{image file-path="img/topics/col_binary_counting_pattern.png" alt="Schéma de comptage binaire"}

Si vous avez 4 cartes et tous sont visibles, vous aurez le numéro 15, qui est 1 de moins que la valeur de la carte suivante, 16. Ce schéma est-il toujours vrai ?

La quantité de nombres que vous pouvez représenter avec un certain nombre de bits est la même que la valeur du prochain bit qui peut être ajouté. Par exemple, à l'aide de 4 cartes (1, 2, 4, 8) vous pouvez représenter les 16 nombres (de 0 à 15), et la prochaine carte dans la série est le nombre 16. Chaque fois que nous ajoutons une nouvelle carte, nous doublons également la quantité de nombres différents que nous pouvons représenter.

Travailler avec ces schémas est précieux pour travailler sur la relation entre le nombre de bits utilisés et la puissance de ce qu'ils peuvent représenter.

#### Exemples de ce que vous pourriez observer :

Quels élèves ont reconnu rapidement que chaque carte doublait le nombre de points ? Quels élèves comprennent facilement les schémas de retournement des cartes lors du comptage croissant avec des nombres binaires ?

{panel end}

{panel type="ct-logic"}

# Logique

La pensée logique signifie utiliser des règles que vous connaissez déjà et utilisez la logique pour déduire plus de règles et d'informations de celles-ci. Une fois que nous savons quels nombres sont représentés par chacune des cartes binaires, nous pouvons utiliser ces connaissances pour comprendre comment représenter d'autres nombres avec des cartes. Si vous mémorisez la façon de représenter les nombres avec 4 cartes, est-ce que vous comprenez comment représenter n'importe quel nombre avec un nombre quelconque de bits ? Ce n'est pas le cas, mais vous pouvez comprendre comment le faire si vous comprenez la logique derrière la façon dont ces nombres sont faits avec les 4 cartes.

Un bon exemple de la pensée logique pour les nombres binaires est le raisonnement pour expliquer pourquoi chaque bit "doit" avoir une valeur particulière (par exemple, il doit être allumé ou éteint) pour représenter un nombre donné. Cela permet de comprendre qu'il y a une seule représentation pour chaque nombre.

#### Exemples de ce que vous pourriez observer :

Les élèves peuvent-ils explicitement expliquer que le bit le plus à droite doit être 1, car il est le seul nombre impair et est donc nécessaire pour que nous puissions faire n'importe quel nombre impair ? Sans lui, nous ne pourrions faire que des nombres pairs. Les élèves sont-ils capables d'expliquer que chaque carte "doit" être comme elle est pour un nombre donné, par exemple la carte à 8 points est nécessaire pour le numéro 9 parce que, sans elle, il ne reste que 7 points à sa droite (pas assez) ; mais la carte à 8 points n'est pas nécessaire pour le numéro 6 car elle donnerait trop de points ?

{panel end}

{panel type="ct-evaluation"}

# Évaluation

Un exemple d'évaluation est de déterminer combien de valeurs différentes peuvent être représentées par un nombre donné de bits (par exemple, 4 bits peuvent représenter 16 valeurs différentes), et vice versa (pour représenter 1000 valeurs différentes, vous avez besoin d'au moins 10 bits).

#### Exemples de ce que vous pourriez observer :

Est-ce qu'un élève peut déterminer l'intervalle de nombre possibles avec 2 bits ? (4)

3 bits ? (8)

4 bits ? (16)

Si l'on ajoute un bit de plus à une représentation, de combien est l'augmentation de l'intervalle ? (il double)

{panel end}