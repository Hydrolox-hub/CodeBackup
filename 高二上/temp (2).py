# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

que=[""]*100
head=0
tail=0
s=input("请输入字符串：")
for i in range(len(s)):
    que[tail]=s[i]
    tail+=1
while head<tail:
    print(que[head])
    head+=1
    if head=tail:
        que[tail]=que[head]
        tail+=1
        head+=1