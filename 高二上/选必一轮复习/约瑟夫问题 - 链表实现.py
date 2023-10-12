# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:23:13 2021

@author: lenovo
"""

import time
llist=[]
n=int(input(" 请输入参与人数（ N ） :"))
m=int(input(" 请输入淘汰数（ M ） :"))
#开始计时
start = time.perf_counter()

for i in range(n-1):
    llist.append([i+1,i+1])
llist.append([n,0])  # 将尾结点的指针指向头结点，构成循环单向链表
head=0
long=n
k=head
i=1
while long>1:
    i=i+1  # k  s
    if i==m:
        t=llist[k][1]
        llist[k][1]=llist[t][1]
        if t==head: # 删除结点为头结点
            head=llist[k][1]
        i=1
        long=long-1
    k=llist[k][1]    
print(llist[head][0])

end = time.perf_counter()
print("\n it  cost %s s for func running " %(end - start))