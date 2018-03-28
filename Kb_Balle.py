#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonctions lie a la balle

from upemtk import *
import random
import time
import sys

__all__ = ['afficher_balle','deplacer_balle']

def afficher_balle(x,y,rayon,couleur,remplissage):
    '''
    cqfd
    '''
    cercle(x,y,rayon,couleur,remplissage)

def deplacer_balle(x,y,vitesse_balle,k1,k2,sens_Bx,sens_By,Fenetre_hauteur):
    '''
    Applique le vecteur sur la balle par rapport a la direction
    '''
    
    dx = k1 * vitesse_balle
    dy = k2 * vitesse_balle
    
    if sens_By=='nord':
        y -= dy
    if sens_By=='sud':
        y += dy
    if sens_Bx=='ouest':
        x -= dx
    if sens_Bx=='est':
        x += dx

    
    afficher_balle(x,y,Fenetre_hauteur/120,"red","red")
    return x,y
