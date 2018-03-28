#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonction lie a Labarre (lol)

from upemtk import *
import random
import time
import sys

__all__ = ['C_barre', 'afficher_labarre']


def C_barre(xb,yb,x,y1,y2,sens_By,sens_Bx,k1,k2,taille_barre):
    '''
    Verifie quand la balle rentre en contact avec Labarre
    change la direction de la balle
    change la valeur de l angle par rapport au point de colision
    '''
    if xb>x-taille_barre and xb<x+taille_barre:
        if yb>y2 and yb>y2+2:
            sens_By='nord'
            if xb<x:
                sens_Bx='ouest'
                k1=(x-xb)
                k1=(k1 - 0) * (3 - 0) / (taille_barre - 0) + 0
                k2=4-k1
            else:
                sens_Bx='est'
                k1=(xb-x)
                k1=(k1 - 0) * (3 - 0) / (taille_barre - 0) + 0
                k2=4-k1
                
    return sens_By,sens_Bx,k1,k2


def afficher_labarre(x,y1,y2,couleur,remplissage,taille_barre,vitesse_barre,touches,Fenetre_largeur):
    '''
    affiche Labarre
    empeche Labarre de sortir de l ecran
    '''
    if x>Fenetre_largeur-taille_barre:
        x=Fenetre_largeur-taille_barre
    if x<taille_barre:
        x=taille_barre
    x1=x-taille_barre
    x2=x+taille_barre
    rectangle(x1,y1,x2,y2,couleur,remplissage)
    return x
