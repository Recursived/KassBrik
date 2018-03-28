#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonctions lie aux bonus


from upemtk import *
import random
import time
import sys

__all__ = ['bonus_dispo', 'deplacer_bonus','afficher_bonus','C_bonus','Traitement_effet','Texte_effet']



def bonus_dispo(liste_brique,liste_bonus,Fenetre_hauteur,Fenetre_largeur):
        '''
        verifie la destruction d'une brique et sa valeur bonus
        '''
        for i in range(len(liste_brique)):
                if liste_brique[i][4] == 0:
                    if liste_brique[i][5] > 5:
                        liste_bonus.append((liste_brique[i][0]+(Fenetre_largeur/20), liste_brique[i][1]+(Fenetre_hauteur/40),liste_brique[i][5]))
                        liste_brique[i] = (liste_brique[i][0], liste_brique[i][1], liste_brique[i][2], liste_brique[i][3], liste_brique[i][4],0)
        return(liste_brique,liste_bonus)

def deplacer_bonus(liste_bonus,Fenetre_hauteur,Fenetre_largeur):
        '''
        deplace la bille
        '''
        for i in range(len(liste_bonus)):
                if liste_bonus[i][2] > 5:
                        y=liste_bonus[i][1]+1
                        liste_bonus[i]=(liste_bonus[i][0],y,liste_bonus[i][2])
                        if liste_bonus[i][1]>Fenetre_hauteur:
                                liste_bonus[i]=(liste_bonus[i][0],liste_bonus[i][1],0)
                        afficher_bonus(liste_bonus[i],Fenetre_largeur)
        return(liste_bonus)

def afficher_bonus(bonus,Fenetre_largeur):
        '''
        Affiche la bille
        '''
        color="#"
        for i in range(6):
                color2=str(hex(random.randint(0,15)))
                color2=color2[2:]
                color=color+color2
        rectangle(bonus[0]-Fenetre_largeur/120,bonus[1]-Fenetre_largeur/120,bonus[0]+Fenetre_largeur/120,bonus[1]+Fenetre_largeur/120,remplissage=color)

def C_bonus(x,y1,taille,liste_bonus,effet,msg,timer):
        '''
        verifie que la bille est recuperee
        '''
        x1=x-taille
        x2=x+taille
        for i in range(len(liste_bonus)):
                if liste_bonus[i][2] > 5:
                        if y1-2<liste_bonus[i][1]<y1+2:
                                if x1<liste_bonus[i][0]<x2:
                                        effet.append(liste_bonus[i][2])
                                        msg=liste_bonus[i][2]
                                        timer=time.time()
                                        liste_bonus[i]=(liste_bonus[i][0],liste_bonus[i][1],0)
                                        
        return(liste_bonus,effet,msg,timer)

def Traitement_effet(effet,taille,score,Fenetre_largeur):
        '''
        traite les effets recuperes
        '''
        for i in range(len(effet)):
                if effet[i]==6:
                        taille+=Fenetre_largeur/60
                        effet[i]=0
                if effet[i]==7:
                        score+=100
                        effet[i]=0
        return(effet,taille,score)

def Texte_effet(msg,timer):
        '''
        affiche un descriptif de l'effet recupere
        '''
        timer2=time.time()
        if timer+2>timer2:
                if msg==6:
                        texte(10,530,"Barre +1", taille=18)
                if msg==7:
                        texte(10,530,"Score +100", taille=18)
