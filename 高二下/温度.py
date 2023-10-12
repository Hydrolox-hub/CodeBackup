# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import serial
ser=serial.Serial()
ser.baudrate=115200
ser.port='COM4'
ser.open()
f=open('microbit.txt','wb')
a=20
while a>0:
    a-=1
    line=ser.readline()
    f.write(line)
    print(line)
f.close()
ser.close()    