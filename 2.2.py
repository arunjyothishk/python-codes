# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:39:29 2020

@author: arunjyothish
"""

from numpy import *
from math import pi
angle=float(input("Enter an angle to find it's trignometric values: "))
angle*=pi/180
print(sin(angle))
realp=int(input("Enter Real part of an imaginary number: "))
imagp=int(input("Enter Imaginary part of an imaginary number: "))
complex_num=complex(realp,imagp)
print("your Entered imaginary number: ",complex_num)
print("Its real part: ",real(complex_num))
print("Its real part: ",imag(complex_num))

