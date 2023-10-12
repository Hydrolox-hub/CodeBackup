# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 10:54:07 2021

@author: Administrator
"""

d=[10,16,18,30,67,69,91,98,99]
key=int(input('要查找的数值：'))
i=0
j=len(d)-1
while i <= j:
    m=(i+j)//2
    if d[m]==key:
        print('找到，下标为：',m)
        break
    elif key<d[m]:
        j=m-1
    else:
        i=m+1
if i>j:
    print('未找到')