# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:49:50 2021

@author: lenovo
"""

from random import randint
n=[[0 for i in range(2)]for j in range(10)]
data=randint(1, 100)
n[0][0]=data    #第1个节点赋值
n[0][1]=-1   
print("第1个节点：[" +str(data)+",-1]") 
 
head=0          #初始化头节点 
for i in range(1,10):
    data=randint(1, 100)  
    n[i][0]=data    #第i+1个节点赋值
    print("第"+str(i+1)+"个节点数据：" +str(data))
    
    p=head #每次产生的新数据都要从 头节点 开始比较大小
    if data<=n[head][0]: #新产生的 i节点data 比 头节点数据 还要小
        head=i      #更新头指针，i成为头节点
        n[i][1]=p   #新节点i 指向 原头节点
    else:
        q=n[p][1]   #p为头节点，q为头节点的下一个节点
        while n[q][0]<data and q!=-1:
            p=q     #迭代
            q=n[p][1]   #q为p的下一个节点
        n[p][1]=i   #i节点插入p，q之间，修改p节点的指针，指向i（位置）
        n[i][1]=q   #i节点的指针指向q
        
    print("逐步无序输出链表:");print(n)  
#根据data值有序输出链表
print("\n根据data值有序输出链表:")
p=head
while p!=-1:
    print(n[p][0])
    p=n[p][1]
   