# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:34:29 2022

@author: Administrator
"""

s=''
n=int(input('请输入要转换的十进制数：'))
k=int(input('请输入要转换的进制数：'))
while n > 0:
    r=n%k
    n//k
    if 0<=r<=9:
        s1=str(r)
    else:
        s1=chr(r+65)
    s=s1+s
print('转换后:',s)



h=input('待转换的值：')
k=int(input('要转的位数：'))
num=0
for i in range(0,len(h),1):
    ch=h(i)
    if 'A'<=ch<='Z':
        x=ord(ch)-55
    else:
        x=int(ch)
    num=num*k+x
print(num)


    