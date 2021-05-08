{panel type="ct-algorithm"}

# Pensée algorithmique

Dans ce cours, nous avons utilisé un algorithme pour trier les nombres dans l'ordre à l'aide d'un processeur parallèle (normalement, ce processeur doit être mis en œuvre au niveau matériel, mais notre réseau à la craie en est un ! Il est alimenté par des gens plutôt que par de l'électricité).

#### Exemples de ce que vous pourriez observer :

- Est-ce que les élèves ont compris comment chaque nœud fonctionnait (en prenant deux valeurs et en les permutant s'ils n'étaient pas dans le bon ordre) ? Sont-ils en mesure d'expliquer aux autres élèves comment utiliser le réseau correctement?

- Est-ce que les élèves ont observé que les nombres ou les données que nous avons mis dans le réseau importaient peu, et que nous obtenions toujours une solution si nous suivons correctement l'algorithme ?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

Le Réseau de tri utilisé dans ces activités est lui-même une représentation abstraite de la façon dont les Réseaux de tri sont mis en œuvre au niveau matériel et logiciel. Il représente la fonctionnalité de base d'un Réseau de tri, tout en cachant tous les les détails sur la façon dont le matériel et les circuits fonctionnent.

#### Exemples de ce que vous pourriez observer :

- Les étudiants peuvent-ils faire le lien entre les lignes et les nœuds sur ce graphique et la façon dont les ordinateurs peuvent traiter l'information en faisant des comparaisons ?
- Les élèves peuvent-ils comprendre que cette représentation peut être utilisée pour modéliser la façon dont un véritable ordinateur de traitement parallèle fonctionnerait ?

{panel end}

{panel type="ct-decomposition"}

# Décomposition

L'ensemble du processus de tri dans cette activité est décomposée en de très simples opérations : la comparaison de deux valeurs. Cette opération seule est très simpliste, mais quand elle est effectuée de nombreuses fois, elle peut être utilisée pour construire une solution pour une tâche beaucoup plus grande.

#### Exemples de ce que vous pourriez observer :

- Les élèves peuvent-ils comprendre comment concevoir un Réseau de tri pour trier seulement 2 valeurs? (Il ne serait qu'un simple nœud de comparaison).

{panel end}

{panel type="ct-pattern"}

# Généralisation et motifs

Dans ce cours, les élèves ont travaillé avec un certain type d'informations, les nombres, donc il n'y avait pas beaucoup d'utilité à la généralisation. La généralisation sera plus importante dans le prochain cours.

{panel end}

{panel type="ct-evaluation"}

# Évaluation

Pour ce Réseau de tri il peut y avoir jusqu'à trois comparaisons simultanément, et la longueur du réseau détermine combien de temps il faudrait pour effectuer toutes ces comparaisons. Bien que 12 comparaisons soient nécessaires pour traverser le réseau, le réseau peut être parcouru pendant le temps nécessaire à un seul nœud pour faire 5 comparaisons.

#### Exemples de ce que vous pourriez observer :

- Les élèves peuvent-ils identifier le plus long chemin qu'un nombre quelconque peut parcourir pour arriver à la fin ? (Les deux nombres du milieu doivent faire 5 comparaisons).
- Les élèves peuvent-ils expliquer que si chaque comparaison prenait, disons 2 secondes, le tri serait fini dans 5x2 secondes, et pas en 12x2 secondes ?

{panel end}

{panel type="ct-logic"}

# Logique

La plus petite valeur prendra toujours le chemin de gauche à chaque comparaison, et à partir de chaque point de départ le chemin qui prend toujours la branche de gauche mènera à ce nœud, la plus petite valeur terminera donc toujours à la position la plus à gauche à la fin.

#### Exemples de ce que vous pourriez observer :

- Les élèves peuvent-ils expliquer où la plus petite valeur terminera indépendamment des autres valeurs ?
- Est-ce que les élèves comprennent la fonction de chaque nœud ? Évitent-ils d'aller directement au nœud final sans faire les comparaisons ?

{panel end}