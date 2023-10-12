# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:18:13 2022

@author: Administrator
"""

def main():
    print("请选择数字1或2：")
    print("1:加密")
    print("2:解密")
    se=input()
    if se == "1":
        code = input("请输入加密字符串：")
        key=int(input("请输入偏移位数："))
        encrypt(code,key)
    if se == "2":
        code = input("请输入解密字符串：")
        key=int(input("请输入偏移位数："))
        decrypt(code,key)
def encrypt(code,key):
    code_new=""
    for s in code:
        if ord(s)<=90 and ord(s)>=65:
            code_new+=chr(65+((ord(s)-65)+key)%26)
        elif ord(s)<=122 and ord(s)>=97:
            code_new+=chr(97+((ord(s)-97)+key)%26)
        elif ord(s)<=57 and ord(s)>=48:
            code_new+=chr(48+((ord(s)-48)+key)%10)
        else:
            print("无法加密")
            break
    print(code_new)
    return code_new
def decrypt(code,key):
    code_new=""
    for s in code:
        m=ord(s)-key
        if m<48:
            m+=10
        elif m>57 and m<65:
            m+=26
        elif m>90 and m<97:
            m+=26
        code_new+=chr(m)
    print(code_new)
    return code_new 
if __name__ == '__main__':
    main()
