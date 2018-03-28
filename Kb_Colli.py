#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonctions lie aux collisions


from upemtk import *
import random
import time
import sys
from Kb_Text import get_arguments, demarage_horloge,affichage_temps_score,perdu

__all__ = ['C_briques','C_murLargeur','C_murHauteur']



def C_briques(liste_brique,x,y,sens_Bx,sens_By,score):
    '''
    verifie ou est ce que la balle est rentree en contact avec la briques
    '''
    for i in range(len(liste_brique)):
        explose_res = -1
        coingauchex, coingauchey, coindroitx, coindroity, resistance, bonus= liste_brique[i][0], liste_brique[i][1], liste_brique[i][2], liste_brique[i][3], liste_brique[i][4], liste_brique[i][5]
        if resistance == 0:
            continue
        else:
            if x>= coingauchex and x<=coindroitx and y<=coingauchey+3 and y>=coingauchey-3:
                resistance += explose_res
                liste_brique[i] = (coingauchex, coingauchey, coindroitx, coindroity, resistance, bonus)
                sens_By='nord'
                score += 10
                return sens_Bx, sens_By, score
            if x>= coingauchex and x<=coindroitx and y<=coindroity+3 and y>=coindroity-3:
                resistance += explose_res
                liste_brique[i] = (coingauchex, coingauchey, coindroitx, coindroity, resistance, bonus)
                sens_By='sud'
                score += 10
                return sens_Bx, sens_By, score
            if y>=coingauchey and y<=coindroity and x<=coingauchex+3 and x>=coingauchex-3:
                resistance += explose_res
                liste_brique[i] = (coingauchex, coingauchey, coindroitx, coindroity, resistance, bonus)
                sens_Bx='ouest'
                score += 10
                return sens_Bx, sens_By, score
            if y>=coingauchey and y<=coindroity and x<=coindroitx+3 and x>=coindroitx-3:
                resistance += explose_res
                liste_brique[i] = (coingauchex, coingauchey, coindroitx, coindroity, resistance, bonus)
                sens_Bx='est'
                score += 10
                return sens_Bx, sens_By, score


    return sens_Bx, sens_By,score



def C_murLargeur(x,sens_Bx,Fenetre_largeur):
    '''
    rebondis sur les murs
    '''
    if x<0:
        sens_Bx='est'
    if x>Fenetre_largeur:
        sens_Bx='ouest'
    
    return sens_Bx
    
def C_murHauteur(y,sens_By,Fenetre_largeur,Fenetre_hauteur,menu,vie,depart,xb,effet,bonus,x,y1,y2):
    '''
    rebondis au plafond
    perd au sol
    '''
    if y<0:
        sens_By='sud'
    if y>Fenetre_hauteur:
        sens_By='nord'
        if vie<=1:
            perdu(Fenetre_largeur,Fenetre_hauteur)
            menu=1
        else:
            depart=1
            vie-=1
            xb=(Fenetre_largeur/2)+1
            y=Fenetre_hauteur-25
            effet=[]
            bonus=[]
            x=(Fenetre_largeur/2)
            y1=Fenetre_hauteur-10
            y2=Fenetre_hauteur-20
    
    return sens_By,menu,depart,xb,y,vie,effet,bonus,x,y1,y2
