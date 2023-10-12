# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

d=[7,99,77,16,33,44,55,24]
def bubble_sort(a):
    n=len(a)
    for i in range(1,n):
        for j in range(0,n-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
print(bubble_sort(d))