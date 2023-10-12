# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:43:51 2021

@author: lenovo
"""

class Stack():
    
    def __init__(self):
        self.zhan=[]
    def push(self,num):
        self.zhan.append(num)
    def pop(self):
        return self.zhan.pop()
    def isEmpty(self):
        if len(self.zhan)>0:
            return False
        else:
            return True
if __name__=='__main__':      
    stack1=Stack()  
    stack1.push(1)  
    print(stack1.isEmpty()) 
    print(stack1.pop())
    print(stack1.isEmpty())

