
# main.py 

import numpy as np
import matplotlib.pyplot as plt

from scipy.special import eval_legendre

y_Ne = np.zeros([4,5])
y_Te = np.zeros([4,5])

# model implementation A(l,n) n values
n_actual = [0,1,2,-1,-2]


# Ne model from the paper
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


# Te model from the paper
y_Te[0,:] = [2.1855,4.4093,-4.2144,.2070,-.01284]
y_Te[1,:] = [-.9786,3.7677,-4.7405,.1190,-.005077]
y_Te[2,:] = [.2465,-.2892,-0.8883,-.03985,.001987]
y_Te[3,:] = [-.02676,-.4893,0.7477,.03220,-.002536]

mu_0 = 1.256e-6 # ref:wiki
x_l = 1e5
x_h = 3e5

k_b = 1.38e-23 # ref:wiki

SZA = np.deg2rad(0)

def fun_eq1(l,n,h,y,SZA=0):
    # Te,Ne model based on observations 
    
    # print("{},{}: {}".format(l,n_actual[n],y[l,n]))
    return y[l,n]*eval_legendre(l,np.cos(SZA))*np.power(h/2000,n_actual[n])
 

# get Te,Ne as a function of altitude
def Y_h(h,y,SZA=0):
    y_sum = 0
    # print(y)
    for l in range (0,4):
        for n in range(0,5):
            y_sum = y_sum + fun_eq1(l,n,h,y,SZA)
    return y_sum

#Q1 conditions to find sigma
def B_x(x,B_sw,J):
    return 2*B_sw - J*mu_0*(x_h-x)


# neumerically get the pressure balance condition
def get_R_ion(B_sw,u_sw,J,debug=1):
    h = np.arange(160,300,5)
    Ne = np.zeros_like(h)
    Te = np.zeros_like(h)
    Pb = []
    
    #populate the pressure conditions    
    for i,h_i in enumerate(h): 
        # print(h,i)
        Ne[i] = 10**Y_h(h_i,y_Ne,SZA)
        Te[i] = 10**Y_h(h_i,y_Te)
        
        Pb.append(np.power(B_x(h_i*1e3,B_sw,J),2)/(2*mu_0)) 
    
    # get particle pressure based on 
    # model Ne,Te values
    
    nkbT = (Ne*1e6)*k_b*Te
    
    #find the balance neumerically 
    R_indx = np.argmin(np.abs(nkbT - Pb))
    R_ion = h[R_indx]
    
    plt.plot(h,nkbT)
    plt.plot(h,Pb)
    plt.plot(h[R_indx],nkbT[R_indx],'ro')
    h[R_indx]/1e3
    
    return R_ion
  
    
if __name__=='__main__':
    
    #define initial conditions
    B_sw = 50e-9 #T
    u_sw = 6e6 #ms^-1
    
    
    #find B based on the condition that field at h=100km goes to 0
    J = B_sw*2/(x_l*mu_0)
    sigma = 2/((x_h-x_l)*mu_0*u_sw)
    
    B_sw_list = []
    U_sw_list = []
    R_ion = []
    
    # # find the variation of R_ion with B_sw
    # for B_sw in range (50,100,10):
        
    #     J = (B_sw*1e-9)*2/(x_l*mu_0)
    #     B_sw_list.append(B_sw)
    #     R_ion.append(get_R_ion(B_sw*1e-9,u_sw,J))
    
    
    # find the variation of R_ion with U_sw
    for U_sw in range (400,600,20):
        
        U_sw_list.append(U_sw)
        R_ion.append(get_R_ion(B_sw*1e-9,u_sw*1e3,J))
    
    
    plt.figure(2)
    
    plt.plot(U_sw_list,R_ion,'o-')
    plt.xlabel("$U_{sw}$  ($kms^{-1}$)")
    plt.ylabel(r'$R_{ion}$ altitude (km)')
        
