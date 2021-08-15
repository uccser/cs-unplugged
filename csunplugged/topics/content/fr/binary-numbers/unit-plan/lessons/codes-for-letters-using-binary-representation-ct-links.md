{panel type="ct-algorithm"}

# Pensée algorithmique

Nous avons utilisé deux algorithmes dans cette leçon : un pour convertir une lettre en un nombre décimal, puis en un nombre binaire, et vice versa. On les appelle des algorithmes car ce sont des processus pas-à-pas qui donneront toujours le bon résultat quels que soient les paramètres fournis en entrée, tant que ces processus sont appliqués correctement.

Voici un algorithme pour la conversion d'une lettre en un nombre décimal :

Choisissez une lettre à convertir en un nombre décimal. Trouvez le numéro de la lettre dans l'alphabet comme suit :

- Disons « A » (la première lettre de l’alphabet)
- Disons « 1 » (le premier nombre dans notre séquence de nombres) 
    - Répétez les instructions suivantes jusqu'à ce que vous arriviez à la lettre que vous cherchez à convertir 
        - Dites la lettre suivante dans l'alphabet
        - Dites le nombre suivant (en ajoutant 1 au précédent)
- Le nombre que vous venez de dire est le nombre décimal correspondant à votre lettre convertie.

Par exemple, pour convertir la lettre E, l'algorithme vous ferait compter ainsi : A,1 ; B,2 ; C,3 ; D,4 ; E,5.

{image file-path="img/topics/binary_count_girl.png" alt="Fille réfléchissant à l'algorithme" alignment="right"}

(Un algorithme plus efficace serait d'avoir une table d'équivalence, comme celle créée au début de l'activité, et la plupart des langages de programmation peuvent convertir directement des lettres en nombres, à l'exception notable de Scratch, qui a besoin d'utiliser l'algorithme ci-dessus.)

L'algorithme suivant est le même algorithme que celui utilisé dans la leçon 1, qui nous servait à convertir un nombre décimal en nombre binaire :

- Trouvez le nombre de points à afficher. (Nous nous référerons à "le nombre de points restants" qui, initialement, est le nombre total devant être affiché.)
- Pour chaque carte, de la gauche vers la droite (c'est à dire 16, 8, 4, 2, 1) : 
    - Si le nombre de points sur la carte est plus grand que le nombre de points restants : 
        - Cachez la carte
    - Sinon : 
        - Montrez la carte
        - Soustrayez le nombre de points sur la carte du nombre de points restants

#### Exemples de ce que vous pourriez observer :

Demandez aux élèves de créer des instructions pour la conversion d'une lettre dans un nombre décimal (avec ou sans la table) ou d'en faire une démonstration, puis de convertir un nombre décimal en binaire ; sont-ils en mesure de trouver une solution valable pour tous les cas ? Peuvent-ils expliciter ce qu'ils font à chaque étape et pourquoi ?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

Cette activité est particulièrement pertinente concernant l'abstraction, puisque nous représentons du texte écrit avec un simple nombre, et ce nombre peut être représenté à l'aide de chiffres binaires, qui, comme nous le savons depuis la leçon 1, sont une abstraction de l'électronique physique et des circuits à l'intérieur d'un ordinateur. Nous pourrions également élargir notre abstraction parce que nous pourrions utiliser deux symboles autres que des 0 et des 1 pour représenter notre message (bien que nous vous recommandons de rester sur les 1 et les 0 pour les élèves qui voient cette notion pour la première fois). Par exemple, vous pourriez représenter votre message par le clignotement d'une lampe torche (ce qui donne une idée de la façon dont les informations peuvent être envoyées sur un câble à fibre optique !), ou par le tracé d'une ligne de carrés et de triangles sur le tableau blanc.

{image file-path="img/topics/binary_torch.png" alt="Lampe torche" alignment="right"}

L'abstraction permet de nous simplifier les choses parce que nous pouvons ignorer les détails que nous n'avons pas besoin de connaitre. La représentation du nombre binaire est une abstraction qui masque la complexité de l'électronique et du matériel à l'intérieur d'un ordinateur qui stocke les données. Les lettres sont une abstraction que l'homme peut comprendre rapidement ; parler de la lettre H est généralement plus significatif que de l'appeler "la 10e lettre de l'alphabet", et quand nous lisons ou parlons, nous n'avons pas besoin de savoir que c'est la 10e lettre de toute façon.

#### Exemples de ce que vous pourriez observer :

Lorsque vous utilisez différentes représentations pour le binaire, telles que l'activation de la lampe torche, quels sont les étudiants qui voient vite que c'est l'équivalent de l'activité où ils ont utilisé des 0 et des 1 ? Ils vont probablement se sentir à l'aise pour travailler avec cette nouvelle représentation rapidement, tandis que d'autres élèves peuvent être très dérangés par ce changement. Cherchez les élèves qui décident de créer leurs propres représentations de nombres binaires.

{panel end}

{panel type="ct-decomposition"}

# Décomposition

Le principal exemple de décomposition dans cette activité est de comprendre qu'en informatique nous devons décomposer toute information en petits morceaux pour que les ordinateurs puissent stocker et envoyer ces données sous forme de bits et d'octets. Tout ce que nous stockons à l'intérieur d'un ordinateur et voyons apparaitre sur l'écran doit avoir été, d'une façon ou d'une autre, décomposé en chiffres binaires.

Dans cette leçon, les élèves ont effectué plusieurs étapes de décomposition en codant un message et en le décomposant en étapes simples. Pour écrire un message en binaire, nous devons d'abord regarder le message une lettre à la fois et les convertir une par une, en nombres décimaux, et ensuite convertir chacun de ces nombres, un par un, en nombres binaires. Les élèves effectuent ces étapes dans l'ordre inverse pour convertir de nouveau le message en texte.

#### Exemples de ce que vous pourriez observer :

Les élèves peuvent-ils expliquer pourquoi il est important que nous puissions utiliser le binaire pour représenter des lettres ? Demandez-leur pourquoi il est utile de choisir une valeur de nombre (binaire ou décimal) représentant chaque lettre, plutôt que de choisir une valeur de nombre représentant chaque mot.

{panel end}

{panel type="ct-pattern"}

# Généralisation et modèles

Reconnaître des motifs dans le fonctionnement du système de numération binaire nous aide à mieux comprendre les concepts impliqués et nous aide à généraliser ces concepts et ces motifs afin de les appliquer à d'autres problèmes.

#### Exemples de ce que vous pourriez observer :

Demandez aux élèves de décoder le message binaire d'un autre élève, par la conversion des nombres binaires en nombres décimaux, et ensuite en texte pour afficher le message. Demandez-leur ce qu'ils feraient s'ils voulaient inclure d'autres caractères dans leur message : que faire si nous voulions des lettres majuscules et minuscules ? Que faire si nous voulons utiliser le point d'exclamation ou d'interrogation ? Observer quels élèves trouvent qu'on peut généraliser la méthode qu'ils utilisent déjà et faire correspondre à d'autres caractères de plus grands nombres décimaux, par exemple, a-z peut être 1-26, et A-Z peuvent être 27-52. Si l'on peut représenter 32 caractères différents en binaire avec 5 bits pour chaque caractère, combien en aurions-nous besoin pour 64 caractères ? Quels élèves peuvent voir le motif du binaire et du doublement dans cette situation, et voir que nous avons simplement besoin d'utiliser 1 bit de plus pour ce faire?

{panel end}

{panel type="ct-logic"}

# Logique

La pensée logique implique de prendre des décisions fondées sur les connaissances que vous avez, et ces décisions doivent être raisonnable et bien pensées. Si vous mémorisez que la lettre H est représentée par 01010 en binaire, ce n'est pas aussi utile que d'apprendre à représenter n'importe quel caractère à l'aide de la procédure décrite dans cette activité. Si vous pouvez comprendre la logique des étapes que vous suivez pour convertir une lettre en un nombre binaire, et comment vous pouvez convertir dans l'autre sens, alors vous serez en mesure de représenter n'importe quel caractère binaire, et plus important encore, vous comprendrez le processus, puisque que vous le ferez certainement faire à un ordinateur plutôt que de le faire vous-même à la main. Ceci est particulièrement vrai si vous voulez représenter un grand nombre de caractères. Que faire si nous voulions représenter chaque caractère chinois ? Il en existe plus de 50 000, donc essayer de les mémoriser tous pourrait prendre un certain temps ! Lorsque nous choisissons d'utiliser les nombres décimaux pour chacune des lettres, nous n'avons pas à choisir de 1 à 26, on aurait pu décider de commencer plutôt à 17 et aller de 17 à 42, ou bien nous pourrions avoir choisi des nombres complètement au hasard ! Que se passerait-il si nous décidions que A = 82, B = 5, C = 42, ... Serait-ce une décision logique à prendre ? 1 à 26 c'est beaucoup plus logique, parce que c'est beaucoup plus facile à décrire et à mémoriser.

#### Exemples de ce que vous pourriez observer :

Observez les systèmes que les élèves ont créés pour traduire leurs lettres en binaire et vice-versa. Quelle logique a-t-elle été appliquée ? Ces systèmes sont-ils efficaces ? Peuvent-il expliquer ce qu'ils font à chaque étape ? Demandez aux élèves pourquoi nous utilisons les nombres de 1 à 26 pour représenter nos lettres, ou s'ils pensent qu'il pourrait y avoir un meilleur choix. Demandez-leur comment ils choisiraient les nombres pour les autres caractères, par exemple un nombre pour représenter une espace. Lesquels donnent des réponses logiques et peuvent expliquer pourquoi leur solution est un bon choix ?

{panel end}

{panel type="ct-evaluation"}

# Évaluation

Un exemple d'évaluation est de travailler sur la façon dont beaucoup de caractères différents peuvent être représentés par un nombre donné de bits. Par exemple 5 bits peuvent représenter 26 caractères confortablement, mais 16 bits sont nécessaires pour une langue avec 50 000 caractères. Lorsque vous pensez à combien de bits doivent être utilisés pour représenter quelque chose, les chercheurs en informatique doivent aussi réfléchir à la quantité d'espace que cela prendra dans un ordinateur (les caractères de 16 bits prennent deux fois plus d'espace que les caractères 8 bits), et si nous devrions utiliser des bits supplémentaires au cas où nous voudrions ajouter plus de caractères dans le futur. Évaluer les bénéfices et les coûts de l'utilisation d'un certain nombre de bits est également une idée que les élèves peuvent explorer.

#### Exemples de ce que vous pourriez observer :

Un élève peut-il déterminer combien de bits sont nécessaires pour représenter les caractères dans une langue qui en compte 100 ? (7 bits sont nécessaires) Comment représenter les émoticônes, lorsque vous avez au bas mot 4 000 émoticônes disponibles (12 bits seront nécessaires pour chacun).

{panel end}