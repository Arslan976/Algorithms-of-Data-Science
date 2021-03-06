# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:42:05 2021

@author: hp
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
#%matplotlib inline

dataframe = pd.DataFrame({
    'x': [12, 20, 28, 28, 29, 33, 24, 45, 45, 52, 52, 52, 55, 53, 55, 61, 64, 69, 72],
    'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
    })

np.random.seed(200)
k = 3

centroids = {
    i + 1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}

fig = plt.figure(figsize=(5, 5))
plt.scatter(dataframe['x'], dataframe['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()
