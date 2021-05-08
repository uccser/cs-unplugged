{panel type="ct-algorithm"}

# Raisonnement algorithmique

Dans ces cours, les élèves vont trier une variété de choses dans l'ordre, mais l'algorithme sous-jacent pour effectuer ces tâches restera le même. C'est un algorithme parce que c'est un processus pas à pas qui donnera toujours la bonne solution, à condition qu'il soit suivi exactement. Dans ce cas, il s'agit d'un type particulier d'algorithme appelé "algorithme parallèle". Les élèves devront suivre cet algorithme précisément pour obtenir la bonne solution (ceci est particulièrement clair quand les élèves essaient de "tricher" en allant directement à la fin du réseau, puis se rendent compte que les autres élèves se retrouvent bloqués au milieu ! C'est une excellente opportunité d'apprentissage quand quelqu'un fait cela).

{panel end}

{panel type="ct-abstraction"}

# Abstraction

Le Réseau de Tri que nous utilisons dans ces activités est une simple représentation de quelque chose de beaucoup plus complexe : comment les Réseaux de Tri sont implémentés en utilisant du matériel et des logiciels spécifiques sur certains ordinateurs pour effectuer un traitement parallèle. Les lignes, les cercles et les carrés que nous utiliserons dans nos Réseaux de Tri masquent les détails compliqués du matériel et des logiciels.

Un autre détail que nous pouvons ignorer lorsque nous utilisons un Réseau de Tri est ce que les données que nous trions sont réellement, ou ce qu'elles représentent. Peu importe si nous trions des nombres dans l'ordre, des mots, ou des notes de musique, de toute façon nous suivrons le même processus à chaque fois. La seule chose qui importe à propos des données est que nous pouvons comparer chaque objet et que ces objets ont une manière précise d'être ordonnés (par exemple, l'ordre alphabétique). Ceci est décrit plus en détail dans la section sur la logique.

L'idée générale d'un Réseau de tri est aussi un concept abstrait, qui est expliqué plus en détail dans la rubrique généralisation.

{panel end}

{panel type="ct-decomposition"}

# Décomposition

{image file-path="img/topics/sorting-network-comparing-apples.png" alt="Une personne compare une grosse pomme et une petite." alignment="right"}

Pour créer un algorithme capable de résoudre efficacement les problèmes informatiques à l'aide de processeurs parallèles, nous devons d'abord être capable décomposer une tâche en petites opérations de base qui, répétées plusieurs fois, permettent de construire une solution au problème. Cette opération est ce qui sera effectué par chaque processeur dans le réseau. Pour le Réseau de tri dans ces cours, cette opération de base est la comparaison de deux valeurs que nous effectuons à chaque nœud. Ces opérations doivent être si simples que les nœuds peuvent être exécutés simultanément et indépendamment. Les algorithmes parallèles fonctionnent mieux pour des tâches effectuant des calculs répétitifs, et indépendants, avec de grandes quantités de données.

La décomposition est l'une des étapes les plus importantes dans la création d'algorithmes de traitement parallèles !

{panel end}

{panel type="ct-pattern"}

# Généralisation et motifs

Il existe de nombreux liens entre cette section et la section abstraction ci-dessus, essayez de les trouver !

Les Réseaux de tri que nous allons examiner sont tous construits pour prendre en compte un nombre spécifique d'entrées, et ce nombre seulement. Nous ne pouvons pas utiliser un Réseau de Tri qui trie 6 nombres pour trier 10 nombres à la place. Cependant, l'idée généralisée d'un Réseau de tri peut être appliquée à d'autres problèmes. Le concept généralisé d'un Réseau de tri est simplement un réseau de comparaison (cela signifie qu'il fait des comparaisons, comme nous comparons les nombres dans chacun des cercles dans le réseau) qui prend un certain nombre d'entrées, et les trie dans l'ordre. Cette idée générale d'un Réseau de tri peut être appliquée à la résolution de nombreux problèmes différents, en créant un Réseau de tri pour le nombre spécifique d'entrées nécessaires pour le problème et en plaçant les nœuds de comparaison suivant un schéma spécifique.

Il existe également des motifs dans la disposition des Réseaux de tri ; reconnaitre ceux-ci nous aide à concevoir de plus grands réseaux. Par exemple, les Réseaux de tri à deux voies (optimal), à quatre voies et à six voies suivent un modèle similaire dans leur disposition. Un schéma simple pour générer des Réseaux de tri est exploré à la fin du cours 3 pour les 11-14 ans (mais cela peut être utilisé avec n'importe quel groupe d'âge si les élèves sont intéressés !).

Il existe également un motif commun que les élèves peuvent observer entre les différents types d'informations que nous trions avec le Réseau de tri, à savoir qu'ils peuvent être comparés et classés de manière précise. Ceci est décrit dans la section logique.

{panel end}

{panel type="ct-evaluation"}

# Évaluation

Les systèmes parallèles doivent être évalués pour leur exactitude : trient-ils toujours les valeurs correctement ? Ils doivent également faire l'objet d'une évaluation de leur efficacité : combien de temps ce réseau prend-il pour trier les valeurs, et y a-t-il un arrangement plus rapide que nous pourrions utiliser ? Ce problème pourrait-il être résolu plus facilement par un système non parallèle ?

{panel end}

{panel type="ct-logic"}

# Logique

Une règle très importante pour les données que les Réseaux de tri peuvent traiter est que les données doivent avoir une relation appelée "relation transitive". La relation transitive signifie que si a est inférieur à b, et b est inférieur à c, alors a est inférieur à c. Par exemple, les nombres ont une relation transitive : le nombre 5 est inférieur à 10 et 10 est inférieur à 15, ce qui signifie que 5 doit également être inférieur à 15. Les données doivent avoir cette relation pour qu'un Réseau de Tri puisse les trier. Si les objets n'ont pas cette relation, il n'y a aucun moyen logique pour nous de les trier !

Nous verrons aussi que les Réseaux de tri ne peuvent pas être évalués en essayant toutes les entrées possibles (bien qu'ils pourraient l'être, mais cela prendrait des heures, des jours ou même des centaines d'années pour les grands réseaux !), sauf si une très petite quantité de données est triée. Donc, à la place, nous devons appliquer la logique et la raison pour prouver pourquoi il triera toujours les données correctement. Dans ces cours, nous n'entrerons pas dans les preuves avancées pour montrer que tout le réseau fonctionne, mais les élèves peuvent appliquer leurs capacités de raisonnement logique pour prouver que les valeurs les plus petites et les plus grandes finiront toujours au bon endroit.

{panel end}