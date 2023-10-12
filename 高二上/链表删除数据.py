# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:45:12 2021

@author: Administrator
"""

from random import randint
data=[]
head=0
tmp=randint(95,100)
data.append([tmp,-1])
for i in range(1,20):
    tmp=tmp-randint(0,5)
    data.append([tmp,-1])
    data[i-1][1]=i
print(data)
n=int(input("请输入："))
flag=False
if data[0][0]==n:
    head=data[head][1]
    print("已找到n的位置：")
    print(0)
p=head
while(p!=-1):
    q=data[p][1]
    if data[q][0]==n:
        print("已找到n的位置：")
        print(q)
        flag=True
        data[p][1]=data[q][1]
    p=q
if flag==False:
    print("没有找到")
a=head
while data[a][1]!=-1:
    print(data[a],end=" ")
    a=data[a][1]
print(data[a])