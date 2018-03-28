#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonction restantes

from upemtk import *
import random
import time
import sys
import math
from Kb_Touches import t_fleche,t_fleche2

__all__ = ['JeuIa','Tdepart','background','get_brique_cible']


def JeuIa(x,xb,Fenetre_largeur,taille_barre,typeIA,brique,yhaut):
    '''
    l'ordinateur joue --> presente une IA passive et une IA active qui est capable de viser
    '''
    if typeIA == 1:
        IaPos=random.randint(-taille_barre,taille_barre)
        x=xb+IaPos
        if x>Fenetre_largeur-taille_barre:
            x=Fenetre_largeur-taille_barre
        if x<taille_barre:
            x=taille_barre
        return x
    elif typeIA == 2:
        negatif = False
        milieu_x_brique, y_brique = get_brique_cible(brique)
        mid = x
        #Cote horizontal du triangle rectangle
        cote1 = mid - milieu_x_brique   
        #Coté vertical du triangle rectangle
        cote2 = y_brique - yhaut
        if cote1 < 0:
            negatif = True
        else:
            negatif = False
        #print(mid,milieu_x_brique,"---> valeur cote 1:",cote1)
        if cote1 != 0:
            angle = math.degrees(abs(math.atan(cote2/cote1)))
            go_x = ((((math.tan(math.radians(angle))+1)**-1)*4)*taille_barre)/3+xb
        else:
            return xb
        if negatif == True:
            return -(((((math.tan(math.radians(angle))+1)**-1)*4)*taille_barre)/3-xb)
        else:
            return ((((math.tan(math.radians(angle))+1)**-1)*4)*taille_barre)/3+xb

def Tdepart():
    '''
    verifie que la touche haut est pressee
    lance la balle aleatoirement
    '''
    touches=''
    k1=3
    k2=2
    sens_Bx='ouest'
    touches=t_fleche2(touches)
    if touches=='Up':
        k1=random.randint(1,3)
        k2=5-k1
        randir=random.randint(1,2)
        if randir ==1:
            sens_Bx='est'
        return 0,k1,k2,sens_Bx
    else:
        return 1,k1,k2,sens_Bx

def background(Fenetre_largeur,Fenetre_hauteur,menu):
    rectangle(0,0,Fenetre_largeur,Fenetre_hauteur,remplissage="#ccffff",couleur="#ccffff")
    if menu==1 or menu==2:
        rectangle(20,20,Fenetre_largeur-20,Fenetre_hauteur-20,remplissage="#ffffdb",couleur="#ffffdb")
    else:
        rectangle(0,0,Fenetre_largeur,Fenetre_hauteur,remplissage="#ffffdb",couleur="#ffffdb")

def get_brique_cible(brique):
    """cherche toutes les briques que l'ia peut cibler et lui retourne ses coordonnees"""
    if len(brique) >0 :
        for i in range(len(brique)-1,-1,-1):
            if brique[i][4] != 0:
                #Donne le milieu du côté bas de la brique
                cercle((brique[i][0]+brique[i][2])//2,brique[i][3],4,remplissage="green")
                return (brique[i][0]+brique[i][2])//2,brique[i][3]
            #Sinon ne fait rien du tout
        return 0,0 
