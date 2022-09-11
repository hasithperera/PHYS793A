#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 00:04:45 2022
Author : Hasith Perera

"""

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd


import astropy.units as u
from astropy.time import Time, TimeDelta

import sunpy.timeseries as ts
from sunpy.net import Fido
from sunpy.net import attrs as a
from sunpy.time import TimeRange


time_range = TimeRange("2010-01-01 00:00", "2022-04-17 00:00")
result = Fido.search(a.Time(time_range), a.Instrument('noaa-indices'))
f_noaa_indices = Fido.fetch(result)

# file = 'out_const_thresh.dat'
# file = 'ahe.dat'
file = './out/out_auto_thresh.dat'

df = pd.read_csv(file,header=None,delimiter=',',names=['date','ssn','bw_thresh'])
df['date_fix'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')
plt.plot(df['date_fix'],df['ssn'],'o:',label='SDO HMI based SSN')

noaa = ts.TimeSeries(f_noaa_indices, source='noaaindices').truncate(time_range)
plt.plot(noaa.index, noaa.quantity('sunspot RI'), label='NOAA based SSN')
plt.legend()