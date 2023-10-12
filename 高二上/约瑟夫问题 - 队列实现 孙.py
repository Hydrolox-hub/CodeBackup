# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:29:36 2021

@author: lenovo
"""

#import time
llist=[0]
n=int(input(" 请输入参与人数（ N ） :"))
m=int(input(" 请输入淘汰数（ M ） :"))
#开始计时
#start = time.clock()

head=0
tail=0
a=int(n*0.5*(n+1))
que=[""]*a
for i in range(n):
    que[tail]=str(i)
    tail+=1
k=1
while head<tail:
    while k<m:
        que[tail]=que[head]
        head+=1
        k+=1
        tail+=1
    head+=1
    k=1
print(str(int(que[head-1])+1))
#end = time.clock()
#print("it  cost %s s for func running " %(end - start))