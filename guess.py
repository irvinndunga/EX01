# Guess the Number - branch2
# Fonctionnalites : limite de tentatives, progression, validation saisie
import random

MAX_TENTATIVES = 7

def jouer():
    print("=== Guess the Number ===")
    print(f"Trouvez le nombre entre 1 et 100 en {MAX_TENTATIVES} essais.")
    nombre_secret = random.randint(1, 100)
    tentatives = 0

    while tentatives < MAX_TENTATIVES:
        restantes = MAX_TENTATIVES - tentatives
        print(f"[{restantes} chance(s) restante(s)]")
        saisie = input(f"Tentative {tentatives+1}/{MAX_TENTATIVES} : ")

        if not saisie.isdigit():
            print("Entrez un nombre entier positif.")
            continue

        choix = int(saisie)
        tentatives += 1

        if choix < nombre_secret:
            print("Trop petit !")
        elif choix > nombre_secret:
            print("Trop grand !")
        else:
            print(f"Bravo ! Trouve en {tentatives} tentative(s) !")
            return

    print(f"Perdu ! Le nombre etait {nombre_secret}.")

jouer()
