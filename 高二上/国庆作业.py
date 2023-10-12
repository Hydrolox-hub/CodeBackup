# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:49:59 2021

@author: Administrator
"""

from random import randint
llist=[]
n=randint(10,15)
for i in range(n-1):
    llist.append([randint(1, 100),i+1])
llist.append([randint(1, 100),-1])  
print("\n输出前的链表:")
print(llist)

head=0
p=head
q=llist[p][1]
x=0
while q!=-1:
    p=q
    q=llist[p][1]
    x+=0.5
print('中间节点是:')
print(llist[int(x)])
