# -*- coding: utf-8 -*-
"""
Created on Wed Dec  16 10:39:29 2020

@author: arunjyothish
"""

from numpy import array as arr

print("3+4j,5+6j,7+2j,2+3j\n")

complx_inp = input("Enter complex numbers ( ',' seperated ) : ")


cmplx_list = complx_inp.split(',')

# print(cmplx_list)

p = arr(cmplx_list)
q = arr(cmplx_list,dtype=int)

print("Complex array : \n",p)
print("Integer array : \n",q)
r = p * q
print("Product of Integer array and complex array : \n", r)
