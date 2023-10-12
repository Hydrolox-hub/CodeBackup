# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:01:21 2021

@author: lenovo
"""

# 四则运算式6 + ( 8 - 2 ) * 2 ÷ 3(中间有一个空格分开)
#运算规则的优先级
ops_rule = {
    '+': 1,
    '-': 1,
    '*': 2,
    '÷': 2
}

s=input("输入中缀表达式（格式如 6 + ( 8 - 2 ) * 2 ÷ 3 ）：")
ss=s.split()
ops=[' ']*100
top=-1
for item in ss:
    if item in ['+', '-', '*', '÷']:
        while top>=-1:
            if top==-1:
                top+=1
                ops[top]=item
                break
            else:
                if ops[top]=="(" or ops_rule[item]>ops_rule[ops[top]]:
                    top+=1
                    ops[top]=item
                    break
                else:
                    print(ops[top]," ",end="")
                    top-=1
    elif item=="(":
        top+=1
        ops[top]=item 
    elif item==")":
        while top>=0:
            if ops[top]=="(":
                top-=1
                break
            else:
                print(ops[top]," ",end="")
                top-=1
    else:
        print(item," ",end="") 
while top>=0:
    print(ops[top]," ",end="")
    top-=1

