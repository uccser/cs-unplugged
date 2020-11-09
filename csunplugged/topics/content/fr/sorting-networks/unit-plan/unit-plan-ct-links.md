{panel type="ct-algorithm"}

# Raisonnement algorithmique

In these lessons students will be sorting a variety of things into order, but the underlying algorithm for performing these tasks will remain the same. C'est un algorithme parce que c'est un processus pas à pas qui donnera toujours la bonne solution, à condition qu'il soit suivi exactement. Dans ce cas, il s'agit d'un type particulier d'algorithme appelé "algorithme parallèle". Students will need to follow this algorithm precisely to get to the correct solution (this is particularly clear when students try to ‘cheat’ by dashing straight to the end of the network, and then realise this means other students are now stuck in the middle! It’s a great learning opportunity when someone does this).

{panel end}

{panel type="ct-abstraction"}

# Abstraction

Le Réseau de Tri que nous utilisons dans ces activités est une simple représentation de quelque chose de beaucoup plus complexe : comment les Réseaux de Tri sont implémentés en utilisant du matériel et des logiciels spécifiques sur certains ordinateurs pour effectuer un traitement parallèle. Les lignes, les cercles et les carrés que nous utiliserons dans nos Réseaux de Tri masquent les détails compliqués du matériel et des logiciels.

Another detail we can ignore when we are using a Sorting Network is what the data we are sorting actually is, or represents. It doesn’t matter if we are sorting numbers into order, or words, or musical notes, we will still follow the same process each time. The one thing about the data that does matter however is that we can compare each item and that they have a precise way of being ordered (e.g. alphabetical order). Ceci est décrit plus en détail dans la section sur la logique.

The overall idea of a Sorting Network is actually an abstract concept as well, this is explained under the generalisation heading.

{panel end}

{panel type="ct-decomposition"}

# Décomposition

{image file-path="img/topics/sorting-network-comparing-apples.png" alt="A person compares a large apple and a small apple." alignment="right"}

In order to create an algorithm that can solve computational problems effectively using parallel processors, we must first be able decompose the task into very small and basic operations that, when repeated many times, can build up a solution to the problem. Cette opération est ce qui sera effectué par chaque processeur dans le réseau. For the Sorting Network in these lessons this basic operation is the comparison of two values that we perform at each node. Ces opérations doivent être si simples que les nœuds peuvent être exécutés simultanément et indépendamment. Parallel algorithms work best for tasks that need to do repetitive, and independent, calculations with large amounts of data.

Decomposition is one of the most important steps in creating parallel processing algorithms!

{panel end}

{panel type="ct-pattern"}

# Généralisation et motifs

There are many links between this section and the abstraction section above, see if you can spot them!

The Sorting Networks we will look at are each constructed to take in a specific number of inputs, and that number only. Nous ne pouvons pas utiliser un Réseau de Tri qui trie 6 nombres pour trier 10 nombres à la place. However the generalised idea of a Sorting Network can be applied to different problems. The generalised concept of a Sorting Network is simply a comparator network (comparator just means it makes comparisons, like how we compare numbers in each of the circles in the network) that takes in a number of inputs, and sorts them into order. This general idea of a Sorting Network can then be applied to solving many different problems, by creating a Sorting Network for the specific number of inputs needed for the problem and placing its comparison nodes in a specific pattern.

There are patterns in the layout of Sorting Networks as well; recognising these helps us design larger networks. For example, the (optimal) two-way, four-way and six-way Sorting Networks follow a similar pattern in their layout. A simple pattern for generating Sorting Networks is explored at the end of lesson 3 for ages 11-14 (but this can be used with any age group if the students are interested!).

There is also a common pattern that students can observe between all the different types of information we sort with the Sorting Network, which is that they can be compared and ordered in a precise way. Ceci est décrit dans la section logique.

{panel end}

{panel type="ct-evaluation"}

# Évaluation

Les systèmes parallèles doivent être évalués pour leur exactitude : trient-ils toujours les valeurs correctement ? Ils doivent également faire l'objet d'une évaluation de leur efficacité : combien de temps ce réseau prend-il pour trier les valeurs, et y a-t-il un arrangement plus rapide que nous pourrions utiliser ? Ce problème pourrait-il être résolu plus facilement par un système non parallèle ?

{panel end}

{panel type="ct-logic"}

# Logique

A very important rule for the data that Sorting Networks can process is the data must have something called a transitive relation. The transitive relation means: if a is less than b, and b is less than c, then a is less than c. Par exemple, les nombres ont une relation transitive : le nombre 5 est inférieur à 10 et 10 est inférieur à 15, ce qui signifie que 5 doit également être inférieur à 15. Les données doivent avoir cette relation pour qu'un Réseau de Tri puisse les trier. If items don’t have this relation then there is no logical way for us to order it!

We will also see that Sorting Networks can't be evaluated by trying every possible input (well they could be, but it could take hours, days, or even hundreds of years for big networks!), unless a very small amount of data is being sorted. So instead, we must apply logic and reason to prove why it will always sort the data correctly. In these lessons we don't get into the advanced proofs that the whole network will work, but students can apply their logical thinking skills to prove that the smallest and largest values will always end up in the correct place.

{panel end}