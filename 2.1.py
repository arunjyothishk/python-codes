# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:39:29 2020

@author: arunjyothish
"""

def OPERATION(a,b):
    
    result=a+b
    avg=result/2
        
        
    return result,avg


a=input("Enter first Number: ")

b=input("Enter Second Number: ")
val1,val2 = OPERATION(int(a),int(b))
print("The sum is ",val1,"; The average is ",val2,";")
