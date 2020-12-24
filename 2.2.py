# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:39:29 2020

@author: arunjyothish
"""
from numpy import *

def complx():
    comp=complex(input("Enter a complex number: "))
    print("Entered complex number is : ",comp)
    print("Real part of the complex number is : ",real(comp))
    print("Imaginary part of the complex number is : ",imag(comp))

def sinn():
    angle=float(input("Enter angle in degree : "))
    rad=angle*pi/180
    # print("Angle in radian : ",rad)
    print("Sine value of the angle : ",round(sin(rad),3))

def sincc():
    angle_str=input("Enter angles seperated with ','  : ")
    list_angles=angle_str.split(',')
    print("Entered angles list: ",list_angles)
    rad=[]
    
    for count in range(len(list_angles)):
        rad.insert(count,float(list_angles[count])*pi/180)
    print("Radian angle list : ",rad)
    sinc_values=sinc(rad)
    print("Sinc values list : ",sinc_values)


complx()
print()
sinn()
print()
sincc()
print()

