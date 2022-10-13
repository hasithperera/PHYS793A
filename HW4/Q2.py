#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:52:48 2022
Author : Hasith Perera

"""

import numpy as np

## initial conditions 

R_E = 6.372e6 #m
# R_E = 1

r_0 = np.matrix([[3.4*R_E],[.3*R_E],[0]])
epsilon = 1.02
alpha = np.deg2rad(4.8)
L = 22.3 * R_E


# MMS observation - location

# # Shock 1
# x_gse = 9.34 * R_E
# y_gse = 6.10 * R_E
# z_gse = -5.65 * R_E

# # Shock 1 : IMF
# bx = .3
# by = -.3
# bz = 3.9

# Shock 2
x_gse = 8.9 * R_E
y_gse =  11.5 * R_E
z_gse =  -5.4  * R_E

# Shock 2 : IMF
bx = -3.3
by = -2.9
bz = 0.1

# # Shock 3
# x_gse = 12.7 * R_E
# y_gse = -2.9  * R_E
# z_gse = 5.7  * R_E

# # Shock 3 : IMF
# bx = -1.3
# by = -2.5
# bz = -1.2



B = np.matrix([[bx],[by],[bz]]) # in GSE
r = np.matrix([[x_gse],[y_gse],[z_gse]]) # x,y,z in GSE


def GSE_to_abd(r,alpha,r_0):
    # GSE to aberrated coordinate transformation
    trans = np.matrix([[np.cos(alpha),-np.sin(alpha),0],[np.sin(alpha),np.cos(alpha),0],[0,0,1]])
    
    return trans*r - r_0


def Grad_S(r_abd,alpha,epsilon,L):
    # finding grad(S)
    calc = np.matrix([ [(r_abd[0,0]*(1-epsilon**2)+epsilon*L)*np.cos(alpha)+r_abd[1,0]*np.sin(alpha)],
                       [-(r_abd[0,0]*(1-epsilon**2)+epsilon*L)*np.sin(alpha)+r_abd[1,0]*np.cos(alpha)],
                       [r_abd[2,0]] ])
    
    return 2*L*calc/np.linalg.norm(r_abd)


r_abd = GSE_to_abd(r,alpha,r_0)
G_s = Grad_S(r_abd,alpha,epsilon,L)

#  finding the unit normal vector for the shock surface
n_hat = np.array(G_s/np.linalg.norm(G_s)) 
b_hat = np.array( B/np.linalg.norm(B))

n_dot_b = np.vdot(n_hat,b_hat)

print("n_hat",n_hat)
# print(b_hat)
shock_angle = np.rad2deg(np.arccos(n_dot_b))


if shock_angle > 90:
    #if n should be -n
    shock_angle = 180 - shock_angle
    print("n should be -n")


print("Shock Angle:",shock_angle)