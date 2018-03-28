#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonction lié au texte et a l'affichage

from upemtk import *
import random
import time
import sys

__all__ = ['get_arguments', 'demarage_horloge','affichage_temps_score','perdu','gagne','victoire','gagne2']

def get_arguments():
	"""
        renvoie les parametres mis en ligne de commande sous forme de liste
        """
	if not sys.argv[1:]:
		raise AssertionError
	return sys.argv[1:]


def demarage_horloge():
    """
    cqfd
    """
    time.clock()

def affichage_temps_score(score,nomstage,vie,highscore):
    """
    Affiche le temps et le score
    """
    valeur = time.clock()
    heure = int(valeur // 3600)
    minute = int(valeur % 60)
    seconde = int(valeur % 60)
    print("{0}:heure(s), {1}:minute(s), {2}:seconde(s) / score: {3} / stage: {4} / vie: {5} / highscore: {6}              ".format(heure,minute,seconde,score,nomstage,vie,highscore), end="\r")
    timer2=time.time()


def perdu(Fenetre_largeur,Fenetre_hauteur):
    """
    Affiche le message perdu au centre de l'ecran
    """
    texte(Fenetre_largeur//2,Fenetre_hauteur//2,"Perdu!","red","center")
    attente_touche()
    

def gagne(Fenetre_largeur,Fenetre_hauteur):
    """
    Affiche le message gagne au centre de l'ecran
    """
    texte(Fenetre_largeur//2,Fenetre_hauteur//2,"Gagné!","red","center")
    attente_touche()

def gagne2(Fenetre_largeur,Fenetre_hauteur):
    """
    Affiche le message Final au centre de l'ecran
    """
    texte(Fenetre_largeur//2,Fenetre_hauteur//2,"Finis!","red","center")
    attente_touche()

def victoire(liste_brique,Fenetre_largeur,Fenetre_hauteur,menu,stage):
    """
    Vérifie si le joueur a fini une partie
    """
    etat = True
    for i in range(len(liste_brique)):
        if liste_brique[i][4] != 0:
            etat = False
    if etat == True:
        stage+=1
        if stage>=4 or stage<0:
                gagne2(Fenetre_largeur,Fenetre_hauteur)
                stage=0
                menu=1
        else:
                gagne(Fenetre_largeur,Fenetre_hauteur)
                menu=999
    return menu,stage
