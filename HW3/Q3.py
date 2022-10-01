#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:50:40 2022
Author : Hasith Perera

"""

import matplotlib.pyplot as plt
import numpy as np

Rs = 6.957e8/(8*60*3e8) #solar radius in au
v = 700e3/(8*60*3e8) #ms-1
phi_0 = 0

w_days = 27
w = 2*np.pi/(w_days*24*3600)  #hz
long = np.pi /2  #ecliptic plane

fig = plt.figure(figsize=(4,4))
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')

markers = ['o','v','^']

#set longitude of the ejection point. 
for i,long in enumerate([1,90,178]):
    
    #set up phi values 
    phi = np.arange(0,10*np.pi,.2)
    
    #find spiral point for give theta and phi value
    r = Rs - v*phi/(w*np.sin(np.deg2rad(long)))
    
    ax.plot3D(r*np.sin(np.deg2rad(long))*np.cos(phi),r*np.sin(np.deg2rad(long))*np.sin(phi),r*np.cos(np.deg2rad(long)),'o')
    
    plt.figure(2,figsize=(4,4))
    plt.plot(r*np.sin(np.deg2rad(long))*np.cos(phi),r*np.cos(np.deg2rad(long)),':'+markers[i])
    
    
plt.figure(2)
plt.xlabel('Au')
plt.ylabel('Au')

plt.legend([1,90,178])

plt.figure(1)
plt.xlabel('Au')
plt.ylabel('Au')
plt.legend([1,90,178])
# ax.zlabel('Au')
