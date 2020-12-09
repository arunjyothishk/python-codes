
# Consolas, 'Courier New', monospace 
# 'cascadia code'
# 'fira code'

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:39:29 2020

@author: arunjyothish
"""
import math

name=input("Enter your Name: ")

print("Hello "+name+" !")

while("y"==input("Check a number ? y/n : ")):
    
    var=input("Input a number : ")
    var=int(var)
    
    if var ==0:
        print("The number is Zero")
    elif var%2 ==0:
        print("The number is an Even")
    else:
        print("The number is Odd")

print("Exiting ..")