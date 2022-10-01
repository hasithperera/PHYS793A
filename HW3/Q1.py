#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:28:09 2022
Author : Hasith Perera

"""

import numpy as np
import matplotlib.pyplot as plt


#initial conditions : using AU as the distance unit

B_0 = 3e-3 #T
Rs = 6.957e8/(8*60*3e8) #solar radius in au
v = 400e3/(8*60*3e8) #ms-1
w_days = 27
w = 2*np.pi/(w_days*24*3600)  #hz
beta = Rs*w/v
theta = np.pi/2 #ecliptic plane

#getting an array of points from solar radius to 1.5 AU
r = np.arange(Rs,1.5,.01)

#calculating B_r for each point based on eq 1
B_r = B_0*(Rs/r)**2         


# plotting and format specification 
plt.figure(1,figsize=(6,2))

# B_r is converted to nT for plotting
plt.plot(r,B_r*1e9,'b-')

# 1 AU line
plt.plot([1,1],[0, max(B_r*1e9)],':k')

#formatting the plot for output 
plt.ylabel(r'$| B_R|$ (nT)')
plt.xlabel('Distance (AU)')
plt.margins(y=.1)
plt.subplots_adjust(bottom=.25,left=.2,top=.9)



# calculation based on eq 3
B_phi =  beta*B_r*(r/Rs)*np.sin(theta)

# plotting and format specification 
plt.figure(2,figsize=(6,2))
plt.plot(r,B_phi*1e9,'b-')
plt.plot([1,1],[0, max(B_phi*1e9)],':k')
plt.ylabel(r'$| B_\phi|$ (nT)')
plt.xlabel('Distance (AU)')
plt.margins(y=.1)
plt.subplots_adjust(bottom=.25,left=.2,top=.9)


# fix r = 1 AU
r = 1
# an array of values created from 0 - 2 *pi
theta = np.arange(0,2*np.pi,.1)

# calculation based on eq 1
B_r = B_0*(Rs/r)**2

#calculation base on eq 3 for all theta values
B_phi =  beta*B_r*(r/Rs)*np.sin(theta)

# plotting and format specification 
plt.figure(3,figsize=(6,2))
plt.plot(theta,B_phi*1e9,'b-')
plt.ylabel(r'$| B_\phi|$ (nT)')
plt.xlabel(r'$\theta$ (rad)')
plt.margins(y=.1)
plt.subplots_adjust(bottom=.25,left=.2,top=.9)

