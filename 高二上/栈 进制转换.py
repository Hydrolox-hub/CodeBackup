# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input("请输入:"))
st=[-1]*40
top=-1
ans=0
while n!=0:
   top+=1
   ans=n % 2
   st[top]=ans
   n//=2
   
while top!=-1:
    print(st[top],end="")
    top-=1
    