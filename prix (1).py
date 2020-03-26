import os
from random import randint

def choix_article() :
    global p, article                                                        #définie l'article et le prix dans le fichier
	
    prix = open("prix.txt", "r")
    ligne_choix= int(randint(1,5))

    for i in range(ligne_choix) :                                               #lecture de toutes les lignes
        ligne = prix.readline()


    ligne_nom = ligne.split()                                                   #lit les mots de la ligne et recupère dans une variable
    p, article = int(ligne_nom[1]), ligne_nom[0]



def joueur():
    global joueur_1, joueur_2, joueur_3
    joueur_1 = input("Nom du joueur 1\n")
    joueur_2 = input("Nom du joueur 2\n")
    joueur_3 = input("Nom du joueur 3\n")

def estimation() :
	global a,b,c
	print("Donner le prix de l'article :", article)
	a = int(input("joueur 1 : "))
	b = int(input("joueur 2 : "))
	c = int(input("joueur 3 : "))



def jeu() :
    choix_article()
    estimation()

    if a<=p and b<=p and c<=p:														#Désigne le gagnant
        if a<b<c or b<a<c : print("C'est ",joueur_3, " qui gagne")
        elif b<c<a or c<b<a : print("C'est ",joueur_1, " qui gagne")
        elif c<a<b or a<c<b : print("C'est ",joueur_2, " qui gagne")

    elif a<=p and b<=p :
        if a<b :
            print("C'est ",joueur_2, " qui gagne")
        else : print("C'est ",joueur_1, " qui gagne")

    elif b<=p and c<=p :
            if b<c :
                print("C'est ",joueur_3, " qui gagne")

            else : print("C'est ",joueur_2, " qui gagne")

    elif a<=p and c<=p :
            if a<c :
                print("C'est ",joueur_3, " qui gagne")
            else : print("C'est ",joueur_1, " qui gagne")


    elif a<=p and b>=p and c>=p : print("C'est ",joueur_1, " qui gagne")

    elif a>=p and b<=p and c>=p : print("C'est ",joueur_2, " qui gagne")

    elif a>=p and b>=p and c<=p : print("C'est ",joueur_3, " qui gagne")
    elif a>=p and b>=p and c>=p : print("Personne à gagné")


joueur()
jeu()                                                                           #Lancement du jeu et demande de rejouer
r = int(input("Voulez vous rejouer ?(Taper 1 pour oui ou 0 pour non)"))
while r==1 :
    jeu()
    r = int(input("Voulez vous rejouer ?(Taper 1 pour oui ou 0 pour non)"))
print("Fin du programme")
