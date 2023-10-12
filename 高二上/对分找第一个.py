# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 14:59:28 2021

@author: Administrator
"""

key=int(input('要查找的数值：'))
d=[6,12,18,25,25,25,35,46,58,60]
f=False
i=0
j=len(d)-1
while i<=j:
    m=(i+j)//2
    if d[m]<=key:
        j=m-1
    else:
        i=m+1
if d[i]==key:
    print(key,i)
else:
    print('不存在')