# Réseaux de Tri

{panel type="video"}

# Voir l'activité en action

Une démonstration d'enseignement des réseaux de tri est disponible ici :

{video url="https://vimeo.com/437722996"}

Quelques autres vidéos montrant différents contextes d'utilisation des réseaux de tri :

- [Vidéo 1](https://vimeo.com/437726931)
- [Vidéo 2](https://vimeo.com/437726955)

{panel end}

As we use computers more and more, and the amount of data we use increases, we want them to process information as quickly as possible. Une façon d'augmenter la vitesse d'un ordinateur est d'écrire des programmes qui utilisent de moins en moins d'instructions (comme indiqué dans les leçons sur les tris et les algorithmes de recherche). Une autre façon de résoudre les problèmes plus rapidement est de faire travailler plusieurs processeurs sur différentes parties d'une même tâche simultanément, c'est ce que ce module va détailler. Malheureusement, il n'est pas toujours simple de répartir le travail entre les différents processeurs !

{image file-path="img/topics/sorting-network-many-computers-vs-one.png" alt="Image montrant un groupe d'étudiants travaillant sur leurs ordinateurs, comparé à une seule personne sur son ordinateur."}

Sorting Networks are used to sort values into ascending order by comparing pairs of values; unlike a conventional sorting algorithm, a Sorting Network can have more than one comparison happening at the same time. For example, in the six-number Sorting Network that we use a lot in this unit, a total of 12 comparisons are used to sort the numbers, but up to three comparisons can be performed simultaneously. This means that the time required will be the same as what one computer by itself would take to make only 5 comparison steps. It's a bit like the situation where you might need to type in 4 pages of writing; if you have 4 people typing at the same time on 4 computers, then you can probably get the typing done 4 times faster than if one person did all the work.

A parallel Sorting Network enables us to explore how much faster we can sort values into order if we can make simultaneous comparisons. The main six-way parallel network used in these lessons sorts a list of values more than twice as quickly as a system that can only perform one comparison at a time.

{image file-path="img/topics/sorting-network-digging-hole-text-en.png" alt="One person is digging a hole and the other person states they can't start digging until the other person is done."}

Not all tasks can be completed faster by using parallel computation however. Par analogie, imaginez une personne creuser un fossé de dix mètres de long. If ten people each dug one metre of the ditch at the same time the task would be completed much faster. However, the same strategy could not be applied to a ditch ten metres deep, the second metre is not accessible until the first metre has been dug.

{image file-path="img/topics/sorting-network-confused-people.png" alt="A group of people are confused in front of computers as they try to coordinate a simple job across many people."}

And for typing our four page document, if you have 400 people helping, you'll probably spend so much time coordinating all the work that it might not be very fast at all! Les informaticiens sont toujours en train d'essayer de trouver les meilleurs moyens de découper les problèmes de sorte à ce qu'ils puissent être résolus par des ordinateurs travaillant en parallèle, en trouvant combien, et quelles parties du programme peuvent être faites en même temps, ainsi que l'ordre des parties.

In these lessons we use a fun team activity to demonstrate an approach to parallel sorting. It can be done on paper, but we like to get students to do it on a large scale, running from node to node in the network.

En aparté, bien que cela s'appelle un "réseau", il ne s'agit que de l'un des nombreux types de réseaux que l'on rencontre en Informatique. A common kind of “network” is a communication network, such as the telecommunication networks that mobile phones use, and of course the Internet! Il existe également des réseaux pour la représentation de choses comme des cartes routières ou les itinéraires aériens. It’s important to recognise that the Sorting Network in this activity is **not** one of these types of networks, it is called a comparator network, because it’s a network where each node compares two values, rather than linking different devices (such as phones and computers) together.

## Technologies numériques | Algorithmes

{image file-path="img/topics/sorting-network-too-far-kid.png" alt="A child walks too far in the sorting network activity, failing the activity for everyone."}

To use the Sorting Network students need to follow a simple algorithm and should recognise that if they do not follow this algorithm precisely, the way a computer would, then they will probably not get to a correct result, or may not get a result at all! Students will be working collaboratively to ensure that each part of the algorithm is coordinated, because if one person moves too far ahead, without stopping at the nodes they are meant to, it causes the process to fail for everyone. There are also many algorithms that are used to construct extremely efficient Sorting Networks of different sizes, and Computer Scientists study these to try and create even better ones. These can be very complex however, so when students construct their own networks they will be doing this in a simplified way.

## Vocabulaire

- **Processor/CPU:** A device that can run computer programs.
- **Parallel processing:** Using multiple processors to work on different parts of a problem at the same time.
- **Calcul séquentiel:** Exécuter un programme sur un seul processeur, les instructions sont alors exécutées les une après les autres.
- **Network:** A series of connected nodes such as a computer network, a road map, or a comparator network.
- **Computational step:** A basic operation that is part of an algorithm.
- **GPU/Carte graphique:** Processeur spécialisé qui peut faire des opérations simples sur de nombreux pixels d'une image en parallèle. Ils sont souvent utilisés pour d'autres types de calculs en raison de leur capacité à traiter des données en parallèle.

{panel type="math"}

# Liens mathématiques

Cette activité soutient fortement l'apprentissage à propos de la notion d'ordre pour les nombres, notamment la détermination de la relation entre deux nombres (supérieur, inférieur).

{panel end}

## Implications dans le monde réel

{image file-path="img/topics/sorting-network-tortoises-vs-rabbit.png" alt="Un groupe de tortues construisent un mur plus rapidement qu'un lapin."}

Souvent il est moins cher et plus rapide de faire travailler sur un problème un grand nombre de processeurs lents, plutôt qu'un seul processeur très rapide. Companies that have massive cloud servers often find it more economical to have many slower, cheaper devices rather than fewer expensive ones. Bien sûr, cela vous oblige à être en mesure de diviser une tâche de calcul sur plusieurs processeurs. Pour certains problèmes c'est très facile à faire, mais pour d'autres, c'est impossible. La tâche à laquelle nous nous intéressons ici se trouve entre ces deux extrêmes.

Having such a small operation (comparing two values) split over multiple devices means that this kind of algorithm needs to run on special hardware. It is only used for specialist applications at present, but, for example, it is sometimes done on the graphics processor (GPU) of a computer, because these processors are good at doing parallel computation of simple tasks.

{image file-path="img/topics/sorting-network-ancient-sorting-network-text-en.png" alt="Un GPU trouve une peinture d'un ancien réseau de tri dans une caverne."}

Sorting Networks were invented long before powerful GPUs came along; this is an exciting thing about Computer Science - some of our discoveries are ahead of the hardware that is available, so we're ready for the hardware if it does become commonly available! Note that the approach explored in these lessons is **not** a conventional sorting algorithm, as the sorting that is done on a conventional system can make only one comparison at a time; conventional sorting algorithms are explored in another lesson. L'objectif principal de ce cours est d'aider les élèves à explorer les compromis entre le partage de travail sur plusieurs processeurs et l'utilisation d'un seul processeur.

One approach to parallel computation that is currently popular is called "MapReduce", which is widely used in Cloud Computing systems where large amounts of computing are spread over a large number of processors.

## Questions de réflexion

- What was most surprising about the learning that happened from the teaching of this unit?
- Who were the students that were very systematic when working through the activities?
- Quels étaient les étudiants très minutieux dans leurs activités ?
- Que changerais-je dans ma façon d'enseigner ce module ?