# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:58:17 2021

@author: lenovo velocity
""" 
class Person:
    def __init__(self,name,s,t):
        self.name=name
        self.s=s
        self.t=t
    def talk(self) :
        print("Hello ，My name is",self.name)
    def run(self):       
        print("刚刚跑了",self.s,"米，用时",self.t,"s，速度为",self.s/self.t,"米/秒") 
    def swim(self) :
        print("现在在游泳……")
    def pingpang(self):
        print("现在在打乒乓球……")
aa = Person("Tom",100,13)
aa.talk()
aa.run()
aa.swim()

bb=Person("Jack", 100, 14)
bb.talk()
bb.run()
bb.pingpang()