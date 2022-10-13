#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:59:31 2022
Author : Hasith Perera

"""

import numpy as np

# # Quasi - Perpendicular case
# # Shock 1
# rho = [15e6,50e6]
# u_x = [-450,-150]
# u_y = [70,-110]
# u_z = [40,-80]

# b_x = [-5,0]
# b_y = [5,15]

#Shock 3
rho = [4e6,26e6]
u_x = [-300,-110]
#u_y = [70,-110]
#u_z = [40,-80]

#b_x = [-5,0]
b_y = [-3,-11]

u_n = u_x
b_l = b_y

val_u = rho[0]*u_n[0]
val_d = rho[1]*u_n[1]

mu_0 = 4e-7*np.pi


v2u = rho[0]*u_n[0]**2 + (b_l[0]**2)/(2*mu_0)
v2d = rho[1]*u_n[1]**2 + (b_l[1]**2)/(2*mu_0)


v3u = u_n[0]*b_l[0]
v3d = u_n[1]*b_l[1]


def p_diff(u,d):
    return (u - d)*100/u

print(p_diff(val_u,val_d))
print(p_diff(v2u,v2d))
print(p_diff(v3u,v3d))


print('\n Q-Par \n')
# # Quasi - parallel case
# Shock 2
rho = [4e6,19e6]
u_x = [-320,-150]
u_y = [50,100]
u_z = [-30,-75]

b_x = [-5,10]
b_y = [-5,10]

u_n = u_x
b_l = b_y
b_n = b_x


val_u = rho[0]*u_n[0]
val_d = rho[1]*u_n[1]

mu_0 = 4e-7*np.pi


v2u = rho[0]*u_n[0]**2 + (b_l[0]**2)/(2*mu_0)
v2d = rho[1]*u_n[1]**2 + (b_l[1]**2)/(2*mu_0)


v3u = u_n[0]*b_l[0]
v3d = u_n[1]*b_l[1]

v4u = b_l[0]*b_n[0]
v4d = b_l[1]*b_n[1]

print(p_diff(val_u,val_d))
print(p_diff(v2u,v2d))
print(p_diff(v3u,v3d))
print(p_diff(v4u,v4d))



