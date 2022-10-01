#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:25:40 2022
Author : Hasith Perera

"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# df = pd.read_csv('./data/ace-swepam.txt',skiprows=18,header=None,delimiter="    ")



#file read after treating with a sed 's/    /,/g'>mod.txt
df = pd.read_csv('./data/mod.txt',skiprows=22,header=None,delimiter=",")
# df1 =  pd.read_csv('./data/mod_1.txt',skiprows=22,header=None,delimiter=",")

# 3,4,5 columns has the x,y,z B components

#calculate B_phi/B_r = Bx/-By

val = - df[4]/df[3]

plt.plot(df[3])
plt.plot(df[4])
plt.plot(df[5])

sim_values_1 = [-70.0229296875, 67.89614860774216, 1.3022778209062907e-16]
sim_values_2 = [-7.002292968749998, 3.3948074303871087, 2.2089478087632396e-16]


for val in sim_values_2:
    plt.plot([1,120],[val,val],':')

plt.xlabel('Time (index)')
plt.ylabel('B component (nT)')
plt.legend(['B_x','B_y','B_z'])




