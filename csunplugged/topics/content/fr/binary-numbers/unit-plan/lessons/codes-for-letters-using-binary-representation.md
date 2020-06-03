# Codes pour les lettres utilisant la représentation binaire

## Questions clés

- Combien de caractères différents pouvez-vous taper sur un ordinateur ? (La discussion peut commencer par les 26 lettres de l'alphabet latin, puis s'étendre à d'autres caractères du clavier, y compris les lettres majuscules, les caractères accentués, les chiffres et les ponctuations. Les élèves savent peut-être que d'autres langues peuvent avoir des milliers de caractères et le nombre de caractères est également en pleine expansion depuis l'invention des émoticônes !)

## Lancement du cours

{panel type="general"}

# Notes sur les ressources

Il existe également une version interactive en ligne des cartes binaires [ici](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), du [Computer Science Field Guide ](http://www.csfieldguide.org.nz/), mais il est préférable de travailler avec des cartes physiques.

{panel end}

{image file-path="img/topics/col_binary_robot_convo.png" alt="Garçon dessiné parlant à un robot" alignment="left"}

Discutez de la manière dont vous communiqueriez une lettre de l'alphabet à quelqu'un si vous ne pouviez le faire qu'en utilisant des nombres entre 0 et 26. *(Les élèves recommanderont généralement d'utiliser un code de 1 pour a, 2 pour b, et ainsi de suite)*.

Calculez et écrivez les nombres binaires en utilisant 5 bits de 0 à 26 sur la feuille Binaire vers Alphabet, puis ajoutez les lettres de l'alphabet.

{panel type="teaching"}

# Observations pour l'enseignant

- Vérifier que leur code binaire pour 3 est bien 00011 parce que les élèves écrivent couramment 00100 en anticipant le motif sans forcément vérifier qu'elle est correcte.
- Vérifier qu'ils écrivent le code binaire dans le bon ordre avec la valeur la plus petite à droite - par exemple, certains vont commencer avec 1 écrit 10000 au lieu de 00001.
- Identifiez les élèves qui montrent une ou plusieurs caractéristiques de la pensée informatique ; ceux qui sont très méthodiques, qui alignent tout de façon exacte, qui sont les premiers à reconnaître la logique et n'ont plus besoin des cartes.
- Vérifiez que tous les étudiants peuvent vous décrire comment calculer le nombre qu'ils doivent chercher. Cela permet d'identifier ceux qui devinent le motif.
- Notez que si votre alphabet local est légèrement différent (par exemple, avec des signes diacritiques tels que les macrons ou les accents) vous pouvez adapter le code pour faire correspondre les caractères les plus communs ; cette question est également examinée ci-après.

{panel end}

## Activités de la leçon

En utilisant le tableau que les élèves ont créé ci-dessus, donnez-leur un message à décoder, tel que votre nom ou le nom d'un auteur (par exemple 00001 00010 00010 11001 pour ABBY).

Maintenant, demandez aux élèves d'écrire et de communiquer leurs propres messages. Rappelez-leur qu'ils peuvent écrire les 0 et les 1 en utilisant n'importe quels symboles, tels que des case à cocher vides ou remplies.

Considérez aussi des représentations inhabituelles ; par exemple, chaque bit pourrait être communiqué avec un son qui soit grave ou aigu. Ou bien, un nombre à 5 bits peut être représenté par les cinq doigts de la main, chaque doigt correspondant à un bit.

## Ajouter plus de caractères

Certaines langues ont un peu plus ou moins de caractères, en incluant celles qui ont des marques diacritiques. Si les élèves pensent à un alphabet avec plus de 32 caractères, alors 5 bits ne seront pas suffisants. Les élèves peuvent aussi se rendre compte qu'un code est nécessaire pour une espace (0 est un bon choix pour cela), donc 5 bits ne couvrent que 31 caractères alphabétiques.

Demandez aux élèves de concevoir un système qui peut gérer quelques caractères supplémentaires tels que les caractères diacritiques. (Cela peut généralement être fait en allouant des nombres plus importants, comme 27 à 31, aux autres caractères).

Un clavier français typique possède environ 100 caractères (lettres majuscules et minuscules, ponctuations, chiffres et symboles spéciaux). Combien de bits sont nécessaires pour donner un nombre unique à chaque caractère du clavier ? (En général 7 bits sont suffisants, car ils permettent 128 codes différents).

Demandez maintenant aux élèves d'envisager des alphabets plus grands. Combien de bits sont nécessaires si vous voulez un nombre pour chacun des 50 000 idéogrammes chinois ? (16 bits permettent jusqu'à 65 536 représentations différentes).

{panel type="teaching"}

# Observations pour l'enseignant

Il peut être surprenant que seuls 16 bits soient nécessaires pour des dizaines de milliers de caractères. C'est parce que chaque bit double la quantité, de sorte que vous n'avez pas besoin d'ajouter beaucoup de bits pour couvrir un grand alphabet. Il s'agit d'une propriété importante du codage binaire que les étudiants doivent connaitre.

{panel end}

{panel type="math"}

# Liens mathématiques

L'augmentation rapide du nombre de valeurs différentes qui peuvent être représentés au fur et à mesure que des bits sont ajoutés est une croissance *exponentielle* c'est à dire qu'elle double à chaque bit supplémentaire. Après avoir doublé 16 fois, nous pouvons représenter 65 536 valeurs différentes, et 20 bits peuvent représenter plus d'un million de valeurs différentes. La croissance exponentielle est parfois illustrée par le pliage d'un papier en deux, et à nouveau en deux. Après ces deux plis, on a une épaisseur de 4 feuilles, et un seul pli de plus donne une épaisseur de 8 feuilles. 16 plis font une épaisseur de 65 536 feuilles ! En fait, environ 6 ou 7 plis sont déjà impossibles, même avec une grande feuille de papier.

{panel end}

{panel type="teaching"}

# Observations pour l'enseignant

L'utilisation d'un code de 5 bits pour un alphabet remonte à au moins 1870 (le code "Baudot") ; beaucoup de systèmes de codage de nombres en lettres ont été utilisés au fil des années pour représenter des alphabets, mais celui qui a été utilisé un certain temps s'appelle le code "ASCII", il utilisait 7 bits et donc pouvait représenter plus de 100 caractères différents. À l'heure actuelle, l'"Unicode" est fréquent, il est capable de représenter plus de 100 000 caractères différents. Néanmoins, chacun de ces codes, y compris Unicode, contient toujours des éléments de code simple utilisé dans cette leçon (1 pour A, 2 pour B, ...). Par exemple, le code ASCII pour "A" est 65 et pour "B" 66, etc. ; si vous calculez les représentations binaires de ces nombres, gardez les 5 bits les plus à droite, vous obtiendrez le code que nous avons utilisé ci-dessus.

{panel end}

## Réflexion sur la leçon

- Quelles sont certaines des raisons pour lesquelles nous n'utilisons pas le système de numération binaire pour notre langue écrite ?
- Comment pensez-vous que les Égyptiens de l'antiquité auraient converti leurs hiéroglyphes en binaire ?
- Qu'avez-vous trouvé difficile au cours de cette leçon ?
- Comment avez-vous surmonté ces défis ?