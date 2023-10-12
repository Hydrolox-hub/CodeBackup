# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:51:27 2022

@author: Administrator
"""

def main():
    print("请选择数字1或2：")
    print("1:加密")
    print("2:解密")
    se=input()
    if se == "1":
        code = input("请输入加密字符串：")
        key=int(input("请输入8位秘钥："))
        encrypt(code,key)
    if se == "2":
        code = input("请输入解密字符串：")
        key=int(input("请输入8位秘钥："))
        decrypt(code,key)
def encrypt(code,key):
    for i in key:
        key_d=key_d*2+int(i)
    for s in code:
        code_a=ord(s)
        code_new=code_a ^ key_d
        print(chr(code_new,end="")
def decrypt(code,key):
    for i in key:
        key_d=key_d*2+int(i)
    for s in code:
        code_a=ord(s)
        code_new=code_a ^ key_d
        print(chr(code_new,end="")        
    
    