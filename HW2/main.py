#import sunpy.data.sample

import cv2 as cv
import sunpy.map

import matplotlib.pyplot as plt
import matplotlib.patches as patches

import numpy as np

import time

from scipy.optimize import curve_fit


def gauss2(x,a0,x0,sig0,a1,x1,sig1,b):
    return func(x,a0,x0,sig0)+func(x,a1,x0,sig1)+b
    
def gauss1(x,a0,x0,sig0,b):
    return func(x,a0,x0,sig0)+b

def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))


def get_sun_thresh(data,debug=0):
    ''' get a threshold for the sun'''
    #get the hist from the image data without NAN's
    freq,indx = np.histogram(data[~np.isnan(data)],100)
    fit_data = np.log(freq)
    
    #init estimates and bounds
    max_indx = np.argmax(fit_data)
    a0 = fit_data[max_indx]
    x0 = indx[max_indx]


    popt, pcov = curve_fit(gauss1, indx[1:],np.log(freq),p0=[a0,x0,0.01,np.min(fit_data)],bounds=[(0,x0-10,0.01,0),(np.inf,x0+10,1,a0)])
    # fit_val =  gauss1(indx[1:],popt[0], popt[1], popt[2],popt[3])
    bw_thresh = popt[1]-1.5*popt[2];
    
    if debug:
        plt.plot(indx[1:],np.log(freq),'o')
        plt.plot([bw_thresh,bw_thresh],[0,a0])
    
    return bw_thresh

def find_ssn(bw):
     
     #normalize
     bw = bw/np.max(bw)
     
     grow = np.zeros(np.shape(bw))
     grow_old = grow+3;

     strel = np.ones([3,3])
     # strel[0,[0,2]]=0
     # strel[2,[0,2]]=0
     # strel = [[0,1,0],[1,1,1],[0,1,0]]
     n = 0
 
     while np.sum(bw)!= 0 :
     # for n in range(0,2):
         active_indx = np.nonzero(bw)
         # print("seed:",active_indx[0][0],active_indx[1][0])
         grow[active_indx[0][0],active_indx[1][0]] = 1
         i = 1
         while np.sum(grow_old-grow)!=0:
         # for i in range(0,50):
         #seed pixel
             grow_old = grow
             grow = grow + ((bw + cv.dilate(grow,strel)) == 2)*1.0

             i = i + 1
         n = n + 1       
         #export stats
         
         # print("n:{} sz:{}".format(n,np.sum(grow)))
         bw = bw-grow>0
     
     return n


image_name = './data/test.fits'




if __name__=='__main__':
    
    # hmi = sunpy.map.Map(image_name)
 
    # # # plotting the data - map/grid
    # # hmi.plot()
    # # hmi.draw_limb()
    # # hmi.draw_grid()
    
    # print(hmi.reference_pixel)
    
    # data = hmi.data
    # # plt.imshow(hmi.data)
    # # plt.plot(hmi.reference_pixel,'or')
    
    # bw_thresh = get_sun_thresh(data,1);
    
    # bw_img = data<bw_thresh;
    
    img = cv.imread('spot_smpl.png');
    bw = img[:,:,1]
    plt.imshow(bw)
    
    ssn = find_ssn(bw)
    print(ssn)
    
   
        # plt.colorbar()
        
        # bw = bw - grow/np.max(grow)
    
        
        
        # break;
    
    #dialate
    
    
    
    # plt.figure(2)
    

    
    
    
    
    
    
