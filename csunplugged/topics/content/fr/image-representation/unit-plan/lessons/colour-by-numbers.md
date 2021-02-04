# Couleur par les nombres

## Questions clé

- Comment pensez-vous que les ordinateurs affichent des images sur un écran?
- Comment les ordinateurs stockent-ils des images s'ils ne peuvent mémoriser que des informations sous forme de chiffres ?

## Lancement du cours

Ce cours contient 2 activités : une que les élèves peuvent faire seuls et une activité de groupe. Pour chaque activité, vous aurez besoin de suffisamment de feuilles pour que chaque élève en ait une. Chaque activité nécessite différentes versions des feuilles du Peintre Pixel. Utilisez les couleurs **Noir et Blanc** (la première option de la liste), et :

- Pour la première activité choisissez les images de la page 1 (l'étoile, la tasse de thé, ou le chat). Vous pouvez utiliser une combinaison de ces images, les élèves n'ont pas besoin de tous faire la même,
- Pour la seconde activité, choisissez parmi les images des pages 6, 8 et 9. Imprimez suffisamment d'exemplaires pour que chaque groupe d'élèves possède l'ensemble des images.

{panel type="general"}

# Notes sur les ressources

- Imprimez des copies de chaque feuille de travail au cas où les élèves se trompent et aient besoin d'une nouvelle feuille.
- Utilisez les choix de couleur **Noir et Blanc (2 valeur binaires possibles)**, et **pas** l'option qui dit "en codage par plages".
- Les élèves peuvent utiliser des pastels noirs, un crayon, ou un feutre, mais des crayons effaçables fonctionnent bien mieux la première fois que les élèves font l'activité.

{panel end}

Le professeur à la classe : Les écrans des ordinateurs sont découpés en une grille de petits carrés, chacun pouvant afficher une couleur. On appelle ces carrés "Picture elements", ou pixels.

Écrivez les mots "Picture elements" au tableau. Pour montrer comment nous obtenons le mot pixel, entourez le "pi" de picture et le "el" de elements, et écrivez "pixel" en dessous.

L'enseignant à la classe : Chacun de ces pixels peut être d'une couleur différente, et quand il y en a beaucoup sur un écran, ils forment une image. Quelqu'un a déjà entendu parler de pixels ? Et de megapixels ?

{panel type="general"}

# Observations pour l'enseignant

Megapixel signifie un million de pixels. Les élèves peuvent avoir entendu le terme "megapixel" précédemment car les appareils photos sont souvent décrits par une quantité de megapixels, par exemple un téléphone peut avoir un appareil photo de *12 megapixels*. Cela décrit la résolution des photos que la caméra peut prendre. Une caméra de 12 megapixels peut produire une image contenant 12 millions de pixels.

Les écrans de télé et les projecteurs affichent aussi des images en utilisant des pixels.

{panel end}

L'enseignant à la classe : Chacune des images que l'on voit sur un écran, que ce soit une photo, une vidéo, ou du texte, est affichée en utilisant des pixels, et tout ce qu'un ordinateur a besoin de stocker est la couleur que doit avoir chaque pixel de l'écran.

Montrez les images suivantes aux étudiants sur un écran ou au tableau.

L'enseignant à la classe : Dans une image en noir et blanc, chaque pixel peut être soit noir soit blanc, donc la seule chose que les ordinateurs ont besoin de stocker est quels sont les pixels noirs et quels sont les pixels blancs. Par exemple, si nous voulons afficher la lettre **C**, nous devons commencer par diviser la lettre en carrés. Si on zoome encore plus, on peut observer une grille de pixels similaire à ça :

{image file-path="img/topics/letter-zooming-to-pixels.png" alt="Trois images de la lettre majuscule 'C' sont montrées. Elles zooment progressivement pour montrer les carrés noir et blancs qui forment la lettre à l'écran."}

Nous pouvons représenter cette image en utilisant des chiffres binaires (bits). Si un 1 indique un carré blanc et un 0 un carré noir, alors on peut représenter notre lettre **C**, sur une grille de 5x6 pixels, comme cela :

**10001, 01110, 01111, 01111, 01110, 10001**

Si nous prenons ces nombres et dessinons l'image qu'ils représentent, nous obtenons la lettre **C** :

{image file-path="img/topics/pixel-visible-grid-with-letter-and-numbers.png" alt="Une grille 6x5 est affichée. Certains des carrés sont blancs, d'autres sont noirs, ce qui permet de créer la forme de la lettre 'C'. À la droite de chaque ligne de carrés, il y a 5 chiffres binaires qui décrivent l'image."}

Nous utilisons 1 pour représenter blanc et 0 pour représenter noir, de la même manière que nous avons utilisé les cartes noires et blanches pour représenter 'on' et 'off' dans le module des nombres binaires.

## Activités de la leçon

Donnez la première feuille de travail aux élèves et demandez leur de regarder la grille de carrés. Que remarquent-ils à propos des nombres dans les carrés ? Il sont tous soit 1 soit 0.

L'enseignant à la classe : Les grilles sur ces feuilles représentent les pixels sur un écran d'ordinateur. Maintenant vous allez être l'ordinateur et utiliser les nombres dans les carrés pour faire une image.

Sur les feuilles, demandez aux élèves de colorer chaque carré avec un 0 en noir, et laissez les carrés avec un 1 en blanc. Nous utilisons 1 pour représenter blanc et 0 pour représenter noir, car 1 indique qu'un pixel est 'allumé' (et donc blanc) alors que 0 indique qu'il est 'éteint' (et donc il est noir). En coloriant les carrés 0 durant cette activité, les élèves 'éteignent' ces pixels. Conseillez-leur de colorier légèrement les carrés au début, puis lorsqu'ils sont certains qu'ils n'ont pas fait d'erreur ils peuvent les colorier complètement. Alors qu'ils travaillent sur les feuilles ils devraient voir une image apparaître.

L'enseignant à la classe : Maintenant que nous avons fait des images simples avec nos nombres et nos pixels, nous pouvons essayer d'en faire des plus détaillées et plus dures. Comment pensez-vous que nous pourrions faire des images plus détaillées ?

{panel type="general"}

# Observations pour l'enseignant

Les réponses possibles incluent d'ajouter plus de couleurs. C'est une bonne réponse et les couleurs seront dans des leçons plus avancées de ce cours, mais cette leçon se concentre seulement sur les pixels en noir et blanc, rappelez donc aux élèves cette contrainte et demandez leur comment faire une image plus détaillée en noir et blanc.

Ils peuvent aussi suggérer d'utiliser des pixels plus petits pour la même image. C'est une bonne réponse et cela pourrait être une idée à explorer par les élèves dans un futur cours. Pour le moment, nous cherchons à créer des images plus compliquées et plus détaillées, plutôt que de rendre les précédentes plus détaillées.

{panel end}

La réponse que vous attendez est d'utiliser plus de pixels pour l'image, c'est ce que les élèves vont faire dans la prochaine activité.

Mettez les élèves en groupes et donnez à chaque groupe l'ensemble des images sur plusieurs pages, de sorte que chaque élève ait une page sur laquelle travailler. Si ce n'est pas possible avec le nombre d'élèves que vous avez, assurez-vous que les groupes soient suffisamment petits pour que chaque élève ait au moins une page, ou, de préférence, que chaque élève ait le même nombre de pages. Par exemple, faites travailler les groupes de 3 sur 6 pages, de sorte que chaque élève ait 2 pages à remplir.

L'enseignant à la classe : Ces ensembles de grilles peuvent être combinés pour créer une image plus grande, qui contient bien plus de pixels que les précédentes. Vous allez tous colorier les pixels sur votre propre feuille, comme précédemment, puis assembler l'image complète.

Une fois que les élèves ont colorié leur feuille, il peuvent les assembler pour former l'image complète. Il y a des indications sur les imprimables que les enseignants peuvent utiliser pour aider les élèves à assembler leurs images s'ils sont coincés.

## Appliquer ce que nous venons d'apprendre

- Les élèves peuvent utiliser une grille ou un papier quadrillé pour créer leurs propres images. Demandez aux élèves d'écrire les chiffres binaires qui représentent leur image (de la même façon que le 'C' dans la section de démarrage du cours, au lieu d'écrire les 1 et les 0 dans chacune des cases de la grille), donnez ceci à d'autres élèves, et voyez s'ils peuvent recréer la même image.

- Il y a un certain nombre de sites disponibles que les élèves peuvent utiliser pour créer facilement du pixel art. Ils peuvent créer leur propre pixel art, convertir cela en une grille de chiffres, et ensuite faire en sorte que leurs amis essaient de recréer leur image.

- Maintenant que les élèves ont essayé de créer des images plus grandes, ils pourraient aller plus loin et faire une image en tant que classe entière. L'option Perroquet du Peintre Pixels est composée de 32 pages, et constitue un grand défi pour une classe.

{panel type="general"}

# Notes sur les ressources

Il y a une [grille]('resources:resource' 'grid') de 8 par 8 dans la section des imprimables qui peut être utilisée pour dessiner ces images.

{panel end}

## Réflexion sur la leçon

Cette leçon portait sur les images en noir et blanc; pourquoi ne pouvons-nous pas faire plus de deux couleurs avec cette activité ?

- Avec un chiffre binaire, nous ne pouvons représenter que deux valeurs différentes. Cela signifie que si nous utilisons un chiffre pour représenter la couleur d'un pixel, chaque pixel ne peut être qu'une de deux couleurs différentes.

Que pourrions-nous faire pour représenter plus de couleurs ?

- Si nous voulons que chaque pixel soit capable de montrer plus de couleurs que le noir et le blanc, alors nous devons utiliser plus de nombres (i.e., plus de chiffres binaires) pour représenter la couleur de chaque pixel. Cela sera exploré lors des prochaines leçons.