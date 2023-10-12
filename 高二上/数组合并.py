# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 07:49:54 2021

@author: Administrator
"""

from random import randint

a=[0]*20
b=[0]*15
c=[0]*35
a[0]=randint(95,100)
for i in range(1,20):            #随机产生降序数据序列一
    a[i]=a[i-1]-randint(1,5)
b[0]=randint(95,100)
for i in range(1,15):            #随机产生降序数据序列二
    b[i]=b[i-1]-randint(1,5) 
print('原始数据序列一为:')
print(a)
print('原始数据序列二为:')
print(b)
i=0
j=0
k=0
while(i<20 and j<15):            #合并数据直至某个数组数据合并完成
    if a[i]>=b[j]:
        c[k]=a[i]
        i=i+1
        k=k+1
    else:
        c[k]=b[j]
        j=j+1
        k=k+1
while i<20:                      #当数据序列一中还有数据时的处理
    c[k]=a[i]
    i=i+1
    k=k+1
while j<15:                      #当数据序列二中还有数据时的处理                  
    c[k]=b[j]
    j=j+1
    k=k+1
print('合并后的数据序列为:')
print(c)