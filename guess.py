# Jeu : Devinez le nombre secret
import random

print("=== Guess the Number ===")
print("Je pense a un nombre entre 1 et 100.")

nombre_secret = random.randint(1, 100)
choix = int(input("Votre tentative : "))

if choix < nombre_secret:
    print("Trop petit !")
elif choix > nombre_secret:
    print("Trop grand !")
else:
    print("Bravo ! Vous avez trouve !")
