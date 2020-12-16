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

length=len(arr1)

def classic_method(arr1,arr2):
    result=zeros((length,length)) # initializing result matrix (row*coloum)
    for i in range(length):  #row loop
        for j in range(length):
            result[i][j]=arr1[i]*arr2[j]
    return result

def vectorization_method(arr1,arr2):
    result=outer(arr1,arr2)
    return result

time_init=time.time()
print(classic_method(arr1,arr2))
time_end=time.time()
print()
print("Process time classical method: ",(time_end-time_init)*1000,"ms")
print()

time_init=time.time()
print(vectorization_method(arr1,arr2))
time_end=time.time()
print("Process time vectorization method: ",1000*(time_end-time_init),"ms")