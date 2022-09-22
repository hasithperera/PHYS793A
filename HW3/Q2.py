#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:50:40 2022
Author : Hasith Perera

"""

import matplotlib.pyplot as plt
import numpy as np




Rs = 0.004652#6.957e8/(24e8) #solar radius in au
v = 400e3/24e8 #ms-1
phi_0 = 0
B_0 = 30

w_days = 27
w = 2*np.pi/(w_days*24*3600)  #hz
long = np.pi /2  #ecliptic plane

#initial 
for phi_d in range(0,360,40):
    phi_shift = phi_d*np.pi/180
    r = np.arange(Rs,15,.2) #spiral radiusnp.pi
    phi = phi_shift + (B_0*w*np.sin(long)/v)*(Rs - r) + phi_0*np.pi/180
    plt.plot(r*np.cos(phi),r*np.sin(phi),'b-')
    
B_0 = 1
v = 100e3/24e8 #ms-1
w_days = 27
w = 2*np.pi/(w_days*24*3600)  #hz
long = np.pi /2  #ecliptic plane

#initial 
for phi_d in range(0,360,40):
    phi_shift = phi_d*np.pi/180
    r = np.arange(Rs,15,.2) #spiral radiusnp.pi
    phi = phi_shift + (B_0*w*np.sin(long)/v)*(Rs - r) + phi_0*np.pi/180
    plt.plot(r*np.cos(phi),r*np.sin(phi),'r-')
    
th = np.arange(0,2.1*np.pi,.1)

plt.plot(10*np.cos(th),10*np.sin(th),'k:')
    
#modify B0
plt.xlabel('Au')
plt.ylabel('Au')