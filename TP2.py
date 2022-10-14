"""
Évangéline Pourbaix
Gr:402
TP2- Jeu des devinettes
"""
from random import *

boucle_jeu = True

nb_essais = 1

def borne():
   global nb_minimum
   global nb_maximum

   nb_minimum = int(input("Choisissez le nombre minimal à deviner"))
   nb_maximum = int(input("Choisissez le nombre maximal à deviner"))

while boucle_jeu:
   borne()
   chiffre_choisit = randint(nb_minimum, nb_maximum)

   not_found = True
   while not_found:
       numero_joue = int(input(f"J'ai choisi un nombre entre {nb_minimum} et {nb_maximum}. À vous de le deviner"))
       if numero_joue == chiffre_choisit:
           rejouer = str(input(f"C'est le bon numéro, voulez-vous rejouer (oui/non)? Vous avez réussi en {nb_essais} essais"))
           if rejouer == "oui":
                not_found = True #changer de numéro
           elif rejouer == "non":
               not_found = False
               print("Merci d'avoir joué")
               boucle_jeu = False
       if numero_joue > chiffre_choisit:
           print("Le chiffre est plus petit, réessayez")
           nb_essais += 1
       elif numero_joue < chiffre_choisit:
           print("Le chiffre est plus grand, réessayez")
           nb_essais += 1


