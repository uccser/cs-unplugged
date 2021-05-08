# Représentation d'image

{panel type="text"}

# Connaissances préalables

Les élèves doivent avoir terminé le Cours 1 (pour le groupe d'âge concerné) du module [Nombres Binaires]('topics:unit_plan' 'binary-numbers' 'unit-plan') avant de commencer ce module.

{panel end}

Les images sont partout dans les ordinateurs et autres appareils numériques. Si vous pensez à tous les différents appareils que vous utilisez, et ce que vous faites avec, il est probable que presque tout implique un écran ou un affichage quelconque ! Tout ce que vous voyez sur des écrans d'ordinateur, que ce soit des photos, vidéos, sites web, ou même du texte, sont des images que l'appareil numérique a été programmé pour afficher. Parce que les ordinateurs stockent les données sous forme de nombres, les images sont en fait représentées à l'intérieur d'un ordinateur en utilisant des 0 et des 1.

{comment Add teaching this in action video here}

{panel type="text"}

# Note de terminologie

Dans ce module et les cours le mot **image** se réfère à ce qui est affiché sur l'écran d'un ordinateur ou un affichage à tout moment. Cela inclue tout ce qui est vu à l'écran, comme des vidéos, des sites web, des applications, du texte, plutôt que seulement une image statique ou une photo.

{panel end}

Les écrans d'ordinateurs sont divisés en une grille de minuscules carrés appelés {glossary-link term="pixel"}pixels{glossary-link end}. Chaque pixel peut afficher une couleur différente, et parce qu'ils sont si petits nous ne voyons pas chaque pixel individuellement sur un écran — nous voyons à la place tous les pixels qui se mélangent pour former une image. Si vous regardez un écran d'ordinateur ou une télévision (en particulier les plus anciens) très très proche alors vous pourriez être capable de voir ces pixels individuels.

Les chiffres stockés dans un ordinateur indiquent à chacun de ces pixels de quelle couleur ils doivent être et quand ils doivent changer de couleur, ce qui signifie que les ordinateurs peuvent transformer un tas de chiffres binaires (bits) d'apparence aléatoires en toutes ces belles images que nous voyons sur nos écrans.

Il existe de nombreuses méthodes différentes que nous pouvons utilisez pour convertir des images en données numériques, puis de nouveau en images. La méthode que nous choisissons dépend du type d'image dans lequel les données doivent être converties. Une image en noir et blanc, où chaque pixel ne peut être que noir ou blanc, est beaucoup plus simple à représenter en utilisant des chiffres qu'un film entier, en couleur, et haute définition ! Dans ce module les élèves sont initiés à des exemples simples de la façon dont ils peuvent utiliser des chiffres pour créer des images, comment le nombre de couleurs qu'une image peut avoir est basé sur le nombre de bits utilisés pour stocker l'image, et comment les images peuvent être compressées pour qu'elles prennent moins de place en mémoire.

## Technologies numériques | Représentation des données

Toutes les données dans les ordinateurs sont représentées par des chiffres, et l'utilisation de ces chiffres pour représenter d'autres types de données et d'information est un concept fondamental de l'Informatique. À ce stade, vous avez probablement remarqué que les mots **représenter** et **représentation** sont beaucoup utilisés, voyons exactement ce que nous entendons par là.

{image file-path="img/topics/binary-picture-showing-bits.png" alt="Si nous regardons de plus près une image sur un écran d'ordinateur nous pouvons voir qu'elle est composée d'une grille de minuscules points appelés pixels. La couleur de chacun d'entre eux est stockée dans un ordinateur en binaire."}

La façon dont un ensemble de chiffres **représente** une information change la façon dont nous l'interprétons. Par exemple, si un ensemble de chiffres représente une image alors nous interprétons ces chiffres comme les couleurs des différents pixels. Par contre, si l'ensemble est censé être un texte nous interprétons les chiffres comme des caractères. La capacité des ordinateurs à représenter plusieurs types d'information en utilisant uniquement des chiffres binaires est l'une des choses qui les rendent si puissants. Les ordinateurs utilisent des informations supplémentaires, telles que les extensions de fichiers comme `.txt` ou `.gif` pour montrer comment les données doivent être interprétées et traitées.

Tout comme apprendre le système binaire, explorer la représentation d'image familiarise les élèves aux concepts de Pensée Informatique que sont l'Abstraction et la Décomposition. Les élèves apprennent à découper des images en pixels et ensuite en chiffres, et comment remonter des chiffres aux pixels, puis aux images.

## Technologies Numériques | Algorithmes

Lorsque les pixels sont utilisés pour représenter des images, le processus que nous utilisons pour convertir les chiffres en ces pixels est un type d'algorithme. Si une image a été compressée pour économiser de l'espace, des algorithmes sont nécessaires pour décompresser ... Il existe de nombreux d'algorithmes différents que les ordinateurs utilisent pour faire cela, et ceux qu'ils utilisent dépendent de choses comme le type de fichier des images à afficher, par exemple si c'est une image `.png` ou `.jpeg`, ou un fichier vidéo comme `.mp4` ou `.avi`, ou de la résolution de l'image. Nous utilisons aussi des algorithmes pour compresser des images vers des tailles plus petites, ce qui signifie qu'elles utilisent moins de mémoire et sont plus rapides à télécharger et à copier. Par l'apprentissage de la représentation d'image les élèves pratiquent la pensée algorithmique, la correspondance de modèles, et la pensée abstraite.

## Explication du Vocabulaire

### Pixel

Les écrans d'ordinateur sont divisés en une grille de minuscules carrés colorés, appelés pixels. La couleur de chaque pixel peut être réglée par un ordinateur et est utilisée pour afficher des images sur un écran d'ordinateur. Le mot pixel est l'abréviation de *picture element*.

### Résolution d'affichage

La résolution d'un écran fait référence au nombre, ou à la densité, de pixels à l'écran. Elle est généralement définie soit comme le nombre de pixels par pouce sur l'écran, ou la largeur et la hauteur de l'écran mesurées en pixels. Par exemple, une résolution d'écran commune est de 1920 par 1080 pixels (désignée comme 1080p), ce qui signifie qu'elle a 2 073 600 pixels, un peu plus de 2 millions de pixels !

## Implications dans le monde réel

La façon dont les images sont représentées numériquement affecte la façon dont elles sont affichées, créées, stockées et manipulées. Plus nous utilisons de bits (chiffres binaires) pour stocker la couleur d'un pixel, plus grande est la variété de couleurs que nous pouvons faire. Si nous utilisons un bit pour stocker la couleur d'un pixel, alors nous n'avons que deux options pour ce que cette couleur peut être (souvenez-vous, avec un bit nous ne pouvons représenter que deux valeurs différentes, car nous ne pouvons utiliser que 0 ou 1). Si nous utilisons 8 bits (1 octet) par pixel, nous pouvons afficher 256 couleurs différentes à la place, et si nous utilisons 24 bits (3 octets) alors nous pouvons afficher plus de 16 millions de couleurs différentes, ce qui est plus que ce que l'œil humain peut discerner.

Cependant, utiliser plus de bits pour représenter une couleur augmentera la taille d'un fichier image. Ça signifie que cela prendra plus d'espace en mémoire, plus de temps pour qu'un ordinateur puisse traiter et afficher, et plus de temps pour être transmis entre ordinateurs et sur Internet. Les cinéastes doivent utiliser des ordinateurs puissants et stocker de grandes quantités de données lorsqu'ils modifient leurs vidéos, sinon il leur faudrait beaucoup trop de temps pour le faire, ou alors ils devraient diminuer la qualité d'image de leurs films. C'est aussi la raison pour laquelle les vieux ordinateurs ne peuvent pas toujours lancer de nouveaux jeux ; les anciens ordinateurs ne peuvent tout simplement pas traiter les graphismes du jeu assez rapidement pour les afficher.

Pour certains types d’images, nous pouvons utiliser un algorithme de {glossary-link term="compression"}compression{glossary-link end} pour diminuer la taille de leur fichier. Les algorithmes de compression peuvent le faire sans perdre ou perdre une petite partie de la qualité de l'image. Les algorithmes de compression d'images nous permettent de stocker, de traiter, de transmettre et de créer des images plus rapidement.

## Questions pour réfléchir

- Qu'est-ce qui a été le plus surprenant dans l'apprentissage de ce module ?
- Quels étaient les élèves très méthodiques dans leurs activités ?
- Quels étaient les élèves très minutieux dans leurs activités ?
- Que changerais-je dans ma façon d'enseigner ce module ?