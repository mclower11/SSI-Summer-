# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 11:09:05 2018

@author: mclower
"""

import numpy as np
n=6
p1=5
p2=3
def f(n,p1,p2):
    Sum=0
    for ii in range(n):
        if(ii % p1 == 0):
            Sum= Sum +ii
        elif(ii % p2==0):
            Sum=Sum +ii
    
    
    return Sum
X=f(n,p1,p2)
print(X)

