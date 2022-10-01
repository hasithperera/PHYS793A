#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:41:51 2022
Author : Hasith Perera

"""
import numpy as np
import matplotlib.pyplot as plt


#initial conditions : using AU as the distance unit

# modified conditions to match the observations
B_0 = .3e-3 #T
Rs = 6.957e8/(8*60*3e8) #solar radius in au
v = 800e3/(8*60*3e8) #ms-1

# # #orignal values in Q1
# B_0 = 3e-3 #T
# Rs = 6.957e8/(8*60*3e8) #solar radius in au
# v = 400e3/(8*60*3e8) #ms-1

w_days = 27
w = 2*np.pi/(w_days*24*3600)  #hz
beta = Rs*w/v
theta = np.pi/2 #ecliptic plane

#getting an array of points from solar radius to 1.5 AU
r = 1
#calculating B_r for each point based on eq 1
B_r = B_0*(Rs/r)**2         



# calculation based on eq 3
B_phi =  -beta*B_r*(r/Rs)*np.sin(theta)

print("B_r = {} nT".format(B_r*1e9))
print("B_phi = {} nT".format(B_phi*1e9))

B_r= B_r*1e9
B_phi =B_phi*1e9
B_theta = 0


theta = np.deg2rad(90)
phi = np.deg2rad(90)

def transform_to_GSM(B_r,B_theta,B_phi,theta,phi):
    """
    Return GSM B_fields
    """
    
    r_hat  = [np.cos(theta)*np.sin(phi),np.sin(theta)*np.sin(phi),np.cos(phi)]
    theta_hat = [-np.sin(theta),np.cos(theta),0]
    phi_hat = [np.cos(theta)*np.sin(phi),np.sin(theta)*np.cos(phi),-np.sin(phi)]
    
    cart = B_r*np.transpose(r_hat) + B_theta*np.transpose(theta_hat) + B_phi * np.transpose(phi_hat)
    # cart : z,y,x
    # to GSM 
    # -y > x
    #  y > x
    #  z > z
    return [-cart[1],cart[2],cart[0]]

a = transform_to_GSM(B_r,0,B_phi,theta,phi)
print('\n In GSM X,Y,Z (nT)')
print(a)

