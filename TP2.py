"""
Évangéline Pourbaix
Gr:402
TP2- jeu des devinettes
"""
from random import *

boucle_jeu = True

def borne_jeu():
    global nb_minimum
    global nb_maximal

    nb_minimum = str(input("Choisissez le nombre minimal à deviner"))
    nb_maximal = str(input("Choisissez le nombre maximal à devniner"))

while boucle_jeu:
    chiffre_choisit = randint(nb_minimum, nb_maximal)

    not_found = True
    while not_found:
        numero_joue = int(input("J'ai choisi un nombre entre 0 et 5. À vous de le deviner"))
        if numero_joue == chiffre_choisit:
            rejouer = str(input("C'est le bon numéro, voulez-vous rejouer (oui/non)?"))
            if rejouer == "oui":
                boucle_jeu = True
            elif rejouer == "non":
                boucle_jeu = False
        if numero_joue > chiffre_choisit:
            print("Le chiffre est plus petit, réessayez")
        elif numero_joue < chiffre_choisit:
            print("Le chiffre est plus grand, réessayez")

