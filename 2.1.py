# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:39:29 2020

@author: arunjyothish
"""

def OPERATION(a,b):
    try:
        a,b=float(a),float(b)
        result=a+b
        avg=result/2
    except ValueError:
        print("FUNCTION RECEIVE INTEGER ARGUMENTS ONLY")
        result=avg=0
        
        
    return result,avg


a=input("Enter first Number: ")

b=input("Enter Second Number: ")
val1,val2 = OPERATION(a,b)
print("The sum is ",val1,"; The average is ",val2,";")
