#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fichier contenant les fonction lié aux event touches

from upemtk import *
import random
import time
import sys

__all__ = ['t_fleche','t_fleche2','clavier']


def t_fleche(t):
    """
    Evenement lie a la souris
    """
    ev=donne_evenement()
    type_ev=type_evenement(ev)
    if type_ev=="Deplacement":
        t=clic_x(ev)
    else:
        t=t
    return t

def t_fleche2(t):
    """
    Evenement lie aux touches
    """
    ev=donne_evenement()
    type_ev=type_evenement(ev)
    if type_ev=="Touche":
        t=touche(ev)
    else:
        t="kek"
    return t

def clavier(t,x,s):
    if t=="Right":
        x+=s
    if t=="Left":
        x-=s
    return x
