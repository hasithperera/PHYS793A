#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:50:40 2022
Author : Hasith Perera

"""

import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(4,4))
# fig = plt.figure()
# plt.axes(projection='polar')


Rs = 6.957e8/(8*60*3e8) #solar radius in au
v = 400e3/(8*60*3e8) #ms-1
phi_0 = 0


w_days = 27
w = 2*np.pi/(w_days*24*3600)  #hz
long = np.pi /2  #ecliptic plane

#initial 
for phi_d in range(0,360,40):
    phi_shift = phi_d*np.pi/180
    r = np.arange(Rs,2,.1) #spiral radiusnp.pi
    phi = phi_shift + (w*np.sin(long)/v)*(Rs - r) + phi_0*np.pi/180
    
    # plt.plot(phi,r)
    h3, = plt.plot(r*np.cos(phi),r*np.sin(phi),'b-')
    
# p1 = np.arange(0,2*np.pi,.1)
# plt.plot(p1,1*np.ones(np.size(p1)),':k')
# w_days = 50
# w = 2*np.pi/(w_days*24*3600)  #hz
v = 200e3/(8*60*3e8) #ms-1

# initial 
for phi_d in range(0,360,40):
    phi_shift = phi_d*np.pi/180
    r = np.arange(Rs,2,.1) #spiral radiusnp.pi
    phi = phi_shift + (w*np.sin(long)/v)*(Rs - r) + phi_0*np.pi/180
    h1, = plt.plot(r*np.cos(phi),r*np.sin(phi),'r-')
    
th = np.arange(0,2.1*np.pi,.1)

h2, = plt.plot(1*np.cos(th),1*np.sin(th),'k:')




# h3, = plt.plot(.3*np.cos(th),.3*np.sin(th),'k:')
    
# modify B0
plt.xlabel('Au')
plt.ylabel('Au')
plt.legend(handles=[h3,h1,h2],labels = [r'V=400 $kms^{-1}$',r'V=200 $kms^{-1}$','1AU orbit'])
