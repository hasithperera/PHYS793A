#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:50:40 2022
Author : Hasith Perera

"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(4,4))

Rs = 6.957e8/(8*60*3e8) #solar radius in au
v = 400e3/(8*60*3e8) #ms-1
phi_0 = 0
w_days = 27
w = 2*np.pi/(w_days*24*3600)  #hz
long = np.pi /2  #ecliptic plane

#generating r range 
r = np.arange(Rs,2,.2) 

# plot arms of the spiral by
# changing the initial location $phi_0
for phi_d in range(0,360,40):
    phi_0 = phi_d*np.pi/180

    phi = phi_0 + (w*np.sin(long)/v)*(Rs - r)

    #plotting each arm in a cartician axis
    h3, = plt.plot(r*np.cos(phi),r*np.sin(phi),'bo-')
    
w_days = 50
w = 2*np.pi/(w_days*24*3600)  #hz
# v = 100e3/(8*60*3e8) #ms-1
    
for phi_d in range(0,360,40):
    phi_0 = phi_d*np.pi/180

    phi = phi_0 + (w*np.sin(long)/v)*(Rs - r)

    #plotting each arm in a cartician axis
    h1, = plt.plot(r*np.cos(phi),r*np.sin(phi),'^-r')    
    
#plotting the 1 AU circle
th = np.arange(0,2.01*np.pi,.1)
h2, = plt.plot(1*np.cos(th),1*np.sin(th),'k:')


plt.xlabel('Au')
plt.ylabel('Au')
# plt.legend(handles=[h3,h1,h2],labels = [r'$\omega$ = 27 days',r'$\omega$ = 50 days','1AU orbit'])
plt.legend(handles=[h3,h1,h2],labels = [r'v = 400 $kms^{-1}$',r'v = 800 $kms^{-1}$','1 AU orbit'])
