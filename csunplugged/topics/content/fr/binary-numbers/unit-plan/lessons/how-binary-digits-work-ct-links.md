{panel type="ct-algorithm"}

# Pensée algorithmique

Dans cette leçon, nous avons utilisé un algorithme pour convertir un nombre décimal en nombre binaire. C'est un algorithme, car c'est un processus étape par étape qui donnera toujours la bonne solution pour n'importe quelle entrée donnée tant que le processus est suivi à la lettre.

Voici un algorithme pour calculer quelles cartes à points doivent être montrées, écrit en texte :

- Trouvez le nombre de points à afficher. (Nous nous référerons à "le nombre de points restants" qui, initialement, est le nombre total devant être affiché.)
- Pour chaque carte, de la gauche vers la droite (c'est à dire 16, 8, 4, 2 puis 1) : 
    - Si le nombre de points sur la carte est plus grand que le nombre de points restants : 
        - Cachez la carte
    - Sinon : 
        - Montrez la carte
        - Soustrayez le nombre de points sur la carte du nombre de points restants

Notez que cet algorithme (de droite à gauche) fonctionne très bien avec les cartes, mais si vous regardez les programmes d'ordinateur qui font cela, vous risquez de rencontrer un autre algorithme qui travaille de droite à gauche. Il est courant d'avoir plusieurs algorithmes qui permettent d'accomplir la même chose.

#### Exemples de ce que vous pourriez observer :

Quels étudiants sont méthodiques lorsqu'ils convertissent entre décimal et binaire ? Quels élèves commencent avec la carte de gauche et retournent une carte à la fois vers la droite, plutôt que de choisir des cartes au hasard et de les retourner jusqu'à obtenir le bon nombre ?

{panel end}

{panel type="ct-abstraction"}

# Résumé

La représentation des nombres binaires (utilisant seulement des 0 et 1) est une abstraction qui cache la complexité de l'électronique et du matériel à l'intérieur d'un ordinateur qui stocke des données. L’abstraction nous aide à simplifier les choses parce que nous pouvons ignorer les détails que nous n’avons pas besoin de connaitre.

Dans ce cas, les détails que nous pouvons ignorer incluent : les ordinateurs utilisent des dispositifs physiques comme des circuits électroniques et des tensions dans ces circuits pour stocker et déplacer des données, et cela demande beaucoup de théories physico-mathématiques complexes pour faire ce travail correctement.

Nous n'avons pas besoin de comprendre comment ces circuits fonctionnent pour utiliser des données et représenter les choses à l'aide du binaire. L’utilisation du binaire en tant qu'abstraction de ces circuits nous permet de représenter des nombres par des bits (des 0 et des 1), de comprendre les données et de travailler sur des problèmes sans avoir à réfléchir à ce qui se passe «sous le capot» de l’ordinateur.

Une autre utilisation de l'abstraction est de considérer ce qui est nécessaire pour représenter un nombre donné en binaire. La réponse est : tout ce dont vous avez besoin c'est deux choses différentes. Ces choses peuvent être n'importe quoi ! Deux couleurs différentes, deux animaux, deux symboles, etc. Tant qu'il y en a deux et qu'ils sont différents, vous pouvez les utiliser pour représenter n'importe quel nombre, en utilisant le binaire, de la même façon qu'un ordinateur utilise l'électricité pour représenter les données.

Nous pouvons utiliser des chiffres binaires pour représenter n'importe quel type de données stockées sur un ordinateur. Lorsque nous représentons d'autres formes de données (telles que des lettres, des images et du son), nous utilisons également de l'abstraction parce que nous masquons les détails de tous les nombres binaires sous-jacents et il suffit de regarder les données dans leur ensemble. Toutes les formes de données finissent par être représentées sous forme de nombres (qui sont vraiment juste des combinaisons de bits) - pour le texte, nous avons un des nombres pour chaque lettre, pour les images, nous utilisons des nombres pour chaque couleur, et ainsi de suite. Nous utilisons plusieurs couches d'abstraction ! Par exemple, une forme familière d'abstraction, c'est que le mois "octobre", pourrait être représenté par le nombre dix, qui à son tour est représenté par les bits 01010, et si ceux-ci sont stockés comme des tensions dans la mémoire de l'ordinateur, ce sont en fin de compte des tensions "bas, haut, bas, haut, bas".

#### Exemples de ce que vous pourriez observer :

Qui sont les élèves qui démontrent la conversion et la représentation de nombres binaires à l'aide d'autres choses que de “1 et de 0”, “noir et blanc”, et “éteint et allumé” (par exemple à l'aide de 😀 et 🙁, ou à l'aide de gens debout ou assis). Si vous êtes en mesure d'échanger des termes comme "noir" et "blanc" avec des 0 et des 1 sans que les élèves ne se préoccupent de la différence, c'est qu'ils font de l'abstraction.

{panel end}

{panel type="ct-decomposition"}

# Décomposition

Un exemple de décomposition est de découper la conversion d'un nombre en binaire un bit à la fois. Les questions "Devrait-il être 1 ou 0" pour chacune des cartes points décomposent le problème en une série de questions.

#### Exemples de ce que vous pourriez observer :

Quels élèves se rendent compte qu'il est important de commencer par la carte la plus à gauche et de ne considérer qu'un seul bit à la fois? Quels élèves se concentrent sur chaque bit individuellement, plutôt que d'être submergé en essayant de travailler avec tous d'un seul coup ?

{panel end}

{panel type="ct-pattern"}

# Généralisation et motifs

La reconnaissance de motifs dans la façon dont le système de numération binaire fonctionne nous aide à donner une compréhension approfondie des concepts en jeu, et nous aide dans la généralisation de ces concepts et modèles de sorte que nous pouvons les appliquer à d'autres problèmes.

À un niveau simple, nous avons commencé avec les numéros 1, 2, et 4, et les étudiants ont généralisé cela par le doublement des valeurs. L'exercice utilisait 5 bits, mais les élèves doivent être en mesure de généraliser avec 8 bits, ou plus.

L'algorithme de conversion d'un nombre décimal en binaire suit un modèle qui peut être généralisé pour résoudre le problème du rendu de monnaie quand quelqu'un paie en espèces. Pour les nombres binaires, vous commencez avec le bit le plus grand, vous l'activez si vous en avez besoin, tout comme lorsque vous rendez la monnaie, vous commencez avec la valeur la plus grande, puis vous prenez toujours une pièce (ou un billet) quand vous en avez besoin. Remarque de jargon : C'est un algorithme glouton - il prend la plus grande valeur possible à chaque fois !

{panel type="math"}

# Liens mathématiques

Demandez aux élèves ce qui est spécial au sujet de la virgule dans la conversion en binaire, en opposition avec l'algorithme habituel de rendu de monnaie, et faites-leur observer que, dans le cas général, vous devrez peut-être donner plus d'une pièce de la même valeur, alors que dans la conversion en binaire il y a toujours une seule fois (ou non) chaque valeur.

{panel end}

Lorsque l'on compte de façon croissante en binaire, il existe un schéma pour la façon dont on tourne les cartes. Le 1er bit (1 point) se retourne à chaque fois, le 2e (avec 2 points) se retourne une fois sur 2, le 3e (4 points) se retourne une fois sur 4... Existe-t-il un schéma de ce genre quand on compte en nombres décimaux ?

{image file-path="img/topics/col_binary_counting_pattern.png" alt="Schéma de comptage binaire"}

Si vous avez 5 cartes et que toutes sont visibles, vous aurez le numéro 31, qui est 1 de moins que la valeur de la carte suivante, 32. Ce schéma est-il toujours vrai ?

La quantité de nombres que vous pouvez représenter avec un certain nombre de bits est la même que la valeur du prochain bit qui peut être ajouté. Par exemple, à l'aide de 4 cartes (1, 2, 4, 8) vous pouvez représenter les 16 nombres (de 0 à 15), et la prochaine carte dans la série est le nombre 16. Chaque fois que nous ajoutons une nouvelle carte, nous doublons également la quantité de nombres différents que nous pouvons représenter.

Travailler avec ces schémas est précieux pour travailler sur la relation entre le nombre de bits utilisés et la puissance de ce qu'ils peuvent représenter.

Expliquez un ou plusieurs des schémas suivants :

- Avec un certain nombre de cartes, vous pouvez faire la même quantité de nombres différents que le nombre de points qui seraient sur la carte suivante ajoutée à gauche (rappelez-vous que 0 est un nombre).
- Lorsque vous comptez de façon croissante : la première carte (1 point) se retourne à chaque fois, la deuxième carte (2 points) se retourne une fois sur deux, la troisième (4 points), toutes les quatre fois, et le quatrième (8 points), toutes les huit fois, ...
- Lorsque toutes les cartes sont visibles, leur somme est la valeur de la prochaine carte binaire moins 1.

#### Exemples de ce que vous pourriez observer :

Quels élèves ont reconnu rapidement que chaque carte doublait le nombre de points ? Les élèves peuvent-ils voir les similitudes entre ceci et multiplier les valeurs par 10 quand ils utilisent le système décimal ?

Quels élèves comprennent facilement les schémas de retournement des cartes lors du comptage croissant avec des nombres binaires ?

{panel end}

{panel type="ct-logic"}

# Logique

La pensée logique signifie utiliser des règles que vous connaissez déjà et utilisez la logique pour déduire plus de règles et d'informations de celles-ci. Une fois que nous savons quels nombres sont représentés par chacune des cartes binaires, nous pouvons utiliser ces connaissances pour comprendre comment représenter d'autres nombres avec des cartes. Si vous mémorisez la façon de représenter les nombres avec 5 cartes, est-ce que vous comprenez comment représenter n'importe quel nombre avec un nombre quelconque de bits ? Ce n'est pas le cas, mais vous pouvez comprendre comment le faire si vous comprenez la logique derrière la façon dont ces nombres sont faits avec les 5 cartes.

Un bon exemple de la pensée logique pour les nombres binaires est le raisonnement pour expliquer pourquoi chaque bit "doit" avoir une valeur particulière (par exemple, il doit être à 1 ou à 0) pour représenter un nombre donné. Cela permet de comprendre qu'il y a une seule représentation pour chaque nombre.

#### Exemples de ce que vous pourriez observer :

Les élèves peuvent-ils explicitement expliquer que le bit le plus à droite doit être 1, car il est le seul nombre impair et est donc nécessaire pour que nous puissions faire n'importe quel nombre impair ? Sans lui, nous ne pourrions faire que des nombres pairs.

Les élèves sont-ils capables d'expliquer que chaque carte "doit" être comme elle est pour un nombre donné, par exemple la carte à 16 points est nécessaire pour le numéro 19 parce que, sans elle, il ne reste que 15 points à sa droite (pas assez) ; mais la carte à 16 points n'est pas nécessaire pour le numéro 9 car elle donnerait trop de points ?

{panel end}

{panel type="ct-evaluation"}

# Évaluation

Un exemple d'évaluation est de déterminer combien de valeurs différentes peuvent être représentées par un nombre donné de bits (par exemple, 5 bits peuvent représenter 32 valeurs différentes), et vice versa (pour représenter 1000 valeurs différentes, vous avez besoin d'au moins 10 bits).

#### Exemples de ce que vous pourriez observer :

Est-ce qu'un élève peut déterminer l'intervalle de nombre possibles avec 4 bits ? (16)

6 bits ? (64)

8 bits ? (256)

Si l'on ajoute un bit de plus à une représentation, de combien est l'augmentation de l'intervalle ? (il double)

Si nous ajoutons deux bits à une représentation, de combien est l'augmentation de l'intervalle ? (il est quatre fois plus grand)

Combien de bits avons-nous besoin pour représenter 1000 valeurs différentes? (10 sont suffisants)

{panel end}