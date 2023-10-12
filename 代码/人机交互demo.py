# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:22:51 2021

@author: lenovo
"""

import sys
sys.path.insert(0, "../")

import aiml               
k = aiml.Kernel()	   #创建aiml聊天机器人         
k.learn("cn-startup.xml")  #学习aiml语料库
k.respond("load aiml cn")   #初步交互   
k.respond("start")

while True:
    print(k.respond(input(">>")))  
    #人机交互并输出
