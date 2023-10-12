# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fibo(n):
    if n==1:
        s=1
    elif n==0:
        s=0
    else:
        s=fibo(n-1)+fibo(n-2)
    return s
n=int(input())
print(fibo(n))

#优化
s1=[]*int(n)
s2=[False]*int(n)
def fibo(n):
    if n==1:
        s=1
    elif n==0:
        s=0
    
    return s
n=int(input())
print(fibo(n))
         