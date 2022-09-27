#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:41:51 2022
Author : Hasith Perera

"""
import numpy as np

B_r = 10;
B_theta = 0
B_phi = 0

theta = np.pi/2
phi = 0

# def trans(B_r,B_theta,B_phi,theta,phi):
    
r_hat  = [np.cos(theta)*np.sin(phi),np.sin(theta)*np.sin(phi),np.cos(phi)]
theta_hat = [-np.sin(theta),np.cos(theta),0]
phi_hat = [np.cos(theta)*np.sin(phi),np.sin(theta)*np.cos(phi),-np.sin(phi)]

cart = B_r*np.transpose(r_hat) + B_theta*np.transpose(theta_hat + B_phi * phi_hat
    
    # return cart

# a = trans(10,0,0,np.pi/2,0)
print(cart)