# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
data1=input('输入字符串:')
ue=0
le=0
nu=0
el=0
for i in range(len(data1)):
    n=data1[i]
    if n<='9' and n>='0':
        nu+=1
    if n<='z' and n>='a':
        le+=1
    if n<='Z' and n>='A':
        ue+=1
    
    
