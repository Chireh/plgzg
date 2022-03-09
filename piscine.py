#function.py

#main.py
import datetime
from math import *


#1. Créer une fonction qui demande à l'utilisateur son nom et prénom et affiche un message dans la console.
def function1():
    nom = input("Nom: ")
    prenom = input('Prenom: ')
    print('Voila ton nom et prenom:'+nom+' '+prenom)
#2. Créer une fonction qui demande à l'utilisateur son age et affiche l'année ou il aura 100 ans.
def function2():
    age = int(input("Age: "))
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    annee=(100-age)+int(year)
    if(age<=100):
        print("Vous aurez 100 ans en "+str(annee))
    else:
        print('Vous avez plus de 100')

#3. Écrire un fonction qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.
def function3():
    rayon = int(input('Rayon :'))
    hauteur=int(input('Hauteur :'))
    Base=pi*(rayon*rayon)
    print(Base)
    Volume=(hauteur*Base)/3
    print(Volume)
#4. Ecrire un foncton qui demande à l'utilisateur un nombre et détermine si ce nombre est pair ou impar avec un message d'affichage.
def function4():
    nombre=int(input('Nombre : '))
    if(nombre%2 == 0):
        print('nombre pair')
    else:
        sprint('nombre impair')


#5. Ecrire une fonction qui calcul la suite de fibonnaci pour un rang donnée.
def fibo(n):
    if(n<=1):
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
def function4():          
    nombre=int(input('Nombre : '))
    resultat=fibo(nombre)
    print(resultat)

#6. Ecrire une fonction qui détermine tous les ppcm et pgcd d'un nombre donnée
def function4(): 
    nombre1=int(input('Nombre 1 : '))
    nombre2=int(input('Nombre 2 : '))
    while nombre1!=nombre2: 
        pgcd=abs(nombre2-nombre1) 
        nombre2=nombre1 
        nombre1=pgcd 
    print("pgcd=",pgcd) 
 

#7. Ecrire une fonction qui prend deux liste en paramètres et renvoie tous les elements communs au deux listes
def function5():     
    liste1=[1,3,4,7,9,2]
    liste2=[4,8,2,3,1,3]
    liste3=[]
    for i in liste1:
        for j in liste2:
            if(i==j):
                liste3.append(i) 
                print('i = '+str(i))
                break
 
    for x in liste3:
        print (liste3[x-1])
#8. Ecrire une fonction qui determine si une chaine de caractère est un palyndrome

#palyndrome=int(input('mot : '))

#9. Ecrire une fonction qui enelve tout les doublons d'une liste

#10. Ecrire une fonction qui valide si une adresse IP est valide.

#11. Ecrire un programme qui transcrit un nombre en paramètre en binaire en gardant les 0 devant
#12. La même chose pour l’hexadecimal
#13. Ecrire une fonction Qui trace un carré d’étoile de taille n
#14. Ecrire une fonction qui trace un triangle d’étoile de taille n