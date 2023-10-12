# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:59:10 2021

@author: Administrator
"""

pi=0
fm=1
i=1
while abs(1/fm) >= 0.0000001:
    pi=pi+i*1/fm
    fm+=2*i
    i+=i/abs(i)*1
    i=-i
pi=pi*4
print(round(pi,6))