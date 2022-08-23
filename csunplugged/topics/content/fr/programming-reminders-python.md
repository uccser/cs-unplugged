# Rappels de programmation

#### Affichage

```python3
# Afficher directement une chaîne de caractères
print("Hello World!")

# Afficher une variable
print(ma_var)
```

#### Variables

```Python
# Déclarer une chaîne de caractères
nom_fruit = "Pomme"

# Déclarer un entier
parts_de_fruit = 7

# Déclarer une variable à partir d'un calcul
prix_fruit = parts_de_fruit * prix_par_unite

# Ajouter un à une valeur
parts_de_fruit += 1
```

#### Conditions

```Python
# Trouver la remise sur un fruit
if parts_de_fruit > 100:
    print("Remise en gros")
elif parts_de_fruit > 5:
    print("Simple remise")
else:
    print("Pas de remise")
```

#### Boucles for

```Python
# Afficher les nombres de 0 à 9 - N'oubliez pas que Python commence à compter à partir de 0
for nombre in range(10):
    print(nombre)
```

#### Boucles while

```Python
# Afficher les nombres de 0 à 9 en utilisant une boucle while et une variable
nombre = 0
while nombre < 10:
    print(nombre)

    # Incrémenter la variable de 1
    # Cela évite une boucle infinie !
    nombre += 1 
```

#### Listes

```Python
# Crée une liste de fruits
fruit = ["Pomme", "Banane", "Orange", "Poire"]
```

#### Fonctions

```Python
# Crée une fonction qui affiche une salutation
def salutation(nom):
    print("Bonjour", nom)

# Appel de la fonction
salutation("Spiderman")
```
