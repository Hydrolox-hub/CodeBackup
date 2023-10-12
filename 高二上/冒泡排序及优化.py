# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:00:19 2021

@author: lenovo
"""
#python内部排序
a=[5,7,6,1,2,3,4]
b=sorted(a)
print(a)
print(b)
a.sort()
print(a)
a.sort(reverse=True)
print(a)


#冒泡排序
d=[5,7,6,1,2,3,4]
def bubble_sort(d):
    length=len(d)
    for i in range(1,length):
        for j in range(0,length-i):
            if d[j]>d[j+1]:
                temp=d[j]
                d[j]=d[j+1]
                d[j+1]=temp
bubble_sort(d)
print(d)


#冒泡排序优化1
dd=[5,7,6,1,2,3,4]
count=0
def bubble_sort_opt(d):
    flag=False
    global count
    length=len(d)
    for i in range(1,length):
        flag=False
        count+=1
        for j in range(0,length-i):
            if d[j]>d[j+1]:                
                temp=d[j];d[j]=d[j+1];d[j+1]=temp
                flag=True
        if flag==False:
             break
bubble_sort_opt(dd)
print(count)
print(dd)

#冒泡排序优化2
dd=[5,3,4,1,2,6,7]
def bubble_sort_opt_2(d):
    length=len(d)
    last=length-1
    for i in range(1,length):
        for j in range(0,last):
            if d[j]>d[j+1]:              
                d[j],d[j+1]=d[j+1],d[j]
                pos=j
        last=pos
bubble_sort_opt_2(dd)
print(dd)

#冒泡排序优化1_2
dd=[5,3,4,1,2,6,7]
def bubble_sort_opt_1_2(d):
    flag=False
    length=len(d)
    last=length-1
    for i in range(1,length):
        flag=False
        for j in range(0,last):
            if d[j]>d[j+1]:              
                d[j],d[j+1]=d[j+1],d[j]
                flag=True
                last=j
        if flag==False:
             break
bubble_sort_opt_1_2(dd)
print(dd)

# 双向冒泡排序
dd=[5,3,4,1,2,6,7]
def bubble_sort_lr(d):
    l=0
    r=len(d)-1
    while l<r:
        for i in range(l,r):
            if d[i]>d[i+1]:
               d[i],d[i+1]=d[i+1],d[i] 
        r=r-1
        for i in range(r,l,-1):
            if d[i]<d[i-1]:
               d[i],d[i-1]=d[i-1],d[i] 
        l=l+1
bubble_sort_lr(dd)
print(dd)

# 双向冒泡排序优化
dd=[5,3,4,1,2,6,7]
def bubble_sort_lr_opt(d):
    st=0
    ed=len(d)-1
    k=1
    while st!=ed:
        for i in range(st,ed,k):
            if d[i]*k>d[i+k]*k:
                d[i],d[i+k]=d[i+k],d[i]
                last=i
        ed=last;k=-k
        st,ed=ed,st             
bubble_sort_lr_opt(dd)
print(dd)