# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:04:11 2021

@author: Administrator
"""

#import time
list=[]
n=int(input(" 请输入参与人数（ N ） :"))
m=int(input(" 请输入淘汰数（ M ） :"))
#start = time.clock()
for i in range(n-1):
    list.append([i+1,i+1])
list.append([n,0])
head=0
long=n
k=head
i=1
while long>1:
    i=i+1
    if i==m:
        t=list[k][1]
        list[k][1]=list[t][1]
        if t==head:
            head=list[k][1]
        i=1
        long=long-1
    k=list[k][1]
print(list[head][0])
#end = time.clock()
#print("it  cost %s s for func running " %(end - start))