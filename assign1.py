# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:20:14 2018
@author: chandu
"""
import random

def genrandom(a, b):
    if a > b:
        return 'please enter valid input';
    arr=[];   
    for i in range(10):
        arr.append(random.randint(a, b));
#    else:
 #        print('something went wrong');
     return arr       
        
        
print('random numbers are',genrandom(1,20));        
    
    
