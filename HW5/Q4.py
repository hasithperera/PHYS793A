#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 07:03:48 2022
Author : Hasith Perera

"""
import numpy as np
import matplotlib.pyplot as plt

B_sw = 5e-9 #T
u_sw = 4e6 #ms^-1
sigma_sw = -4.49e-4 # Hz^-1 from ref

B_0 = 30.2e-6 #T
R_E = 6.371e6 #m
mu_0 = 1.256e-6 # ref:wiki
k_b = 1.38e-23 # ref:wiki
k_ev = 8.61733e-5 #ev/K


def dipole_B_h(r):
    return B_0*np.power(R_E/r,3)
  
def find_Rmp(B_sw,u_sw,r_max=20,debug=0):  
    r = np.arange(2,r_max,.5) 
    r_m = r * R_E
    P_mag = np.power(dipole_B_h(r_m),2)/(2*mu_0)
    print(P_mag)
    
    # Measurements in 1 AU
    
    n_sw = 5.56e6 #no in m^3 ref:Klein 2019
    T_e_sw = 11.9 #ev
    T_e_K = T_e_sw /k_ev
    # P_sw = 
    
    u_avg = 4e6
    rho_est = np.power(B_0*1e-3,2)/(2*mu_0*u_avg*u_avg) 
   
    P_sw = np.power(B_sw,2)/(2*mu_0) + n_sw*k_b*T_e_K + rho_est * np.power(u_sw,2)
    print(P_sw)
    
    val = np.argmin(np.abs(P_sw - P_mag))
    
    if (debug==1):
        plt.figure(1)
        plt.semilogy(r,P_mag,"o:")
        plt.semilogy(plt.xlim(),[P_sw,P_sw],'-')
        plt.semilogy([r[val],r[val]],plt.ylim(),":")
        
        plt.xlabel(r'Altitude ($r/R_E$)')
        plt.ylabel('Pressure terms (J)')
        plt.legend([r"$P_{mag}$",r"$P_{sw}$",r"$R_{mp}$"])
        
        
    return r[val]


if __name__=='__main__':
    
    u_sw = 4e6
    B_sw = 5e-9
    find_Rmp(B_sw*1e-9,u_sw,debug=1)
    
    
    
    B_list = []
    U_list = []
    R_list = []
    
    
    for B_sw in range(5,50,5):
        R_list.append(find_Rmp(B_sw*1e-9,u_sw))
        B_list.append(B_sw)
        
    plt.figure(figsize=(6,3))
    plt.plot(B_list,R_list,'o:')
    plt.xlabel(r"$B_{sw}$ (nT) ")
    plt.ylabel(r"$R_{mp}/R_E$")
        
    
    #variation of u_sw with fixed B_sw
    B_sw = 5e-9
    # u_sw = 1000
    # find_Rmp(B_sw,u_sw*1e3,debug=0)
    
    R_list = []
    U_list = []
    
    for u_sw in range(300,600,20):
        R_list.append(find_Rmp(B_sw,u_sw*1e3,debug=0))
        U_list.append(u_sw)
    
    plt.figure(figsize=(6,3))
    plt.plot(U_list,R_list,'o:')
    plt.xlabel(r"$U_{sw}$ ($kms^{-1}$) ")
    plt.ylabel(r"$R_{mp}/R_E$")
    

    # plt.figure(1)

    
    # # plt.plot()
   