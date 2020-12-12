# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:39:29 2020

@author: arunjyothish
"""


list_var=[10,20,30,50,10]

count=element=total=0
for element in list_var:
    total+=element
    count+=1
print("Sum of List Elements is: "+str(total))
average=total/count
print("The Average of List Elements is: "+str(average))
