# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:10:19 2021

@author: Myself
"""
a=[5,2,6,1,7,3,4]
"""1、冒泡排序 基础版"""
n=len(a)
for i in range(1,n):
    for j in range(0,n-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)




"""2、冒泡排序 flag 优化版"""
a=[5,2,6,1,7,3,4]
n=len(a)
flag=True
for i in range(1,n):
    for j in range(0,n-i):
        flag=False
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            flag=True
    if not flag:
        break
print(a)



"""3、冒泡排序 last 优化版"""
a=[5,2,6,1,7,3,4]
n=len(a)
last=n-1
for i in range(1,n):
    for j in range(0,last):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            last=j
print(a)



"""4、冒泡排序 flag+last 优化版"""
a=[5,2,6,1,7,3,4]
n=len(a)
last=n-1
flag=True
for i in range(1,n):
    for j in range(0,last):
        flag=False
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            last=j
            flag=True
    if not flag:
        break
print(a)



"""5、冒泡排序 双向 基础版"""
a=[5,2,6,1,7,3,4]
l=0
r=len(a)-1
while l < r:
    for i in range(l,r):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    r=r-1
    for i in range(r,l,-1):
        if a[i]<a[i+1]:
            a[i],a[i-1]=a[i-1],a[i]
    l=l+1
print(a)

"""6、冒泡排序 双向 升级版（*）"""




"""7、选择排序 基础版"""
a=[5,2,6,1,7,3,4]
n=len(a)
for i in range(0,n-1):
    k=i
    for j in range(i+1,n):
        if a[j]<a[k]:
            k=j
    if i!=k:
        a[i],a[k]=a[k],a[i]
print(a)
            
    


"""8、选择排序 双向"""