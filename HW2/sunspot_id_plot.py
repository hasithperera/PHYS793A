#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 13:07:34 2022
Author : Hasith Perera

"""

from main import *
import matplotlib.pyplot as plt
import cv2 as cv

import numpy as np

image_name ='./data/hmi.Ic_noLimbDark_720s.20140321_000000_TAI.1.continuum.fits'


if __name__=='__main__':
    
    hmi = sunpy.map.Map(image_name)
    bw_thresh = get_sun_thresh(hmi.data);
    
    plt.subplot(121)
    plt.imshow(hmi.data[2100:2500,2500:3050],cmap='gray')
    bw_img = hmi.data<bw_thresh;
    
    bw_img = bw_img*1.0
    plt.title('HMI IC limb corrected data')
    
    plt.subplot(122)
    plt.imshow(hmi.data[2100:2500,2500:3050])
    
    strel = np.array([[0,1,0],[1,1,1],[0,1,0]]).astype(np.uint8)
    # bw_img = cv.morphologyEx(bw_img.astype(np.uint8),cv.MORPH_ERODE,strel)
    # bw_img = cv.morphologyEx(bw_img.astype(np.uint8),cv.MORPH_ERODE,strel)
    
    ssn,id1=find_ssn_ahe(bw_img[2100:2500,2500:3050])
    
    alpha = np.ones(np.shape(bw_img[2100:2500,2500:3050]));
    
    
    
    plt.imshow(id1,alpha=1,cmap='jet')
    plt.title('Identified spots')
    # plt.colorbar()

    
    
