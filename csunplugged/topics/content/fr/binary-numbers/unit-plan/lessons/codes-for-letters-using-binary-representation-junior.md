# Codes pour les lettres utilisant la représentation binaire

## Questions clés

Comment pensez-vous que l'ordinateur sait quelle lettre il doit afficher à l'écran ?

{panel type="teaching"}

# Observations pour l'enseignant

La discussion peut commencer à partir des 26 lettres de l'alphabet occidental, puis s'étendre à d'autres caractères du clavier, y compris les lettres majuscules, les chiffres et les signes de ponctuation. Les élèves savent peut-être que d'autres langues peuvent avoir des milliers de caractères, et l'ensemble des caractères est également en pleine expansion avec l'invention des émoticônes !

{panel end}

## Lancement du cours

{panel type="general"}

# Notes sur les ressources

Il existe également une version interactive en ligne des cartes binaires [ici](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), du [Computer Science Field Guide ](http://www.csfieldguide.org.nz/), mais il est préférable de travailler avec des cartes physiques.

{panel end}

Peut-on faire correspondre les lettres à des nombres pour que nous puissions nous envoyer des messages codés les uns aux autres ?

Combien de lettres y a-t-il dans l'alphabet ? Comptons-les sur nos cartes d'alphabet.

Comment pouvons-nous représenter les lettres à l'aide de nombres ? (Menez les élèves vers l'idée d'utiliser 1 pour A, 2 pour B, et ainsi de suite.)

On peut représenter les nombres à l'aide du binaire, mais dans la dernière leçon avec 4 bits, quel était le plus grand nombre que l'on pouvait représenter ? (15)

Comment peut-on représenter des nombres plus grands ? (Ajoutez une carte). Combien de points sur la carte supplémentaire ? (16)

Distribuez les cartes, et demandez aux élèves de les placer sur la table dans l'ordre correct (16, 8, 4, 2, 1).

Maintenant, donnez-leur un nombre en disant "Non, Oui, Non, Non, Non" pour les 5 cartes. Demandez-leur combien de points apparaissent. (Le "Oui" est pour la carte du 8, donc c'est le nombre 8.) Quelle est la 8e lettre ? ("H"). Vous pouvez l'écrire au tableau.

Maintenant donnez le nombre suivant : "Non, Oui, Non, Non, Oui" (9). Quelle est la 9e lettre ? ("I", qui peut être écrit après le "H".)

C'est le message en entier - "HI" ("Salut").

Essayez maintenant d'envoyer un autre mot à la classe. La ressource [Binaire vers Alphabet]('resources:resource' 'binary-to-alphabet') ci-dessous montre les valeurs binaires pour les 26 lettres de l'alphabet ; vous pouvez utiliser oui/non pour 1/0, mais vous pouvez également utiliser d'autres façons de dire, comme "allumé/éteint", "haut/bas", ou même "un/zéro". En particulier, il peut être utile de représenter un nombre supérieur à 16, pour leur montrer ce que cela donne avec le 5e bit.

{panel type="teaching"}

# Observations pour l'enseignant

Notez que si votre alphabet local est légèrement différent (par exemple, avec des signes diacritiques tels que les macrons ou les accents), vous pouvez adapter le code pour utiliser les caractères communs ; cette question est également examinée ci-après.

{panel end}

# Activités du cours

Voyons comment écrire notre propre code binaire pour "papa".

Vous chantez/dites l'alphabet lentement et je vais compter le nombre de lettres jusqu'à "P" (P est la 16e lettre).

Comment pouvons-nous donc faire 16 à l'aide de code binaire ?

{image file-path="img/topics/binary-4-equals-d.png" alt="Enfants tenant des cartes binaires"}

OUI NON NON NON NON

Vous chantez l'alphabet lentement et je vais compter le nombre de lettres pour aller jusqu'à ‘A’. A est la 1ère lettre.

Donc, comment faisons-nous 1, en utilisant le code binaire?

{image file-path="img/topics/binary-1-equals-a.png" alt="Enfants tenant des cartes binaires"}

NON NON NON NON OUI

Accrochez-vous bien ! N'avons-nous pas déjà écrit le code binaire pour P et A ? Nous pouvons les réutiliser ! Les chercheurs en informatique cherchent toujours des façons de réutiliser le travail qu'ils ont déjà fait avant. C'est beaucoup plus rapide de cette façon.

Maintenant, nous allons essayer cela avec le nom de quelqu'un ? Quel nom voulez-vous traduire en nombres binaires?

Choisissez un élève et parcourez les étapes pour créer son nom.

Pour renforcer la connaissance des élèves sur l'alphabet, on peut traduire tous les noms des élèves en nombres binaires sur un panneau et l'afficher dans la classe.

{panel type="teaching"}

# Observations pour l'enseignant

Certaines langues ont plus ou moins de caractères, et elles peuvent inclure des signes diacritiques tels que les macrons et les accents. Si des élèves posent des questions sur un alphabet avec plus de 32 caractères, alors 5 bits ne seront pas suffisants. Les élèves peuvent aussi se rendre compte qu'un code est nécessaire pour l'espace (le 0 est un bon choix pour cela), donc 5 bits ne couvrent que 31 lettres de l'alphabet.

Un clavier français typique a environ 100 caractères (c'est à dire les lettres majuscules et minuscules, les ponctuations, les chiffres et les symboles spéciaux). Combien de bits sont nécessaires pour donner un nombre unique à chaque caractère du clavier ? (en général 7 bits sont suffisants, car cela permet 128 codes différents).

Demandez maintenant aux élèves d'envisager des alphabets plus grands. Combien de bits sont nécessaires si vous voulez un nombre pour chacun des 50 000 idéogrammes Chinois ? (16 bits permettent jusqu'à 65 536 représentations différentes).

Il peut être surprenant que seulement 16 bits suffisent pour des dizaines de milliers de caractères. C'est parce que chaque bit double la quantité, de sorte que vous n'avez pas besoin d'ajouter beaucoup de bits pour couvrir un grand alphabet. C'est une propriété importante de la représentation binaire avec laquelle les élèves devraient se familiariser.

{panel end}

{panel type="teaching"}

# Observations pour l'enseignant

L'augmentation rapide du nombre de valeurs différentes qui peuvent être représentées au fur et à mesure que des bits sont ajoutés est une croissance exponentielle, c'est-à-dire qu'elle double avec chaque bit supplémentaire. Après avoir doublé 16 fois, nous pouvons représenter 65 536 valeurs différentes, et 20 bits peuvent représenter plus d'un million de valeurs différentes. La croissance exponentielle est parfois illustrée par pliage de papier en deux, puis en deux à nouveau. Après ces deux plis, la feuille est 4 fois plus épaisse, et un seul pli de plus fait une épaisseur de 8 feuilles. 16 plis font une épaisseur de 65 536 feuilles ! En fait, environ 6 ou 7 plis sont déjà impossibles, même avec une grande feuille de papier.

{panel end}

## Réflexion sur la leçon

- Quelles sont les raisons pour lesquelles nous n’utilisons pas le système de nombres binaires comme représentation pour notre langue écrite ?
- Qu'avez-vous trouvé difficile pendant cette leçon ?
- Comment avez-vous réussi à surmonter ces défis ?