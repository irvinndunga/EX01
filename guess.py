import random
nombre_secret = random.randint(1, 100)
choix = int(input("Devinez : "))
if choix < nombre_secret:
    print("Trop petit")
elif choix > nombre_secret:
    print("Trop grand")
else:
    print("Bravo !")
