# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:26:30 2021

@author: lenovo
"""
# 选择排序1
d=[5,2,6,1,7,3,4]
n=len(d)
for i in range(0,n-1):
    for j in range(i+1,n):
        if d[j]<d[i]:
            d[i],d[j]=d[j],d[i]
print(d)

# 选择排序2
d=[5,2,6,1,7,3,4]
n=len(d)
for i in range(0,n-1):
    k=i
    for j in range(i+1,n):
        if d[j]<d[k]:
            k=j
    d[i],d[k]=d[k],d[i]
print(d)

# 选择排序3
d=[5,2,6,1,7,3,4]
n=len(d)
for i in range(0,n-1):
    k=i
    for j in range(i+1,n):
        if d[j]<d[k]:
            k=j
    if i!=k:
        d[i],d[k]=d[k],d[i]
print(d)

#双向选择排序
d=[7,2,6,1,5,3,4]
p=0
q=len(d)-1
while p<q:
    min=p;max=q
    for i in range(p,q+1):
        if d[i]<d[min]: 
            min=i       
        if d[i]>d[max]: 
            max=i
    d[p],d[min]=d[min],d[p]
    if max==p: 
        max=min
    d[q],d[max]=d[max],d[q]
    p=p+1
    q=q-1
print(d)