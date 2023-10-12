# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input())
a=0
b=1
print(a)
print(b)
for i in range(1,n-1):
    c=a+b
    print(c)
    a=b
    b=c
