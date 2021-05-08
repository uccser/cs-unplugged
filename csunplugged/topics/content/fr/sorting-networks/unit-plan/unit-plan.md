# Réseaux de Tri

{panel type="video"}

# Voir l'activité en action

Une démonstration d'enseignement des réseaux de tri est disponible ici :

{video url="https://vimeo.com/437722996"}

Quelques autres vidéos montrant différents contextes d'utilisation des réseaux de tri :

- [Vidéo 1](https://vimeo.com/437726931)
- [Vidéo 2](https://vimeo.com/437726955)

{panel end}

Comme nous utilisons de plus en plus les ordinateurs, et que la quantité de données que nous utilisons augmente, nous souhaiterions que les ordinateurs traitent ces informations aussi rapidement que possible. Une façon d'augmenter la vitesse d'un ordinateur est d'écrire des programmes qui utilisent de moins en moins d'instructions (comme indiqué dans les leçons sur les tris et les algorithmes de recherche). Une autre façon de résoudre les problèmes plus rapidement est de faire travailler plusieurs processeurs sur différentes parties d'une même tâche simultanément, c'est ce que ce module va détailler. Malheureusement, il n'est pas toujours simple de répartir le travail entre les différents processeurs !

{image file-path="img/topics/sorting-network-many-computers-vs-one.png" alt="Image montrant un groupe d'étudiants travaillant sur leurs ordinateurs, comparé à une seule personne sur son ordinateur."}

Les Réseaux de tri sont utilisés pour trier des valeurs dans l'ordre croissant en comparant des paires de valeurs. À la différence d'un algorithme de tri classique, un Réseau de tri peut effectuer plus d'une comparaison à la fois. Par exemple, dans le Réseau de tri à six nombres que nous utilisons beaucoup dans ce cours, un total de 12 comparaisons sont utilisées pour trier les nombres, et jusqu'à trois comparaisons peuvent être effectuées simultanément. Cela signifie que le temps nécessaire sera équivalent au temps passé pour exécuter 5 étapes de comparaisons sur une seule machine. C'est un peu comme la situation où vous pourriez avoir besoin de copier 4 pages de texte ; si 4 personnes tapent simultanément sur 4 ordinateurs, alors vous devriez pouvoir obtenir le texte complet 4 fois plus rapidement que si une seule personne avait fait tout le travail.

Un Réseau de tri parallèle permet d'observer à quel point on peut accélérer le tri des valeurs si on effectue des comparaisons simultanées. Le principal réseau de tri parallèle à 6 voies utilisé dans ces cours trie une liste de valeurs plus de deux fois plus rapidement qu'un système qui ne peut effectuer qu'une comparaison à la fois.

{image file-path="img/topics/sorting-network-digging-hole-text-en.png" alt="Une personne en train de creuser un trou et l'autre personne dit qu'elle ne peut pas commencer à creuser tant que la première n'a pas terminé."}

Néanmoins, toutes les tâches ne peuvent pas être accomplies plus rapidement en utilisant le calcul parallèle. Par analogie, imaginez une personne creuser un fossé de dix mètres de long. Si une dizaine de personnes pouvaient creuser un mètre du fossé en même temps, la tâche serait effectuée beaucoup plus rapidement. Cependant, la même stratégie ne pourrait pas être appliquée à un fossé de dix mètres de profondeur, le second mètre ne pouvant pas être creusé tant que le premier n'est pas terminé.

{image file-path="img/topics/sorting-network-confused-people.png" alt="Un groupe d'élève confus devant leurs ordinateurs alors qu'ils essayent de coordonner une tâche simple entre plusieurs personnes."}

Et pour la saisie de nos quatre pages de texte, si vous avez 400 personnes pour le faire, vous passerez probablement tellement de temps à coordonner le travail que ce ne sera pas rapide du tout ! Les informaticiens sont toujours en train d'essayer de trouver les meilleurs moyens de découper les problèmes de sorte à ce qu'ils puissent être résolus par des ordinateurs travaillant en parallèle, en trouvant combien, et quelles parties du programme peuvent être faites en même temps, ainsi que l'ordre des parties.

Dans ces cours, nous utilisons une activité ludique en équipe pour aborder une méthode de tri parallèle. Elle peut être faite sur papier, mais il est préférable que les élèves le fassent à plus grande échelle, en courant de nœud en nœud dans le réseau.

En aparté, bien que cela s'appelle un "réseau", il ne s'agit que de l'un des nombreux types de réseaux que l'on rencontre en Informatique. Un type habituel de “réseaux” sont les réseaux de communication, tels que les réseaux de télécommunications utilisés par les téléphones mobiles, et bien sûr l'Internet ! Il existe également des réseaux pour la représentation de choses comme des cartes routières ou les itinéraires aériens. Il est important de préciser que le Réseau de tri de cette activité n'est **pas** l'un de ces types de réseaux, c'est ce que l'on appelle un réseau de comparaison parce que c'est un réseau dans lequel chaque nœud compare deux valeurs, plutôt que de lier différents appareils (tels que les téléphones et ordinateurs) les uns aux autres.

## Technologies numériques | Algorithmes

{image file-path="img/topics/tri-réseau-trop-loin-kid.png" alt="Un enfant marche trop loin dans l'activité du Réseau de tri, faisant échouer l'activité pour tout le monde."}

Pour utiliser le Réseau de tri, les élèves doivent suivre un algorithme simple et comprendre que s'ils ne suivent pas cet algorithme précisément, comme le ferait un ordinateur, alors ils n'obtiendraient probablement pas un résultat correct, ou n'auraient pas de résultat du tout ! Les élèves travailleront en collaboration afin d'assurer que chaque partie de l'algorithme est coordonné, parce que si une personne se déplace trop loin à l'avance, sans s'arrêter aux bons nœuds, cela entraine l'échec du processus pour tout le monde. Il y a également de nombreux algorithmes qui sont utilisés pour construire des Réseaux de tri de différentes tailles extrêmement performants, que les informaticiens étudient pour essayer d'en créer d'encore meilleurs. Ceux-ci peuvent être très complexes, cependant, de sorte que lorsque les élèves construisent leurs propres réseaux ils vont le faire de manière simplifiée.

## Vocabulaire

- **Processeur/CPU :** Un appareil qui exécute des programmes.
- **Calcul parallèle :** Utiliser plusieurs processeurs pour travailler sur différentes parties d'un problème en simultané.
- **Calcul séquentiel:** Exécuter un programme sur un seul processeur, les instructions sont alors exécutées les une après les autres.
- **Réseau :** Une suite de nœuds connectés, tel un réseau informatique, une carte routière, ou un réseau de comparaisons.
- **Instruction :** Opération de base d'un algorithme.
- **GPU/Carte graphique:** Processeur spécialisé qui peut faire des opérations simples sur de nombreux pixels d'une image en parallèle. Ils sont souvent utilisés pour d'autres types de calculs en raison de leur capacité à traiter des données en parallèle.

{panel type="math"}

# Liens mathématiques

Cette activité soutient fortement l'apprentissage à propos de la notion d'ordre pour les nombres, notamment la détermination de la relation entre deux nombres (supérieur, inférieur).

{panel end}

## Implications dans le monde réel

{image file-path="img/topics/sorting-network-tortoises-vs-rabbit.png" alt="Un groupe de tortues construisent un mur plus rapidement qu'un lapin."}

Souvent il est moins cher et plus rapide de faire travailler sur un problème un grand nombre de processeurs lents, plutôt qu'un seul processeur très rapide. Les entreprises qui ont d'énormes serveurs cloud trouvent souvent qu'il est plus économique d'avoir des machines beaucoup plus lentes, mais moins chères, que moins de machines très chères. Bien sûr, cela vous oblige à être en mesure de diviser une tâche de calcul sur plusieurs processeurs. Pour certains problèmes c'est très facile à faire, mais pour d'autres, c'est impossible. La tâche à laquelle nous nous intéressons ici se trouve entre ces deux extrêmes.

Avoir une petite opération (comparaison de deux valeurs) divisée sur plusieurs appareils signifie que ce type d'algorithme a besoin de fonctionner sur du matériel spécial. Cet algorithme est seulement utilisé pour des applications spécialisées à l'heure actuelle, mais, par exemple, il est parfois fait sur le processeur graphique (GPU) d'un ordinateur, parce que ces processeurs sont bons pour faire des calculs simples en parallèle.

{image file-path="img/topics/sorting-network-ancient-sorting-network-text-en.png" alt="Un GPU trouve une peinture d'un ancien réseau de tri dans une caverne."}

Les Réseaux de tri ont été inventés bien avant que les GPUs n'apparaissent ; c'est une des choses excitantes en informatique — certaines découvertes se font avant que le matériel soit disponible, ainsi, nous sommes prêts lorsque le matériel devient disponible ! Notez que l'approche explorée dans ces cours n'est **pas** un algorithme de tri conventionnel, car le tri qui est fait sur un système conventionnel ne peut faire qu'une seule comparaison à la fois ; les algorithmes de tri classiques sont explorées dans un autre cours. L'objectif principal de ce cours est d'aider les élèves à explorer les compromis entre le partage de travail sur plusieurs processeurs et l'utilisation d'un seul processeur.

Une approche pour le calcul parallèle qui est actuellement populaire s'appelle "MapReduce", elle est largement utilisée dans les systèmes cloud où de grandes quantités de calcul sont réparties sur un grand nombre de processeurs.

## Questions de réflexion

- Qu'est-ce qui était le plus surprenant au sujet de l'apprentissage qui s'est passé au cours de ce module ?
- Quels sont les élèves qui ont été très méthodiques dans la réalisation des activités ?
- Quels élèves étaient très minutieux dans leurs activités ?
- Que changerais-je dans ma façon d'enseigner ce module ?