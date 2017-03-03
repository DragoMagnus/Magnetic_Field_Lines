# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 13:36:08 2017

@author: wdubosclard

Ce script cherche à tracer les lignes de champs que l'on obtient lorsque
l'on fait passer du courant au travers de fils conducteurs.
"""

from __future__ import division
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

"""
Champ magnétique sur un fil unique
"""

mu_0 = 4*np.pi*10**-7
print mu_0

xmin, xmax, ymin, ymax = 2.5, -2.5, 2.5, -2.5
print xmax, xmin, ymax, ymin #### Zone d'affichage -- Taille de la puce

h = 0.01
X = np.arange(xmin, xmax, h)
Y = np.arange(ymin, ymax, h) #### points de la grille

XX, YY = np.meshgrid(X, Y) #### Creation de la grille 

R = np.sqrt(XX**2 + YY**2) #### Distance entre le fil et le point de l'espace considéré
print R 

###############################################################################
#### Mise en place du fil

wire = [(1, 0, 0)]
vect = [np.array([XX-x_position, YY-y_position]) for q_lineique, x_position, y_position in wire]
vect[0].shape


dist = [norm(Ve, axis=0) for Ve in vect]

# dist = [norm(ve, axis=0) for ve in vect] #### Distance R
V = np.sum(-q_lineique*np.log(D) for (q_lineique, x_position, y_position), D in zip(wire, dist))



#### Tracer du fil et de ses lignes de champ
plt.title(u"Équipotentielles")
plt.axis('equal')
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
ax = plt.gca()
# Représentation de la section des fils
for q_lineique, x_position, y_position in wire:
    radius = .05*q_lineique
    color = 'red' if q_lineique > 0 else 'blue'
    circle = plt.Circle((x_position, y_position), radius, color=color)
    ax.add_artist(circle)
    
# Représentation de 20 équipotentielles
C = plt.contourf(XX, YY, V, 20, cmap='bone')
plt.colorbar(C)

plt.show()

