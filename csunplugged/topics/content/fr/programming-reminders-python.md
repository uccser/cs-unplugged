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
# Print numbers 0-9 - remember Python starts counting from 0 
for num in range(10):
    print(num)
```

#### While loops

```Python
# Print numbers 0-9 using a while loop and a variable
num = 0
while num < 10:
    print(num)

    # Increment the variable by one.
    # It will prevent an infinite loop!
    num += 1 
```

#### Lists

```Python
# Create a list of fruit 
fruit = ["Apple", "Banana", "Orange", "Pear"]
```

#### Functions

```Python
# Create a function which prints a greeting
def greeting(name):
    print("Hello " + name)

# Call the function
greeting("Spiderman")
```
