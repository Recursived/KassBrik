from upemtk import *
import random
import time
import sys

#C_ = Collision
from Kb_Text import get_arguments, demarage_horloge,affichage_temps_score,perdu,gagne,victoire,gagne2
from Kb_Barre import C_barre,afficher_labarre
from Kb_Balle import afficher_balle,deplacer_balle
from Kb_Briques import creation_brique,couleur_brique_res,affiche_brique
from Kb_Bonus import bonus_dispo,deplacer_bonus,afficher_bonus,C_bonus,Traitement_effet,Texte_effet
from Kb_Colli import C_briques,C_murLargeur,C_murHauteur
from Kb_Touches import t_fleche,t_fleche2,clavier
from Kb_Autres import JeuIa,Tdepart,background
from Kb_Menu import index,curseur,parametre
from Kb_Stages import Template,Select_ligne,Save,HighScore_r,HighScore_w,Config_r
   
############################################# Debut du jeu avec initialisation et boucle main####################################
if __name__ == "__main__":

    #VARIABLES INIT-------------
    Fenetre_hauteur,Fenetre_largeur,vitesse_balle,control,IA,cur4,cur5,sensi=Config_r()
    cree_fenetre(Fenetre_largeur,Fenetre_hauteur)
    x=(Fenetre_largeur/2)
    y1=Fenetre_hauteur-10
    y2=Fenetre_hauteur-20
    taille_barre=Fenetre_largeur/12
    vitesse_barre=15
    k1=1
    k2=3
    xb=(Fenetre_largeur/2)+1
    yb=Fenetre_hauteur-25
    sens_Bx='est'
    sens_By='nord'
    temps = 0
    touches="kek"
    depart=1
    score = 0
    bonus=[]
    effet=[]
    msgB=0
    timerB=0
    temps=0
    menu=1
    cur=0
    cur2=0
    cur3=0
    stage=0
    posp=0
    highscore=0
    vie=3
    #---------------------------
    while True:
        highscore=HighScore_r()
        while  menu==1 or menu==2:
            affichage_temps_score(score,"menu",vie,highscore)
            background(Fenetre_largeur,Fenetre_hauteur,menu)
            touches=t_fleche2(touches)
            cur,menu,cur2,cur3,cur4,cur5=curseur(touches,cur,menu,cur2,cur3,cur4,cur5,Fenetre_largeur,Fenetre_hauteur)
            index(cur,cur2,Fenetre_largeur,Fenetre_hauteur,menu,cur3,cur4,cur5)
            IA,vitesse_balle=parametre(cur4,cur5)
            stage=cur2
            mise_a_jour()
            efface_tout()
            score = 0
            vie=3
            

        #JEU PRINCIPAL
            
        #iNIT
        menu=0
        briques,nomstage,stage,score,vie,menu = creation_brique(Fenetre_largeur,Fenetre_hauteur,stage,score,vie)
        cur2=0
        depart=1
        xb=(Fenetre_largeur/2)+1
        yb=Fenetre_hauteur-25
        x=(Fenetre_largeur/2)
        y1=Fenetre_hauteur-10
        y2=Fenetre_hauteur-20
        taille_barre=Fenetre_largeur/8
        bonus=[]
        effet=[]
        sens_By='nord'
        pause=0
        
        while menu==0:
            if temps%10000==0:
                if IA==0:
                    HighScore_w(highscore,score)
                highscore=HighScore_r()
                background(Fenetre_largeur,Fenetre_hauteur,menu)
                menu,stage=victoire(briques,Fenetre_largeur,Fenetre_hauteur,menu,stage)
                affiche_brique(briques,Fenetre_hauteur,Fenetre_largeur,stage)
                if control==0:
                    x=t_fleche(x)
                touches=t_fleche2(touches)
                if control==1:
                    x=clavier(touches,x,sensi)
                        
                affichage_temps_score(score,nomstage,vie,highscore)
                if IA!=0:
                    x=JeuIa(x,xb,Fenetre_largeur,taille_barre,cur5,briques,y2)
                    
                    
                x=afficher_labarre(x,y1,y2,"black","black",taille_barre,vitesse_barre,touches,Fenetre_largeur)
                xb,yb =deplacer_balle(xb,yb,vitesse_balle,k1,k2,sens_Bx,sens_By,Fenetre_hauteur)
                while depart==1:
                    mise_a_jour()
                    depart,k1,k2,sens_Bx=Tdepart()
                    
                sens_By,sens_Bx,k1,k2=C_barre(xb,yb,x,y1,y2,sens_By,sens_Bx,k1,k2,taille_barre)
                sens_Bx, sens_By, score = C_briques(briques,xb,yb,sens_Bx,sens_By,score)
                
                briques,bonus=bonus_dispo(briques,bonus,Fenetre_hauteur,Fenetre_largeur)
                bonus=deplacer_bonus(bonus,Fenetre_hauteur,Fenetre_largeur)
                liste_bonus,effet,msgB,timerB=C_bonus(x,y1,taille_barre,bonus,effet,msgB,timerB)
                #Texte_effet(msgB,timerB)
                effet,taille_barre,score=Traitement_effet(effet,taille_barre,score,Fenetre_largeur)
                
                sens_Bx=C_murLargeur(xb,sens_Bx,Fenetre_largeur)
                sens_By,menu,depart,xb,yb,vie,effet,bonus,x,y1,y2=C_murHauteur(yb,sens_By,Fenetre_largeur,Fenetre_hauteur,menu,vie,depart,xb,effet,bonus,x,y1,y2)

                if touches=="Escape":
                    pause=1
                    posp=0
                    
                while pause==1:
                    touches=t_fleche2(touches)
                    background(Fenetre_largeur,Fenetre_hauteur,menu)
                    texte(Fenetre_largeur//2,Fenetre_hauteur//2,"Pause","black","center")
                    if posp==0:
                        texte((Fenetre_largeur//2)-100,(Fenetre_hauteur//2)+20,"Save","red")
                    else:
                        texte((Fenetre_largeur//2)-100,(Fenetre_hauteur//2)+20,"Save","black")
                    if posp==1:
                        texte((Fenetre_largeur//2)+35,(Fenetre_hauteur//2)+20,"Quit","red")
                    else:
                        texte((Fenetre_largeur//2)+35,(Fenetre_hauteur//2)+20,"Quit","black")
                    mise_a_jour()
                    efface_tout()
                    if touches=="p":
                        pause=0
                    if touches=="Right":
                        posp=1
                    if touches=="Left":
                        posp=0
                    if touches=="Return" and posp==0:
                        Save(score,vie,briques,Fenetre_hauteur,stage)
                        menu=1
                        pause=0
                    if touches=="Return" and posp==1:
                        menu=1
                        pause=0
                        
                mise_a_jour()
                efface_tout()
            temps+=1
