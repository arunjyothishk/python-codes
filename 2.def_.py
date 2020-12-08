# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:39:29 2020

@author: arunjyothish
"""

def OPERATION(a,b,c):
    if c=="+":
        result=a+b
        other="a+b"
    elif c=="-":
        result=a-b
        other="a-b"
    elif c=="*":
        result=a*b
        other="a*b"
    else:
        result=a/b
        other="a/b"
        
    return result,other


a=input("Enter first Number: ")
c=input("Enter operator symbol: ")
b=input("Enter Second Number: ")
val1,val2 = OPERATION(int(a),int(b),c)
print("Operation performed ",val2," The result is ",val1)