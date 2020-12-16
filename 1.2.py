# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:39:29 2020

@author: arunjyothish
"""

var=input("Input a number : ")
var2=input("input other number :")
var=int(var)
var2=int(var2)

var=var+var2
    
if var < 0:
    print("Sum of The numbers is Negative")
elif var>0:
    print("Sum of The numbers is an Positive")
else:
    print("Sum of The numbers is Zero")
print("Exiting ..")