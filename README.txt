                                  _______________________________________________
                                 ( M      _  __               ____       _ _     )
                                 ( S     | |/ /__ _ ___ ___  | __ ) _ __(_) | __ )
                                 (       | ' // _` / __/ __| |  _ \| '__| | |/ / )
                                 ( A     | . \ (_| \__ \__ \ | |_) | |  | |   <  )
                                 ( M     |_|\_\__,_|___/___/ |____/|_|  |_|_|\_\ )
                                 (_______________________________________________)

*---------------Les Optimisations--------------*                    *------------------Organisation du programme----------------*

--> La barre renvoit la balle dans une direction                     --> 8 groupe de fonctions:
et un angle proportionnels a son lieu d'impact                                -Autre
                                                                              -Labarre
--> La barre se deplace de maniere fluide avec                                -Laballe
la souris                                                                     -Les briques
                                                                              -Les bonus                    
--> le jeu contient plusieur timers, pour compter                             -Les colisions  
le temps de jeu, pour determiner une vitesse compatible                       -Les touches
intermachine, et pour faire disparaitre des bonus/malus                       -Stage
                                                                              -Menu
                                                                              -Textes

--> l'Ia renvois la balle dans une direction et un                   --> Main:
angle aléatoire, pour eviter de se coincer dans une                           -Init Variable
boucle interminable                                                           -Boucle principale:
                                                                                 -test victoire
--> Le bonus clingote de maniere multicolore, pour le                            -Affichage brique et score
voir facilement                                                                  -evenement touches
                                                                                 -Groupe Barre
--> La brique affiche si elle a un bonus ou non, avec                            -colisions Barre/Brique
un caractere different pour chaque bonus                                         -Groupe bonus
                                                                                 -colisions Mur
--> possibilité de faire pause (echap: pause, P:retour)                          -Rafrachissement Espace/Temps
						                                 -Boucle while de menu et de pause
                                                                                 
--> Amélioration de l'IA --> vise les briques

--> Menu visuel avec option, création de level,
Quitter...

--> Possibilité de modifier les options de jeu
via texte ou directement sur le jeu
(vitesse, souris ou clavier...)

--> Possibilité de sauver/créer/charger les
niveaux (load: fleche gauche sur jouer 0)


*---------------Les choix techniques--------------*                 *------------------Problèmes Rencontrés----------------*

--> time.clock pour l'affichage du temps                            --> rendu 1 réalisé en moins d'une semaines, donc ça va

--> duo de time.time pour les timers systemes                       --> deplacement avec fleche: moche, il manque un evenement key_release dans upemtk
                                                                    --> Bouton annulé de la fenêtre de dialogue windows qui faisait crasher le jeu
--> cercle pour le bonus et la balle
                                                                    --> Vérification de fichier pour ne pas charger des fichiers quelconques
--> rectangle pour les briques

--> briques et bonus dans des listes de tuples

--> barre et balle positioné avec des variables indépendantes

--> couleurs du jeu en valeur héxadécimales

--> lancer de la balle: fleche haute

--> deplacement de la barre: Xsouris

--> La barre ne peut pas sortir de l'ecran

--> Ia: suit la balle, et ajoute une valeur entre
-taille_barre et +taillebarre

--> Rajout d'un système de vie 

--> affichage des éléments relatifs au jeu sur la
fenêtre de dialogue

--> Génération d'un niveau aléatoire avec le random.txt
quand on charge les niveaux