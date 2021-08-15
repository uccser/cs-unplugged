{panel type="ct-algorithm"}

# Pensée algorithmique

Nous avons utilisé plusieurs algorithmes dans cette leçon : un pour convertir une lettre en un nombre décimal, puis en un nombre binaire, et vice versa. On les appelle des algorithmes car ce sont des processus pas-à-pas qui donneront toujours le bon résultat quels que soient les paramètres fournis en entrée, tant que ces processus sont appliqués correctement.

Voici un algorithme pour convertir une lettre en un nombre décimal :

Choisissez une lettre à convertir en un nombre décimal. Trouvez le numéro de la lettre dans l'alphabet comme suit :

- Dites « A » (la première lettre de l'alphabet)
- Dites « 1 » (le premier nombre de notre suite de nombres) 
    - Répétez les instructions suivantes jusqu'à arriver à la lettre que vous cherchez à convertir 
        - Dites la lettre suivante dans l'alphabet
        - Dites le nombre suivant (en ajoutant 1 au précédent)
- Le nombre que vous venez de dire est le nombre décimal correspondant à votre lettre convertie.

Par exemple, pour convertir la lettre E, l'algorithme vous ferait compter ainsi : A,1 ; B,2 ; C,3 ; D,4 ; E,5.

{image file-path="img/topics/binary_count_girl.png" alt="Fille pensant à l'alphabet et aux nombres" alignement="right"}

(Un algorithme plus efficace serait d'avoir une table d'équivalence, comme celle créée au début de l'activité, et la plupart des langages de programmation peuvent convertir directement des lettres en nombres, à l'exception notable de Scratch, qui a besoin d'utiliser l'algorithme ci-dessus.)

L'algorithme suivant est le même algorithme que celui utilisé dans la leçon 1 qui nous servait à convertir un nombre décimal en nombre binaire :

- Trouvez le nombre de points à afficher. (Nous l'appellerons "le nombre de points restants" qui, initialement, est le nombre total devant être affiché.)
- Pour chaque carte, à partir de la gauche vers la droite (c'est à dire 16, 8, 4, 2 puis 1) : 
    - Si le nombre de points sur la carte est plus grand que le nombre de points restants : 
        - Cachez la carte
    - Sinon : 
        - Montrez la carte
        - Soustrayez le nombre de points sur la carte du nombre de points restants

#### Exemples de ce que vous pourriez observer :

Les élèves peuvent-ils créer des instructions pour convertir une lettre en un nombre décimal, ou bien en faire la démonstration, puis convertir un nombre décimal en binaire ; sont-ils en mesure de montrer une solution systématique?

{panel end}

{panel type="ct-abstraction"}

# Résumé

Cette activité est particulièrement pertinente concernant l'abstraction, puisque nous représentons du texte écrit avec un simple nombre, et ce nombre peut être représenté à l'aide de chiffres binaires, qui, comme nous le savons depuis la leçon 1, sont une abstraction de l'électronique physique et des circuits à l'intérieur d'un ordinateur. Nous pourrions également élargir notre abstraction parce que nous ne sommes pas obligés d'utiliser des 0 et des 1 pour représenter notre message. On peut utiliser n'importe quelle paire de valeurs, par exemple, vous pouvez représenter votre message par le clignotement d'une lampe torche, ou le tracé d'une ligne de carrés et de triangles sur le tableau blanc.

{image file-path="img/topics/binary_torch.png" alt="Lampe torche" alignment="right"}

L'abstraction permet de nous simplifier les choses parce que nous pouvons ignorer les détails que nous n'avons pas besoin de connaitre. Représenter un nombre binaire est une abstraction qui masque la complexité de l'électronique et du matériel à l'intérieur d'un ordinateur qui stocke les données. Les lettres sont une abstraction que l'homme peut comprendre rapidement ; parler de la lettre H est généralement plus significatif que de l'appeler "la 10e lettre de l'alphabet", et quand nous lisons ou parlons, nous n'avons pas besoin de savoir que c'est la 10e lettre de toute façon.

#### Exemples de ce que vous pourriez observer :

Demandez aux élèves de créer ou de faire démonstration de nouvelles instructions pour expliquer comment représenter de nouveaux éléments de langue, comme une virgule.

{panel end}

{panel type="ct-pattern"}

# Généralisation et motifs

La reconnaissance de motifs dans le fonctionnement du système de numération binaire nous aide à mieux comprendre les concepts à l’œuvre et nous aide à généraliser ces concepts et motifs afin de pouvoir les appliquer à d'autres problèmes.

#### Exemples de ce que vous pourriez observer :

Demandez aux élèves de décoder le message binaire d'un autre élève, en convertissant les nombres binaires en texte pour afficher le message. Peuvent-ils reconnaître des motifs dans le code binaire pour anticiper ce qu'est le mot ? Peuvent-ils travailler avec un ensemble différent de lettres en utilisant les mêmes principes ?

{panel end}

{panel type="ct-logic"}

# Logique

La pensée logique signifie reconnaître la logique que vous utilisez pour comprendre ces choses. Si vous mémorisez la façon de représenter la lettre H en binaire par 01010, ce n'est pas une méthode aussi généralement applicable qu'apprendre la logique qui permet à n'importe quel caractère d'être représenté par le processus décrit dans cette activité.

#### Exemples de ce que vous pourriez observer :

Observez les systèmes que les élèves ont créés pour traduire leurs lettres en binaire et vice versa. Quelle logique a été appliquée à ces systèmes ? Est-ce que ces systèmes sont efficaces ?

{panel end}

{panel type="ct-decomposition"}

# Décomposition

Un exemple de décomposition est de casser un long message comme 00001000100001011001 en morceaux de 5 bits (00001 00010 00010 11001), chacun peut maintenant être converti en lettre. Les morceaux de 5 bits sont ensuite décomposés en la valeur des bits individuels.

#### Exemples de ce que vous pourriez observer :

Les élèves peuvent-ils convertir un message codé sans espaces ?

{panel end}

{panel type="ct-evaluation"}

# Évaluation

Un exemple d'évaluation est de déterminer combien de caractères différents peuvent être représentés par un nombre donné de bits (par exemple, 5 bits peuvent représenter confortablement 26 caractères, mais 6 bits sont nécessaires si vous avez besoin de plus de 32 caractères, et 16 bits sont nécessaires pour une langue de 50 000 caractères).

#### Exemples de ce que vous pourriez observer :

Un élève peut-il déterminer combien de bits sont nécessaires pour représenter les caractères dans une langue comportant 50 caractères ? (6 bits sont nécessaires) Et comment représenter les émoticônes, si vous avez environ 10 émoticônes disponibles ? (10 bits seront nécessaires pour chacun).

{panel end}