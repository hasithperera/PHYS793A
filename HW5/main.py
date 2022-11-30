
# main.py 

import numpy as np
import matplotlib.pyplot as plt

import scipy as sp

from scipy.special import eval_legendre
from scipy import constants as const

y_Ne = np.zeros([4,5])
y_Te = np.zeros([4,5])


n_actual = [0,1,2,-1,-2]

y_Ne[0,0] = 96.31
y_Ne[1,0] = -163.19
y_Ne[2,0] = 124.48

y_Ne[0,1] =-464.86
y_Ne[1,1] = 818.69
y_Ne[2,1] = -621.82

y_Ne[0,2]= 846.52
y_Ne[1,2] = -1490.95
y_Ne[2,2] = 1124.95

y_Ne[0,3] = -7.917
y_Ne[1,3] = 14.088
y_Ne[2,3] = -10.653


y_Ne[0,4] =.2556
y_Ne[1,4] =-.4418
y_Ne[2,4] =.3289

y_Te[0,:] = [2.1855,4.4093,-4.2144,.2070,-.01284]
y_Te[1,:] = [-.9786,3.7677,-4.7405,.1190,-.005077]
y_Te[2,:] = [.2465,-.2892,-0.8883,-.03985,.001987]
y_Te[3,:] = [-.02676,-.4893,0.7477,.03220,-.002536]


B_sw = 19e-9 #T
u_sw = 1000e3 #ms^-1
mu_0 = 1.256e-6 # ref:wiki
x_l = 1e5
x_h = 3e5
n_sw = 5.5e-6 #num/m^3

# J = B_sw*2/((x_h-x_l)*mu_0)
# sigma = J/(u_sw*B_sw)
sigma =  1.9904458598726117e-05

def fun_eq1(l,n,h,y,SZA=0):
    # print("{},{}: {}".format(l,n_actual[n],y[l,n]))
    return y[l,n]*eval_legendre(l,np.cos(SZA))*np.power(h/2000,n_actual[n])


def Y_h(h,y,SZA=0):
    y_sum = 0
    # print(y)
    for l in range (0,4):
        for n in range(0,5):
            y_sum = y_sum + fun_eq1(l,n,h,y,SZA)
    return y_sum

J = sigma*u_sw*B_sw

def B_x(x):
    print(J)
    return 2*B_sw - J*mu_0*(x_h-x)


    
    

        
h = np.arange(150,300,5)
Ne = np.zeros_like(h)
Te = np.zeros_like(h)
Pb = []

# h = h*1e3     # convert to m
k_b = 1.38e-23 # ref:wiki
e =const.m_e






print("J = {} A".format(J))
print("Sigma = {}".format(sigma))

# print("u^2/sig = ",(u_sw**2)*sigma)






SZA = np.deg2rad(0)

for i,h_i in enumerate(h): 
    # print(h,i)
    Ne[i] = 10**Y_h(h_i,y_Ne,SZA)
    Te[i] = 10**Y_h(h_i,y_Te)
    
    P_ram = e*n_sw*np.power(u_sw,2)
    P_mag = np.power(B_x(h_i*1e3),2)/(2*mu_0)
    print("mag:",P_mag)
    print("ram:",P_ram)
    Pb.append(P_ram+P_mag) 

    # Pe[i] = i#tmp*1.0
    # Pe[i] = (np.power(,2)/(2*mu_0))
    
    

# print(P_val)
# print(Pe)
nkbT = (Ne*1e6)*k_b*Te


# # print(nkbT)
plt.plot(h,nkbT,'o:')

h_new = np.arange(0,300,10)
Pb_new = []


plt.plot(h_new,np.mean(nkbT)*np.ones_like(h_new),'b-')


for i,h_i in enumerate(h_new): 

    
    P_ram = e*n_sw*np.power(u_sw,2)
    P_mag = np.power(B_x(h_i*1e3),2)/(2*mu_0)
    Pb_new.append(P_ram+P_mag) 


plt.plot(h_new,Pb_new,'^:')

# R_indx = np.argmin(np.abs(nkbT - Pb))
# R_ion = h[R_indx]/1e3
# plt.plot([R_ion,R_ion],plt.ylim(),'k:')

plt.ylabel('Pressure components (J = [nkbT])')
plt.xlabel('Altitude (km)')
plt.legend([r'$P_{thermal}$ model',r'$P_{thermal}$ average',r'$P_{sw}$'])