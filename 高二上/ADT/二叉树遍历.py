# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:28:39 2021
@author: lenovo
"""
class Node:                 #建立二叉树（类）
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left    #左子树
        self.right=right  #右子树
        
def preTraverse(root):      #前序遍历
    if root==None: 
        return 
    print(root.value) 
    preTraverse(root.left) 
    preTraverse(root.right)
def midTraverse(root):      #中序遍历
    if root==None: 
        return     
    midTraverse(root.left) 
    print(root.value) 
    midTraverse(root.right)
def afterTraverse(root):    #后序遍历
    if root==None: 
        return     
    afterTraverse(root.left) 
    afterTraverse(root.right)
    print(root.value)
        
#if __name_=='__main_':  #通过二叉树（类）生成对象root
root=Node('A',Node("B",Node('D'),Node('E')),Node('C',right=Node('F',Node('G'))))
print('前序遍历：')
preTraverse(root) 
print('中序遍历：')
midTraverse( root) 
print('后序遍历：')
afterTraverse(root)