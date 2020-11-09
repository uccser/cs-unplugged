# Enquêter sur les variantes en utilisant le Réseau de Tri

## Connaissances préalables

Les élèves doivent avoir terminé le cours 1 qui présente le Réseau de Tri.

## Questions clés

- In the Sorting Network, what do we think will happen if the smaller card goes right instead of left at each box and vice versa? (Students should be able to reason that the values will come out in reverse sorted order.)

- Est-ce que cela fonctionnera si nous essayons d'utiliser le Réseau de Tri à l'envers, en commençant avec les nombres dans le désordre à la fin, et en progressant à rebours ? (Students may have different views on this; it appears to work most of the time, but in this lesson we will find an example that doesn't.)

## Lancement du cours

Montrez à nouveau aux élèves le Réseau de Tri (si le réseau a besoin d'être redessiné, les élèves aiment souvent le faire, et le dessiner avec précision à partir du diagramme est un exercice utile). Dites-leur qu'ils vont l'essayer avec quelques variantes cette fois-ci.

Several variations are shown below, and you can choose the ones that suit the students, or you may come up with other items that could be sorted. The key is that the comparisons obey the transitive rule: that if a is smaller than b, and b is smaller than c, then a is smaller than c. Sorting by student height or other personal attributes can be problematic - not only might it be a sensitive issue, but comparing two students to find the highest might not give a consistent result if they are a similar height.

{panel type="math"}

# Liens mathématiques

Predicting outcomes: by understanding how the Sorting Network works students will be investigating different ways of using the Sorting Network and exploring how the outputs are affected by these changes.

{panel end}

## Variantes avec des nombres

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

### Variation 4: Words made of letters in alphabetical order

As an interesting variation of sorting letters, there are some English words that have the letters in alphabetical order, such as BIOPSY. If you give the students the letters out of order (such as P, O, I, B, Y, and S) and have them sort them in the Sorting Network, it will form the world BIOPSY at the end. There are few common words with this property; other examples include ALMOST and ABHORS. Have the students try the Sorting Network with some of these words (note that you will need to read the sorted letters from the direction of the starting position to see the word in the correct order).

There is also a number of words that have the letters in reverse alphabetical order, such as SPONGE and ZONKED (these can be sorted using the "larger to the left" variation, or can be read from the far side of the Sorting Network). Some words with this property have double letters in them, such as BELLOW; these will sort correctly, since the order of the double letters is immaterial.

{panel type="general"}

# Liste des mots avec les lettres dans l'ordre alphabétique

Here is a longer list of 6-letter words that can be used for this exercise. They are all from a dictionary, although some are rather obscure!

{image file-path="img/topics/sorting-network-toffees-cellos-sponge.png" align="right" alt="2 toffees, 2 cellos and a sponge."}

AFFLUX, AGLOOS, ALMOST, BEGILT, BEGINS, BEGIRT, BEKNOT, BELLOW, BIJOUX, BILLOW, BIOPSY, BLOOPS, BLOTTY, CELLOS, CHIKOR, CHILLS, CHILLY, CHIMPS, CHINOS, CHINTZ, CHIPPY, CHIRRS, CHITTY, CHIVVY, CHOOSY, CHOPPY, CLOOPS, CLOTTY, DEFFLY, DEHORT, DEKKOS, DIKKOP, DIMPSY, EFFLUX, EFFORT, ELLOPS, FILLOS, FLOORS, FLOOSY, FLOPPY, FLOSSY, GHOSTY, GIMMOR, GLOOPS, GLOOPY, GLOPPY, GLOSSY, HILLOS, KNOTTY, JIGGED, LIGGED, MIFFED, NIFFED, PIGGED, POLKED, POLLED, POLLEE, POMMEE, POMMIE, PONGED, PONGEE, PONIED, PONKED, POOHED, POOLED, RIFFED, RIGGED, ROLFED, ROLLED, RONNIE, ROOFED, ROOKED, ROOKIE, ROOMED, ROOMIE, SOGGED, SOOGEE, SOOKED, SOOLED, SOOMED, SPLIFF, SPOKED, SPONGE, TIFFED, TIGGED, TOFFEE, TOGGED, TOLLED, TOLLIE, TOMMED, TONGED, TONKED, TOOLED, TOOMED, TOONIE, TROKED, UNFEED, VOMICA, VUMMED, WIGGED, WOLFED, WONNED, WOOFED, WOOLED, WOOLIE, WOONED, WULLED, WURLIE, YOKKED, YOLKED, YONNIE, YTTRIA, YTTRIC, YUKKED, YUPPIE, YWROKE, ZIGGED, ZONKED, ZOOMED, ZOONED, ZOONIC.

{panel end}

### Variation 5: Sorting words in dictionary order

{image file-path="img/topics/tri-réseau-variation-words.png" alt="Les mots crochet et crocodile."}

Give the students cards with dictionary words on them, and ask how these might be compared. Students should observe that they could be placed in dictionary order. A variation is to give them books and have them sort them in order of the authors' names.

{image file-path="img/topics/sorting-network-crochet-v-crocodile.png" alt="Crochet vs crocodile."}

Comparing two words or names is challenging; they will need to know to compare each character until two differ (e.g. for "crochet" and "crocodile", the "croc" prefix is the same, so it is the "h" and "o" that determine their order; this process is an algorithm in itself!)

{image file-path="img/topics/sorting-network-variation-words-2.png" alt="The words kowhai and kākāriki."}

The words being compared could also be used to reinforce spelling or meaning; for example, the words above are the colours in Te Reo Māori, so the student with the word "kowhai" would be reinforcing that it means the colour yellow. The use of macrons and other diacritical marks also gives the opportunity to explore the order that is used in the such languages for those letters.

### Variation 6: Music notation

{image file-path="img/topics/sorting-network-variation-music.png" alt="Two treble clefs."}

Students can compare the pitch of music notation, with higher notes going to the right. If all the cards have the same clef (such as the treble clef here) then it reinforces that the height on the stave corresponds to the pitch. Advanced music students can do the comparisons with different clefs (bass, alto and/or tenor) to exercise note reading.

### Variation 7: Music pitch - aural

{image file-path="img/topics/sorting-network-variation-aural.jpg" alt="Two students compare the pitch of their bells."}

In this variation, students compare the pitch of simple instruments that they are carrying. The bells shown above are ideal because they are all the same size, and force students to compare them by listening. This variation can be challenging because students need to learn what high and low notes are; it can help to have a teacher or music student help with any comparisons that the students aren't sure about, and it may pay to start with notes that aren't close in pitch.

Choosing the 6 notes from a pentatonic scale (e.g. C, D, E, G, A, C) happens to work well, as the sound of all 6 being compared at the same time is a little more pleasant!

## Utiliser le réseau à l'envers

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