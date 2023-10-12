# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=[16,55,79,99,12,46,77,44]
num=0
def bubble_sort(k):
    n=len(k)
    #global num
    #num=0
    for i in range(1,n):
        for j in range(0,n-i):
            if k[j]>k[j+1]:
                k[j],k[j+1]=k[j+1],k[j]
                #num+=1
    return k
def bubble_sort_re(k):
    n=len(k)
    #global num
    #num=0
    for i in range(1,n):
        for j in range(0,n-i):
            if k[j]<k[j+1]:
                k[j],k[j+1]=k[j+1],k[j]
                #num+=1
    return k
def bubble_sort_1(k):
    n=len(k)
    #global num
    #num=0
    flag=True
    for i in range(1,n):
        if not flag:
            break
        for j in range(0,n-i):
            flag=False
            if k[j]>k[j+1]:
                k[j],k[j+1]=k[j+1],k[j]
                flag=True
                #num+=1
    return k
def bubble_sort_2(k):
    n=len(k)
    last=n-1
    #global num
    #num=0
    for i in range(1,n):
        for j in range(0,last):
            if k[j]>k[j+1]:
                k[j],k[j+1]=k[j+1],k[j]
                last=j
                #num+=1
    return k
def bubble_sort_3(k):
    n=len(k)
    flag=True
    last=n-1
    #global num
    #num=0
    for i in range(1,n):
        if not flag:
            break
        for j in range(0,last):
            flag=False
            if k[j]>k[j+1]:
                k[j],k[j+1]=k[j+1],k[j]
                flag=True
                last=j
                #num+=1
    return k
print(bubble_sort(a))
print(bubble_sort_re(a))
print(bubble_sort_1(a))
print(bubble_sort_2(a))
print(bubble_sort_3(a))
#print(num)
def bubble_sort_double(k):
    n=len(k)
    L=0
    R=n-1
    while L<R:
        for i in range(L,R):
            if k[i]>k[i+1]:
                k[i],k[i+1]=k[i+1],k[i]
        R=R-1
        for i in range(R,L,-1):
            if k[i]<k[i+1]:
                k[i],k[i-1]=k[i-1],k[i]
        L=L+1
    return k
print(bubble_sort_double(a))

