#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonctions lie au briques


from upemtk import *
import random
import time
import sys
import os
from tkinter import filedialog
import tkinter as tk
import string

__all__ = ['creation_brique', 'couleur_brique_res','affiche_brique','Load','Verif_stage','Verif_Save']

def creation_brique(lar,hau,stage,score,vie):
    '''
    cree la liste de briques
    '''
    brique = []
    ax1=0
    ay1=0
    ax2=lar/10
    ay2=hau/20
    create_brique=[]
    l=8
    if stage!=999 and stage!=-1:
        nomstage=str(stage)
        l,lst_brique=fichier_brique("stages/campagne/"+str(stage)+".txt")
        for i in lst_brique:
                if i[0]!=0:
                    create_brique.append((1,i[0],i[1]))
                else:
                    create_brique.append((0,1,0))
                
    if stage==999:
        root = tk.Tk()
        root.withdraw()
        chemin = filedialog.askopenfilename()
        if chemin=="":
            return [],"",999,0,3,1
        if Verif_stage(chemin) == False:
            return [],"",999,0,3,1
        nomstage=""
        for elm in chemin:
            nomstage+=elm
            if elm=="/":
                nomstage=""
        nomstage=nomstage[:-4]
        if Verif_stage(chemin)!="kek":
            l,lst_brique=fichier_brique(chemin)
            for i in lst_brique:
                if i[0]!=0:
                    create_brique.append((1,i[0],i[1]))
                else:
                    create_brique.append((0,1,0))
        else:
            for i in range(80):
                create_brique.append((random.randint(0,1),random.randint(1,3),random.randint(0,7)))
            

    i2=0
    if stage!=-1:
        while True:
            if ax1 == lar:
                ax1 = 0
                ax2 = lar/10
                ay2 += hau/20
                ay1 += hau/20
            if ay1 >= (hau/20)*l:
                break
            if create_brique[i2][0] == 1:
                brique.append((ax1,ay1,ax2,ay2,create_brique[i2][1],create_brique[i2][2])) # tuples d'une brique (coingauchex, coingauchey, coindroitx, coindroity, resistance,bonus,bonus_droped) 
            ax1 += lar/10
            ax2 += lar/10
            i2+=1
    else:
        root = tk.Tk()
        root.withdraw()
        chemin = filedialog.askopenfilename()
        if chemin=="":
            return [],"",999,0,3,1
        if Verif_Save(chemin) == False:
            return [],"",999,0,3,1
        brique,stage,score,vie=Load(chemin)
        nomstage=str(stage)

    return brique,nomstage,stage,score,vie,0

def couleur_brique_res(res_brique,y,Fenetre_hauteur,stage):
    '''
    definis la couleur de la briques en fonction de la ligne et de la res
    '''
    couleur = ''
    ligne=Fenetre_hauteur/20
    if y<ligne*8:
        if res_brique == 1:
            couleur = '#ffa8fc'
        elif res_brique == 2:
            couleur = "#ff60fb"
        elif res_brique == 3:
            couleur = "#ff00fa"
    if y<ligne*6:
        if res_brique == 1:
            couleur = '#adb7ff'
        elif res_brique == 2:
            couleur = "#3d54ff"
        elif res_brique == 3:
            couleur = "#0220ff"
    if y<ligne*4:
        if res_brique == 1:
            couleur = '#adffa0'
        elif res_brique == 2:
            couleur = "#64ff4c"
        elif res_brique == 3:
            couleur = "#21ff00"
    if y<ligne*2:
        if res_brique == 1:
            couleur = '#ff9b89'
        elif res_brique == 2:
            couleur = "#ff5c3f"
        elif res_brique == 3:
            couleur = "#ff2600"

    return couleur 

def affiche_brique(liste_brique,Fenetre_hauteur,Fenetre_largeur,stage):
    '''
    cqfd
    '''
    for i in range(len(liste_brique)):
        ax1, ay1, ax2, ay2 = liste_brique[i][0], liste_brique[i][1], liste_brique[i][2], liste_brique[i][3]
        if liste_brique[i][4] == 0:
            continue
        couleur = couleur_brique_res(liste_brique[i][4],ay1,Fenetre_hauteur,stage)
        rectangle(ax1,ay1,ax2,ay2,"black",couleur)
        if liste_brique[i][5] >=6:
            rectangle(ax1+(Fenetre_largeur/24),ay1+(Fenetre_hauteur/400)+8,ax1+(Fenetre_largeur/17),ay1+(Fenetre_hauteur/31),couleur='black',remplissage="yellow")

def fichier_brique(chemin):
    """
    Permet de lire un fichier niveau et de l'appliquer
    """
    fichier=open(chemin,"r")
    lst=[]
    nb=0
    count=0
    for ligne in fichier:
        if nb==0:
            l=int(ligne[:-1])
        if nb>1 and nb<=l+1:
            for elm in ligne:
                if elm=="\n":
                    break
                elif count==0:
                    res=int(elm)
                elif count==2:
                    bonus=int(elm)
                count+=1
                if elm=="|":
                    count=0
                    lst.append((res,bonus))
        nb+=1
    fichier.close()
    return l,lst

def Load(chemin):
    """
    Permet de charger un fichier niveau 
    """
    cnt=0
    cnt2=0
    cnt3=0
    x1=""
    x2=""
    y1=""
    y2=""
    res=""
    bonus=""
    brick=[]
    fichier=open(chemin,"r")
    for ligne in fichier:
        if cnt==0:
            stage=ligne[:-1]
        if cnt==1:
            score=ligne[:-1]
        if cnt==2:
            vie=ligne[:-1]
        if cnt==3:
            for elm in ligne:
                if cnt2==0 and elm!="," and elm!="|" and elm!="." and cnt3==0:
                    x1+=elm
                if cnt2==1 and elm!="," and elm!="|" and elm!="." and cnt3==0:
                    y1+=elm
                if cnt2==2 and elm!="," and elm!="|" and elm!="." and cnt3==0:
                    x2+=elm
                if cnt2==3 and elm!="," and elm!="|" and elm!="." and cnt3==0:
                    y2+=elm
                if cnt2==4 and elm!="," and elm!="|" and elm!="." and cnt3==0:
                    res+=elm
                if cnt2==5 and elm!="," and elm!="|" and elm!="." and cnt3==0:
                    bonus+=elm
                if elm=="|":
                    cnt2=0
                    brick.append((int(x1),int(y1),int(x2),int(y2),int(res),int(bonus)))
                    x1=""
                    x2=""
                    y1=""
                    y2=""
                    res=""
                    bonus=""
                if elm==",":
                    cnt2+=1
                    cnt3=0
                if elm==".":
                    cnt3=1
        cnt+=1
    fichier.close()
    return brick,int(stage),int(score),int(vie)

def Verif_stage(chemin):
    """
    Verifie le fichier texte correspondant au stage est valide
    """
    if os.stat(chemin).st_size == 0:
        return "kek"
    fichier=open(chemin,"r")
    cnt=0
    for ligne in fichier:
        if cnt==0:
            if ligne in string.digits:
                return False
            if ligne[:-1] not in string.digits:
                return False
            else:
                li=int(ligne[:-1])
        if cnt==1:
            if ligne != "\n":
                return False
        if cnt>1:
            if cnt<li+2:
                cnt2=0
                for elm in ligne:
                    if elm=="\n":
                        cnt2+=1
                        continue
                    elif cnt2==0 or cnt2==2:
                        cnt2+=1
                        if elm not in string.digits:
                            return False
                    elif cnt2==1:
                        cnt2+=1
                        if elm!=",":
                            return False
                    elif cnt2==3:
                        cnt2+=1
                        if elm!="|":
                            return False
                        else:
                            cnt2==0
                            continue
            
        cnt+=1
    if cnt<li+1:
        return False
    return True

def Verif_Save(chemin):
    """
    Verifie l'existence du fichier save
    """
    if os.stat(chemin).st_size == 0:
        return False
    fichier=open(chemin,"r")
    cnt=0
    for ligne in fichier:
        if cnt==0 or cnt==1 or cnt==2:
            for elm in ligne:
                if elm not in string.digits and elm!="\n":
                    return False
        if cnt==3:
            cnt2=0
            dvir=0
            cnt3=0
            for elm in ligne:
                if elm==",":
                    if dvir==1:
                        return False
                    cnt2+=1
                    dvir=1
                elif cnt3==1:
                    if elm!="|":
                        return False
                    cnt2=0
                    cnt3=0
                    dvir=0
                elif cnt2==5:
                    if elm not in string.digits:
                        return False
                    dvir=0
                    cnt3=1
                elif elm not in string.digits and elm!="\n" and elm!=".":
                    return False
                else:
                    dvir=0
        cnt+=1
    if cnt<4:
        return False
    return True
        
