# Jeu : Devinez le nombre secret
import random

# Génération du nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)

# Demande à l'utilisateur de deviner
choix = int(input("Devinez : "))

# Comparaison et affichage du résultat
if choix < nombre_secret:
    print("Trop petit")
elif choix > nombre_secret:
    print("Trop grand")
else:
    print("Bravo !")
