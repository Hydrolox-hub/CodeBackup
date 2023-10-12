# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:52:53 2021

@author: lenovo
"""
import sys
sys.path.append('../')
#sys.path.append('C:/Users/lenovo/Desktop/2020级高二/选修1 数据与数据结构/3-3 栈/代码')
import Stack
N=int(input("输入一个十进制数："))
stack2 = Stack.Stack()
num = ''
digits = "0123456789ABCDEF"						
while N > 0:
    stack2.push(N%16)						#入栈
    N = N//16
while not stack2.isEmpty():
    num += digits[stack2.pop()]
print(num)