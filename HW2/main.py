#import sunpy.data.sample

import cv2 as cv
import sunpy.map

import matplotlib.pyplot as plt
import matplotlib.patches as patches

import glob as glob

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
        plt.figure(2)
        plt.plot(indx[1:],np.log(freq),'o')
        plt.plot([bw_thresh,bw_thresh],[0,a0])
    
    return bw_thresh



def find_ssn_ahe(bw):
     
     #normalize
     bw = bw/np.max(bw)
     id_img = np.zeros(np.shape(bw))
     
     grow = np.zeros(np.shape(bw))
     grow_old = grow+3;

     strel = np.ones([3,3])
     # strel = np.array([[0,1,0],[1,1,1],[0,1,0]]).astype(np.uint8)
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
         
         
         bw = bw-grow>0
         id_img = id_img + (grow>0)*1.0;
         print("n:{} sz:{} mx:{}".format(n,np.sum(grow),np.max(id_img)))
         
     
     return n,id_img

# based on my work from the flake detection
# https://github.com/hasithperera/cenlab-tools/blob/main/src/flake_filter.py

def find_ssn(data):
    ''' Using opencv to find spots'''
    
    data = data.astype(np.uint8);
    strel = np.ones([3,3]);
    
    
    blobs, hierarchy = cv.findContours(data, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    return blobs

def get_blob_details(blob,size=5):

    true_size = len(blob)
        # print(i,"size:",len(blob))
    x = []
    y = []
    if len(blob)>size:
        
        
        for p in blob:
            if p!=np.nan:
                print(p)
                val = p
                print('valiid')
                x.append(p[0][0])
                y.append(p[0][1])
    
        center_x = np.min(x)
        center_y = np.min(y)
        height = max(x) - min(x)
        width = max(y) - min(y)
        return [true_size,center_x, center_y,height,width,true_size]
    else:
        return []
    
    
# not currently working
# WPI: need to figure out a better way to get the blob stats anc centers out 
# handel NAN values 

def label_spots(blobs):
    for blob in blobs:
        blob_stats = get_blob_details(blob,5)
        if (len(blob_stats)>0):
            # ROI.append(blob_stats)
            rect = patches.Rectangle((blob_stats[1], blob_stats[2]), blob_stats[3], blob_stats[4], linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

    
    
def process_file(hmi):
    '''find ssn and return the number'''
    bw_thresh = .91#get_sun_thresh(hmi.data);
    
    bw_img = hmi.data<bw_thresh;
    
    strel = np.array([[0,1,0],[1,1,1],[0,1,0]]).astype(np.uint8)

    bw_img = cv.morphologyEx(bw_img.astype(np.uint8),cv.MORPH_ERODE,strel)   
    blobs = find_ssn(bw_img)
    ssn = len(blobs)
    
    return [ssn,bw_thresh]


# image_name = './data/test.fits'

# #active sun - 2014 image
# image_name ='./data/hmi.Ic_noLimbDark_720s.20140321_000000_TAI.1.continuum.fits'

#inactive sun- 2020 image
image_name ='./data/hmi.Ic_noLimbDark_720s.20200418_000000_TAI.3.continuum.fits'



if __name__=='__main__':
    
    err = 0
    i = 0 
    files = glob.glob('./data/*.fits')
    files.sort()
    with open('out_91_thresh.dat','a+') as fp:
        for image_name in files:
            hmi = sunpy.map.Map(image_name)
            i = i + 1
            print(i)
            try:
                
                info = process_file(hmi)
                print(image_name)
                fp.write("{},{},{}\n".format(hmi.date.value,info[0],info[1]))
            except:
                err = err + 1
                continue
    print(err)
    # # # plotting the data - map/grid
    # # hmi.plot()
    # # hmi.draw_limb()
    # # hmi.draw_grid()
    

    