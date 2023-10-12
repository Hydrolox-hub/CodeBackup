# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:54:37 2021

@author: lenovo
"""

stack=[]                       
s=input("请输入逆波兰表达式：")  #6 8 2 - 2 * 3 ÷ +
x=0
for i in range(len(s)):
    ch=s[i]
    if ch>="0" and ch<="9": #处理2位数及以上
        x=x*10+ord(ch)-ord("0")
    elif ch==" ":
        stack.append(x)
        print(stack)
        x=0
    else:
        num1=stack.pop()
        num2=stack.pop()
        if ch=="+":
            x=num2+num1
        if ch=="-":
            x=num2-num1
        if ch=="*":
            x=num2*num1
        if ch=="÷":
            x=int(num2/num1)
print("后缀表达式计算结果为%d"%x)