#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:28:09 2022
Author : Hasith Perera

"""

import numpy as np
import matplotlib.pyplot as plt

B_0 = 3e-3 #Gauss > Tessla
Rs = 6.957e8/(8*60*3e8) #solar radius in au

v = 400e3/(8*60*3e8) #ms-1
phi_0 = 0

w_days = 27
w = 2*np.pi/(w_days*24*3600)  #hz
long = np.pi /2  #ecliptic plane


beta = Rs*w/v
theta = np.pi/2 #ecliptic plane

# r = np.arange(Rs,1.5,.01)

# theta = np.arange(0,2*np.pi,.1)
r = 1
B_r = B_0*(Rs/r)**2
B_phi =  -beta*B_r*(r/Rs)*np.sin(theta)

print("B_r = {} nT".format(B_r))
print("B_phi = {} nT".format(B_phi))
# plt.figure(figsize=(6,2))
# # plt.subplot(211)
# # plt.plot(r,B_r,'b-')
# plt.plot(theta,B_phi,'b-')

# # plt.legend()
# # plt.subplot(212)
# # plt.plot(r,-B_phi,'r-')
# # plt.plot([1,1],[0, min(B_phi)],':k')
# # plt.plot([1,1],[0, max(B_r)],':k')
# plt.legend([r'$| B_\phi |$'])
# plt.ylabel(r'$| B_\phi|$ (nT)')
# plt.xlabel(r'$\theta$ (rad)')
# plt.xlabel('Distance (AU)')