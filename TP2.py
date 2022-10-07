"""
Évangéline Pourbaix
Gr:402
TP2- jeu de devinettes
"""
from random import *

chiffre_choisit = randint(0, 5)

boucle_jeu = True
while boucle_jeu:
    numero_joue = int(input("J'ai choisi un nombre entre 0 et 5. À vous de le deviner"))
    if numero_joue == chiffre_choisit:
        fin_jeu = str(input("C'est le bon numéro, voulez-vous rejouer (oui/non)?"))
        if fin_jeu == "oui":
            boucle_jeu = True
        elif fin_jeu == "non":
            boucle_jeu = False
    if numero_joue > chiffre_choisit:
        print("Le chiffre est plus petit, réessayez")
    elif numero_joue < chiffre_choisit:
        print("Le chiffre est plus grand, réessayez")
