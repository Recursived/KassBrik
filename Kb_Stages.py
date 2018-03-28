#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonction lié aux event touches

from upemtk import *
import random
import time
import sys
import string
from pathlib import Path
from tkinter import filedialog
import tkinter as tk
from Kb_Autres import JeuIa,Tdepart,background
from Kb_Touches import t_fleche,t_fleche2
import datetime

__all__ = ['Template','Select_ligne','Save','HighScore_r','HighScore_w','Config_r']


def Template(Fenetre_largeur,Fenetre_hauteur):
    """
    Permet de creer un fichier de stage d'un certain nombre de lignes de briques
    """
    li= Select_ligne("Nombre de lignes: ",Fenetre_largeur,Fenetre_hauteur)
    nom="Template"
    fich="Template"
    version=0
    while Path("stages/"+fich+".txt").is_file() == True:
        version+=1
        fich=nom+str(version)
    fichier=open("stages/"+fich+".txt",'w')
    fichier.write(str(li))
    fichier.write("\n")
    fichier.write("\n")
    for i in range(li):
        for j in range(10):
            fichier.write("0,0|")
        fichier.write("\n")
    fichier.write("\n")
    fichier.write("gauche: resistance, droite: bonus")
    fichier.write("\n")
    fichier.write("resistance max: 3")
    fichier.write("\n")
    fichier.write("6=barre+")
    fichier.write("\n")
    fichier.write("7=score+")
    fichier.close()

def Select_ligne(question,Fenetre_largeur,Fenetre_hauteur):
    """ Permet de faire varier le nombre de ligne que l'on souhaite dans l'editeur de niveau"""
    t="None"
    efface_tout()
    l=1
    while True:
        background(Fenetre_largeur,Fenetre_hauteur,1)
        texte(150,250,question)
        texte(410,250,l)
        mise_a_jour()
        efface_tout()
        t=t_fleche2(t)
        if t=="Return":
            break
        if t=="Right" and l<8:
            l+=1
        if t=="Left" and l>1:
            l-=1
    return l

def Save(score,vie,briques,hau,stage):
    """
    Permet de sauvegarder un fichier txt correspondant à l'etat de la partie dans laquelle se trouvait le joueur
    """
    now=datetime.datetime.now()
    nom=str(now)[:10]+" s_"+str(stage)
    fich=str(now)[:10]+" s_"+str(stage)
    version=0
    while Path("save/"+fich+".txt").is_file() == True:
        version+=1
        fich=nom+" v"+str(version)
    fichier=open("save/"+fich+".txt",'w')
    fichier.write(str(stage))
    fichier.write("\n")
    fichier.write(str(score))
    fichier.write("\n")
    fichier.write(str(vie))
    fichier.write("\n")
    for i in range(len(briques)-1):
        fichier.write("{0},{1},{2},{3},{4},{5}|".format(briques[i][0],briques[i][1],briques[i][2],briques[i][3],briques[i][4],briques[i][5]))
    fichier.write("\n")
    fichier.close()

def HighScore_r():
    """
    Lit le highscore dans un fichier txt
    """
    fichier=open("save/HGSC/HIGHSCORE.txt","r")
    l=1
    for ligne in fichier:
        if l==1:
            highscore=int(ligne)
        l=0
    fichier.close()
    return highscore

def HighScore_w(highscore,score):
    """
    Ecrit le highscore dans un fichier txt
    """

    if score>highscore:
        fichier=open("save/HGSC/HIGHSCORE.txt","w")
        fichier.write(str(score))
        fichier.close()

def Config_r():
    """
    Permet de lire le fichier txt contenant les configs pour les appliquer directement au jeu
    """
    fichier=open("config/config.txt","r")
    cnt=0
    f=""
    control=""
    IA=""
    cur4=""
    sensi=""
    
    for ligne in fichier:
        par=0
        for elm in ligne:
            if cnt==0 and par==1 and elm!="\n":
                cur4+=elm
            if cnt==1 and par==1 and elm!="\n":
                f+=elm
            if cnt==2 and par==1 and elm!="\n":
                control+=elm
            if cnt==3 and par==1 and elm!="\n":
                IA+=elm
            if cnt==4 and par==1 and elm!="\n":
                sensi+=elm
            if elm==":":
                par=1
        cnt+=1
        
    f=int(f)
    control=int(control)
    IA=int(IA)
    cur4=int(cur4)
    sensi=int(sensi)

    if sensi<1:
        sensi=1
    elif sensi>50:
        sensi=50
    
    if cur4<=0:
        vb=0.2
    elif cur4==1:
        vb=0.3
    elif cur4==2:
        vb=0.5
    elif cur4==3:
        vb=1
    elif cur4>=4:
        vb=1.5
    if IA<=0:
        cur5=0
    else:
        cur5=1
    return f,f,vb,control,IA,cur4,cur5,sensi
    
        
