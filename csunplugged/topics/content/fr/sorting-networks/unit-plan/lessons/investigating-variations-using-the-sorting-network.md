# Enquêter sur les variantes en utilisant le Réseau de Tri

## Connaissances préalables

Les élèves doivent avoir terminé le cours 1 qui présente le Réseau de Tri.

## Questions clés

- Dans le Réseau de tri, que pensez-vous qu'il se passerait si la plus petite carte allait à droite au lieu d'aller à gauche dans chaque case, et vice versa ? (Les élèves devraient être en mesure de trouver que les valeurs sortiront dans l'ordre inverse.)

- Est-ce que cela fonctionnera si nous essayons d'utiliser le Réseau de Tri à l'envers, en commençant avec les nombres dans le désordre à la fin, et en progressant à rebours ? (Les élèves peuvent avoir des points de vue différents ; cela semble fonctionner la plupart du temps, mais dans ce cours nous allons trouver un exemple qui ne fonctionne pas.)

## Lancement du cours

Montrez à nouveau aux élèves le Réseau de Tri (si le réseau a besoin d'être redessiné, les élèves aiment souvent le faire, et le dessiner avec précision à partir du diagramme est un exercice utile). Dites-leur qu'ils vont l'essayer avec quelques variantes cette fois-ci.

Plusieurs variantes sont décrites ci-dessous, et vous pouvez choisir celles qui conviennent aux élèves, ou vous pouvez essayer avec d'autres éléments qui pourraient être triés. La clé est que les comparaisons obéissent à la règle de transitivité : si a est plus petit que b, et b est plus petit que c, alors a est plus petit que c. Le tri des élèves par leur taille ou d'autres attributs personnels peut être problématique — non seulement ce pourrait être une question délicate, mais comparer deux élèves pour trouver le plus grand pourrait ne pas donner un résultat cohérent s'ils sont d'une taille similaire.

{panel type="math"}

# Liens mathématiques

Résultats à prévoir : en comprenant le fonctionnement du Réseau de tri, les élèves étudieront différentes façons de l'utiliser et exploreront comment les résultats sont affectés par ces changements.

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

### Variante 4 : Mots composés de lettres dans l'ordre alphabétique

Comme variante intéressante pour le tri des lettres, il y a certains mots français qui ont leurs lettres dans l'ordre alphabétique, comme BIJOUX. Si vous donnez aux élèves les lettres mélangées (par exemple O, J, I, B, X et U) et que vous leur demandez de les trier avec le Réseau de tri, cela formera le mot BIJOUX à la fin. Peu de mots communs ont cette propriété ; on peut citer par exemple ACCENT et DEHORS. Demandez aux élèves d'essayer le Réseau de tri avec certains de ces mots (notez que vous aurez besoin de lire les lettres triées dans la direction de la position de départ pour voir le mot dans le bon sens).

Il y a également un certain nombre de mots qui ont leurs lettres dans l'ordre alphabétique inverse, comme SONGEA et VOLIGE (ceux-ci peuvent être triées à l'aide de la variante "la plus grande à gauche", ou peut-être, lus depuis l'autre côté du Réseau de tri). Certains mots avec cette propriété ont des lettres doubles, tels que BILLOT ou TROLLA ; ils seront triés correctement, puisque l'ordre des lettres doubles n'importe pas.

{panel type="general"}

# Liste des mots avec les lettres dans l'ordre alphabétique

Voici une liste plus longue de mots de 6 lettres qui peuvent être utilisés pour cet exercice. Ils sont tous issus d'un dictionnaire, même si certains sont plutôt obscures !

{image file-path="img/topics/sorting-network-toffees-cellos-sponge.png" align="right" alt="2 bonbons (toffees), 2 violoncelles (cellos) et une éponge (sponge)."}

ACCENT, ACCORT, AFFINS, AFFLUX, AGGLOS, BELLOT, BIJOUX, BILLOT, CHINOS, CHINTZ, DEHORS, DHIKRS, EFFORT, FILMOS, KIFFEE, PIFFEE, POLICA, POMMEE, PONGEE, RONGEA, RONGEE, SNIFEE, SNIFFA, SNIFFE, SOMMEE, SONGEA, SONGEE, SONNEE, SPEEDA, SPOLIA, SPOLIE, TOFFEE, TROLLA, TROLLE, TSONGA, VOLIGE, YTTRIA, YUPPIE, ZOOMEE.

{panel end}

### Variante 5 : Tri des mots dans l'ordre du dictionnaire

{image file-path="img/topics/tri-réseau-variation-words.png" alt="Les mots crochet et crocodile."}

Donnez aux élèves des cartes avec des mots du dictionnaire, et demandez-leur comment ils pourraient être comparés. Les élèves doivent faire remarquer qu'ils pourraient être placés dans l'ordre du dictionnaire. Une variante consiste à leur donner des livres et de leur demander de les trier selon le nom des auteurs.

{image file-path="img/topics/sorting-network-crochet-v-crocodile.png" alt="Crochet vs crocodile."}

Comparer deux mots ou deux noms est difficile ; ils devront savoir comparer chaque lettre jusqu'à ce que deux diffèrent (par exemple pour "crochet" et "crocodile", le préfixe "croc" est le même, donc c'est le "h" et le "o" qui déterminent l'ordre ; ce processus est un algorithme en lui-même !)

{image file-path="img/topics/sorting-network-variation-words-2.png" alt="Les mots kowhai et kākāriki."}

Les mots comparés pourraient également être utilisés pour renforcer l'orthographe ou le sens ; par exemple, les mots ci-dessus sont des couleurs en Te Reo Māori, afin que l'élève avec le mot "kowhai" comprenne qu'il s'agit de la couleur jaune. L'utilisation des macrons ( ˉ ) et autres signes diacritiques donne également l'opportunité d'explorer l'ordre utilisé dans les langues pour ces lettres.

### Variante 6 : Notes de musique

{image file-path="img/topics/sorting-network-variation-music.png" alt="Deux clefs de Sol."}

Les élèves peuvent comparer la hauteur des notes de musique, avec les notes les plus hautes allant vers la droite. Si toutes les cartes ont la même clef (comme la clef de Sol ici), alors cela montre que la hauteur sur la portée correspond à la hauteur de la note. Les élèves faisant des études de musique avancées peuvent faire des comparaisons entre différentes clefs (basse, alto et/ou ténor) pour entrainer leur lecture de notes.

### Variante 7 : Ton musical

{image file-path="img/topics/sorting-network-variation-aural.jpg" alt="Deux élèves comparent le ton de leur cloche."}

Dans cette variante, les élèves comparent la hauteur de simples instruments qu'ils ont en main. Les cloches indiqués ci-dessus sont idéales car elles sont toutes de la même taille, et cela force les élèves à les comparer à l'écoute. Cette variante peut être difficile, car les élèves ont besoin d'apprendre ce que sont les notes hautes et basses ; il peut être utile d'avoir l'aide d'un professeur ou d'un étudiant en musique pour aider avec toutes les comparaisons pour lesquelles les élèves ne sont pas sûrs, et il peut être utile de démarrer avec des notes qui ne sont pas proches les unes des autres.

Le choix des 6 notes sur la gamme pentatonique (e.g. Do, Ré, Mi, Sol, La, Do) fonctionne très bien, car le son des 6 notes comparées en même temps est plus agréable à entendre !

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

Ce type d'algorithmes doit fonctionner sur un équipement spécial pour tirer parti de la possibilité d'effectuer plusieurs comparaisons en même temps. À l'heure actuelle, ils sont seulement utilisés pour des applications spécialisées. Par exemple, ils sont parfois exécutés sur le processeur graphique (GPU) d'un ordinateur, parce que ces processeurs sont bons pour faire du calcul en parallèle. Les Réseaux de Tri ont été inventés bien avant l'apparition des GPU puissants ; c'est un aspect passionnant de l'informatique : certaines de nos découvertes sont en avance sur le matériel disponible, nous sommes donc prêts à utiliser le matériel lorsqu'il sera couramment disponible ! Notez que ce n'est *pas* un algorithme de tri classique. L'algorithme effectué sur un système conventionnel ne peut faire qu'une comparaison à la fois ; les algorithmes de tri classiques sont étudiés dans un autre cours.

## Réflexion sur le cours

Qu'avez-vous remarqué à chaque variante de l'utilisation du Réseau de Tri ?

Était-ce ce que vous aviez prévu ?