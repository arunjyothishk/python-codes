# -*- coding: utf-8 -*-
"""
Created on Wed Dec  16 10:39:29 2020

@author: arunjyothish
"""
from numpy import *
import time
arr1=arange(0,1000) # assuming as a row matrix
# print(arr1)
arr2=arange(1000,2000) # assuming as a coloum matrix

def classic_method(arr1,arr2):
    result=zeros(len(arr1),len(arr2)) # initializing result matrix (row*coloum)
    for i in range(len(arr1)):  #row loop
        for j in range(len(arr2)):
            result[i][j]=arr1[i]*arr2[j]
    return result

def vectorization_method(arr1,arr2):
    result=arr1+arr2
    return result

time_init=time.time()
classic_method(arr1,arr2)
time_end=time.time()
print("Process time classical method: ",time.end-time.init)
print()

time_init=time.time()
vectorization_method(arr1,arr2)
time_end=time.time()
print("Process time vectorization method: ",time.end-time.init)