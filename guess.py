import random

print("=== Guess the Number ===")
nombre_secret = random.randint(1, 100)
tentatives = 0
MAX = 7

while tentatives < MAX:
    try:
        choix = int(input(f"Tentative {tentatives+1}/{MAX} : "))
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
else:
    print(f"Perdu ! Le nombre etait {nombre_secret}.")
