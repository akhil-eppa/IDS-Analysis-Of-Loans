# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:20:40 2019

@author: Akhil
"""
import pandas as pd
x=pd.read_csv("loan_dirty.csv")
print(x.isnull().sum())
x_fill=x.fillna(x.mean())
print(x_fill.isnull().sum())
x_fill=x_fill.fillna(method="ffill")
x_fill.iloc[:,1:].to_csv("loan.csv")