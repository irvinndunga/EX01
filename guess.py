import random

print("=== Guess the Number ===")
nombre_secret = random.randint(1, 100)
tentatives = 0

while True:
    try:
        choix = int(input("Votre tentative : "))
    except ValueError:
        print("Entrez un nombre entier valide.")
        continue
    tentatives += 1
    if choix < nombre_secret:
        print("Trop petit !")
    elif choix > nombre_secret:
        print("Trop grand !")
    else:
        print(f"Bravo ! Trouve en {tentatives} tentative(s) !")
        break
