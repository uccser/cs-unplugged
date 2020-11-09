# Enquêter sur les variantes en utilisant le Réseau de Tri

## Connaissances préalables

Les élèves doivent avoir terminé le cours 1 qui présente le Réseau de Tri.

## Questions clés

- Dans les Réseaux de Tri, pensez-vous que nous pouvons trier autre chose que des nombres ? Que pensez-vous que nous pourrions trier ? (Les réponses potentielles peuvent inclure le tri de choses par couleur, taille, âge et hauteur).

## Lancement du cours

Montrez à nouveau aux élèves le Réseau de Tri (si le réseau a besoin d'être redessiné, les élèves aiment souvent le faire, et le dessiner avec précision à partir du diagramme est un exercice utile). Dites-leur qu'ils vont l'essayer avec quelques variantes cette fois-ci.

{panel type="math"}

# Liens mathématiques

Résultats à prévoir : en comprenant le fonctionnement du Réseau de Tri, les élèves étudieront différentes façons de l'utiliser et exploreront comment le nombre le plus bas et le plus élevé se retrouvent toujours dans la position de sortie correcte.

{panel end}

## Variantes

Cette partie du cours explore les différentes façons dont les nombres sont utilisés.

### Variante 1 : valeurs identiques

{image file-path="img/topics/sorting-network-equal-3.png" alt="Deux personnes tenant chacun une carte avec le nombre 3 écrit dessus."}

Dans cette variante, les élèves essaient le Réseau de Tri avec un ensemble de cartes dont certaines ont des valeurs identiques, comme 1, 2, 3, 3, 4, 5. Ils se demanderont probablement ce qu'il faut faire en comparant les cartes identiques — demandez-leur ce qu'ils en pensent, et ils se rendront probablement compte que cela ne fera aucune différence (si 3 et 3 se rencontrent, alors peu importe laquelle va à gauche et laquelle va à droite !). Demandez-leur de prédire ce qui se passera au bout du réseau (ils peuvent se rendre compte que les valeurs identiques finiront par être adjacentes).

Passez maintenant les numéros dans le réseau pour vérifier. Voici un bref rappel des instructions du Réseau de Tri ; tous les détails se trouvent dans le cours 1.

1. Six élèves commencent dans les cercles d'entrée, chacun détenant une carte avec un nombre.

2. Ils avancent tous en même temps, et quand ils rencontrent quelqu'un dans une case, ils comparent leurs cartes.

3. La personne avec la plus petite carte suit la ligne vers la gauche, et celui avec la plus grande vers la droite (c'est l'inverse dans la deuxième variante de ce cours).

4. Cela continue jusqu'à ce que tous les élèves atteignent les cercles de sortie, où ils devraient alors être classés dans l'ordre.

### Variante 2 : la plus grande à gauche

Cette fois, la personne avec le plus grand nombre passe à gauche au lieu de la droite et suit la ligne jusqu'à la case suivante, alors que la personne avec le plus petit nombre va vers la droite au lieu de la gauche et suit la ligne jusqu'à la case suivante.

Demandez aux élèves de prédire ce qui va arriver (ils devraient être en mesure de trouver que les valeurs sortiront dans l'ordre de tri inverse c'est à dire de la plus grande à la plus petite et non de la plus petite à la plus grande).

Demandez-leur d'essayer avec quelques nombres pour vérifier.

{panel type="teaching"}

# Observations sur l'enseignement

En inversant la décision gauche/droite, le résultat final sera dans l'ordre inverse de ce qu'il aurait été dans le cours 1.

{panel end}

### Variante 3 : Les lettres de l'alphabet

{image file-path="img/topics/sorting-network-variation-alphabet.png" alt="Cartes avec des lettres."}

Donnez aux élèves des cartes avec des lettres. Demandez comment on pourrait les comparer (les élèves doivent remarquer qu'elles peuvent être classées par ordre alphabétique). Demandez-leur de tester cela en triant les cartes.

## Using the network backwards

C'est une expérience qui répond à une question que les élèves peuvent avoir posée : le Réseau de Tri fonctionne-t-il correctement si les valeurs partent de l'autre côté ?

Demandez aux élèves d'essayer avec quelques valeurs simples (comme les nombres de 1 à 6). Il y a de fortes chances que cela fonctionne pour de nombreux ordres de départ des valeurs. Cependant, encouragez-les à continuer d'essayer jusqu'à ce qu'ils trouvent un ordre initial pour lequel cela ne fonctionne pas. Pour y parvenir, il faudra un raisonnement approfondi.

S'ils ont du mal à trouver un exemple, vous pouvez leur donner celui ci-dessous, puis les mettre au défi d'en trouver un autre qui n'en sortira pas trié.

{panel type="teaching"}

# Observations sur l'enseignement

Le Réseau de Tri est conçu pour fonctionner de manière cohérente dans un sens, plutôt que dans les deux sens. Par exemple, la première image ci-dessous montre des entrées qui sortent triées lorsque vous traversez le réseau à l'envers, alors que pour la seconde image, ce n'est pas le cas. Si cela échoue pour seulement un ensemble d'entrées (le deuxième) alors on ne peut pas compter sur ce réseau, même si cela fonctionne parfois. Dans l'autre sens, il saura toujours trier correctement.

{image file-path="img/topics/sorting-network-backwards-1.png" alt="Ce diagramme montre que lorsque l'on donne les entrées 654321 au Réseau de Tri, il peut arriver qu'elles sortent triées lorsqu'il est exécuté à l'envers."}

{image file-path="img/topics/sorting-network-backwards-2.png" alt="Ce diagramme montre que lorsque le Réseau de Tri reçoit les entrées 512364, elles ne sortent pas triées lorsqu'il est exécuté à l'envers."}

{panel end}

## Appliquer ce que nous venons d'apprendre

Ce type d'algorithmes doit fonctionner sur un équipement spécial pour tirer parti de la possibilité d'effectuer plusieurs comparaisons en même temps. À l'heure actuelle, ils sont seulement utilisés pour des applications spécialisées. Par exemple, ils sont parfois exécutés sur le processeur graphique (GPU) d'un ordinateur, parce que ces processeurs sont bons pour faire du calcul en parallèle. Les Réseaux de Tri ont été inventés bien avant l'apparition des GPU puissants ; c'est un aspect passionnant de l'informatique : certaines de nos découvertes sont en avance sur le matériel disponible, nous sommes donc prêts à utiliser le matériel lorsqu'il sera couramment disponible ! Note that this is *not* a conventional sorting algorithm, as the sorting that is done on a conventional system can make only one comparison at a time; conventional sorting algorithms are explored in another lesson.

## Réflexion sur le cours

Qu'avez-vous remarqué à chaque variante de l'utilisation du Réseau de Tri ?

Était-ce ce que vous aviez prévu ?