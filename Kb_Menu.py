#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonction lié aux event touches

from upemtk import *
import random
import time
import sys
from Kb_Stages import Template,Select_ligne

__all__ = ['index','curseur','parametre']


def index(curseur,curseur2,Fenetre_largeur,Fenetre_hauteur,menu,cur3,cur4,cur5):
    """
    Effectue des changements visuelles en fonction des menus et des curseurs
    """
    if menu==1:
        texte(200,30,"KassBrik",taille=40)
        if curseur==0:
            texte(200,150,"Jouer",couleur="red")
            if curseur2>=0:
                texte(300,150,str(curseur2),couleur="red")
            else:
                texte(300,150,"load",couleur="red")
        else:
            texte(200,150,"Jouer")
            if curseur2>=0:
                texte(300,150,str(curseur2))
            else:
                texte(300,150,"load")
        if curseur==1:
            texte(200,250,"Stage select",couleur="red")
        else:
            texte(200,250,"Stage select")
        if curseur==2:
            texte(200,350,"Option",couleur="red")
        else:
            texte(200,350,"Option")
        if curseur==3:
            texte(200,450,"Quitter",couleur="red")
        else:
            texte(200,450,"Quitter")
    if menu==2:
        texte(200,30,"KassBrik",taille=40)
        if cur3==0:
            texte(200,150,"Vitesse",couleur="red")
            texte(350,150,str(cur4),couleur="red")
        else:
            texte(200,150,"Vitesse")
            texte(350,150,str(cur4))
        if cur3==1:
            texte(200,250,"IA",couleur="red")
            texte(250,250,str(cur5),couleur="red")
        else:
            texte(200,250,"IA")
            texte(250,250,str(cur5))
        if cur3==2:
            texte(200,350,"Creer template",couleur="red")
        else:
            texte(200,350,"Creer template")
        if cur3==3:
            texte(200,450,"Retour",couleur="red")
        else:
            texte(200,450,"Retour")
        

def curseur(t,cur,menu,cur2,cur3,cur4,cur5,Fenetre_largeur,Fenetre_hauteur):
    """
    Permet de faire varier la valeur des curseurs en fonction des touches appuyes
    """
    if menu==1:
        if t=='Up' and cur>0:
            cur-=1
        if t=='Down' and cur<3:
            cur+=1

        if cur==0:
            if t=='Right' and cur2<3:
                cur2+=1
            if t=='Left' and cur2>=0:
                cur2-=1

        if t=="Return" and cur==0:
            menu=0
        if t=="Return" and cur==1:
            menu=0
            cur2=999
        if t=="Return" and cur==2:
            menu=2
            cur3=0
        if t=="Return" and cur==3:
            ferme_fenetre()

        return cur,menu,cur2,cur3,cur4,cur5
    
    if menu==2:
        if t=='Up' and cur3>0:
            cur3-=1
        if t=='Down' and cur3<3:
            cur3+=1

        if cur3==0:
            if t=='Right' and cur4<4:
                cur4+=1
            if t=='Left' and cur4>0:
                cur4-=1
        
        if cur3==1:
            if t=='Right' and cur5<2:
                cur5+=1
            if t=='Left' and cur5>0:
                cur5-=1

        if t=="Return" and cur3==0:
            pass
        if t=="Return" and cur3==1:
            pass
        if t=="Return" and cur3==3:
            menu=1
        if t=="Return" and cur3==2:
            Template(Fenetre_largeur,Fenetre_hauteur)
            
        return cur,menu,cur2,cur3,cur4,cur5

def parametre(cur4,cur5):
    """
    Effectue des changements de parametres en fonction des curseurs
    """
    if cur4==0:
        vitesse_balle=0.2
    if cur4==1:
        vitesse_balle=0.3
    if cur4==2:
        vitesse_balle=0.5
    if cur4==3:
        vitesse_balle=1
    if cur4==4:
        vitesse_balle=1.5
    if cur5==0:
        IA=0
    if cur5==1:
        IA=1
    if cur5==2:
        IA=2
    return IA,vitesse_balle

