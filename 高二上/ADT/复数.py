# -*- coding: utf-8 -*-
import math
"""
方案 1
计算 2+3i 与 3-2i 的和
"""
def complex_plus_1(a1,b1,a2,b2):
    realpart = a1 +a2
    imaginarypart = b1 + b2
    return realpart,imaginarypart

a3,b3 = complex_plus_1(2,3,3,-2)
print(a3,"+",b3,"i")

"""
方案 2
计算 2+3i 与 3-2i 的和
"""
c1=[2,3]
c2=[3,-2]

def complex_plus_2(c1,c2):
    realpart = c1[0] + c2[0]
    imaginarypart = c1[1] + c2[1]
    return realpart,imaginarypart

c3 = complex_plus_2(c1,c2)
print(c3[0],"+",c3[1],"i")

"""
方案 3
计算 2+3i 与 3-4i 的和
"""
class ComplexNumber:
    def __init__(self,realpart,imaginarypart=0):
        self.realpart = realpart
        self.imaginarypart = imaginarypart
 
    def plus(self,another):
        realpart = self.realpart + another.realpart
        imaginarypart = self.imaginarypart + another.imaginarypart
        return ComplexNumber(realpart, imaginarypart)
 
    def module(self):
        return math.sqrt(self.realpart*self.realpart + self.imaginarypart*self.imaginarypart)

    def print(self):        
        print(str(self.realpart) + " +(" +str(self.imaginarypart) + ") i")
c1 = ComplexNumber(2,3)
c1.print()
c3 = c1.plus(ComplexNumber(3,-2))
c3.print()
print(c3.module())
