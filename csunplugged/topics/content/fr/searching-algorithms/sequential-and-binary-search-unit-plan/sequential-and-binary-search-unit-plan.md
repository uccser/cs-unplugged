# Sequential and binary search

{comment Video 1: Sequential search: Random numbered cards with pictures on them. (using numbers from 0 - 31) - SETTING: As if it’s a maths group in a class setting}

{comment Video 2: Binary search using numbered cards with pictures on them ranging from 0 - 999.}

{comment Video 3: Linking the "Number Hunt" activities to statistics.}

{image file-path="img/topics/different-sized-haystacks.png" alt="A farmer can easily find a needle in a small haystack, but can't find it in a large haystack."}

Searching for a keyword, a value, or a specific piece of data (information) is the basis of many computing applications, whether it’s looking up a bank account balance, using an internet search engine, or searching for a file on your laptop. Computers deal with a lot of information so we need efficient algorithms for searching. This unit explores some common algorithms that are used to search for data on computers, with the opportunity to integrate this learning with statistics.

Parce que les ordinateurs sont souvent tenus de trouver des informations dans des collections de données qui peuvent être très, très volumineuses, il est crucial d'utiliser le bon algorithme de recherche ! A key idea in computer science that we'll be illustrating with searching algorithms is just how fast an algorithm can be; students might think that if you're searching twice as much data then it should take twice as long, but we'll look at a way to search that takes almost the same amount of time to search 2 million items as it would for 1 million.

We'll also look at the kind of steps that algorithms use to solve the important problem of searching data. When you’re telling a computer how to find exactly what you’re looking for you need to remember that computers are simple machines, they can only look at one piece of data at a time, and check if it is what you’re searching for. Imagine if every time a computer had to search for something, it had to compare every single piece of information it contained to the information it was searching for before it found what you were looking for? It would take a very long time to find what you wanted. C'est pourquoi les informaticiens doivent développer des moyens rapides et efficaces de le faire.

For computer scientists finding the right algorithm requires analysing the time taken and the amount of memory used. Some great discussion questions are:

Is it always useful to sort your data so you can complete a binary search? Regardons un traitement de texte, vous avez 100 pages de texte et vous voulez trouver un mot. Pourquoi le traitement de texte ne trierait-il pas vos mots pour trouver le mot que vous recherchez ?

Une considération que les informaticiens prennent en compte est combien de fois êtes-vous susceptible de rechercher quelque chose. If it’s only once, then it isn’t worth the effort to sort and then find the item.

## Technologies numériques | Algorithmes

This unit demonstrates two different search methods: *sequential* (sometimes called *linear*) search, and *binary* search. We'll see that binary search is remarkably fast, and although there are other search algorithms that are can do even better (such as the *hash table*, which is covered in the unit on Data Structures for search algorithms), the step-up from sequential search to binary search demonstrates how much there is to gain there is to be made by applying the right algorithm to the job.

{image file-path="img/topics/computer_searching.png" alt="Cartoon computer looking around with a magnifying glass"}

Les gens s'attendent à ce que les ordinateurs trouvent l'information très rapidement, et la vitesse des algorithmes de recherche a une grande influence sur notre expérience en tant qu'utilisateurs. A search engine typically searches billions of web pages in less than a second, which is the kind of time-frame that humans are used to working in. We don’t like seeing the “wheel of doom” appear while the computer is processing/thinking about what to do, and if an app is too slow then people won’t want to use it.

This unit focuses on understanding two simple searching algorithms, and comparing how long they can take to reliably find the correct data (a number or word, for example).

## Vocabulaire expliqué

**Données**: La façon dont les informations sont stockées. Numbers are a type of data you will come across very often (e.g. account numbers, customer numbers, card numbers, serial numbers, product numbers and so on). Il peut également s'agir de texte (comme les mots que nous recherchons), de dates et même d'images et de sons. You can think of anything stored in a computer's memory as data; it’s all pieces of information.

**Raw data**: Raw data means ‘unprocessed data’ which has been collected from a source, and has not been cleaned up or used yet. Par exemple, disons que vous avez mesuré la température tous les jours de l'année, et maintenant vous avez un tas de chiffres, cela pourrait s'appeler vos ‘données non traitées’. If you then divided this data into each month of the year, and averaged it so you had the average temperature for each month, this would be your ‘processed data’.

**Sequential search**: A sequential search is when you look at each piece of data, one by one, and don’t stop until you find what you are looking for. You can use a sequential search on any data, whether it is sorted or unsorted (though it would be potentially a slow way to locate what you are looking for if the data is in sorted order!) However, sequential search is the **only** option you can use when you need to search through data that is **unsorted**. Say for example you are looking for the word “is” in the following list: “the”, “my”, "it", “is”, “said”, “a”, “from”. A computer would go to the first word “the” and ask is it the same as “is”. If it is it will stop searching, if it isn’t, it will go to the next word and repeat this process until it finds the matching data. In this case it takes 5 guesses to find the word. It could have taken up to 7 guesses or just 1 guess, depending on which word you were searching for.

Imaginez que notre détective (ci-dessous) soit programmé pour faire une recherche séquentielle pour trouver le mot **"dit"**. Voici le processus ou l'algorithme qu'il suivrait pour le trouver. Remarquez qu'il ne peut comparer qu'un seul mot à la fois !

Now imagine if he has a million words to search!

{image file-path="img/topics/sequential_detective.gif" alt="A detective looking at words sequentially in a sentence until he finds the word 'said'"}

**Recherche dichotomique (binaire)**: Un algorithme qui nous indique comment trouver efficacement une valeur spécifique dans une liste **ordonnée (triée)**. It is called ‘binary’ search because each time you look at a value in the list you divide the list into 2 parts, one is discarded and the other is kept. Ici, le mot "binaire" signifie simplement quelque chose qui a deux parties, comme un système d'étoiles binaire (avec deux étoiles); la recherche binaire ne doit pas être confondue avec les nombres binaires.

Suppose our detective is looking for the word **"said"** from the following list, which is in alphabetical order: “a”, “from”, “is”, “it”, “my”, “said”, “the”. First the computer will go straight to the middle word, “it” and see if that matches - because it doesn’t, the computer doesn’t need to check the 3 words to the left. Now the computer finds the middle word of the right half of the list, which is “said”. Binary search narrows in on the location of the word very quickly.

{image file-path="img/topics/binary_detective.gif" alt="A detective trying to find the word 'said' in a sentence using binary search"}

## Implications dans le monde réel

We can apply these search strategies ourselves when we are looking to find one thing. Every time we play games like “guess my number” we can apply the binary search to it. Likewise if we are searching for a book in the library that hasn’t been returned to the correct place, we’ll need to do a sequential search to find it. Searching is everywhere in our lives, from finding a person’s address to looking up a phone number in a phone book. We can apply binary or sequential search methods depending on how the data has been organised to start with.

{panel type="math"}

# Liens mathématiques

This unit could be taught within a statistics unit at all curriculum levels to support students' understanding of why particular searching methods are faster than others.

{panel end}

## Questions de réflexion

Qu'est-ce qui était le plus surprenant dans l'apprentissage de ce module ?

Quels étaient les étudiants très méthodiques dans leurs activités ?

Quels étaient les étudiants très minutieux dans leurs activités ?

Que changerais-je dans ma façon d'enseigner ce module ?