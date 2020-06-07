# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:21:11 2019

@author: Akhil
"""

import pandas as pd
import numpy as np
x=pd.read_csv("loan_reduced.csv")
x.shape
print(x.isnull().sum())
'''
nan_mat1 = np.random.random(x.iloc[:,3:4].shape)<0.10
nan_mat1.sum()
df1 = x.iloc[:,3:4].mask(nan_mat1)
dirty = pd.concat([x.iloc[:,3:4],df1],axis = 1)
#dirty.head(10)
dirty.to_csv("loan_dirty.csv")
nan_mat2=np.random.random(df1.iloc[:,6:7].shape)<0.12
nan_mat2.sum()
df2 = df1.iloc[:,6:7].mask(nan_mat1)
dirty2 = pd.concat([df1.iloc[:,3:4],df2],axis = 1)
'''
import random

for i in range(500):
    r=random.randint(1,5850)
    x.iloc[r,6]=np.nan
    x.iloc[r,7]=np.nan
for i in range(561):
    r=random.randint(1,5850)
    x.iloc[r,10]=np.nan
for i in range(300):
    r=random.randint(1,5850)
    x.iloc[r,11]=np.nan
for i in range(450):
    r=random.randint(1,5850)
    x.iloc[r,12]=np.nan
print(x.isnull().sum())
x.to_csv("loan_dirty.csv")