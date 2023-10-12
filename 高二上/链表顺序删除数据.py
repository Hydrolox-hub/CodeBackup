# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:35:50 2021

@author: lenovo
删除某个节点
"""

from random import randint
llist=[]
n=10
for i in range(n-1):
    llist.append([randint(1, 100),i+1])
llist.append([randint(1, 100),-1])  # 将尾结点的指针指向头结点，构成循环单向链表
print("\n输出删除前的链表:")
print(llist)

head=0
data=int(input("请输入删除的数字:"))
p=head
if llist[head][0]==data:
    head=llist[head][1]
else:   
    q=llist[p][1]
    while  llist[q][0]!=data and q!=-1:
        p=q
        q=llist[p][1]
    if q==-1:
        print("输入的数字不存在!")
    else:
        llist[p][1]=llist[q][1]
        
print("\n输出删除后的链表:")
p=head
print(llist)
'''
while p!=-1:
    print(llist[p][0])
    p=llist[p][1]
    '''