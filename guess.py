import random

print("=== Guess the Number ===")
nombre_secret = random.randint(1, 100)

while True:
    choix = int(input("Votre tentative : "))
    if choix < nombre_secret:
        print("Trop petit !")
    elif choix > nombre_secret:
        print("Trop grand !")
    else:
        print("Bravo ! Vous avez trouve !")
        break
