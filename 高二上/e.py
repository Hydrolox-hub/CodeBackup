# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:54:05 2021

@author: Administrator
"""

e=0
jc=1
i=0
while 1/jc >= 0.00001:
    e=e+1/jc
    i+=1
    jc=jc*i
print(round(e,5))